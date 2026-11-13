import json
import re
import time
import os
import yaml
from html import escape
from typing import LiteralString, cast
from pathlib import Path

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

_SCHEMA_CONTEXT_CACHE: tuple[str, int, str] | None = None

_SCHEMA_DETAIL_KEYS = (
    "description",
    "range",
    "required",
    "multivalued",
    "slot_uri",
    "aliases",
    "inlined",
    "inlined_as_list",
    "unit",
)


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


def run_neo4j_query_with_warnings(uri: str, user: str, password: str, database: str, query: str):
    """Run a read-only query and return (records, Neo4j warning descriptions)."""
    safe_query = validate_read_only_cypher(query)
    typed_query = cast(LiteralString, safe_query)
    if not uri.strip() or not user.strip() or not password.strip() or not database.strip():
        raise gr.Error("Neo4j URI, user, password, and database are required when graph context is enabled.")

    with GraphDatabase.driver(uri.strip(), auth=(user.strip(), password.strip())) as driver:
        with driver.session(database=database.strip()) as session:
            result = session.run(Query(typed_query))
            records = result.data()
            summary = result.consume()
    # e.g. "warn: label does not exist. The label `pals` does not exist. ..."
    warnings = [status.status_description for status in summary.gql_status_objects if status.is_notification]
    return records, warnings


def run_neo4j_query(uri: str, user: str, password: str, database: str, query: str):
    records, _warnings = run_neo4j_query_with_warnings(uri, user, password, database, query)
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

def _schema_details(definition: dict) -> dict:
    """Return the schema fields useful to an agent, omitting generator-only details."""
    return {
        key: definition[key]
        for key in _SCHEMA_DETAIL_KEYS
        if key in definition
    }

def _merge_properties(target: dict, source: dict) -> None:
    """Merge property definitions while preserving inherited details."""
    for name, details in source.items():
        merged = dict(target.get(name, {}))
        merged.update(details)
        target[name] = merged

def build_linkml_schema_context(schema_path: str | None = None) -> str:
    """Load a compact, inheritance-aware LinkML schema description for the agent."""
    global _SCHEMA_CONTEXT_CACHE

    path = Path(
        schema_path
        or os.getenv("LINKML_SCHEMA_FILE", "src/narad/schema/narad.yaml")
    )
    mtime_ns = path.stat().st_mtime_ns
    cache_key = str(path.resolve())

    if (
        _SCHEMA_CONTEXT_CACHE is not None
        and _SCHEMA_CONTEXT_CACHE[0] == cache_key
        and _SCHEMA_CONTEXT_CACHE[1] == mtime_ns
    ):
        return _SCHEMA_CONTEXT_CACHE[2]

    schema = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw_classes = schema.get("classes", {})
    raw_slots = schema.get("slots", {})
    raw_enums = schema.get("enums", {})

    def effective_properties(class_name: str, visiting: frozenset[str] = frozenset()) -> dict:
        """Collect inherited slots, mixins, attributes, and class-specific slot usage."""
        if class_name in visiting or class_name not in raw_classes:
            return {}

        class_def = raw_classes[class_name]
        next_visiting = visiting | {class_name}
        properties: dict = {}

        parent_names = []
        if class_def.get("is_a"):
            parent_names.append(class_def["is_a"])
        parent_names.extend(class_def.get("mixins", []))

        for parent_name in parent_names:
            _merge_properties(
                properties,
                effective_properties(parent_name, next_visiting),
            )

        # Slots inherit their common definition from the schema-level slots map.
        for slot_name in class_def.get("slots", []):
            _merge_properties(
                properties,
                {slot_name: _schema_details(raw_slots.get(slot_name, {}))},
            )

        # Attributes are class-defined properties.
        for attribute_name, attribute_def in class_def.get("attributes", {}).items():
            _merge_properties(
                properties,
                {attribute_name: _schema_details(attribute_def)},
            )

        # slot_usage provides class-specific overrides, e.g. subject range=Component.
        for slot_name, usage_def in class_def.get("slot_usage", {}).items():
            _merge_properties(
                properties,
                {slot_name: _schema_details(usage_def)},
            )

        return properties

    class_context = {}
    class_aliases: dict[str, list[str]] = {}
    for class_name, class_def in raw_classes.items():
        annotations = class_def.get("annotations", {})
        predicate_annotation = annotations.get("rdf_predicate")
        if isinstance(predicate_annotation, dict):
            predicate_annotation = predicate_annotation.get("value")

        aliases = class_def.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]

        for alias in aliases:
            class_aliases.setdefault(alias.casefold(), []).append(class_name)

        class_context[class_name] = {
            "description": class_def.get("description"),
            "is_a": class_def.get("is_a"),
            "mixins": class_def.get("mixins", []),
            "aliases": class_def.get("aliases", []),
            "abstract": class_def.get("abstract", False),
            "class_uri": class_def.get("class_uri"),
            "rdf_predicate": predicate_annotation,
            "properties": effective_properties(class_name),
        }

    enum_context = {}
    for enum_name, enum_def in raw_enums.items():
        enum_context[enum_name] = {
            "description": enum_def.get("description"),
            "values": {
                value_name: value_def.get("description")
                if isinstance(value_def, dict)
                else None
                for value_name, value_def in enum_def.get("permissible_values", {}).items()
            },
        }

    context = {
        "schema": {
            "name": schema.get("name"),
            "title": schema.get("title"),
            "description": schema.get("description"),
            "class_aliases": class_aliases,
        },
        "classes": class_context,
        "enums": enum_context,
        "interpretation_notes": [
            "This is LinkML semantic documentation; use the live Neo4j snapshot for exact labels and property names.",
            "Relationship classes have subject/object properties and may also have class-specific qualifiers.",
            "Classes with rdf_predicate define direct RDF relationships; in this graph, those can be traversed as Neo4j relationships.",
            "A direct relationship and its reified relation node are distinct representations; qualifiers may be on the reified node, not on the direct relationship.",
        ],
    }

    rendered = json.dumps(context, ensure_ascii=False, separators=(",", ":"))
    _SCHEMA_CONTEXT_CACHE = (cache_key, mtime_ns, rendered)
    return rendered


