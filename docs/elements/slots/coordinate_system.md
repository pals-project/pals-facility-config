

# Slot: coordinate_system 


_The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical)._





URI: [pals_config:slot/coordinate_system](https://w3id.org/pals-config/slot/coordinate_system)
Alias: coordinate_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoordinateSet](../classes/CoordinateSet.md) | A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CoordinateSystemEnum](../enums/CoordinateSystemEnum.md) |
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
| self | pals_config:coordinate_system |
| native | pals_config:coordinate_system |




## LinkML Source

<details>
```yaml
name: coordinate_system
description: The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: coordinate_system
owner: CoordinateSet
domain_of:
- CoordinateSet
range: CoordinateSystemEnum

```
</details>