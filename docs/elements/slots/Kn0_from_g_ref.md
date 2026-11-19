

# Slot: Kn0_from_g_ref 


_Whether the normal dipole component defaults to the value computed from the reference curvature or reference bend field._





URI: [pals_config:slot/Kn0_from_g_ref](https://w3id.org/pals-config/slot/Kn0_from_g_ref)
Alias: Kn0_from_g_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [BendParamGroup](../classes/BendParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BendParamGroup](../classes/BendParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Kn0_from_g_ref |
| native | pals_config:Kn0_from_g_ref |
| close | pals:Kn0_from_g_ref |




## LinkML Source

<details>
```yaml
name: Kn0_from_g_ref
description: Whether the normal dipole component defaults to the value computed from
  the reference curvature or reference bend field.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:Kn0_from_g_ref
rank: 1000
alias: Kn0_from_g_ref
owner: BendParamGroup
domain_of:
- BendParamGroup
range: boolean

```
</details>