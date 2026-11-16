

# Slot: y_rot 


_Rotation around the Y-axis in the facility floor plan._





URI: [pals_config:slot/y_rot](https://w3id.org/pals-config/slot/y_rot)
Alias: y_rot

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BodyShiftParamGroup](../classes/BodyShiftParamGroup.md) | Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [BodyShiftParamGroup](../classes/BodyShiftParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BodyShiftParamGroup](../classes/BodyShiftParamGroup.md) |









## Aliases


* delta_theta
* theta_shift
* GlobalOffsetTheta




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:y_rot |
| native | pals_config:y_rot |
| close | pals:y_rot |




## LinkML Source

<details>
```yaml
name: y_rot
description: Rotation around the Y-axis in the facility floor plan.
from_schema: https://w3id.org/pals-config
aliases:
- delta_theta
- theta_shift
- GlobalOffsetTheta
close_mappings:
- pals:y_rot
rank: 1000
alias: y_rot
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>