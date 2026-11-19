

# Slot: e2_rect 


_Exit end pole face rotation with respect to a rectangular geometry._





URI: [pals_config:slot/e2_rect](https://w3id.org/pals-config/slot/e2_rect)
Alias: e2_rect

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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:e2_rect |
| native | pals_config:e2_rect |
| close | pals:e2_rect |




## LinkML Source

<details>
```yaml
name: e2_rect
description: Exit end pole face rotation with respect to a rectangular geometry.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:e2_rect
rank: 1000
alias: e2_rect
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: rad

```
</details>