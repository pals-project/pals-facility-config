

# Slot: signals 


_Signals within a capability, keyed by signal name._





URI: [narad:signals](https://w3id.org/narad_linkml/schema/narad/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect... |  no  |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile that extends a gen... |  no  |






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
description: Signals within a capability, keyed by signal name.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: signals
domain_of:
- Capability
range: Signal
multivalued: true
inlined: true

```
</details>