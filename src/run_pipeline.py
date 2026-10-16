#!/usr/bin/env python3
"""Automates: LinkML schema/instance -> RDF -> Neo4j graph -> LLM Q&A via gradio-chat.

Example usage:
    uv run python3 src/run_pipeline.py \\
        --schema src/narad/schema/narad.yaml \\
        --instance examples/core_acc_narad_instance.yaml \\
        --queries examples/benchmark_queries/UITF_v1.yaml \\
        --answers examples/benchmark_queries/UITF_v1_answers.yaml
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import copy
import yaml
from dotenv import load_dotenv
from gradio_client import Client
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph, URIRef, RDF, Literal, Namespace
from postprocess_for_rdf import load_predicate_uris

REPO_ROOT = Path(__file__).resolve().parents[1]

@dataclass
class IntermediatePaths:
    """Paths to the RDF files generated from a LinkML schema/instance pair."""

    schema_ttl: Path
    instance_raw_ttl: Path
    instance_rdf_ttl: Path


@dataclass
class GradioSettings:
    """Values forwarded to the gradio-chat `respond()` endpoint on every query."""

    model_name: str
    base_url: str
    api_key: str
    temperature: float
    system_prompt: str
    use_graph_context: bool
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str
    neo4j_database: str
    show_reasoning: bool


def resolve_target_class(schema_path: Path) -> str:
    """Return the name of the schema's tree_root class, used as -C for linkml-convert."""
    schema_view = SchemaView(str(schema_path))
    for class_name in schema_view.all_classes():
        class_def = schema_view.get_class(class_name)
        if getattr(class_def, "tree_root", False):
            return class_name
    raise ValueError(f"No class with 'tree_root: true' found in schema: {schema_path}")


def run_command(command: list[str], *, cwd: Path, env: dict[str, str] | None = None, stdout: Path | None = None) -> None:
    """Run a subprocess, optionally redirecting stdout to a file, and raise on failure."""
    print(f"$ {' '.join(command)}" + (f" > {stdout}" if stdout else ""))
    if stdout is not None:
        stdout.parent.mkdir(parents=True, exist_ok=True)
        with stdout.open("w") as handle:
            subprocess.run(command, cwd=cwd, env=env, stdout=handle, check=True)
    else:
        subprocess.run(command, cwd=cwd, env=env, check=True)


def generate_rdf(schema_path: Path, instance_path: Path, gen_owl_args: str) -> IntermediatePaths:
    """Reproduces the `gen-owl` / `gen-instance-ttl` / `gen-post` justfile recipes directly."""
    target_class = resolve_target_class(schema_path)
    paths = IntermediatePaths(
        schema_ttl=schema_path.with_suffix(".owl.ttl"),
        instance_raw_ttl=instance_path.with_suffix(".ttl"),
        instance_rdf_ttl=instance_path.with_name(f"{instance_path.stem}_rdf.ttl"),
    )

    gen_owl_command = ["uv", "run", "gen-owl", *([gen_owl_args] if gen_owl_args else []), str(schema_path)]
    run_command(gen_owl_command, cwd=REPO_ROOT, stdout=paths.schema_ttl)

    run_command(
        [
            "uv", "run", "linkml-convert",
            "-s", str(schema_path),
            "-C", target_class,
            "-t", "ttl",
            str(instance_path),
            "-o", str(paths.instance_raw_ttl),
        ],
        cwd=REPO_ROOT,
    )

    run_command(
        [
            "uv", "run", "python3", "src/postprocess_for_rdf.py",
            "--schema", str(schema_path),
            "--instance_file", str(paths.instance_raw_ttl),
            "--output_file", str(paths.instance_rdf_ttl),
        ],
        cwd=REPO_ROOT,
    )
    return paths

