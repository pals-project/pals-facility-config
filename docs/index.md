# PALS Facility Configuration

A lightweight [LinkML](https://linkml.io/) schema for describing accelerator facilities in a
facility-agnostic way: their components, the beamline relationships between them, and the
control-system signals attached to them.

## Start here

| If you want to… | Go to |
| --- | --- |
| Browse every class, slot, enum and type | [Schema reference](elements/index.md) |
| See the top-level class of a facility description | [PALSAccelerator](elements/classes/PALSAccelerator.md) |
| Download the merged schema (imports resolved) | [narad.yaml](schema/narad.yaml) |
| See example facility descriptions | [examples/ on GitHub](https://github.com/pals-project/pals-facility-config/tree/main/examples) |
| Edit the schema itself | [src/narad/schema/ on GitHub](https://github.com/pals-project/pals-facility-config/tree/main/src/narad/schema) |

## Validating a file
```bash
uv run linkml-validate --schema src/narad/schema/narad.yaml examples/GUN_thru_MV.linkml.yaml
```

Without `--target-class`, a file is validated against the schema's root class, `PALSAccelerator`.

## About these pages
The **Schema reference** section is generated from the LinkML schema by `just gen-doc` on every
pull request and published here when changes reach `main`. Don't edit those pages by hand; change
the schema in `src/narad/schema/` instead. To preview the site locally, run `just testdoc`.