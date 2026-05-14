

# Slot: facility_identifier 


_Globally unique identifier for the facility, with specified type and value._





URI: [narad:facility_identifier](https://w3id.org/narad_linkml/schema/narad/facility_identifier)
Alias: facility_identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |






## Properties

* Range: [FacilityIdentifier](FacilityIdentifier.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:facility_identifier |
| native | narad:facility_identifier |




## LinkML Source

<details>
```yaml
name: facility_identifier
description: Globally unique identifier for the facility, with specified type and
  value.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: facility_identifier
domain_of:
- FacilitySystem
range: FacilityIdentifier
multivalued: true
inlined: false

```
</details>