def docker_compose_up(paths: IntermediatePaths, schema_path: Path, *, fresh: bool, compose_file: Path) -> None:
    """Point docker-compose at the generated RDF files and the source schema, then (re)start the stack."""
    env = os.environ.copy()
    env["NEO4J_SCHEMA_TTL_PATH"] = str(paths.schema_ttl)
    env["NEO4J_INSTANCE_TTL_PATH"] = str(paths.instance_rdf_ttl)
    # gradio-chat reads the LinkML schema directly to give the LLM class/slot/enum descriptions.
    env["LINKML_SCHEMA_HOST_PATH"] = str(schema_path)

    if fresh:
        run_command(["docker", "compose", "-f", str(compose_file), "down", "-v"], cwd=REPO_ROOT, env=env)
    # --build: gradio-chat's code is copied into its image, so rebuild to pick up source changes.
    run_command(["docker", "compose", "-f", str(compose_file), "up", "-d", "--build"], cwd=REPO_ROOT, env=env)


def wait_for_gradio_ready(url: str, *, timeout_seconds: float, poll_interval_seconds: float = 3.0) -> Any:
    """Poll the gradio-chat endpoint until a client connection succeeds or timeout elapses."""
    deadline = time.monotonic() + timeout_seconds
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            return Client(url)
        except Exception as exc:  # noqa: BLE001 - retry on any startup failure
            last_error = exc
            time.sleep(poll_interval_seconds)
    raise TimeoutError(f"gradio-chat at {url} did not become ready within {timeout_seconds}s: {last_error}")


def load_gradio_settings() -> GradioSettings:
    """Build GradioSettings from environment variables, mirroring main.py's UI defaults."""

    def env_bool(name: str, default: bool) -> bool:
        value = os.getenv(name)
        if value is None:
            return default
        return value.strip().lower() in {"1", "true", "yes", "on"}

    return GradioSettings(
        model_name=os.getenv("LLM_MODEL_NAME", "gpt-4o-mini"),
        base_url=os.getenv("OPENAI_BASE_URL", ""),
        api_key=os.getenv("OPENAI_API_KEY", ""),
        temperature=float(os.getenv("OPENAI_TEMPERATURE", "0.7")),
        system_prompt=os.getenv("OPENAI_SYSTEM_PROMPT", ""),
        use_graph_context=env_bool("USE_GRAPH_CONTEXT", True),
        # gradio-chat runs inside Docker, where "neo4j-kg" is the compose service name (see docker-compose.yml).
        neo4j_uri=os.getenv("NEO4J_URI", "bolt://neo4j-kg:7687"),
        neo4j_user=os.getenv("NEO4J_USER", "neo4j"),
        neo4j_password=os.getenv("NEO4J_PASSWORD", ""),
        neo4j_database=os.getenv("NEO4J_DATABASE", "neo4j"),
        show_reasoning=env_bool("SHOW_REASONING", False),
    )


def query_gradio(
    client: Any,
    message: str,
    history: list[dict[str, str]],
    settings: GradioSettings,
) -> tuple[str, list[dict[str, str]]]:
    """Send one message to the gradio-chat `respond()` endpoint and return (answer, updated history)."""
    _cleared_message, new_history, _trace = client.predict(
        message,
        history,
        settings.model_name,
        settings.base_url,
        settings.api_key,
        settings.temperature,
        settings.system_prompt,
        settings.use_graph_context,
        settings.neo4j_uri,
        settings.neo4j_user,
        settings.neo4j_password,
        settings.neo4j_database,
        settings.show_reasoning,
        api_name="/respond",
    )
    answer = extract_message_text(new_history[-1]["content"]) if new_history else ""
    return answer, new_history


