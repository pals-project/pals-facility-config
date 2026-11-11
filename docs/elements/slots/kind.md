

# Slot: kind 


_The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor` (no prefix)._





URI: [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type)
Alias: kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kicker](../classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Octupole](../classes/Octupole.md) | A magnet primarily used to focus or defocus the beam. 8 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Drift](../classes/Drift.md) | A field-free space between beamline components. A Drift is a virtual beamline component whose longitudinal extent preserves the separation between adjacent physical or virtual components. |  no  |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is superconducting. |  no  |
| [CrabCavity](../classes/CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflecting. |  no  |
| [ACKicker](../classes/ACKicker.md) | An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression. |  no  |
| [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline. |  no  |
| [Marker](../classes/Marker.md) | A virtual component used as a reference point or marker in the beamline structure. |  no  |
| [Sextupole](../classes/Sextupole.md) | A magnet primarily used to focus or defocus the beam. 6 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Solenoid](../classes/Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing.<br>A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. |  no  |
| [DiagnosticDevice](../classes/DiagnosticDevice.md) | An accelerator device used to measure beam or machine state. |  no  |
| [Cavity](../classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |  no  |
| [Component](../classes/Component.md) | A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc. |  no  |
| [Multipole](../classes/Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or octupole.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [BeginningEle](../classes/BeginningEle.md) | Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch. |  no  |
| [BeamLineSection](../classes/BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components. |  no  |
| [BookkeepingComponent](../classes/BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices. |  no  |
| [PhysicalComponent](../classes/PhysicalComponent.md) | A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system. |  no  |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |  no  |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile. |  no  |
| [Node](../classes/Node.md) | Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology. |  no  |
| [VirtualComponent](../classes/VirtualComponent.md) | A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices. |  no  |
| [RFCavity](../classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |  no  |
| [Magnet](../classes/Magnet.md) | An accelerator device that produces a magnetic field for beam control. |  no  |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  no  |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting. |  no  |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position. |  no  |
| [Aperture](../classes/Aperture.md) | A diagnostic or limiting aperture element used to constrain or characterize beam passage. |  no  |
| [Quadrupole](../classes/Quadrupole.md) | A magnet primarily used to focus or defocus the beam. 4 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |
| [RadiationMonitor](../classes/RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Node](../classes/Node.md), [PALSAccelerator](../classes/PALSAccelerator.md) |
| Slot URI | [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Designates Type | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:type |
| native | pals_config:kind |
| related | saref:DeviceKind |




## LinkML Source

<details>
```yaml
name: kind
description: The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor`
  (no prefix).
from_schema: https://w3id.org/pals-config
related_mappings:
- saref:DeviceKind
rank: 1000
slot_uri: rdf:type
designates_type: true
alias: kind
domain_of:
- Node
- PALSAccelerator
range: string
required: true

```
</details>