

# Slot: description 


_Detailed description of the entity._





URI: [narad:description](https://example.org/narad_linkml/schema/narad/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamingConventionExample](NamingConventionExample.md) | An example of a control system naming convention, illustrating how the templa... |  no  |
| [DeployedSystem](DeployedSystem.md) | A deployed system, with an identified facility, that is the subject of a NARA... |  no  |
| [Capability](Capability.md) | A reusable device-type control profile that extends a generic shared capabili... |  no  |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  no  |
| [Device](Device.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [TemplateExample](TemplateExample.md) | An example of a control system PV name generated from a naming convention tem... |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [TemplateComponent](TemplateComponent.md) | A component of a naming convention template, representing a variable part of ... |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [SignalBinding](SignalBinding.md) | A named control system suffix definition for one semantic signal |  no  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |
| [NamingConvention](NamingConvention.md) | A template for constructing facility-specific signal names from a semantic si... |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |






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
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: description
domain_of:
- NamedThing
- NamingConventionExample
- TemplateExample
range: string

```
</details>