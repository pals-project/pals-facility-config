

# Slot: rho_ref 


_Reference bend radius._





URI: [acc:slot/rho_ref](https://example.org/accelerator-core/slot/rho_ref)
Alias: rho_ref

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
**Unit:** `m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:rho_ref |
| native | acc:rho_ref |
| close | pals:rho_ref |




## LinkML Source

<details>
```yaml
name: rho_ref
description: Reference bend radius.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:rho_ref
rank: 1000
alias: rho_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: m

```
</details>