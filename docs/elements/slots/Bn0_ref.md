

# Slot: Bn0_ref 


_Reference bend field._





URI: [pals_config:slot/Bn0_ref](https://w3id.org/pals-config/slot/Bn0_ref)
Alias: Bn0_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [BendParamGroup](../classes/BendParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BendParamGroup](../classes/BendParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `T`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Bn0_ref |
| native | pals_config:Bn0_ref |
| close | pals:Bn0_ref |




## LinkML Source

<details>
```yaml
name: Bn0_ref
description: Reference bend field.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:Bn0_ref
rank: 1000
alias: Bn0_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: T

```
</details>