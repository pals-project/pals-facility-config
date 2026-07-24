

# Slot: BendP 


_A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:BendP](https://pals-project.readthedocs.io/BendP)
Alias: BendP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasBendP](HasBendP.md) |  |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [BendParamGroup](BendParamGroup.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:BendP |
| native | pals:BendP |




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