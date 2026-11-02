

# Slot: s_position 


_Longitudinal position of the element along the beamline._





URI: [acc:slot/s_position](https://example.org/accelerator-core/slot/s_position)
Alias: s_position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:s_position |
| native | acc:s_position |
| close | pals:s_position |




## LinkML Source

<details>
```yaml
name: s_position
description: Longitudinal position of the element along the beamline.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:s_position
rank: 1000
alias: s_position
owner: LongitudinalPlacementParamGroup
domain_of:
- LongitudinalPlacementParamGroup
range: float
unit:
  ucum_code: m

```
</details>