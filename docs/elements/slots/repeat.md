

# Slot: repeat 


_Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1._

_If value is greater than 1, the beamline is repeated that many times._





URI: [pals_config:slot/repeat](https://w3id.org/pals-config/slot/repeat)
Alias: repeat

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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:repeat |
| native | pals_config:repeat |
| close | pals:repeat |




## LinkML Source

<details>
```yaml
name: repeat
description: 'Repetition count. If not provided, the default assumption is that the
  beamline is not repeated and the value is 1.

  If value is greater than 1, the beamline is repeated that many times.'
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:repeat
rank: 1000
alias: repeat
owner: BeamLine
domain_of:
- BeamLine
range: integer

```
</details>