

# Slot: g_ref 


_Reference bend strength = 1/radius_ref_





URI: [pals:g_ref](https://pals-project.readthedocs.io/g_ref)
Alias: g_ref

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
| Slot URI | [pals:g_ref](https://pals-project.readthedocs.io/g_ref) |

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
| self | pals:g_ref |
| native | pals:g_ref |




## LinkML Source

<details>
```yaml
name: g_ref
description: Reference bend strength = 1/radius_ref
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:g_ref
alias: g_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float

```
</details>