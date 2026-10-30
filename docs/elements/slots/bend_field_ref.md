

# Slot: bend_field_ref 


_Reference bend field._





URI: [acc:slot/bend_field_ref](https://example.org/accelerator-core/slot/bend_field_ref)
Alias: bend_field_ref

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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:bend_field_ref |
| native | acc:bend_field_ref |
| close | pals:bend_field_ref |




## LinkML Source

<details>
```yaml
name: bend_field_ref
description: Reference bend field.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:bend_field_ref
rank: 1000
alias: bend_field_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: T

```
</details>