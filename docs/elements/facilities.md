

# Slot: facilities 


_Facility-specific signal binding configurations keyed by facility name._





URI: [narad:facilities](https://example.org/narad_linkml/schema/narad/facilities)
Alias: facilities

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings |  no  |






## Properties

* Range: [FacilitySystem](FacilitySystem.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:facilities |
| native | narad:facilities |




## LinkML Source

<details>
```yaml
name: facilities
description: Facility-specific signal binding configurations keyed by facility name.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: facilities
domain_of:
- SignalLayer
range: FacilitySystem
multivalued: true
inlined: true

```
</details>