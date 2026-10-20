

# Slot: length 


_Length of the element (arc length for bends)._





URI: [pals:length](https://pals-project.readthedocs.io/length)
Alias: length

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. <br>Corresponds to PALS's ungrouped element parameters `length` and `s_position`.<br>One (or both) `length` or `s_position` must be present. |  no  |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md), [BeamLine](../classes/BeamLine.md) |
| Slot URI | [pals:length](https://pals-project.readthedocs.io/length) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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