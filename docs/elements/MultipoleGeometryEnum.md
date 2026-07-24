# Enum: MultipoleGeometryEnum 




_The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles._



URI: [pals:MultipoleGeometryEnum](https://pals-project.readthedocs.io/MultipoleGeometryEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| follows_ref_geometry | None | Use geometry equivalent to the setting of `ref_geometry` |
| vertically_pure | None | Vertically pure multipoles with arc geometry |
| horizontally_pure | None | Horizontally pure multipoles with arc geometry |
| chord | None | Z-axis is the chord connecting the entrance origin point to the exit origin p... |
| entrance_coords | None | Rectangular coordinates commensurate with the entrance coordinates |
| exit_coords | None | Rectangular coordinates commensurate with the exit coordinates |




## Slots

| Name | Description |
| ---  | --- |
| [multipole_geometry](multipole_geometry.md) | Multipole geometry type |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: MultipoleGeometryEnum
description: The geometric configuration of the multipole field.  Sets the geometry
  used to calculate multipoles.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  follows_ref_geometry:
    text: follows_ref_geometry
    description: Use geometry equivalent to the setting of `ref_geometry`.
  vertically_pure:
    text: vertically_pure
    description: Vertically pure multipoles with arc geometry.
  horizontally_pure:
    text: horizontally_pure
    description: Horizontally pure multipoles with arc geometry.
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