

# Slot: name 


_Name/identifier of the entity._





URI: [https://w3id.org/narad_linkml/schema/narad/name](https://w3id.org/narad_linkml/schema/narad/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](Facility.md) | A facility with specific signal bindings |  no  |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect |  no  |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |  no  |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |  yes  |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal binding set scoped to a device type (for example, Quadrupole or BPM) |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/name |
| native | https://w3id.org/narad_linkml/schema/narad/name |




## LinkML Source

<details>
```yaml
name: name
description: Name/identifier of the entity.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
identifier: true
alias: name
domain_of:
- Facility
- SignalBinding
- DeviceTypeSignalSet
- Signal
- Capability
- CapabilityProfile
- ControlProfileFamily
- BeamlineElement
- PVBinding
range: string
required: true

```
</details>