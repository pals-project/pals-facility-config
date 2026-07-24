# Enum: ReferenceGeometryEnum 




_The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles._



URI: [pals:ReferenceGeometryEnum](https://pals-project.readthedocs.io/ReferenceGeometryEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| arc | None | Default |
| chord | None | Z-axis is the chord connecting the entrance origin point to the exit origin p... |
| entrance_coords | None | Rectangular coordinates commensurate with the entrance coordinates |
| exit_coords | None | Rectangular coordinates commensurate with the exit coordinates |




## Slots

| Name | Description |
| ---  | --- |
| [ref_geometry](ref_geometry.md) | Reference geometry type |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: ReferenceGeometryEnum
description: The reference geometry used to calculate multipoles.  Sets the geometry
  used to calculate multipoles.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  arc:
    text: arc
    description: Default. Reference are the curvelinear arc coordinates.
  chord:
    text: chord
    description: Z-axis is the chord connecting the entrance origin point to the exit
      origin point.
  entrance_coords:
    text: entrance_coords
    description: Rectangular coordinates commensurate with the entrance coordinates.
  exit_coords:
    text: exit_coords
    description: Rectangular coordinates commensurate with the exit coordinates.

```
</details>