

# Slot: tilt_ref 


_Reference tilt of the bend._





URI: [pals_config:slot/tilt_ref](https://w3id.org/pals-config/slot/tilt_ref)
Alias: tilt_ref

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
| self | pals_config:tilt_ref |
| native | pals_config:tilt_ref |
| close | pals:tilt_ref |




## LinkML Source

<details>
```yaml
name: tilt_ref
description: Reference tilt of the bend.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:tilt_ref
rank: 1000
alias: tilt_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: rad

```
</details>