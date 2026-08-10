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