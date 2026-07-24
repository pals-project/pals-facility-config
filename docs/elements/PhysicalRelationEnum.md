# Enum: PhysicalRelationEnum 




_Controlled values for physical relation to the beamline._



URI: [pals:PhysicalRelationEnum](https://pals-project.readthedocs.io/PhysicalRelationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Inline | None | Beam passes through the physical component or beamline aperture |
| AttachedToPipe | None | Mechanically attached to the beam pipe or vacuum envelope |
| NearBeamLine | None | Near and operationally associated with the beamline |
| SupportingFacility | None | Supports accelerator operation without a specific beam-pipe placement |




## Slots

| Name | Description |
| ---  | --- |
| [beamline_relation](beamline_relation.md) | The relationship of the physical component to the beamline,  which can be use... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: PhysicalRelationEnum
description: Controlled values for physical relation to the beamline.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  Inline:
    text: Inline
    description: Beam passes through the physical component or beamline aperture.
      The physical component is physically on the beamline.
  AttachedToPipe:
    text: AttachedToPipe
    description: Mechanically attached to the beam pipe or vacuum envelope.
  NearBeamLine:
    text: NearBeamLine
    description: Near and operationally associated with the beamline.
  SupportingFacility:
    text: SupportingFacility
    description: Supports accelerator operation without a specific beam-pipe placement.

```
</details>