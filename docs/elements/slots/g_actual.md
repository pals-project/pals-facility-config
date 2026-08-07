

# Slot: g_actual 


_Actual bend strength = 1/radius_actual_





URI: [pals:g_actual](https://pals-project.readthedocs.io/g_actual)
Alias: g_actual

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.<br>This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [BendParamGroup](../classes/BendParamGroup.md) |
| Slot URI | [pals:g_actual](https://pals-project.readthedocs.io/g_actual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BendParamGroup](../classes/BendParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:g_actual |
| native | pals:g_actual |




## LinkML Source

<details>
```yaml
name: g_actual
description: Actual bend strength = 1/radius_actual
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:g_actual
alias: g_actual
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float

```
</details>