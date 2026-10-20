

# Slot: LongitudinalPlacementP 


_A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:slot/LongitudinalPlacementP](https://pals-project.readthedocs.io/slot/LongitudinalPlacementP)
Alias: LongitudinalPlacementP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md) |  |  no  |
| [Kicker](../classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Cavity](../classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |  no  |
| [Quadrupole](../classes/Quadrupole.md) | A magnet primarily used to focus or defocus the beam. 4 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [CrabCavity](../classes/CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflecting. |  no  |
| [PhysicalComponent](../classes/PhysicalComponent.md) | A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system. |  no  |
| [RadiationMonitor](../classes/RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate. |  no  |
| [Sextupole](../classes/Sextupole.md) | A magnet primarily used to focus or defocus the beam. 6 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [ACKicker](../classes/ACKicker.md) | An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression. |  no  |
| [Multipole](../classes/Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or octupole.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |  no  |
| [Solenoid](../classes/Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing.<br>A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. |  no  |
| [Magnet](../classes/Magnet.md) | An accelerator device that produces a magnetic field for beam control. |  no  |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile. |  no  |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting. |  no  |
| [Aperture](../classes/Aperture.md) | A diagnostic or limiting aperture element used to constrain or characterize beam passage. |  no  |
| [DiagnosticDevice](../classes/DiagnosticDevice.md) | An accelerator device used to measure beam or machine state. |  no  |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position. |  no  |
| [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline. |  no  |
| [RFCavity](../classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |  no  |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is superconducting. |  no  |
| [Octupole](../classes/Octupole.md) | A magnet primarily used to focus or defocus the beam. 8 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| Domain Of | [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:LongitudinalPlacementP |
| native | pals:LongitudinalPlacementP |




## LinkML Source

<details>
```yaml
name: LongitudinalPlacementP
description: A mixin for an element's extent and position along the longitudinal (beam-direction,
  "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement
  Parameters) for interoperability with the Particle Accelerator Language Standard
  (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: LongitudinalPlacementP
owner: HasLongitudinalPlacementP
domain_of:
- HasLongitudinalPlacementP
range: LongitudinalPlacementParamGroup
inlined: true

```
</details>