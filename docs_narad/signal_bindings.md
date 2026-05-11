

# Slot: signal_bindings 


_Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set._





URI: [narad:signal_bindings](https://w3id.org/narad_linkml/schema/narad/signal_bindings)
Alias: signal_bindings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |  yes  |






## Properties

* Range: [SignalBinding](SignalBinding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:signal_bindings |
| native | narad:signal_bindings |




## LinkML Source

<details>
```yaml
name: signal_bindings
description: Control-system-specific, e.g. EPICS, suffix definitions keyed by signal
  name within a device/domain set.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: signal_bindings
domain_of:
- SignalDefinitions
range: SignalBinding
multivalued: true
inlined: true

```
</details>