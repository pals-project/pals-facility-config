

# Slot: edge2_int 


_Exit end fringe field integral._





URI: [acc:slot/edge2_int](https://example.org/accelerator-core/slot/edge2_int)
Alias: edge2_int

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
| self | acc:edge2_int |
| native | acc:edge2_int |
| close | pals:edge2_int |




## LinkML Source

<details>
```yaml
name: edge2_int
description: Exit end fringe field integral.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:edge2_int
rank: 1000
alias: edge2_int
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: T.m

```
</details>