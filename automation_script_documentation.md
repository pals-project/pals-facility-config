# Automation Script — Automated NARAD Q&A Pipeline

This document describes the work done on this branch: an automation script that
turns the previously manual, multi-step workflow

```
LinkML schema + instance YAML
  --> RDF (Turtle)
  --> Neo4j knowledge graph
  --> gradio-chat (LLM + Neo4j Cypher agent)
  --> answers to a batch of questions
```

into a single command.

## 1. What problem this solves

Before this branch, running the NARAD Q&A pipeline required:

1. Manually running several `just` recipes (`gen-owl`, `gen-instance-ttl`, `gen-post`)
   to turn a LinkML schema + instance YAML into RDF/Turtle files, and knowing which
   recipe took which file as input (this was ambiguous/undocumented).
2. Manually copying/renaming those `.ttl` files to the exact hardcoded paths that
   `docker-compose.yml` expected (`project/owl/narad.owl.ttl`,
   `project/owl/core_acc_narad_instance.ttl`) before starting the stack.
3. Running `docker compose up -d` and waiting for `neo4j-kg` → `neo4j-init` →
   `gradio-chat` to come up in the right order.
4. Manually typing each benchmark question into the Gradio chat UI, one at a
   time, and copying the answers out by hand.

This branch replaces steps 1–4 with a single script:
[`src/run_pipeline.py`](src/run_pipeline.py).

## 2. Inputs and outputs

### Command

```bash
uv run python3 src/run_pipeline.py \
  --schema      <path to LinkML schema YAML> \
  --instance    <path to LinkML instance YAML> \
  --queries     <path to questions YAML> \
  --answers     <path to write answers YAML> \
  [--transformation RDF] \
  [--gen-owl-args "..."] \
  [--compose-file docker-compose.yml] \
  [--gradio-url http://localhost:7860] \
  [--startup-timeout 180] \
  [--delete-intermediate-files] \
  [--no-fresh] \
  [--no-accumulate-history] \
  [--question-key Q] \
  [--llm-answer-key LLM_Ans]
```

### Required inputs

| Argument      | Meaning                                                                 | Example |
|---------------|--------------------------------------------------------------------------|---------|
| `--schema`    | LinkML schema YAML (source of truth for the data model)                  | `src/narad/schema/narad.yaml` |
| `--instance`  | LinkML instance YAML (the actual accelerator data to load into the graph) | `examples/core_acc_narad_instance.yaml` |
| `--queries`   | YAML file with the benchmark questions to ask                            | `examples/benchmark_queries/UITF_v1.yaml` |
| `--answers`   | Where to write the LLM's answers                                         | `examples/benchmark_queries/UITF_v1_LLM_answers.yaml` |

### Optional inputs

| Argument | Default | Meaning |
|----------|---------|---------|
| `--transformation` | `RDF` | Which intermediate representation to build the graph from. Only `RDF` is implemented; anything else raises `NotImplementedError` (a placeholder for future transformation strategies). |
| `--gen-owl-args` | `""` | Extra CLI args forwarded to `gen-owl` (mirrors `LINKML_GENERATORS_OWL_ARGS` in `config.public.mk`). |
| `--compose-file` | `docker-compose.yml` at repo root | Which compose file to drive. |
| `--gradio-url` | `http://localhost:7860` | Where the driver (running on the **host**) reaches the published `gradio-chat` port. |
| `--startup-timeout` | `180` seconds | How long to wait for `gradio-chat` to become reachable before giving up. |
| `--delete-intermediate-files` | off | Delete the generated `.ttl`/`.owl.ttl` files once the graph has been built and queried. |
| `--no-fresh` | off (i.e. fresh by default) | Skip `docker compose down -v` before `up -d`. **Not safe** if the RDF content changed since the last run — see §6. |
| `--no-accumulate-history` | off (i.e. accumulate by default) | Ask every question independently, with no prior chat history, instead of one continuous conversation. |
| `--question-key` | `Q` | Key in each queries entry holding the question text. |
| `--llm-answer-key` | `LLM_Ans` | Key to write the LLM's answer under in each answers entry; the script asserts this key does not already exist in the queries entry. |

### Queries file format (`--queries`)

A YAML list of `{Q, Ans}` dicts, e.g. [`examples/benchmark_queries/UITF_v1.yaml`](examples/benchmark_queries/UITF_v1.yaml):

