# NARAD-DataServices

This repository contains the code for the NARAD Data Services, which provide access to schemas and ontologies for the NARAD project. 
The services are built using LinkML and are designed to facilitate the integration and use of accelerator operations data across various applications.

## Prerequisites
Install [uv](https://docs.astral.sh/uv/), which manages the Python version,
virtual environment, and Python dependencies for this project:

```console
pipx install uv
```

See the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)
for alternatives to `pipx`. For detailed best practices for Python environments
with uv, see the [Berkeley BOP guide](https://berkeleybop.org/best_practice/python_environments).

Install [Just](https://github.com/casey/just), which provides the repository's
build and generation commands:

```console
uv tool install rust-just
```

The project also requires Git, CMake, and a C++ compiler to build its PALS
parser dependency.

## Environment Setup

Run the following commands from the NARAD-DataServices repository root. The
first command creates `.venv` and installs the dependencies declared in
`pyproject.toml` and locked in `uv.lock`:

```console
uv sync
```

The main project uses
[PALSParserPy](https://github.com/pals-project/PALSParserPy), a thin Python
wrapper around the shared library built by
[PALSParserCpp](https://github.com/pals-project/PALSParserCpp). Clone the two
parser repositories side by side, build the C++ library, and then install the
Python wrapper into the NARAD uv environment. This follows the upstream
[PALSParserPy installation guide](https://pals-project.github.io/PALSParserPy/guide/installation.html):

```console
cd ..
git clone https://github.com/pals-project/PALSParserCpp.git
git clone https://github.com/pals-project/PALSParserPy.git

cd PALSParserCpp && cmake -S . -B build && cmake --build build && cd ..

cd PALSParserPy
uv pip install --python ../NARAD-DataServices/.venv/bin/python -e .
cd ../NARAD-DataServices
```

The expected checkout layout is:

```text
parent-directory/
├── NARAD-DataServices/
├── PALSParserCpp/
└── PALSParserPy/
```

If PALSParserCpp is stored elsewhere, set `PALS_PARSER_CPP_DIR` to its checkout
or `PALS_PARSER_CPP_LIB` to the compiled shared library before using
PALSParserPy. Because PALSParserPy is installed separately rather than declared
in `pyproject.toml`, reinstall it after a future exact `uv sync` removes it.

Verify the complete environment with:

```console
uv run python -c "import palsparserpy; print(palsparserpy.__file__)"
uv run pytest
```

For example, generate a PALSParserPy-based NARAD skeleton and then the enriched
BtA instance with:

```console
uv run python src/narad_system/schema/palsparserpy_to_narad.py \
  -input examples/BtA/bta.pals.yaml
uv run python examples/BtA/generate_narad_bta_instance.py
```

## Known PALS-to-NARAD Gaps

The PALSParserPy translator currently produces a flattened, control-neutral
NARAD skeleton. PALSParserPy resolves expressions and expands the selected
lattice before NARAD mapping, but not every source concept has a corresponding
NARAD representation yet.

| PALS feature | Current behavior | Remaining gap |
| --- | --- | --- |
| Multiple branches | PALSParserPy expands all branches, including branches created by forks. | The translator currently requires exactly one branch per lattice. NARAD occurrence identity and relations across multiple beamlines still need to be defined. |
| Forks | PALSParserPy resolves fork destinations and creates the resulting branches. | NARAD has a `Fork` function value and `HasConnectingBranch` relation, but no concrete `Fork` component or `ForkP` parameter group. Fork elements and their connectivity are therefore not translated. |
| Multipass beamlines | The translator preserves the beamline-level `multipass` flag and emits a warning. | NARAD does not yet distinguish a shared physical component from its separate pass occurrences or relate those occurrences across passes. |
| Constants and variables | PALSParserPy evaluates them, and translated component parameters contain the resulting numeric values. | Named constants, variables, original expressions, and evaluation provenance are not retained in NARAD. |
| Controllers | PALSParserPy evaluates controller expressions before translation, so the controlled parameter values are present in the generated components. | Controller entities, knob variables, expressions, control types, and parameter-level dependencies are not represented. The existing NARAD `Controls` relation only describes component-to-component control. |
| Includes, inheritance, repeats, and expressions | These are resolved during PALS expansion, and their expanded component values and order are translated. | The generated skeleton does not preserve the original authoring constructs or their provenance. |
| Other unsupported element kinds | Unsupported expanded elements are reported and omitted. No precedence relation is created across the resulting gap. | Each kind needs an explicit NARAD class/mapping decision before the skeleton can represent the complete lattice. |

Until these gaps are addressed, generated skeletons should be treated as
resolved lattice snapshots rather than lossless round-trip representations of
the original PALS source.


## Repository Structure
* [docs/](docs/) - mkdocs-managed documentation
* [examples/](examples/) - Examples of using the schema
  * [archived/](examples/archived) -- archived examples
  * core_acc_narad_instance.yaml -- example of a core accelerator instance
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [archived/](src/archived) -- archived files
  * [narad](src/narad)
    * [schema/](src/narad/schema) -- LinkML schema (edit this)
    * [datamodel/](src/narad/datamodel) -- generated Python datamodel
    * narad.yaml -- LinkML schema for NARAD data services
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data files for testing

## Using the Schemas
* ```just gen-project```
  * Example of generating the project from the schema. This will generate a Python datamodel and associated files in `project/`: (json/jsonld schemas, OWL, sqlschema, etc).

* `just gen-doc`
  * Generates documentation from the schema into `docs/elements/`. The recipe
    takes no arguments; the following generator flags are set in the `gen-doc`
    recipe in `justfile`:
    * `--truncate-descriptions False`
    * `--diagram-type er_diagram`
    * `--example-directory doc_examples/`, where example files are located
    * `--subfolder-type-separation`, which generates documentation in
      subfolders for compatibility with mkdocs
    * `--template-directory docs/templates-linkml`
  * To pass extra flags, set `LINKML_GENERATORS_DOC_ARGS` in
    `config.public.mk`.

* ```just gen-python```
  * Example of generating the Python datamodel from the schema. This will generate Python classes in `src/narad/datamodel/` that correspond to the classes defined in the LinkML schema.

* ```uv run linkml-validate --schema src/narad/schema/narad.yaml  examples/core_acc_narad_instance.yaml```
  * Example of validating an entire data file against the schema. Add --target-class [CLASS_NAME] to validate against a specific class in the schema.

* Examples of invalid data files are in `tests/data/invalid/` and valid data files are in `tests/data/valid/`. You can validate these using the above command.
  * ```uv run linkml-validate --schema src/narad/schema/narad.yaml tests/data/invalid/narad_invalid.yaml --target-class NaradCapability```

* Generating an OWL/RDF graph of the schema:
  * ```uv run gen-owl  src/narad/schema/narad.yaml > "project/owl/narad.owl.ttl"```
  * This will generate an OWL/RDF graph of the schema in the `project/owl/` directory.  

  * Generate an OWL/RDF graph of the schema and instance data:
    * ```uv run linkml-convert -s src/narad/schema/narad.yaml -t rdf examples/core_acc_narad_instance.yaml -o project/owl/core_acc_narad_instance.ttl```
      * this will generate an OWL/RDF graph of the instance data in Turtle format. You can also use other formats such as RDF/XML or JSON-LD by changing the output file extension.
