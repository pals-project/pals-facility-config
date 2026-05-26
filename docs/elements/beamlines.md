

# Slot: beamlines 


_A top-level NARAD-system container for the ordered beamline definitions keyed by beamline name. Serializes as a keyed map by beamline name._





URI: [narad:beamlines](https://example.org/narad_linkml/schema/narad/beamlines)
Alias: beamlines

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |  no  |






## Properties

* Range: [Beamline](Beamline.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:beamlines |
| native | narad:beamlines |




## LinkML Source

<details>
```yaml
name: beamlines
description: A top-level NARAD-system container for the ordered beamline definitions
  keyed by beamline name. Serializes as a keyed map by beamline name.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: beamlines
domain_of:
- NaradModel
range: Beamline
multivalued: true
inlined: true

```
</details>