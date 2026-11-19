

# Slot: EnL 


_Length-integrated normal component._





URI: [pals_config:slot/EnL](https://w3id.org/pals-config/slot/EnL)
Alias: EnL

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
| self | pals_config:EnL |
| native | pals_config:EnL |
| broad | pals:EnNL |




## LinkML Source

<details>
```yaml
name: EnL
description: Length-integrated normal component.
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:EnNL
rank: 1000
alias: EnL
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>