

# Slot: beamlines 


_A list of beamlines in the accelerator system._





URI: [acc:slot/beamlines](https://example.org/accelerator-core/slot/beamlines)
Alias: beamlines

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BeamLine](../classes/BeamLine.md) |
| Domain Of | [Facility](../classes/Facility.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Facility](../classes/Facility.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:beamlines |
| native | acc:beamlines |




## LinkML Source

<details>
```yaml
name: beamlines
description: A list of beamlines in the accelerator system.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: beamlines
owner: Facility
domain_of:
- Facility
range: BeamLine
multivalued: true
inlined: true
inlined_as_list: true

```
</details>