# Enum: CoordinateSystemEnum 




_Coordinate systems for spatial relationships._



URI: [pals_config:enum/CoordinateSystemEnum](https://w3id.org/pals-config/enum/CoordinateSystemEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Cartesian | None | Cartesian coordinate system (x, y, z). |
| Cylindrical | None | Cylindrical coordinate system (r, theta, z). |
| Spherical | None | Spherical coordinate system (r, theta, phi). |




## Slots

| Name | Description |
| ---  | --- |
| [coordinate_system](../slots/coordinate_system.md) | The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config






## LinkML Source

<details>
```yaml
name: CoordinateSystemEnum
description: Coordinate systems for spatial relationships.
from_schema: https://w3id.org/pals-config
rank: 1000
permissible_values:
  Cartesian:
    text: Cartesian
    description: Cartesian coordinate system (x, y, z).
  Cylindrical:
    text: Cylindrical
    description: Cylindrical coordinate system (r, theta, z).
  Spherical:
    text: Spherical
    description: Spherical coordinate system (r, theta, phi).

```
</details>