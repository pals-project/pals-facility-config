

# Slot: has_signal 


_Signals within a capability, keyed by a semantic signal name._





URI: [narad:has_signal](https://example.org/narad_linkml/schema/narad/has_signal)
Alias: has_signal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Capability](Capability.md) | A reusable device-type control profile that extends a generic shared capabili... |  yes  |






## Properties

* Range: [Signal](Signal.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:has_signal |
| native | narad:has_signal |




## LinkML Source

<details>
```yaml
name: has_signal
description: Signals within a capability, keyed by a semantic signal name.
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: has_signal
domain_of:
- Capability
range: Signal
multivalued: true
inlined: true

```
</details>