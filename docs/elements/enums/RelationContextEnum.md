# Enum: RelationContextEnum 



URI: [acc:enum/RelationContextEnum](https://example.org/accelerator-core/enum/RelationContextEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| beamline_order | None | The order of components along the beamline. |
| Euclidean_3D | None | 3D Euclidean space. |
| Euclidean_2D | None | 2D Euclidean space. |
| floorplan | None | Floorplan coordinate system. |
| containment | None | Containment relationship context. |
| installation_mounting | None | Installation or mounting context. |




## Slots

| Name | Description |
| ---  | --- |
| [context](../slots/context.md) | The frame of reference / domain in which this relationship is asserted to hold. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: RelationContextEnum
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  beamline_order:
    text: beamline_order
    description: The order of components along the beamline.
    aliases:
    - beamline order
    - beamline sequence
    - order
    - sequence
  Euclidean_3D:
    text: Euclidean_3D
    description: 3D Euclidean space.
    aliases:
    - 3D Euclidean space
  Euclidean_2D:
    text: Euclidean_2D
    description: 2D Euclidean space.
    aliases:
    - 2D Euclidean space
  floorplan:
    text: floorplan
    description: Floorplan coordinate system.
    aliases:
    - floor plan
  containment:
    text: containment
    description: Containment relationship context.
    aliases:
    - containment
    - contains
  installation_mounting:
    text: installation_mounting
    description: Installation or mounting context.
    aliases:
    - installation
    - mounting
    - mounted

```
</details>