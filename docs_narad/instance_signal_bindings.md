

# Slot: instance_signal_bindings 


_Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the concrete implementations of the abstract SignalBindings referenced by the element's capability profile._





URI: [narad:instance_signal_bindings](https://w3id.org/narad_linkml/schema/narad/instance_signal_bindings)
Alias: instance_signal_bindings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |






## Properties

* Range: [InstanceSignalBinding](InstanceSignalBinding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:instance_signal_bindings |
| native | narad:instance_signal_bindings |




## LinkML Source

<details>
```yaml
name: instance_signal_bindings
description: Facility-specific bindings of signals to control-system interfaces (e.g.
  EPICS PVs) for a specific beamline element instance. These are the concrete implementations
  of the abstract SignalBindings referenced by the element's capability profile.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: instance_signal_bindings
domain_of:
- BeamlineElement
range: InstanceSignalBinding
multivalued: true
inlined: true

```
</details>