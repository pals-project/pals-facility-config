

# Slot: ref_geometry 


_Reference geometry type. Must be `arc`._





URI: [acc:slot/ref_geometry](https://example.org/accelerator-core/slot/ref_geometry)
Alias: ref_geometry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceGeometryEnum](../enums/ReferenceGeometryEnum.md) |
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
| self | acc:ref_geometry |
| native | acc:ref_geometry |
| close | pals:ref_geometry |




## LinkML Source

<details>
```yaml
name: ref_geometry
description: Reference geometry type. Must be `arc`.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:ref_geometry
rank: 1000
alias: ref_geometry
owner: BendParamGroup
domain_of:
- BendParamGroup
range: ReferenceGeometryEnum

```
</details>