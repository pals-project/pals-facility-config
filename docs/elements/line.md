

# Slot: line 


_Ordered sequence of beamline elements in this beamline. Serializes as a list of element names (BeamlineElement names) referencing the keys in the elements map This is not a direct containment slot; the actual element definitions are in the top-level elements map._





URI: [narad:line](https://example.org/narad_linkml/schema/narad/line)
Alias: line

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |






## Properties

* Range: [BeamlineElement](BeamlineElement.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:line |
| native | narad:line |




## LinkML Source

<details>
```yaml
name: line
description: Ordered sequence of beamline elements in this beamline. Serializes as
  a list of element names (BeamlineElement names) referencing the keys in the elements
  map This is not a direct containment slot; the actual element definitions are in
  the top-level elements map.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: line
domain_of:
- Beamline
range: BeamlineElement
multivalued: true
inlined: false

```
</details>