

# Slot: access_protocol 


_The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service._





URI: [pals:slot/access_protocol](https://pals-project.readthedocs.io/slot/access_protocol)
Alias: access_protocol

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Signal](../classes/Signal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | pals:access_protocol |
| native | pals:access_protocol |




## LinkML Source

<details>
```yaml
name: access_protocol
description: The protocol used to access the signal in the source system,  such as
  EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: access_protocol
owner: Signal
domain_of:
- Signal
range: string

```
</details>