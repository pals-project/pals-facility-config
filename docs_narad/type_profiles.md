

# Slot: type_profiles 


_Device-type profile definitions for this family, keyed by profile name. New device types are accommodated by adding a new entry without schema changes._





URI: [https://w3id.org/narad_linkml/schema/narad/type_profiles](https://w3id.org/narad_linkml/schema/narad/type_profiles)
Alias: type_profiles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |






## Properties

* Range: [CapabilityProfile](CapabilityProfile.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/type_profiles |
| native | https://w3id.org/narad_linkml/schema/narad/type_profiles |




## LinkML Source

<details>
```yaml
name: type_profiles
description: Device-type profile definitions for this family, keyed by profile name.
  New device types are accommodated by adding a new entry without schema changes.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: type_profiles
domain_of:
- ControlProfileFamily
range: CapabilityProfile
multivalued: true
inlined: true

```
</details>