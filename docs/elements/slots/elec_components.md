

# Slot: elec_components 


_Electric multipole components, one per order N._





URI: [pals_config:slot/elec_components](https://w3id.org/pals-config/slot/elec_components)
Alias: elec_components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ElectricMultipoleParamGroup](../classes/ElectricMultipoleParamGroup.md) | Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7<br>  tilt: 0.7<br>- order: 3<br>  En: 27.3<br>- order: 2<br>  EnL: 3.47e1<br>``` |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) |
| Domain Of | [ElectricMultipoleParamGroup](../classes/ElectricMultipoleParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ElectricMultipoleParamGroup](../classes/ElectricMultipoleParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:elec_components |
| native | pals_config:elec_components |




## LinkML Source

<details>
```yaml
name: elec_components
description: Electric multipole components, one per order N.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: elec_components
owner: ElectricMultipoleParamGroup
domain_of:
- ElectricMultipoleParamGroup
range: MultipoleParameterGroup
multivalued: true
inlined: true
inlined_as_list: true

```
</details>