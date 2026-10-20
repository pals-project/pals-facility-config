

# Slot: rho_ref 


_Reference bend radius._





URI: [pals:rho_ref](https://pals-project.readthedocs.io/rho_ref)
Alias: rho_ref

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
| Slot URI | [pals:rho_ref](https://pals-project.readthedocs.io/rho_ref) |

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
| self | pals:rho_ref |
| native | pals:rho_ref |




## LinkML Source

<details>
```yaml
name: rho_ref
description: Reference bend radius.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:rho_ref
alias: rho_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float

```
</details>