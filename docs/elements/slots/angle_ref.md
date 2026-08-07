

# Slot: angle_ref 


_Reference bend angle._





URI: [pals:angle_ref](https://pals-project.readthedocs.io/angle_ref)
Alias: angle_ref

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
| Slot URI | [pals:angle_ref](https://pals-project.readthedocs.io/angle_ref) |

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
| self | pals:angle_ref |
| native | pals:angle_ref |




## LinkML Source

<details>
```yaml
name: angle_ref
description: Reference bend angle.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:angle_ref
alias: angle_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float

```
</details>