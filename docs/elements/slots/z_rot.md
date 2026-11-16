

# Slot: z_rot 


_Rotation around the Z-axis in the facility floor plan._





URI: [pals_config:slot/z_rot](https://w3id.org/pals-config/slot/z_rot)
Alias: z_rot

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


* delta_psi
* psi_shift
* GlobalOffsetPsi




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:z_rot |
| native | pals_config:z_rot |
| close | pals:z_rot |




## LinkML Source

<details>
```yaml
name: z_rot
description: Rotation around the Z-axis in the facility floor plan.
from_schema: https://w3id.org/pals-config
aliases:
- delta_psi
- psi_shift
- GlobalOffsetPsi
close_mappings:
- pals:z_rot
rank: 1000
alias: z_rot
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>