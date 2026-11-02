

# Slot: y_coord 


_The y-coordinate in the specified coordinate system._





URI: [acc:slot/y_coord](https://example.org/accelerator-core/slot/y_coord)
Alias: y_coord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoordinateSet](../classes/CoordinateSet.md) | A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [CoordinateSet](../classes/CoordinateSet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CoordinateSet](../classes/CoordinateSet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:y_coord |
| native | acc:y_coord |




## LinkML Source

<details>
```yaml
name: y_coord
description: The y-coordinate in the specified coordinate system.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: y_coord
owner: CoordinateSet
domain_of:
- CoordinateSet
range: float

```
</details>