# NARAD-DataServices

This repository contains the code for the NARAD Data Services, which provide access to schemas and ontologies for the NARAD project. 
The services are built using LinkML and are designed to facilitate the integration and use of accelerator operations data across various applications.

## Prerequisites
First, install UV, a Python version, build, and dependency management
system. UV provides a streamlined workflow for managing Python projects, including dependency installation, virtual environments, and project scaffolding.
```
pipx install uv
```
* https://docs.astral.sh/uv/getting-started/installation/
  * For detailed best practices for working with Python in UV, please see:
  https://berkeleybop.org/best_practice/python_environments.
  

Then add Just, a build and deployment tool that helps make
command-line build operations less cumbersome.
  * uv tool install rust-just
  * https://github.com/casey/just


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

## Using the Schemas
* ```just gen-project```
  * Example of generating the project from the schema. This will generate a Python datamodel and associated files in `project/`: (json/jsonld schemas, OWL, sqlschema, etc).
* ```just gen-doc```
  * Generates documentation from the schema into `docs/elements/`. The recipe takes no arguments; the following generator flags are set in the `gen-doc` recipe in `justfile`. 
    *  `--truncate-descriptions False `
    * `--diagram-type er_diagram` 
    * `--example-directory doc_examples/ ` (where example files are located)
    * `--subfolder-type-separation` (documentation generated into subfolders for compatibility with mkdocs)
  * To pass extra flags, set `LINKML_GENERATORS_DOC_ARGS` in `config.public.mk`.
* ```just gen-python```
  * Example of generating the Python datamodel from the schema. This will generate Python classes in `src/narad/datamodel/` that correspond to the classes defined in the LinkML schema.
* ```uv run linkml-validate --schema src/narad/schema/narad.yaml examples/core_acc_narad_instance.yaml```
  * Validates an entire data file against the schema. Without `--target-class`, the file is validated against the schema's root class, `PALSAccelerator`.
  * To validate against a specific class, add `--target-class [CLASS_NAME]`, for example:
    * ```uv run linkml-validate --schema src/narad/schema/narad.yaml --target-class PALSAccelerator examples/core_acc_narad_instance.yaml```
* Generating an OWL/RDF graph of the schema:
  * ```uv run gen-owl  src/narad/schema/narad.yaml > "project/owl/narad.owl.ttl"```
  * This will generate an OWL/RDF graph of the schema in the `project/owl/` directory.  

  * Generate an OWL/RDF graph of the schema and instance data:
    * ```uv run linkml-convert -s src/narad/schema/narad.yaml -t rdf examples/core_acc_narad_instance.yaml -o project/owl/core_acc_narad_instance.ttl```
      * this will generate an OWL/RDF graph of the instance data in Turtle format. You can also use other formats such as RDF/XML or JSON-LD by changing the output file extension.
      * To view or explore the generated graphs:
        * [Protégé](https://protege.stanford.edu/) -- open `project/owl/narad.owl.ttl` to browse the schema classes, then also open `project/owl/core_acc_narad_instance.ttl` to browse the instance data.
        * [WebVOWL](https://service.tib.eu/webvowl/) -- upload `project/owl/narad.owl.ttl` for a browser diagram of the schema (schema only, not instance data).
        * [rdflib](https://rdflib.readthedocs.io/) -- load either `.ttl` file in Python to query it with SPARQL (already installed as a LinkML dependency).
