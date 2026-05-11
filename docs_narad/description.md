

# Slot: description 


_Detailed description of the entity._





URI: [narad:description](https://w3id.org/narad_linkml/schema/narad/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |
| [MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |  no  |
| [SignalBinding](SignalBinding.md) | A named control system suffix definition for one semantic signal |  no  |
| [CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |  no  |
| [ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |  no  |
| [CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  no  |
| [InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |  no  |
| [DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |  no  |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |  no  |
| [BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |
| [QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |  no  |
| [SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:description |
| native | narad:description |




## LinkML Source

<details>
```yaml
name: description
description: Detailed description of the entity.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: description
domain_of:
- NamedThing
range: string

```
</details>