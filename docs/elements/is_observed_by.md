

# Slot: is_observed_by 


_Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set. Can also be used to link a BeamlineElement instance to the signal bindings that observe or actuate it,  since the instance of the element is directly observed or controlled through a Device. Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the keyed by the semantic signal name (e.g. current_readback) rather than the control-system suffix, which is captured in the SignalBinding. The semantic signal name links the instance binding to the abstract Signal definition and its place in the capability profile, while the SignalBinding captures the concrete implementations of the abstract SignalBindings referenced by the element's capability profile._





URI: [narad:is_observed_by](https://example.org/narad_linkml/schema/narad/is_observed_by)
Alias: is_observed_by

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  yes  |
| [Device](Device.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  yes  |






## Properties

* Range: [SignalBinding](SignalBinding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:is_observed_by |
| native | narad:is_observed_by |




## LinkML Source

<details>
```yaml
name: is_observed_by
description: Control-system-specific, e.g. EPICS, suffix definitions keyed by signal
  name within a device/domain set. Can also be used to link a BeamlineElement instance
  to the signal bindings that observe or actuate it,  since the instance of the element
  is directly observed or controlled through a Device. Facility-specific bindings
  of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline
  element instance. These are the keyed by the semantic signal name (e.g. current_readback)
  rather than the control-system suffix, which is captured in the SignalBinding. The
  semantic signal name links the instance binding to the abstract Signal definition
  and its place in the capability profile, while the SignalBinding captures the concrete
  implementations of the abstract SignalBindings referenced by the element's capability
  profile.
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: is_observed_by
domain_of:
- BeamlineElement
- Device
range: SignalBinding
multivalued: true
inlined: true

```
</details>