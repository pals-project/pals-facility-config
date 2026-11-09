

# Slot: tilt 


_Tilt of the Nth multipole._





URI: [pals_config:slot/tilt](https://w3id.org/pals-config/slot/tilt)
Alias: tilt

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


<details>
<summary>Additional Constraints</summary>
**Unit:** `rad`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:tilt |
| native | pals_config:tilt |
| broad | pals:tilt |




## LinkML Source

<details>
```yaml
name: tilt
description: Tilt of the Nth multipole.
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:tilt
rank: 1000
alias: tilt
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: float
unit:
  ucum_code: rad

```
</details>