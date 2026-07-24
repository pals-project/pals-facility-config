

# Slot: floorP 


_A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:floorP](https://pals-project.readthedocs.io/floorP)
Alias: floorP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  no  |
| [Marker](Marker.md) | A virtual component used as a reference point or marker in the beamline struc... |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [BeamLineSection](BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizat... |  no  |
| [VirtualComponent](VirtualComponent.md) | A virtual or logical component that represents a concept, function, or role i... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [BookkeepingComponent](BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in t... |  no  |
| [SupportingFacilityComponent](SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific ... |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [BeamPositionMonitor](BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Magnet](Magnet.md) | An accelerator device that produces a magnetic field for beam control |  no  |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [PhysicalComponent](PhysicalComponent.md) | A physical item that participates in or supports accelerator operation |  no  |
| [BeamProfileMonitor](BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile |  no  |
| [RadiationMonitor](RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate |  no  |
| [HasFloorP](HasFloorP.md) |  |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [DiagnosticDevice](DiagnosticDevice.md) | An accelerator device used to measure beam or machine state |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [FloorP](FloorP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:floorP |
| native | pals:floorP |




## LinkML Source

<details>
```yaml
name: floorP
description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor
  Plan Parameters) for interoperability with the Particle Accelerator Language Standard
  (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: floorP
owner: HasFloorP
domain_of:
- HasFloorP
range: FloorP

```
</details>