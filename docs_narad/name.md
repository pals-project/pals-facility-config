

# Slot: name 


_Human-readable name or local string key for the entity._





URI: [narad:name](https://w3id.org/narad_linkml/schema/narad/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect... |  no  |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile that extends a gen... |  no  |
| [BPM](BPM.md) | A Beam Position Monitor |  no  |
| [SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |  no  |
| [Dipole](Dipole.md) | A dipole bending magnet |  no  |
| [CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |  no  |
| [Corrector](Corrector.md) | A dipole corrector magnet for orbit correction |  no  |
| [DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [Quadrupole](Quadrupole.md) | A quadrupole focusing/defocusing magnet |  no  |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds type-specific ... |  no  |
| [Magnet](Magnet.md) | A powered magnet device (generic supertype for all magnet kinds) |  no  |
| [CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |  no  |
| [Marker](Marker.md) | A zero-length reference point, drift space, or survey marker |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |
| [QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |  no  |
| [FacilityConfig](FacilityConfig.md) | Facility-specific signal binding configuration |  no  |
| [Solenoid](Solenoid.md) | A solenoid magnet |  no  |
| [InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |  no  |
| [BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [RFCavity](RFCavity.md) | A radio-frequency accelerating or bunching cavity |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  no  |
| [ElementParamSet](ElementParamSet.md) | Named physics-parameter block for a beamline element |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure ... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:name |
| native | narad:name |




## LinkML Source

<details>
```yaml
name: name
description: Human-readable name or local string key for the entity.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
identifier: true
alias: name
domain_of:
- NamedThing
range: string
required: true

```
</details>