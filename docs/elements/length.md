

# Slot: length 


_Physical length of the element in meters._





URI: [narad:length](https://w3id.org/narad_linkml/schema/narad/length)
Alias: length

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:length |
| native | narad:length |




## LinkML Source

<details>
```yaml
name: length
description: Physical length of the element in meters.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: length
domain_of:
- Beamline
- BeamlineElement
range: float

```
</details>