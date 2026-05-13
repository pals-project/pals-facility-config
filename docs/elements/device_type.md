

# Slot: device_type 


_Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching._





URI: [narad:device_type](https://w3id.org/narad_linkml/schema/narad/device_type)
Alias: device_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |  no  |
| [InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |






## Properties

* Range: [ElementKindEnum](ElementKindEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:device_type |
| native | narad:device_type |




## LinkML Source

<details>
```yaml
name: device_type
description: Represents the generic, semantic class of the device (e.g., "Quadrupole",
  "BPM") and is used for capability, instrument, and signal profile matching.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: device_type
domain_of:
- ControlCapability
- SignalDefinitions
- InstrumentSystem
- SystemCapability
range: ElementKindEnum

```
</details>