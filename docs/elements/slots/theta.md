

# Slot: theta 


_Orientation angle around the Y-axis in the facility floor plan._





URI: [acc:slot/theta](https://example.org/accelerator-core/slot/theta)
Alias: theta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FloorParamGroup](../classes/FloorParamGroup.md) | Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [FloorParamGroup](../classes/FloorParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FloorParamGroup](../classes/FloorParamGroup.md) |









## Aliases


* theta_angle
* ModelYaw
* Model_Yaw




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:theta |
| native | acc:theta |
| close | pals:theta |




## LinkML Source

<details>
```yaml
name: theta
description: Orientation angle around the Y-axis in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- theta_angle
- ModelYaw
- Model_Yaw
close_mappings:
- pals:theta
rank: 1000
alias: theta
owner: FloorParamGroup
domain_of:
- FloorParamGroup
range: float

```
</details>