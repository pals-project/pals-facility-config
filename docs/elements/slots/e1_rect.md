

# Slot: e1_rect 


_Entrance end pole face rotation with respect to a rectangular geometry._





URI: [acc:slot/e1_rect](https://example.org/accelerator-core/slot/e1_rect)
Alias: e1_rect

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
| self | acc:e1_rect |
| native | acc:e1_rect |
| close | pals:e1_rect |




## LinkML Source

<details>
```yaml
name: e1_rect
description: Entrance end pole face rotation with respect to a rectangular geometry.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:e1_rect
rank: 1000
alias: e1_rect
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: rad

```
</details>