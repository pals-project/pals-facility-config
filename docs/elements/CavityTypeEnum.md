# Enum: CavityTypeEnum 




_The type of cavity, which determines the field configuration and mode structure._



URI: [pals:CavityTypeEnum](https://pals-project.readthedocs.io/CavityTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| STANDING_WAVE | None | Default |
| TRAVELING_WAVE | None | A cavity that supports traveling wave modes, typically with a waveguide struc... |




## Slots

| Name | Description |
| ---  | --- |
| [cavity_type](cavity_type.md) | Cavity type |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: CavityTypeEnum
description: The type of cavity, which determines the field configuration and mode
  structure.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  STANDING_WAVE:
    text: STANDING_WAVE
    description: Default. A cavity that supports standing wave modes, typically with
      fixed geometry and resonant frequencies.
  TRAVELING_WAVE:
    text: TRAVELING_WAVE
    description: A cavity that supports traveling wave modes, typically with a waveguide
      structure and phase velocity matching the beam.

```
</details>