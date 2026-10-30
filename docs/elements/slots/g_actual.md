

# Slot: g_actual 


_Actual bend strength = 1/radius_actual_





URI: [acc:slot/g_actual](https://example.org/accelerator-core/slot/g_actual)
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:g_actual |
| native | acc:g_actual |
| close | pals:g_actual |




## LinkML Source

<details>
```yaml
name: g_actual
description: Actual bend strength = 1/radius_actual
from_schema: https://w3id.org/accelerator-core
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