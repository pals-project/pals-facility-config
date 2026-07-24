

# Slot: referenceP 


_A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:referenceP](https://pals-project.readthedocs.io/referenceP)
Alias: referenceP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasReferenceP](HasReferenceP.md) |  |  no  |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |  no  |
| [BeamProfileMonitor](BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [BeamPositionMonitor](BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Magnet](Magnet.md) | An accelerator device that produces a magnetic field for beam control |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [ReferenceP](ReferenceP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:referenceP |
| native | pals:referenceP |




## LinkML Source

<details>
```yaml
name: referenceP
description: A mixin for reference parameters that are aligned with PALS ReferenceP
  (Reference Parameters) for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: referenceP
owner: HasReferenceP
domain_of:
- HasReferenceP
range: ReferenceP

```
</details>