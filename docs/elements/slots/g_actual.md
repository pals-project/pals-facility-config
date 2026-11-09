

# Slot: g_actual 


_Actual bend strength = 1/radius_actual_





URI: [pals_config:slot/g_actual](https://w3id.org/pals-config/slot/g_actual)
Alias: g_actual

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
**Unit:** `1/m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:g_actual |
| native | pals_config:g_actual |
| close | pals:g_actual |




## LinkML Source

<details>
```yaml
name: g_actual
description: Actual bend strength = 1/radius_actual
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:g_actual
rank: 1000
alias: g_actual
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: 1/m

```
</details>