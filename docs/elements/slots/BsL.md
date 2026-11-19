

# Slot: BsL 


_Length-integrated skew component of the magnetic field._





URI: [pals_config:slot/BsL](https://w3id.org/pals-config/slot/BsL)
Alias: BsL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components. |  no  |






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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:BsL |
| native | pals_config:BsL |
| broad | pals:BsNL |




## LinkML Source

<details>
```yaml
name: BsL
description: Length-integrated skew component of the magnetic field.
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:BsNL
rank: 1000
alias: BsL
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>