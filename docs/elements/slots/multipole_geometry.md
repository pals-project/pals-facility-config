

# Slot: multipole_geometry 


_Multipole geometry type. Must be `follows_ref_geometry`._





URI: [pals:multipole_geometry](https://pals-project.readthedocs.io/multipole_geometry)
Alias: multipole_geometry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.<br>This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultipoleGeometryEnum](../enums/MultipoleGeometryEnum.md) |
| Domain Of | [BendParamGroup](../classes/BendParamGroup.md) |
| Slot URI | [pals:multipole_geometry](https://pals-project.readthedocs.io/multipole_geometry) |

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
| self | pals:multipole_geometry |
| native | pals:multipole_geometry |




## LinkML Source

<details>
```yaml
name: multipole_geometry
description: Multipole geometry type. Must be `follows_ref_geometry`.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:multipole_geometry
alias: multipole_geometry
owner: BendParamGroup
domain_of:
- BendParamGroup
range: MultipoleGeometryEnum

```
</details>