```yaml
- Q: Give me the horizontal and vertical beam positions and status at the first BPM
  Ans: IPMK101.XPOS, IPMK101.YPOS, IPMK101.STAT
- Q: What's the status of MFHK101?
  Ans: MFHK101.STAT
```

Only the `Q` field is ever sent to the LLM. `Ans` is the human-authored expected
answer for reference/grading; if present, it is carried through into the
generated answers file (see below) so an evaluator can compare it against the
LLM's answer without checking multiple files.

### Answers file format (`--answers`)

A YAML list of `{Q, Ans, LLM_Ans}` dicts, one per question, in the same order as
the input file. `Ans` is only included if it was present in the corresponding
queries entry:

```yaml
- Q: Give me the horizontal and vertical beam positions and status at the first BPM
  Ans: IPMK101.XPOS, IPMK101.YPOS, IPMK101.STAT
  LLM_Ans: 'At the first BPM in the graph, the beam position fields are not populated: ...'
- Q: What's the status of MFHK101?
  Ans: MFHK101.STAT
  LLM_Ans: 'MFHK101 is a Solenoid instance, but the graph does not show any ...'
```

If `--answers` has no file extension, `.yaml` is appended automatically. If it
has an extension other than `.yml`/`.yaml`, the script raises an error rather
than silently writing YAML content into e.g. a `.txt` file.

## 3. Step-by-step: what the script actually does

`main()` in [`src/run_pipeline.py`](src/run_pipeline.py) runs these stages in order:

### Stage 1 — Load environment

`load_dotenv(REPO_ROOT / ".env")` loads secrets/config from `.env` into the
process environment (API keys, Neo4j credentials, model name, etc. — see §5).

### Stage 2 — Generate RDF (`generate_rdf`)

This reproduces the `gen-owl` / `gen-instance-ttl` / `gen-post` `justfile`
recipes, but calls the underlying tools directly instead of going through
`just`, and writes the outputs **next to the source files** instead of a
hardcoded `project/owl/` directory:

1. `resolve_target_class(schema_path)` — uses LinkML's `SchemaView` to find the
   schema's `tree_root: true` class automatically (e.g. `PALSAccelerator`),
   instead of hardcoding the class name like the old `justfile` recipe did.
   This makes the script schema-agnostic.
2. `uv run gen-owl <schema>.yaml > <schema>.owl.ttl` — generates the OWL/RDF
   version of the schema (the "TBox").
3. `uv run linkml-convert -s <schema>.yaml -C <tree_root_class> -t ttl <instance>.yaml -o <instance>.ttl`
   — converts the instance YAML data to raw RDF/Turtle (the "ABox").
4. `uv run python3 src/postprocess_for_rdf.py --instance_file <instance>.ttl --output_file <instance>_rdf.ttl`
   — rewrites bare relation-class instances (e.g. `HasSignal`, `Contains`) into
   proper RDF predicate URIs, using the existing [`src/postprocess_for_rdf.py`](src/postprocess_for_rdf.py)
   script. This step is required — the raw `linkml-convert` output alone does not
   have correctly-typed relationship edges for the graph import to use.

Result: three files sitting next to the schema/instance sources, e.g.
`src/narad/schema/narad.owl.ttl`, `examples/core_acc_narad_instance.ttl`,
`examples/core_acc_narad_instance_rdf.ttl`.

### Stage 3 — Start the Docker stack (`docker_compose_up`)

1. Sets three environment variables for the `docker compose` subprocess only:
   `NEO4J_SCHEMA_TTL_PATH` and `NEO4J_INSTANCE_TTL_PATH`, pointing at the files
   generated in Stage 2, and `LINKML_SCHEMA_HOST_PATH`, pointing at the
   `--schema` YAML so `gradio-chat` describes the same schema to the LLM that
   the graph was built from.
2. If `--no-fresh` was **not** passed (the default): runs
   `docker compose down -v` to remove any previous containers **and volumes**
   (`neo4j_data`, `neo4j_plugins`), guaranteeing a clean graph.
3. Runs `docker compose up -d`. `docker-compose.yml`'s `neo4j-kg` service now
   mounts:
   ```yaml
   - ${NEO4J_SCHEMA_TTL_PATH:-./project/owl/narad.owl.ttl}:/data/narad.owl.ttl
   - ${NEO4J_INSTANCE_TTL_PATH:-./project/owl/core_acc_narad_instance_rdf.ttl}:/data/narad_instance.ttl
   ```
   so it picks up the freshly generated files (falling back to the old default
   paths if the env vars aren't set, e.g. for manual `docker compose up -d`
   runs).
