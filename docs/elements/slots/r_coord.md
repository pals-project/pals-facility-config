

# Slot: r_coord 


_The radial distance in cylindrical coordinates._





URI: [pals_config:slot/r_coord](https://w3id.org/pals-config/slot/r_coord)
Alias: r_coord

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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:r_coord |
| native | pals_config:r_coord |




## LinkML Source

<details>
```yaml
name: r_coord
description: The radial distance in cylindrical coordinates.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: r_coord
owner: CoordinateSet
domain_of:
- CoordinateSet
range: float

```
</details>