def extract_message_text(content: Any) -> str:
    """Flatten a Chatbot message's `content` field (str, or list of {"type": "text", ...} blocks) to plain text."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(block.get("text", "") if isinstance(block, dict) else str(block) for block in content)
    return str(content)


def normalize_answers_path(answers_path: Path) -> Path:
    """Ensure the answers path has a .yml/.yaml suffix, defaulting to .yaml if none given."""
    suffix = answers_path.suffix.lower()
    if suffix == "":
        return answers_path.with_suffix(".yaml")
    if suffix not in {".yml", ".yaml"}:
        raise ValueError(f"--answers must end in .yml, .yaml, or have no extension, got: {answers_path}")
    return answers_path


def run_benchmark(
    gradio_url: str,
    queries_path: Path,
    answers_path: Path,
    *,
    accumulate_history: bool,
    startup_timeout_seconds: float,
    question_key: str,
    llm_answer_key: str,
) -> None:
    """Run every query in queries_path through gradio-chat and write answers to answers_path."""
    client = wait_for_gradio_ready(gradio_url, timeout_seconds=startup_timeout_seconds)
    settings = load_gradio_settings()

    with open(queries_path, 'r') as handle:
        entries = yaml.safe_load(handle)
    history: list[dict[str, str]] = []
    results: list[dict[str, str]] = []
    for entry in entries:
        question = entry[question_key].strip()
        if not accumulate_history:
            history = []
        answer, history = query_gradio(client, question, history, settings)
        assert llm_answer_key not in entry, f"Entry already contains '{llm_answer_key}' !!!"
        result = copy.deepcopy(entry)
        result[llm_answer_key] = answer
        results.append(result)

    with answers_path.open("w") as handle:
        yaml.safe_dump(results, handle, allow_unicode=True, sort_keys=False)


def delete_intermediate_files(paths: IntermediatePaths) -> None:
    """Remove the generated RDF intermediate files from disk."""
    for path in (paths.schema_ttl, paths.instance_raw_ttl, paths.instance_rdf_ttl):
        path.unlink(missing_ok=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments for the pipeline driver."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--schema", required=True, help="Path to the LinkML schema YAML")
    parser.add_argument("--instance", required=True, help="Path to the LinkML instance YAML")
    parser.add_argument("--transformation", default="RDF", help="Transformation to apply (only 'RDF' is supported)")
    parser.add_argument("--queries", required=True, help="Path to the queries YAML file")
    parser.add_argument("--answers", required=True, help="Path to write the answers YAML file")
    parser.add_argument("--gen-owl-args", default="", help="Extra args forwarded to `gen-owl`")
    parser.add_argument("--compose-file", default=str(REPO_ROOT / "docker-compose.yml"))
    parser.add_argument("--gradio-url", default="http://localhost:7860")
    parser.add_argument("--startup-timeout", type=float, default=180.0, help="Seconds to wait for gradio-chat to come up")
    parser.add_argument("--delete-intermediate-files", action="store_true")
    parser.add_argument("--no-fresh", dest="fresh", action="store_false", help="Skip `docker compose down -v` before starting")
    parser.add_argument(
        "--no-accumulate-history", dest="accumulate_history", action="store_false",
        help="Query each benchmark question independently, without prior chat history",
    )
    parser.add_argument("--question-key", default="Q", help="Key in each queries entry holding the question text")
    parser.add_argument(
        "--llm-answer-key", default="LLM_Ans",
        help="Key to write the LLM's answer under in each answers entry (must not already exist in the queries entry)",
    )
    parser.set_defaults(fresh=True, accumulate_history=True)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    """Run the full schema/instance -> RDF -> Neo4j -> LLM benchmark pipeline."""
    args = parse_args(argv)
    load_dotenv(REPO_ROOT / ".env")

    if args.transformation != "RDF":
        raise NotImplementedError(f"Unsupported transformation: {args.transformation}")

    schema_path = Path(args.schema).resolve()
    instance_path = Path(args.instance).resolve()
    answers_path = normalize_answers_path(Path(args.answers).resolve())


    load_predicate_uris(str(schema_path)) # fail fast if there are missing rdf_predicate annotations
    paths = generate_rdf(schema_path, instance_path, args.gen_owl_args)
    docker_compose_up(paths, schema_path, fresh=args.fresh, compose_file=Path(args.compose_file))
    run_benchmark(
        args.gradio_url,
        Path(args.queries).resolve(),
        answers_path,
        accumulate_history=args.accumulate_history,
        startup_timeout_seconds=args.startup_timeout,
        question_key=args.question_key,
        llm_answer_key=args.llm_answer_key,
    )

    if args.delete_intermediate_files:
        delete_intermediate_files(paths)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
