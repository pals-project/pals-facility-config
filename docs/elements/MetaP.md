

# Slot: MetaP 


_A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:MetaP](https://pals-project.readthedocs.io/MetaP)
Alias: MetaP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLineSection](BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizat... |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |
| [RadiationMonitor](RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate |  no  |
| [BookkeepingComponent](BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in t... |  no  |
| [Signal](Signal.md) | Semantic meaning of a control-system signal associated with a component |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  no  |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [HasMetaP](HasMetaP.md) |  |  no  |
| [Magnet](Magnet.md) | An accelerator device that produces a magnetic field for beam control |  no  |
| [DiagnosticDevice](DiagnosticDevice.md) | An accelerator device used to measure beam or machine state |  no  |
| [Component](Component.md) | A general class for accelerator components, which can be specialized into mor... |  no  |
| [BeamPositionMonitor](BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position |  no  |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [SupportingFacilityComponent](SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific ... |  no  |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |  no  |
| [BeamProfileMonitor](BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [Marker](Marker.md) | A virtual component used as a reference point or marker in the beamline struc... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [VirtualComponent](VirtualComponent.md) | A virtual or logical component that represents a concept, function, or role i... |  no  |
| [PhysicalComponent](PhysicalComponent.md) | A physical item that participates in or supports accelerator operation |  no  |






## Properties

* Range: [MetaParamGroup](MetaParamGroup.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:MetaP |
| native | pals:MetaP |




## LinkML Source

<details>
```yaml
name: MetaP
description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata
  Parameters) for interoperability with the Particle Accelerator Language Standard
  (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: MetaP
owner: HasMetaP
domain_of:
- HasMetaP
range: MetaParamGroup
inlined: true

```
</details>