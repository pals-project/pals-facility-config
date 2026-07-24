

# Slot: electricMultipoleP 


_A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:electricMultipoleP](https://pals-project.readthedocs.io/electricMultipoleP)
Alias: electricMultipoleP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [HasElectricMultipoleP](HasElectricMultipoleP.md) |  |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [ElectricMultipoleP](ElectricMultipoleP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:electricMultipoleP |
| native | pals:electricMultipoleP |




## LinkML Source

<details>
```yaml
name: electricMultipoleP
description: A mixin for electric multipole parameters that are aligned with PALS
  ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the
  Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: electricMultipoleP
owner: HasElectricMultipoleP
domain_of:
- HasElectricMultipoleP
range: ElectricMultipoleP

```
</details>