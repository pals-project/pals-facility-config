# This is a simple general-purpose chatbot built on top of LangChain and Gradio.
# Configure the defaults with environment variables if you want, or change them in the UI.
# - OPENAI_API_KEY
# - OPENAI_BASE_URL
# - OPENAI_MODEL
# - LLM_MODEL_NAME
# - OPENAI_TEMPERATURE
# - OPENAI_SYSTEM_PROMPT

import os
import json

import gradio as gr
from openai import OpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from kg_agent import (
    build_agent_system_prompt,
    build_cypher_tool,
    build_schema_snapshot,
    run_neo4j_query,
    run_graph_agent_loop,
    test_neo4j_connection,
    build_linkml_schema_context
)


def get_env_value(*names: str, default: str = "") -> str:
    for name in names:
        value = os.getenv(name)
        if value is not None and value != "":
            return value
    return default


def get_env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}

MODEL_CHOICES = [
    "gpt-4o-mini",
    "gpt-4.1-mini",
    "gpt-4.1",
    "claude-haiku",
]
DEFAULT_MODEL = get_env_value("OPENAI_MODEL", "LLM_MODEL_NAME", default=MODEL_CHOICES[0])
DEFAULT_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
DEFAULT_NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
DEFAULT_NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
DEFAULT_NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")
DEFAULT_NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")
DEFAULT_AGENT_MAX_ITERATIONS = int(os.getenv("NEO4J_AGENT_MAX_ITERATIONS", "6"))
DEFAULT_TRACE_MAX_CHARS = int(os.getenv("NEO4J_TRACE_MAX_CHARS", "4000"))
DEFAULT_SCHEMA_CACHE_TTL_SECONDS = int(os.getenv("NEO4J_SCHEMA_CACHE_TTL_SECONDS", "300"))
DEFAULT_USE_GRAPH_CONTEXT = get_env_bool("USE_GRAPH_CONTEXT", True)
DEFAULT_SHOW_REASONING = get_env_bool("SHOW_REASONING", False)
DEFAULT_RETURN_NEO4J_WARNINGS = get_env_bool("NEO4J_RETURN_WARNINGS", True)
DEFAULT_MANUAL_QUERY = os.getenv("NEO4J_MANUAL_QUERY", "MATCH (n) RETURN n LIMIT 25")


def make_client(base_url: str, api_key: str) -> OpenAI:
    base_url_value = base_url.strip() or None
    api_key_value = api_key.strip() or None

    return OpenAI(base_url=base_url_value, api_key=api_key_value)


def load_models(base_url: str, api_key: str, current_model: str | None = None):
    try:
        client = make_client(base_url, api_key)
        response = client.models.list()
        model_names = sorted({item.id for item in response.data})

        if not model_names:
            return gr.Dropdown(choices=[], value=None), "Loaded 0 models from the endpoint."

        selected_model = (
            current_model if current_model in model_names else DEFAULT_MODEL if DEFAULT_MODEL in model_names else model_names[0]
        )
        return gr.Dropdown(choices=model_names, value=selected_model), f"Loaded {len(model_names)} models from the endpoint."
    except Exception as exc:
        return gr.Dropdown(choices=[], value=None), f"Could not load models: {exc}"


def build_model(model_name: str, base_url: str, api_key: str, temperature: float) -> ChatOpenAI:
    base_url_value = base_url.strip() or None
    api_key_value = api_key.strip() or None
    secret_api_key = SecretStr(api_key_value) if api_key_value else None

    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        base_url=base_url_value,
        api_key=secret_api_key,
    )


def respond(
    message,
    history,
    model_name,
    base_url,
    api_key,
    temperature,
    system_prompt,
    use_graph_context,
    neo4j_uri,
    neo4j_user,
    neo4j_password,
    neo4j_database,
    show_reasoning,
):
    if not model_name:
        raise gr.Error("Please load models first from Endpoint Settings.")

    history = history or []
    langchain_history = []

    if system_prompt.strip():
        langchain_history.append(SystemMessage(content=system_prompt.strip()))

    if use_graph_context:
        try:
            schema_snapshot = build_schema_snapshot(
                neo4j_uri,
                neo4j_user,
                neo4j_password,
                neo4j_database,
                cache_ttl_seconds=DEFAULT_SCHEMA_CACHE_TTL_SECONDS,
            )
        except Exception as exc:
            schema_snapshot = f"Schema snapshot unavailable: {exc}"

        try:
            linkml_schema_context = build_linkml_schema_context()
        except Exception as exc:
            linkml_schema_context = f"LinkML schema reference unavailable: {exc}"

        langchain_history.append(
            SystemMessage(
                content=build_agent_system_prompt(
                    schema_snapshot=schema_snapshot,
                    linkml_schema_context=linkml_schema_context,
                )
            )
        )

    for msg in history:
        if msg["role"] == "user":
            langchain_history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_history.append(AIMessage(content=msg["content"]))

    langchain_history.append(HumanMessage(content=message))

    model = build_model(model_name, base_url, api_key, temperature)
    if use_graph_context:
        cypher_tool = build_cypher_tool(
            neo4j_uri, neo4j_user, neo4j_password, neo4j_database,
            return_warnings=DEFAULT_RETURN_NEO4J_WARNINGS,
        )
        response_content, query_trace = run_graph_agent_loop(
            model,
            langchain_history,
            cypher_tool,
            DEFAULT_AGENT_MAX_ITERATIONS,
            show_reasoning=show_reasoning,
            trace_max_chars=DEFAULT_TRACE_MAX_CHARS,
        )
    else:
        response_content = model.invoke(langchain_history).content
        query_trace = "Graph mode disabled for this turn, so no Neo4j queries were executed."

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response_content})
    return "", history, query_trace


