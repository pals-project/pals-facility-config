

# Slot: BendP 


_A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [acc:slot/BendP](https://example.org/accelerator-core/slot/BendP)
Alias: BendP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasBendP](../classes/HasBendP.md) |  |  no  |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |  no  |






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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:BendP |
| native | acc:BendP |




## LinkML Source

<details>
```yaml
name: BendP
description: A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters)
  for interoperability with the Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: BendP
owner: HasBendP
domain_of:
- HasBendP
range: BendParamGroup
inlined: true

```
</details>