

# Slot: s_position 


_Longitudinal position of the element along the beamline._





URI: [pals:s_position](https://pals-project.readthedocs.io/s_position)
Alias: s_position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. <br>Corresponds to PALS's ungrouped element parameters `length` and `s_position`.<br>One (or both) `length` or `s_position` must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| Slot URI | [pals:s_position](https://pals-project.readthedocs.io/s_position) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:s_position |
| native | pals:s_position |




## LinkML Source

<details>
```yaml
name: s_position
description: Longitudinal position of the element along the beamline.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:s_position
alias: s_position
owner: LongitudinalPlacementParamGroup
domain_of:
- LongitudinalPlacementParamGroup
range: float

```
</details>