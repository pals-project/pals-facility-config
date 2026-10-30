

# Slot: g_ref 


_Reference bend strength = 1/radius_ref_





URI: [acc:slot/g_ref](https://example.org/accelerator-core/slot/g_ref)
Alias: g_ref

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
| self | acc:g_ref |
| native | acc:g_ref |
| close | pals:g_ref |




## LinkML Source

<details>
```yaml
name: g_ref
description: Reference bend strength = 1/radius_ref
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:g_ref
rank: 1000
alias: g_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: 1/m

```
</details>