import json
import re
import time
from html import escape
from typing import LiteralString, cast

import gradio as gr
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from neo4j import GraphDatabase, Query
from pydantic import BaseModel, Field

WRITE_CYPHER_PATTERN = re.compile(
    r"\\b(CREATE|MERGE|DELETE|DETACH|SET|REMOVE|DROP|LOAD\\s+CSV|CALL\\s+dbms\\.)\\b",
    re.IGNORECASE,
)

_SCHEMA_CACHE: dict[str, tuple[float, str]] = {}


class CypherToolInput(BaseModel):
    cypher_query: str = Field(
        description=(
            "Read-only Cypher query to execute against Neo4j. "
            "Always use LIMIT when returning lists to keep results concise."
        )
    )


def validate_read_only_cypher(query: str) -> str:
    normalized_query = query.strip()
    if not normalized_query:
        raise gr.Error("Cypher query is empty.")
    if WRITE_CYPHER_PATTERN.search(normalized_query):
        raise gr.Error("Only read-only Cypher queries are allowed in this UI.")
    return normalized_query


def run_neo4j_query(uri: str, user: str, password: str, database: str, query: str):
    safe_query = validate_read_only_cypher(query)
    typed_query = cast(LiteralString, safe_query)
    if not uri.strip() or not user.strip() or not password.strip() or not database.strip():
        raise gr.Error("Neo4j URI, user, password, and database are required when graph context is enabled.")

    with GraphDatabase.driver(uri.strip(), auth=(user.strip(), password.strip())) as driver:
        with driver.session(database=database.strip()) as session:
            records = session.run(Query(typed_query)).data()
    return records


def build_graph_context(records) -> str:
    if not records:
        return "No rows returned from Neo4j for this query."
    return json.dumps(records, indent=2, default=str)


def _schema_query_json(uri: str, user: str, password: str, database: str, query: str) -> list[dict]:
    rows = run_neo4j_query(uri, user, password, database, query)
    return rows if isinstance(rows, list) else []


def build_schema_snapshot(
    neo4j_uri: str,
    neo4j_user: str,
    neo4j_password: str,
    neo4j_database: str,
    cache_ttl_seconds: int = 300,
) -> str:
    cache_key = f"{neo4j_uri.strip()}|{neo4j_user.strip()}|{neo4j_database.strip()}"
    now = time.time()
    cached = _SCHEMA_CACHE.get(cache_key)
    if cached and (now - cached[0] < cache_ttl_seconds):
        return cached[1]

    labels_rows = _schema_query_json(
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        "CALL db.labels() YIELD label RETURN label ORDER BY label",
    )
    rel_types_rows = _schema_query_json(
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        "CALL db.relationshipTypes() YIELD relationshipType RETURN relationshipType ORDER BY relationshipType",
    )
    node_prop_rows = _schema_query_json(
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        (
            "MATCH (n) "
            "UNWIND labels(n) AS label "
            "UNWIND keys(n) AS property "
            "RETURN label, property, count(*) AS frequency "
            "ORDER BY frequency DESC "
            "LIMIT 80"
        ),
    )
    rel_prop_rows = _schema_query_json(
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        (
            "MATCH ()-[r]->() "
            "UNWIND keys(r) AS property "
            "RETURN type(r) AS relationship, property, count(*) AS frequency "
            "ORDER BY frequency DESC "
            "LIMIT 80"
        ),
    )
    pattern_rows = _schema_query_json(
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        (
            "MATCH (a)-[r]->(b) "
            "RETURN labels(a) AS source_labels, type(r) AS relationship, labels(b) AS target_labels, count(*) AS frequency "
            "ORDER BY frequency DESC "
            "LIMIT 40"
        ),
    )

    labels = [row["label"] for row in labels_rows if isinstance(row.get("label"), str)]
    rel_types = [row["relationshipType"] for row in rel_types_rows if isinstance(row.get("relationshipType"), str)]

    summary_parts = [
        "SCHEMA SNAPSHOT (auto-generated):",
        f"Labels ({len(labels)}): {', '.join(labels[:40]) if labels else 'none'}",
        f"Relationship types ({len(rel_types)}): {', '.join(rel_types[:40]) if rel_types else 'none'}",
        "Top node properties by label (json):",
        json.dumps(node_prop_rows, indent=2, default=str),
        "Top relationship properties by type (json):",
        json.dumps(rel_prop_rows, indent=2, default=str),
        "Frequent relationship patterns (json):",
        json.dumps(pattern_rows, indent=2, default=str),
    ]

    snapshot = "\n".join(summary_parts)
    _SCHEMA_CACHE[cache_key] = (now, snapshot)
    return snapshot


def build_agent_system_prompt(schema_snapshot: str | None = None) -> str:
    base_prompt = (
        "You are a knowledge-graph assistant with access to a Neo4j tool named execute_cypher. "
        "Use iterative tool calls when needed and do not produce a final answer until you have "
        "enough graph evidence. If a query fails or returns no rows, revise and try again. "
        "Use read-only Cypher only, and keep each query focused with LIMIT when appropriate. "
        "Prefer label/type/property names from the provided schema snapshot."
    )

    parts = [base_prompt]
    if schema_snapshot and schema_snapshot.strip():
        parts.append("\nSchema snapshot:\n" + schema_snapshot.strip())
    return "\n".join(parts)


