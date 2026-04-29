

# Slot: units_uri 


_Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere, si-unit:MegaV-PER-M for MV/m, si-unit:T-M for T*m). The si-unit: prefix maps to http://qudt.org/vocab/unit/. Companion to the human-readable symbol in the units slot. Use the narad:CustomUnit for user-defined units not in QUDT; these should be defined in the graph projection with a narad:CustomUnit class and linked to signals via the units_uri slot._





URI: [https://w3id.org/narad_linkml/schema/narad/units_uri](https://w3id.org/narad_linkml/schema/narad/units_uri)
Alias: units_uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/units_uri |
| native | https://w3id.org/narad_linkml/schema/narad/units_uri |
| broad | si-unit:Unit |




## LinkML Source

<details>
```yaml
name: units_uri
description: 'Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere, si-unit:MegaV-PER-M
  for MV/m, si-unit:T-M for T*m). The si-unit: prefix maps to http://qudt.org/vocab/unit/.
  Companion to the human-readable symbol in the units slot. Use the narad:CustomUnit
  for user-defined units not in QUDT; these should be defined in the graph projection
  with a narad:CustomUnit class and linked to signals via the units_uri slot.'
from_schema: https://w3id.org/narad_linkml/schema/narad/
broad_mappings:
- si-unit:Unit
rank: 1000
alias: units_uri
domain_of:
- Signal
range: uriorcurie

```
</details>