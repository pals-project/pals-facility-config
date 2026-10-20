

# Slot: source_system 


_The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service._





URI: [pals:slot/source_system](https://pals-project.readthedocs.io/slot/source_system)
Alias: source_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SourceSystemEnum](../enums/SourceSystemEnum.md) |
| Domain Of | [Signal](../classes/Signal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Signal](../classes/Signal.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:source_system |
| native | pals:source_system |




## LinkML Source

<details>
```yaml
name: source_system
description: The source system from which the signal originates, such as EPICS, PALS-Ext,
  MYA, an element database, a channel database, or a simulation service.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: source_system
owner: Signal
domain_of:
- Signal
range: SourceSystemEnum
required: true

```
</details>