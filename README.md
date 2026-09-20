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

* ```just gen-doc --truncate-descriptions False --example-directory doc_examples/ --subfolder-type-separation```
  * Example of generating documentation from the schema. Use these arguments to control the output of the documentation generation. The `--example-directory` argument specifies the directory where example files are located, and the `--subfolder-type-separation` argument indicates that the documentation should be organized into subfolders based on type separation. `--subfolder-type-separation` is important for generating the documentation in a way that is compatible with mkdocs (used to build the documentation site) on macOS.

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