def clear_chat():
    return "", [], "Query trace will appear here after you send a message."


def run_manual_query(neo4j_uri, neo4j_user, neo4j_password, neo4j_database, manual_query):
    if not manual_query or not manual_query.strip():
        return "Enter a Cypher query to run."

    try:
        rows = run_neo4j_query(neo4j_uri, neo4j_user, neo4j_password, neo4j_database, manual_query)
        row_count = len(rows)
        payload = json.dumps(rows, indent=2, default=str)
        return (
            f"### Manual Query Result\n"
            f"Rows: {row_count}\n\n"
            "```cypher\n"
            f"{manual_query.strip()}\n"
            "```\n"
            "```json\n"
            f"{payload}\n"
            "```"
        )
    except Exception as exc:
        return f"Manual query error: {exc}"


with gr.Blocks(title="Gradio Chat") as demo:
    gr.Markdown("## Gradio Chat\nUse the settings panel to pick the model, base URL, API key, and other request options.")

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Conversation", height=520)
            message = gr.Textbox(
                label="Message",
                placeholder="Type a message and press Enter",
            )
            with gr.Row():
                send_button = gr.Button("Send", variant="primary")
                clear_button = gr.Button("Clear")
            query_trace = gr.Markdown("Query trace will appear here after you send a message.")

        with gr.Column(scale=1):
            with gr.Accordion("Endpoint Settings", open=True):
                base_url = gr.Textbox(
                    label="Base URL",
                    value=os.getenv("OPENAI_BASE_URL", ""),
                    placeholder="https://your-endpoint/v1",
                )
                api_key = gr.Textbox(
                    label="API Key",
                    value=os.getenv("OPENAI_API_KEY", ""),
                    type="password",
                )
                load_models_button = gr.Button("Refresh Models")
                model_status = gr.Markdown("Click Refresh Models after editing endpoint values.")

            with gr.Accordion("Generation Settings", open=True):
                model_name = gr.Dropdown(
                    choices=[],
                    value=None,
                    label="Model",
                    allow_custom_value=True,  # accept API calls (e.g. automation scripts) that skip "Refresh Models"
                )
                temperature = gr.Slider(
                    minimum=0.0,
                    maximum=2.0,
                    value=DEFAULT_TEMPERATURE,
                    step=0.1,
                    label="Temperature",
                )
                system_prompt = gr.Textbox(
                    label="System Prompt",
                    value=os.getenv("OPENAI_SYSTEM_PROMPT", ""),
                    lines=4,
                    placeholder="Optional instruction that guides the assistant's behavior",
                )

            with gr.Accordion("Neo4j Knowledge Graph", open=False):
                use_graph_context = gr.Checkbox(
                    label="Use Neo4j context for each prompt",
                    value=DEFAULT_USE_GRAPH_CONTEXT,
                )
                show_reasoning = gr.Checkbox(
                    label="Show model reasoning in query trace",
                    value=DEFAULT_SHOW_REASONING,
                )
                neo4j_uri = gr.Textbox(
                    label="Neo4j URI",
                    value=DEFAULT_NEO4J_URI,
                    placeholder="bolt://localhost:7687",
                )
                neo4j_user = gr.Textbox(
                    label="Neo4j User",
                    value=DEFAULT_NEO4J_USER,
                )
                neo4j_password = gr.Textbox(
                    label="Neo4j Password",
                    value=DEFAULT_NEO4J_PASSWORD,
                    type="password",
                )
                neo4j_database = gr.Textbox(
                    label="Neo4j Database",
                    value=DEFAULT_NEO4J_DATABASE,
                )
                manual_query = gr.Textbox(
                    label="Manual Cypher Query (Debug)",
                    value=DEFAULT_MANUAL_QUERY,
                    lines=4,
                    placeholder="MATCH (n) RETURN n LIMIT 25",
                )
                run_manual_query_button = gr.Button("Run Manual Query")
                manual_query_output = gr.Markdown("Manual query results will appear here.")
                test_neo4j_button = gr.Button("Test Neo4j Connection")
                neo4j_status = gr.Markdown("Set Neo4j credentials, then click Test Neo4j Connection.")

    submit_inputs = [
        message,
        chatbot,
        model_name,
        base_url,
        api_key,
        temperature,
        system_prompt,
        use_graph_context,
        neo4j_uri,
        neo4j_user,
        neo4j_password,
        neo4j_database,
        show_reasoning,
    ]
    submit_outputs = [message, chatbot, query_trace]

    message.submit(respond, inputs=submit_inputs, outputs=submit_outputs)
    send_button.click(respond, inputs=submit_inputs, outputs=submit_outputs)
    clear_button.click(clear_chat, outputs=submit_outputs)
    load_models_button.click(load_models, inputs=[base_url, api_key, model_name], outputs=[model_name, model_status])
    test_neo4j_button.click(
        test_neo4j_connection,
        inputs=[neo4j_uri, neo4j_user, neo4j_password, neo4j_database],
        outputs=[neo4j_status],
    )
    run_manual_query_button.click(
        run_manual_query,
        inputs=[neo4j_uri, neo4j_user, neo4j_password, neo4j_database, manual_query],
        outputs=[manual_query_output],
    )

demo.launch(server_name="0.0.0.0", show_error=True)
