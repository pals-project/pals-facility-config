

# Slot: ReferenceP 


_A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals_config:slot/ReferenceP](https://w3id.org/pals-config/slot/ReferenceP)
Alias: ReferenceP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kicker](../classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Octupole](../classes/Octupole.md) | A magnet primarily used to focus or defocus the beam. 8 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is superconducting. |  no  |
| [CrabCavity](../classes/CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflecting. |  no  |
| [ACKicker](../classes/ACKicker.md) | An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression. |  no  |
| [Sextupole](../classes/Sextupole.md) | A magnet primarily used to focus or defocus the beam. 6 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Solenoid](../classes/Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing.<br>A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. |  no  |
| [Cavity](../classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |  no  |
| [HasReferenceP](../classes/HasReferenceP.md) |  |  no  |
| [Multipole](../classes/Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or octupole.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [BeginningEle](../classes/BeginningEle.md) | Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch. |  no  |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |  no  |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile. |  no  |
| [RFCavity](../classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |  no  |
| [Magnet](../classes/Magnet.md) | An accelerator device that produces a magnetic field for beam control. |  no  |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting. |  no  |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position. |  no  |
| [Aperture](../classes/Aperture.md) | A diagnostic or limiting aperture element used to constrain or characterize beam passage. |  no  |
| [Quadrupole](../classes/Quadrupole.md) | A magnet primarily used to focus or defocus the beam. 4 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| Domain Of | [HasReferenceP](../classes/HasReferenceP.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HasReferenceP](../classes/HasReferenceP.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:ReferenceP |
| native | pals_config:ReferenceP |




## LinkML Source

<details>
```yaml
name: ReferenceP
description: A mixin for reference parameters that are aligned with PALS ReferenceP
  (Reference Parameters) for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: ReferenceP
owner: HasReferenceP
domain_of:
- HasReferenceP
range: ReferenceParamGroup
inlined: true

```
</details>