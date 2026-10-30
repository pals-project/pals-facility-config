

# Slot: length 


_Length of the element (arc length for bends)._





URI: [acc:slot/length](https://example.org/accelerator-core/slot/length)
Alias: length

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present. |  no  |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md), [BeamLine](../classes/BeamLine.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:length |
| native | acc:length |
| close | pals:length |




## LinkML Source

<details>
```yaml
name: length
description: Length of the element (arc length for bends).
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:length
rank: 1000
alias: length
domain_of:
- LongitudinalPlacementParamGroup
- BeamLine
range: float

```
</details>