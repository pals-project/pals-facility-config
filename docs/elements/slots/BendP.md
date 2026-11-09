

# Slot: BendP 


_A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals_config:slot/BendP](https://w3id.org/pals-config/slot/BendP)
Alias: BendP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |  no  |
| [HasBendP](../classes/HasBendP.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BendParamGroup](../classes/BendParamGroup.md) |
| Domain Of | [HasBendP](../classes/HasBendP.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HasBendP](../classes/HasBendP.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:BendP |
| native | pals_config:BendP |




## LinkML Source

<details>
```yaml
name: BendP
description: A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters)
  for interoperability with the Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: BendP
owner: HasBendP
domain_of:
- HasBendP
range: BendParamGroup
inlined: true

```
</details>