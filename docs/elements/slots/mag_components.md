

# Slot: mag_components 


_Magnetic multipole components, one per order N._





URI: [acc:slot/mag_components](https://example.org/accelerator-core/slot/mag_components)
Alias: mag_components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) | Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7<br>  tilt: 0.7<br>- order: 3<br>  Bn: 27.3<br>- order: 2<br>  BnL: 3.47e1<br>- order: 1<br>  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength<br>``` |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) |
| Domain Of | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:mag_components |
| native | acc:mag_components |




## LinkML Source

<details>
```yaml
name: mag_components
description: Magnetic multipole components, one per order N.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: mag_components
owner: MagneticMultipoleParamGroup
domain_of:
- MagneticMultipoleParamGroup
range: MultipoleParameterGroup
multivalued: true
inlined: true
inlined_as_list: true

```
</details>