

# Slot: KnL 


_Length-integrated normalized normal component._





URI: [pals_config:slot/KnL](https://w3id.org/pals-config/slot/KnL)
Alias: KnL

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
| self | pals_config:KnL |
| native | pals_config:KnL |
| broad | pals:KnNL |




## LinkML Source

<details>
```yaml
name: KnL
description: Length-integrated normalized normal component.
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:KnNL
rank: 1000
alias: KnL
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>