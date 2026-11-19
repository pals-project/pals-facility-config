

# Slot: signals 


_A list of signals in the accelerator system._





URI: [pals_config:slot/signals](https://w3id.org/pals-config/slot/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Signal](../classes/Signal.md) |
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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:signals |
| native | pals_config:signals |




## LinkML Source

<details>
```yaml
name: signals
description: A list of signals in the accelerator system.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: signals
owner: Facility
domain_of:
- Facility
range: Signal
multivalued: true
inlined: true
inlined_as_list: true

```
</details>