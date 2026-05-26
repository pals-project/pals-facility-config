

# Slot: schema_version 


_Version of the NARAD schema used in this document._





URI: [narad:schema_version](https://example.org/narad_linkml/schema/narad/schema_version)
Alias: schema_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  yes  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:schema_version |
| native | narad:schema_version |




## LinkML Source

<details>
```yaml
name: schema_version
description: Version of the NARAD schema used in this document.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: schema_version
domain_of:
- NaradConfig
range: string

```
</details>