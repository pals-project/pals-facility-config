

# Slot: capability_layer 


_Control Capability definitions for this facility._





URI: [narad:capability_layer](https://example.org/narad_linkml/schema/narad/capability_layer)
Alias: capability_layer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  no  |






## Properties

* Range: [Capability](Capability.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:capability_layer |
| native | narad:capability_layer |




## LinkML Source

<details>
```yaml
name: capability_layer
description: Control Capability definitions for this facility.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: capability_layer
domain_of:
- NaradConfig
range: Capability
required: true
multivalued: true
inlined: true

```
</details>