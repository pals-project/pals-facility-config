

# Slot: psi 


_Rotation around the Z-axis in the facility floor plan._





URI: [acc:slot/psi](https://example.org/accelerator-core/slot/psi)
Alias: psi

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


* psi_angle
* Model_Roll
* Rotation




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:psi |
| native | acc:psi |
| close | pals:psi |




## LinkML Source

<details>
```yaml
name: psi
description: Rotation around the Z-axis in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- psi_angle
- Model_Roll
- Rotation
close_mappings:
- pals:psi
rank: 1000
alias: psi
owner: FloorParamGroup
domain_of:
- FloorParamGroup
range: float

```
</details>