

# Slot: Kn 


_Normalized normal component._





URI: [acc:slot/Kn](https://example.org/accelerator-core/slot/Kn)
Alias: Kn

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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:Kn |
| native | acc:Kn |
| broad | pals:KnN |




## LinkML Source

<details>
```yaml
name: Kn
description: Normalized normal component.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:KnN
rank: 1000
alias: Kn
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>