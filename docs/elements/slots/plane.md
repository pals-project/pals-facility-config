

# Slot: plane 


_The transverse plane in which the kicker operates, either horizontal or vertical._





URI: [pals_config:slot/plane](https://w3id.org/pals-config/slot/plane)
Alias: plane

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kicker](../classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |  no  |
| [ACKicker](../classes/ACKicker.md) | An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PlaneEnum](../enums/PlaneEnum.md) |
| Domain Of | [Kicker](../classes/Kicker.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kicker](../classes/Kicker.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:plane |
| native | pals_config:plane |




## LinkML Source

<details>
```yaml
name: plane
description: The transverse plane in which the kicker operates, either horizontal
  or vertical.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: plane
owner: Kicker
domain_of:
- Kicker
range: PlaneEnum

```
</details>