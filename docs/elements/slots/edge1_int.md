

# Slot: edge1_int 


_Entrance end fringe field integral._





URI: [acc:slot/edge1_int](https://example.org/accelerator-core/slot/edge1_int)
Alias: edge1_int

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
**Unit:** `T.m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:edge1_int |
| native | acc:edge1_int |
| close | pals:edge1_int |




## LinkML Source

<details>
```yaml
name: edge1_int
description: Entrance end fringe field integral.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:edge1_int
rank: 1000
alias: edge1_int
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: T.m

```
</details>