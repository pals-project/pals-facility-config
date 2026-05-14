

# Slot: name 


_Human-readable name or local string key for the entity._





URI: [narad:name](https://w3id.org/narad_linkml/schema/narad/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  no  |
| [SignalBinding](SignalBinding.md) | A named control system suffix definition for one semantic signal |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |
| [ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |  no  |
| [SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |  no  |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |
| [DeviceSystem](DeviceSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |






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