

# Slot: order 


_Multipole order N (0 = dipole, 1 = quadrupole, etc.)_





URI: [pals:slot/order](https://pals-project.readthedocs.io/slot/order)
Alias: order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component.<br>Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.<br>Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | pals:order |
| native | pals:order |




## LinkML Source

<details>
```yaml
name: order
description: Multipole order N (0 = dipole, 1 = quadrupole, etc.)
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: order
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: integer
required: true

```
</details>