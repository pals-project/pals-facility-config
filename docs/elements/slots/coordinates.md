

# Slot: coordinates 


_A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship._





URI: [acc:slot/coordinates](https://example.org/accelerator-core/slot/coordinates)
Alias: coordinates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MountedOn](../classes/MountedOn.md) | A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet. |  no  |
| [NearestTo](../classes/NearestTo.md) | A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet. |  no  |
| [Overlaps](../classes/Overlaps.md) | A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device. |  no  |
| [AdjacentTo](../classes/AdjacentTo.md) | A relationship indicating that the subject component is adjacent to the object component and not overlapping<br> in a specified context, such as radiation detector and a magnet. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CoordinateSet](../classes/CoordinateSet.md) |
| Domain Of | [AdjacentTo](../classes/AdjacentTo.md), [Overlaps](../classes/Overlaps.md), [MountedOn](../classes/MountedOn.md), [NearestTo](../classes/NearestTo.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:coordinates |
| native | acc:coordinates |




## LinkML Source

<details>
```yaml
name: coordinates
description: A set of coordinates that define the spatial relationship between the
  two components. Only an edge-property slot for edges that require a set of coordinates
  to define the spatial relationship between two components in a relationship.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: coordinates
domain_of:
- AdjacentTo
- Overlaps
- MountedOn
- NearestTo
range: CoordinateSet
recommended: true
inlined: true

```
</details>