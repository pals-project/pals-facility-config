

# Slot: device_layer 


_Device definitions for this facility._





URI: [narad:device_layer](https://w3id.org/narad_linkml/schema/narad/device_layer)
Alias: device_layer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  yes  |






## Properties

* Range: [DeviceSystem](DeviceSystem.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:device_layer |
| native | narad:device_layer |




## LinkML Source

<details>
```yaml
name: device_layer
description: Device definitions for this facility.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: device_layer
domain_of:
- NaradConfig
range: DeviceSystem
multivalued: true
inlined: true

```
</details>