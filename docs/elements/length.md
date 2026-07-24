

# Slot: length 


_Length of the element (arc length for bends)._





URI: [pals:length](https://pals-project.readthedocs.io/length)
Alias: length

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direc... |  no  |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  yes  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:length |
| native | pals:length |




## LinkML Source

<details>
```yaml
name: length
description: Length of the element (arc length for bends).
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:length
alias: length
domain_of:
- LongitudinalPlacementParamGroup
- BeamLine
range: float

```
</details>