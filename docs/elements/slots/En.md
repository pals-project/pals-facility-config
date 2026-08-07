

# Slot: En 


_Normal component of the field._





URI: [pals:slot/En](https://pals-project.readthedocs.io/slot/En)
Alias: En

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component.<br>Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.<br>Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:En |
| native | pals:En |
| broad | pals:EnN |




## LinkML Source

<details>
```yaml
name: En
description: Normal component of the field.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:EnN
rank: 1000
alias: En
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>