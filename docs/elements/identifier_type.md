

# Slot: identifier_type 


_The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local)._





URI: [narad:identifier_type](https://example.org/narad_linkml/schema/narad/identifier_type)
Alias: identifier_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilityIdentifier](FacilityIdentifier.md) | A globally unique identifier for an entity (e |  no  |






## Properties

* Range: [IdentifierTypeEnum](IdentifierTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:identifier_type |
| native | narad:identifier_type |




## LinkML Source

<details>
```yaml
name: identifier_type
description: The type of identifier used in the identifier slot (e.g. DOI, ARK, URL,
  local).
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: identifier_type
domain_of:
- FacilityIdentifier
range: IdentifierTypeEnum

```
</details>