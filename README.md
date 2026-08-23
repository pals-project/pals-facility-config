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

* ```just gen-doc --example-directory examples/ --subfolder-type-separation```
  * Example of generating documentation from the schema. The just command for `gen-doc` applies the following arguments: `--example-directory` argument specifies the directory where example files are located, and the `--subfolder-type-separation` argument indicates that the documentation should be organized into subfolders based on type separation. `--subfolder-type-separation` is important for generating the documentation in a way that is compatible with mkdocs (used to build the documentation site) on macOS.

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
    * ```uv run linkml-convert -s src/narad/schema/narad.yaml -t ttl examples/core_acc_narad_instance.yaml -o project/owl/core_acc_narad_instance.ttl```
      * this will generate an OWL/RDF graph of the instance data in Turtle format. You can also use other formats such as RDF/XML or JSON-LD by changing the output file extension.
    
* Generating an OWL/RDF graph of the schema:
  * ```just gen-owl```
  * This will generate an OWL/RDF graph of the schema (the ontology's classes and properties) in `project/owl/narad.owl.ttl`.

* Generating an OWL/RDF graph of instance data:
  * ```just gen-instance-ttl [instance_file]```
  * This will generate an OWL/RDF graph of the given instance data in Turtle format, in `project/owl/`. `instance_file` defaults to `examples/core_acc_narad_instance.yaml` if omitted.
  * Note: the raw output of this step has a known limitation — LinkML's type-designator mechanism (used for the `kind` and `predicate` slots) serializes class names as plain string literals rather than as proper RDF resources (e.g. `rdf:type "BeamPositionMonitor"` instead of `rdf:type pals:BeamPositionMonitor`). Use `just gen-post` (below) to fix this before loading the data into a tool like Protégé.

* Postprocessing instance data to fix `kind`/`predicate` typing:
  * ```just gen-post [instance_file]```
  * Runs `gen-instance-ttl` and then rewrites the literal `kind`/`predicate` values into proper resource IRIs (e.g. `pals:BeamPositionMonitor`, `pals:precedes`), producing `project/owl/<instance_file_stem>_rdf.ttl`.

* Merging the schema ontology with postprocessed instance data:
  * ```just gen-merge [instance_file]```
  * Runs `gen-owl` and `gen-post`, then merges the resulting ontology and instance graphs into a single file, `project/owl/<instance_file_stem>_full.ttl`. This is the file to load into Protégé (or any other OWL tool) to see both the schema's classes and the instance data's individuals together.

* Running the full pipeline in one step:
  * ```just gen-post-merge [instance_file]```
  * Equivalent to running `gen-owl`, `gen-instance-ttl`, `gen-post`, and `gen-merge` in order for the given instance file. `instance_file` defaults to `examples/core_acc_narad_instance.yaml`; pass a different path (e.g. `just gen-post-merge examples/other_beamline_instance.yaml`) to run the pipeline against a different data instance.