4. Compose then brings up the dependency chain automatically:
   `neo4j-kg` (starts, waits for healthcheck) → `neo4j-init` (runs
   `graph_init.cypher`, imports the schema + instance TTL into Neo4j via the
   `n10s` plugin, then exits) → `gradio-chat` (starts once `neo4j-init`
   completes successfully).

### Stage 4 — Wait for the chat app (`wait_for_gradio_ready`)

Polls `gradio_client.Client(url)` every 3 seconds (up to `--startup-timeout`)
until the `gradio-chat` container's web server responds, since building/starting
that container can take a while (image build on first run, then app startup).

### Stage 5 — Ask every question (`run_benchmark` / `query_gradio`)

1. Reads every entry from `--queries` (a list of dicts) directly, with no schema
   validation beyond requiring the `--question-key` field (`Q` by default) on
   each entry.
2. `load_gradio_settings()` builds the full parameter set the `/respond` API
   endpoint expects (model name, base URL, API key, temperature, system
   prompt, graph-context toggle, Neo4j URI/user/password/database, reasoning
   toggle) from environment variables, mirroring the defaults `main.py`'s UI
   uses.
3. For each question, `query_gradio()` calls the `gradio-chat` app's
   `/respond` API endpoint via `gradio_client`, exactly as if a human had
   typed the question into the chat UI and clicked Send. It passes the running
   `history` list so far (unless `--no-accumulate-history` is set, in which
   case history is reset to empty before every question).
4. `extract_message_text()` normalizes the assistant's reply: newer Gradio/LLM
   responses can return `content` as a list of `{"type": "text", "text": ...}`
   blocks instead of a plain string; this flattens either shape into plain
   text before it's written out.
5. For each question, the result dict is a deep copy of the original queries
   entry (so `Ans` and any other extra fields are preserved as-is) with the
   `--llm-answer-key` field (`LLM_Ans` by default) added for the LLM's answer.
   The script asserts that key isn't already present in the entry, to avoid
   silently overwriting existing data. All results are collected into a list
   and written to `--answers` as YAML.

### Stage 6 — Cleanup

If `--delete-intermediate-files` was passed, the three generated `.ttl` files
from Stage 2 are deleted. The Docker containers/volumes are **left running**
intentionally, so you can continue using the interactive Gradio UI afterwards
without rebuilding the graph.

## 4. Supporting changes made on this branch

Beyond the new driver script, the following existing files were changed to
make the automation possible and fix bugs discovered while testing it
end-to-end:

- **[`docker-compose.yml`](docker-compose.yml)**
  - `neo4j-kg`'s TTL volume mounts are now overridable via
    `NEO4J_SCHEMA_TTL_PATH` / `NEO4J_INSTANCE_TTL_PATH` (set automatically by
    `run_pipeline.py`; not meant to be set by hand in `.env`).
  - Fixed a pre-existing bug: the instance volume now defaults to
    `core_acc_narad_instance_rdf.ttl` (the **postprocessed** file), not the
    raw `core_acc_narad_instance.ttl` — the raw file is missing correctly
    typed relationship predicates.
  - `gradio-chat`'s `environment:` block now also forwards
    `OPENAI_TEMPERATURE`, `OPENAI_SYSTEM_PROMPT`, `NEO4J_DATABASE`,
    `NEO4J_AGENT_MAX_ITERATIONS`, and `NEO4J_MANUAL_QUERY` from `.env` (previously
    silently ignored by Compose even though `.env.example` implied otherwise).
    `NEO4J_URI` is intentionally **not** made overridable — it must stay
    `bolt://neo4j-kg:7687` (the Docker-network service name) or the
    containerized app cannot reach Neo4j at all.

- **[`src/llm/main.py`](src/llm/main.py)**
  - `model_name` Dropdown now has `allow_custom_value=True`, so API-driven
    calls (from `run_pipeline.py`) can set a model name without first calling
    the UI's "Refresh Models" button.
  - `demo.launch(..., show_error=True)` so the real exception (e.g. an OpenAI
    API error) is returned to API callers, instead of a generic
    `AppError: ...has not enabled verbose error reporting` message.

