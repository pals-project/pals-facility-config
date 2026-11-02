

# Slot: angle_ref 


_Reference bend angle._





URI: [acc:slot/angle_ref](https://example.org/accelerator-core/slot/angle_ref)
Alias: angle_ref

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
**Unit:** `rad`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:angle_ref |
| native | acc:angle_ref |
| close | pals:angle_ref |




## LinkML Source

<details>
```yaml
name: angle_ref
description: Reference bend angle.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:angle_ref
rank: 1000
alias: angle_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: rad

```
</details>