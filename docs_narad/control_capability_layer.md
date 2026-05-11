

# Slot: control_capability_layer 


_Control Capability definitions for this facility._





URI: [narad:control_capability_layer](https://w3id.org/narad_linkml/schema/narad/control_capability_layer)
Alias: control_capability_layer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  no  |






## Properties

* Range: [ControlCapability](ControlCapability.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:control_capability_layer |
| native | narad:control_capability_layer |




## LinkML Source

<details>
```yaml
name: control_capability_layer
description: Control Capability definitions for this facility.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: control_capability_layer
domain_of:
- NaradConfig
range: ControlCapability
required: true
multivalued: true
inlined: true

```
</details>