- **[`pyproject.toml`](pyproject.toml) / `uv.lock`** — added `gradio-client`,
  `python-dotenv`, `pyyaml` to the `dev` dependency group so `run_pipeline.py`
  can run under `uv run`.

- **[`.env.example`](.env.example)** — documented every environment variable
  actually consulted by `main.py`/`kg_agent.py`/`run_pipeline.py`, including
  which ones are forwarded into the `gradio-chat` container by
  `docker-compose.yml` versus which only affect `run_pipeline.py`.

- **[`examples/benchmark_queries/UITF_v1.yaml`](examples/benchmark_queries/UITF_v1.yaml)**
  — reformatted from the old ad-hoc `Q1: """..."""` / `Ans1: """..."""` text
  format into the `{Q, Ans}` YAML list format `run_pipeline.py` expects.

## 5. Environment variables

See [`.env.example`](.env.example) for the full annotated list. In summary:

- **Required for the stack to start at all:** `NEO4J_USER`, `NEO4J_PASSWORD`,
  `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `LLM_MODEL_NAME`.
- **Forwarded into `gradio-chat` by `docker-compose.yml`** (affect both the
  interactive UI and `run_pipeline.py`): the above, plus
  `USE_GRAPH_CONTEXT`, `SHOW_REASONING`, `NEO4J_TRACE_MAX_CHARS`,
  `NEO4J_SCHEMA_CACHE_TTL_SECONDS`, `OPENAI_TEMPERATURE`,
  `OPENAI_SYSTEM_PROMPT`, `NEO4J_DATABASE`, `NEO4J_AGENT_MAX_ITERATIONS`,
  `NEO4J_MANUAL_QUERY`.
- **Hardcoded, not `.env`-overridable:** `NEO4J_URI` (must stay
  `bolt://neo4j-kg:7687` inside Docker).
- **Internal, set only by `run_pipeline.py` itself:**
  `NEO4J_SCHEMA_TTL_PATH`, `NEO4J_INSTANCE_TTL_PATH`, `LINKML_SCHEMA_HOST_PATH`.

## 6. Known caveats / things to be aware of

- **`--no-fresh` is only safe if the RDF content is unchanged since the last
  `up`.** Regenerating the `.ttl` files changes the volume-mount config for
  `neo4j-kg`, which makes Compose recreate that container, which in turn
  forces `neo4j-init` to re-run against a `neo4j_data` volume that may already
  contain a fully-imported graph — this trips the `n10s_unique_uri` constraint
  and fails. Default `--fresh` behaviour (`docker compose down -v`) avoids
  this entirely at the cost of always rebuilding the graph from scratch.
- **Secrets are visible via the Gradio app's public API schema.** Because
  `main.py`'s `api_key`/`neo4j_password` Textbox components are pre-filled
  from `.env` via `value=os.getenv(...)`, calling `gradio_client(...).view_api()`
  against a running `gradio-chat` instance reveals those default values in
  plaintext to **anyone with network access to port 7860**, authenticated or
  not. This is a pre-existing exposure surfaced (not introduced) while
  building this pipeline, and is not yet fixed on this branch.
- **Answers can differ between the interactive UI and the automated pipeline**
  even with the same model / 0 temperature, for two reasons unrelated to the
  pipeline's correctness: (1) LLM hallucination — e.g. confusing a device's
  physical floor-survey coordinates (`FloorP.x`/`.y`) with an unrelated beam
  position signal (`IPMK101.XPOS`/`.YPOS`) that has no value populated in the
  graph; (2) non-deterministic agentic tool-use search paths, which can be
  further influenced by how much prior chat history is accumulated
  (`--no-accumulate-history` can be used to isolate each question and reduce
  this effect for benchmarking).
- **Only `--transformation RDF` is implemented.** Any other value raises
  `NotImplementedError` — this is a placeholder for future non-RDF
  transformation strategies, per the original design brief for this branch.

## 7. Example Run

```bash
uv run python3 src/run_pipeline.py \
  --schema src/narad/schema/narad.yaml \
  --instance examples/core_acc_narad_instance.yaml \
  --queries examples/benchmark_queries/UITF_v1.yaml \
  --answers examples/benchmark_queries/UITF_v1_LLM_answers.yaml \
  --delete-intermediate-files
```
