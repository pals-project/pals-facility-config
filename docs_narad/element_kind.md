

# Slot: element_kind 


_The type of this beamline element (e.g. Quadrupole, BPM, RFCavity)._





URI: [narad:element_kind](https://w3id.org/narad_linkml/schema/narad/element_kind)
Alias: element_kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |






## Properties

* Range: [ElementKindEnum](ElementKindEnum.md)



## Aliases


* kind


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:element_kind |
| native | narad:element_kind |




## LinkML Source

<details>
```yaml
name: element_kind
description: The type of this beamline element (e.g. Quadrupole, BPM, RFCavity).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
aliases:
- kind
rank: 1000
alias: element_kind
domain_of:
- BeamlineElement
range: ElementKindEnum

```
</details>