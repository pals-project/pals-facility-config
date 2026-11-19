

# Slot: bend_field_actual 


_Actual bend field._





URI: [pals_config:slot/bend_field_actual](https://w3id.org/pals-config/slot/bend_field_actual)
Alias: bend_field_actual

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
| self | pals_config:bend_field_actual |
| native | pals_config:bend_field_actual |
| close | pals:bend_field_actual |




## LinkML Source

<details>
```yaml
name: bend_field_actual
description: Actual bend field.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:bend_field_actual
rank: 1000
alias: bend_field_actual
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: T

```
</details>