def build_agent_system_prompt(
        schema_snapshot: str | None = None,
        linkml_schema_context: str | None = None,
    ) -> str:
        base_prompt = (
            "You are a knowledge-graph assistant with access to a Neo4j tool named execute_cypher. "
            "Use iterative tool calls when needed and do not produce a final answer until you have "
            "enough graph evidence. If a query fails or returns no rows, revise and try again. "
            "Use read-only Cypher only, and keep each query focused with LIMIT when appropriate. "
            "Use the LinkML schema for meanings, descriptions, ranges, and relationship semantics. "
            "Use the live Neo4j schema snapshot for the actual labels, relationship types, and property names."
        )

        parts = [base_prompt]

        if linkml_schema_context and linkml_schema_context.strip():
            parts.append("\nLinkML schema reference:\n" + linkml_schema_context.strip())

        if schema_snapshot and schema_snapshot.strip():
            parts.append("\nLive Neo4j schema snapshot:\n" + schema_snapshot.strip())

        parts.append(
            "\nQuery guidance:\n"
            "- For beamline order, traverse the direct `precedes` relationship when that type appears "
            "in the live Neo4j snapshot.\n"
            "- Use the reified relation node when a question needs relationship qualifiers such as "
            "`context` or `beamline_context`; do not assume those qualifiers are properties of the "
            "direct relationship.\n"
            "- Each direct relationship's `relation_uri` property is the `uri` of the reified "
            "relation node it came from; match `(r {uri: rel.relation_uri})` to reach its "
            "qualifiers. The same pair can have several such relationships (e.g. one per "
            "beamline), so filter on the relation node's qualifiers when that matters.\n"
            "- Beamline order (first, last, Nth, downstream/upstream). Never infer order from the order "
            "of result rows; they come back in storage order.\n"
            "  - Each `precedes` relationship belongs to one beamline: its relation node (`relation_uri`) "
            "links to that BeamLine via `beamline_context`. A beamline's first element has an outgoing "
            "`precedes` in that beamline and no incoming one; its last element has an incoming one and "
            "no outgoing one.\n"
            "  - If the question names a beamline (e.g. KV or MV), search only that beamline's chain.\n"
            "  - Otherwise \"first\" or \"last\" means in the whole machine. Beamlines `is_part_of` a "
            "parent beamline, and the order of sibling beamlines is given by `precedes` between the "
            "BeamLine nodes themselves (e.g. KV precedes MV). For \"first\", search the first "
            "sub-beamline's chain forward from its first element; if nothing matches, search the next "
            "sub-beamline, and so on. For \"last\" (or Nth from the end), do the same in reverse: start "
            "with the last sub-beamline and walk backward from its last element. If none matches, say so.\n"
            "  - Walk a chain with `shortestPath`, binding both endpoints, and order by `length(p)`, e.g.\n"
            "    `MATCH (bl:BeamLine {uri:'KV'}) "
            "MATCH (r:Precedes)-[:beamline_context]->(bl), (r)-[:subject]->(start) "
            "WHERE NOT EXISTS { MATCH (r2:Precedes)-[:beamline_context]->(bl), (r2)-[:object]->(start) } "
            "MATCH (b:BeamPositionMonitor) "
            "WHERE EXISTS { MATCH (q:Precedes)-[:beamline_context]->(bl), (q)-[:object]->(b) } "
            "MATCH p = shortestPath((start)-[:precedes*]->(b)) "
            "RETURN b.uri, length(p) ORDER BY length(p) LIMIT 1`\n"
            "    For \"downstream of X\", use X as `start`. To walk backward (last, upstream of X), use the "
            "beamline's last element (or X) as `end` and `shortestPath((b)-[:precedes*]->(end))`.\n"
            "  - Never use a plain `precedes*1..N` pattern: it lists every path, and because the same "
            "pair can have several `precedes` relationships (one per beamline) the number of paths "
            "grows exponentially and the query may never finish.\n"
            "- Use schema ranges and descriptions to choose properties, then verify the chosen "
            "labels/property names against the live snapshot."
            "\nAlias interpretation:\n"
            "- LinkML class aliases are synonyms for class names, not identifiers for individual graph nodes.\n"
            "- Resolve a class alias using the LinkML class_aliases map. For example, 'Dipole' means the "
            "Bend class; when the live Neo4j snapshot confirms the Bend label, use that label to find Bend instances.\n"
            "- A class alias alone can match many instances. For a specific component, also resolve an instance "
            "identifier, name, or data-instance alias. If multiple instances match, ask which one the user means."
        )

        return "\n".join(parts)


def build_cypher_tool(
        neo4j_uri: str,
        neo4j_user: str,
        neo4j_password: str,
        neo4j_database: str,
        return_warnings: bool = True,
    ) -> StructuredTool:
    def execute_cypher(cypher_query: str) -> str:
        try:
            records, warnings = run_neo4j_query_with_warnings(
                neo4j_uri,
                neo4j_user,
                neo4j_password,
                neo4j_database,
                cypher_query,
            )
            context = build_graph_context(records)
            # Without these, a misspelled or nonexistent label/type/property just looks like an empty result.
            if return_warnings and warnings:
                context += "\n\nNeo4j warnings (revise the query if they explain missing or empty results):\n"
                context += "\n".join(f"- {warning}" for warning in warnings)
            return context
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
