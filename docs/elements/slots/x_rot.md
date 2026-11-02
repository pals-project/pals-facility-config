

# Slot: x_rot 


_Rotation around the X-axis in the facility floor plan._





URI: [acc:slot/x_rot](https://example.org/accelerator-core/slot/x_rot)
Alias: x_rot

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


* delta_phi
* phi_shift
* GlobalOffsetPhi




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:x_rot |
| native | acc:x_rot |
| close | pals:x_rot |




## LinkML Source

<details>
```yaml
name: x_rot
description: Rotation around the X-axis in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- delta_phi
- phi_shift
- GlobalOffsetPhi
close_mappings:
- pals:x_rot
rank: 1000
alias: x_rot
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>