

# Slot: signals 


_Signals within a capability._





URI: [https://w3id.org/narad_linkml/schema/narad/signals](https://w3id.org/narad_linkml/schema/narad/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect |  no  |
| [CapabilityMixin](CapabilityMixin.md) | Shared structure common to all capability types: a description and an ordered... |  no  |






## Properties

* Range: [Signal](Signal.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/signals |
| native | https://w3id.org/narad_linkml/schema/narad/signals |




## LinkML Source

<details>
```yaml
name: signals
description: Signals within a capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: signals
domain_of:
- CapabilityMixin
range: Signal
multivalued: true
inlined: true
inlined_as_list: true

```
</details>