

# Slot: z_offset 


_Shift in the Z direction in the facility floor plan._





URI: [acc:slot/z_offset](https://example.org/accelerator-core/slot/z_offset)
Alias: z_offset

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


* delta_z
* z_shift
* GlobalOffsetZ




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:z_offset |
| native | acc:z_offset |
| close | pals:z_offset |




## LinkML Source

<details>
```yaml
name: z_offset
description: Shift in the Z direction in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- delta_z
- z_shift
- GlobalOffsetZ
close_mappings:
- pals:z_offset
rank: 1000
alias: z_offset
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>