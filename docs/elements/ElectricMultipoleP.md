

# Slot: ElectricMultipoleP 


_A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:ElectricMultipoleP](https://pals-project.readthedocs.io/ElectricMultipoleP)
Alias: ElectricMultipoleP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [HasElectricMultipoleP](HasElectricMultipoleP.md) |  |  no  |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |






## Properties

* Range: [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:ElectricMultipoleP |
| native | pals:ElectricMultipoleP |




## LinkML Source

<details>
```yaml
name: ElectricMultipoleP
description: A mixin for electric multipole parameters that are aligned with PALS
  ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the
  Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: ElectricMultipoleP
owner: HasElectricMultipoleP
domain_of:
- HasElectricMultipoleP
range: ElectricMultipoleParamGroup
inlined: true

```
</details>