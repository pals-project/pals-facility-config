

# Slot: hosts_device 


_Structured container for facility-specific signal suffix templates._





URI: [narad:hosts_device](https://example.org/narad_linkml/schema/narad/hosts_device)
Alias: hosts_device

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |






## Properties

* Range: [Device](Device.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:hosts_device |
| native | narad:hosts_device |




## LinkML Source

<details>
```yaml
name: hosts_device
description: Structured container for facility-specific signal suffix templates.
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
domain: FacilitySystem
alias: hosts_device
domain_of:
- FacilitySystem
range: Device
multivalued: true
inlined: true

```
</details>