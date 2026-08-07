

# Slot: x_offset 


_Shift in the X direction in the facility floor plan._





URI: [pals:x_offset](https://pals-project.readthedocs.io/x_offset)
Alias: x_offset

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
| Slot URI | [pals:x_offset](https://pals-project.readthedocs.io/x_offset) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BodyShiftParamGroup](../classes/BodyShiftParamGroup.md) |









## Aliases


* delta_x
* x_shift
* GlobalOffsetX




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:x_offset |
| native | pals:x_offset |




## LinkML Source

<details>
```yaml
name: x_offset
description: Shift in the X direction in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- delta_x
- x_shift
- GlobalOffsetX
rank: 1000
slot_uri: pals:x_offset
alias: x_offset
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>