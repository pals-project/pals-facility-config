

# Slot: signals 


_Signals within a capability, keyed by a semantic signal name._





URI: [narad:signals](https://w3id.org/narad_linkml/schema/narad/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |  yes  |






## Properties

* Range: [Signal](Signal.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:signals |
| native | narad:signals |




## LinkML Source

<details>
```yaml
name: signals
description: Signals within a capability, keyed by a semantic signal name.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: signals
domain_of:
- ControlCapability
range: Signal
multivalued: true
inlined: true

```
</details>