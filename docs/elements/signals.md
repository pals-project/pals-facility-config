

# Slot: signals 


_A list of signals in the accelerator system._





URI: [pals:signals](https://pals-project.readthedocs.io/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](Facility.md) | A facility that houses one or more accelerators |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Signal](Signal.md) |
| Domain Of | [Facility](Facility.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Facility](Facility.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:signals |
| native | pals:signals |




## LinkML Source

<details>
```yaml
name: signals
description: A list of signals in the accelerator system.
from_schema: https://w3id.org/accelerator-core
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