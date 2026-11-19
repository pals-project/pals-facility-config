

# Slot: radius_ref 


_Reference bend radius._





URI: [pals_config:slot/radius_ref](https://w3id.org/pals-config/slot/radius_ref)
Alias: radius_ref

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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:radius_ref |
| native | pals_config:radius_ref |
| close | pals:radius_ref |




## LinkML Source

<details>
```yaml
name: radius_ref
description: Reference bend radius.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:radius_ref
rank: 1000
alias: radius_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: m

```
</details>