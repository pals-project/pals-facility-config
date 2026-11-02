

# Slot: EsL 


_Length-integrated skew component._





URI: [acc:slot/EsL](https://example.org/accelerator-core/slot/EsL)
Alias: EsL

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
| self | acc:EsL |
| native | acc:EsL |
| broad | pals:EsNL |




## LinkML Source

<details>
```yaml
name: EsL
description: Length-integrated skew component.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:EsNL
rank: 1000
alias: EsL
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float

```
</details>