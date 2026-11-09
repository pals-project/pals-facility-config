

# Slot: y_offset 


_Shift in the Y direction in the facility floor plan._





URI: [pals_config:slot/y_offset](https://w3id.org/pals-config/slot/y_offset)
Alias: y_offset

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


* delta_y
* y_shift
* GlobalOffsetY




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:y_offset |
| native | pals_config:y_offset |
| close | pals:y_offset |




## LinkML Source

<details>
```yaml
name: y_offset
description: Shift in the Y direction in the facility floor plan.
from_schema: https://w3id.org/pals-config
aliases:
- delta_y
- y_shift
- GlobalOffsetY
close_mappings:
- pals:y_offset
rank: 1000
alias: y_offset
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>