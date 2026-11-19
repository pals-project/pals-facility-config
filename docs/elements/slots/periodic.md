

# Slot: periodic 


_Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic._





URI: [pals_config:slot/periodic](https://w3id.org/pals-config/slot/periodic)
Alias: periodic

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
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
| self | pals_config:periodic |
| native | pals_config:periodic |
| close | pals:periodic |




## LinkML Source

<details>
```yaml
name: periodic
description: Indicates whether orbit and Twiss parameters periodic. If not provided,
  the default assumption is that the BeamLine is not periodic.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:periodic
rank: 1000
alias: periodic
owner: BeamLine
domain_of:
- BeamLine
range: boolean

```
</details>