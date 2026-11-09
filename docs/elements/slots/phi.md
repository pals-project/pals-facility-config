

# Slot: phi 


_Rotation around the X-axis in the facility floor plan._





URI: [pals_config:slot/phi](https://w3id.org/pals-config/slot/phi)
Alias: phi

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


* phi_angle
* ModelPitch
* Model_Pitch




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:phi |
| native | pals_config:phi |
| close | pals:phi |




## LinkML Source

<details>
```yaml
name: phi
description: Rotation around the X-axis in the facility floor plan.
from_schema: https://w3id.org/pals-config
aliases:
- phi_angle
- ModelPitch
- Model_Pitch
close_mappings:
- pals:phi
rank: 1000
alias: phi
owner: FloorParamGroup
domain_of:
- FloorParamGroup
range: float

```
</details>