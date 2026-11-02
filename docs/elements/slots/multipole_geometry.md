

# Slot: multipole_geometry 


_Multipole geometry type. Must be `follows_ref_geometry`._





URI: [acc:slot/multipole_geometry](https://example.org/accelerator-core/slot/multipole_geometry)
Alias: multipole_geometry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultipoleGeometryEnum](../enums/MultipoleGeometryEnum.md) |
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:multipole_geometry |
| native | acc:multipole_geometry |
| close | pals:multipole_geometry |




## LinkML Source

<details>
```yaml
name: multipole_geometry
description: Multipole geometry type. Must be `follows_ref_geometry`.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:multipole_geometry
rank: 1000
alias: multipole_geometry
owner: BendParamGroup
domain_of:
- BendParamGroup
range: MultipoleGeometryEnum

```
</details>