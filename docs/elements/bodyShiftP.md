

# Slot: bodyShiftP 


_A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:bodyShiftP](https://pals-project.readthedocs.io/bodyShiftP)
Alias: bodyShiftP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [Marker](Marker.md) | A virtual component used as a reference point or marker in the beamline struc... |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [BeamLineSection](BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizat... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [BookkeepingComponent](BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in t... |  no  |
| [HasBodyShiftP](HasBodyShiftP.md) |  |  no  |
| [SupportingFacilityComponent](SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific ... |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [BeamPositionMonitor](BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Magnet](Magnet.md) | An accelerator device that produces a magnetic field for beam control |  no  |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [BeamProfileMonitor](BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile |  no  |
| [RadiationMonitor](RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [BodyShiftP](BodyShiftP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:bodyShiftP |
| native | pals:bodyShiftP |




## LinkML Source

<details>
```yaml
name: bodyShiftP
description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP
  (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator
  Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: bodyShiftP
owner: HasBodyShiftP
domain_of:
- HasBodyShiftP
range: BodyShiftP

```
</details>