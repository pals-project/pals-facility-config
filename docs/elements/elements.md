

# Slot: elements 


_Beamline element definitions referenced by name from beamline sequences. Serializes as a keyed map by element name._





URI: [narad:elements](https://example.org/narad_linkml/schema/narad/elements)
Alias: elements

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |  no  |






## Properties

* Range: [BeamlineElement](BeamlineElement.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:elements |
| native | narad:elements |




## LinkML Source

<details>
```yaml
name: elements
description: Beamline element definitions referenced by name from beamline sequences.
  Serializes as a keyed map by element name.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: elements
domain_of:
- NaradModel
range: BeamlineElement
multivalued: true
inlined: true
inlined_as_list: true

```
</details>