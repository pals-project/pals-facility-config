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

Then add Copier, a templating system for building repositories with predefined dependencies.
  * uv tool install --with jinja2-time copier
  * https://copier.readthedocs.io/en/stable/
   
Then add Just, a build and deployment tool that helps make
command-line build operations less cumbersome.
  * uv tool install rust-just
  * https://github.com/casey/just


## Repository Structure
* [docs/](docs/) - mkdocs-managed documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [narad_system](src/narad_system)
    * [schema/](src/narad_system/schema) -- LinkML schema (edit this)
    * [datamodel/](src/narad_system/datamodel) -- generated Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data files for testing

## Using the Schemas
* just gen-project
  * Example of generating the project from the schema. This will generate a Python datamodel and associated files in `project/`: (json/jsonld schemas, OWL, sqlschema, etc).

* just gen-doc
  * Example of generating documentation from the schema.

* uv run linkml-validate --schema src/narad_system/schema/narad_system.yaml  src/narad_system/schema/narad_UITF_instance.yaml
  * Example of validating an entire data file against the schema. Add --target-class [CLASS_NAME] to validate against a specific class in the schema.

* Examples of invalid data files are in `tests/data/invalid/` and valid data files are in `tests/data/valid/`. You can validate these using the above command.
  * uv run linkml-validate --schema src/narad_system/schema/narad_system.yaml tests/data/problem/invalid/narad_invalid.yaml --target-class NaradCapability