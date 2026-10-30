

# Slot: direction 


_Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1._





URI: [acc:slot/direction](https://example.org/accelerator-core/slot/direction)
Alias: direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [BeamLine](../classes/BeamLine.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BeamLine](../classes/BeamLine.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:direction |
| native | acc:direction |
| close | pals:direction |




## LinkML Source

<details>
```yaml
name: direction
description: 'Beam direction along the BeamLine: +1 or -1. Longitudinal orientation.
  Default is +1.'
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:direction
rank: 1000
alias: direction
owner: BeamLine
domain_of:
- BeamLine
range: integer

```
</details>