def build_cypher_tool(neo4j_uri: str, neo4j_user: str, neo4j_password: str, neo4j_database: str) -> StructuredTool:
    def execute_cypher(cypher_query: str) -> str:
        try:
            records = run_neo4j_query(
                neo4j_uri,
                neo4j_user,
                neo4j_password,
                neo4j_database,
                cypher_query,
            )
            return build_graph_context(records)
        except Exception as exc:
            return f"Cypher execution error: {exc}"

    return StructuredTool.from_function(
        func=execute_cypher,
        name="execute_cypher",
        description=(
            "Execute a read-only Cypher query on the connected Neo4j graph and return JSON rows. "
            "Use this to gather facts before answering the user."
        ),
        args_schema=CypherToolInput,
    )


def _as_text(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                if "text" in item:
                    parts.append(_as_text(item.get("text")))
                elif "content" in item:
                    parts.append(_as_text(item.get("content")))
                else:
                    parts.append(json.dumps(item, default=str))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)
    if isinstance(value, dict):
        if "text" in value:
            return _as_text(value.get("text"))
        if "content" in value:
            return _as_text(value.get("content"))
        return json.dumps(value, indent=2, default=str)
    if value is None:
        return ""
    return str(value)


def _truncate_text(value: str, max_chars: int) -> str:
    if len(value) <= max_chars:
        return value
    return f"{value[:max_chars]}\n... [truncated {len(value) - max_chars} chars]"


def _format_query_trace(trace_entries: list[dict], show_reasoning: bool, max_chars: int) -> str:
    if not trace_entries:
        return "### Query Trace\nNo Neo4j tool calls were made in the last turn."

    total_calls = len(trace_entries)
    error_calls = sum(1 for entry in trace_entries if entry.get("status") == "error")

    blocks = [
        "### Query Trace",
        f"Calls: {total_calls} | Errors: {error_calls}",
    ]

    for idx, entry in enumerate(trace_entries, start=1):
        cypher_text = _truncate_text(_as_text(entry.get("cypher", "")), max_chars=max_chars)
        result_text = _truncate_text(_as_text(entry.get("result", "")), max_chars=max_chars)
        reasoning_text = _truncate_text(_as_text(entry.get("reasoning", "")), max_chars=max_chars)
        status_text = _as_text(entry.get("status", "ok")).upper()
        iteration = entry.get("iteration", "?")

        blocks.append("")
        blocks.append(f"<details><summary>Call {idx} | Iteration {iteration} | {escape(status_text)}</summary>")

        if show_reasoning and reasoning_text.strip():
            blocks.append("Reasoning")
            blocks.append("<pre><code>")
            blocks.append(escape(reasoning_text))
            blocks.append("</code></pre>")

        blocks.append("Cypher")
        blocks.append("<pre><code>")
        blocks.append(escape(cypher_text))
        blocks.append("</code></pre>")
        blocks.append("Result")
        blocks.append("<pre><code>")
        blocks.append(escape(result_text))
        blocks.append("</code></pre>")
        blocks.append("</details>")

    return "\n".join(blocks)


def run_graph_agent_loop(
    model: ChatOpenAI,
    messages,
    cypher_tool: StructuredTool,
    max_iterations: int,
    show_reasoning: bool = False,
    trace_max_chars: int = 4000,
) -> tuple[str, str]:
    tool_enabled_model = model.bind_tools([cypher_tool], tool_choice="auto")
    agent_messages = list(messages)
    trace_entries: list[dict] = []

    for iteration in range(1, max_iterations + 1):
        ai_response = tool_enabled_model.invoke(agent_messages)
        agent_messages.append(ai_response)
        reasoning_text = _as_text(ai_response.content).strip()

        tool_calls = getattr(ai_response, "tool_calls", None) or []
        if not tool_calls:
            return _as_text(ai_response.content), _format_query_trace(trace_entries, show_reasoning, trace_max_chars)

        for tool_call in tool_calls:
            tool_name = tool_call.get("name", "")
            call_id = tool_call.get("id", "")
            args = tool_call.get("args", {}) or {}
            cypher_query = args.get("cypher_query", "") if isinstance(args, dict) else ""

            if tool_name != "execute_cypher":
                tool_result = f"Unsupported tool '{tool_name}'."
                status = "error"
            else:
                tool_result = cypher_tool.invoke(args)
                status = "error" if _as_text(tool_result).startswith("Cypher execution error:") else "ok"

            trace_entries.append(
                {
                    "iteration": iteration,
                    "cypher": cypher_query,
                    "result": _as_text(tool_result),
                    "status": status,
                    "reasoning": reasoning_text,
                }
            )

            agent_messages.append(
                ToolMessage(
                    content=_as_text(tool_result),
                    tool_call_id=call_id,
                    name=tool_name,
                )
            )

    agent_messages.append(
        HumanMessage(
            content=(
                "You have reached the maximum tool-call iterations. "
                "Provide your best final answer from the gathered evidence."
            )
        )
    )
    # Keep using the tool-bound model because some providers reject histories
    # containing tool messages when the request omits a tools definition.
    final_response = tool_enabled_model.invoke(agent_messages)
    return _as_text(final_response.content), _format_query_trace(trace_entries, show_reasoning, trace_max_chars)


def test_neo4j_connection(uri: str, user: str, password: str, database: str) -> str:
    try:
        records = run_neo4j_query(uri, user, password, database, "RETURN 1 AS ok")
        if records and records[0].get("ok") == 1:
            return "Neo4j connection successful."
        return "Neo4j responded, but health check returned an unexpected payload."
    except Exception as exc:
        return f"Neo4j connection failed: {exc}"
