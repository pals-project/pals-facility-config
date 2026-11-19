

# Slot: signal_bindings 


_A list of signal bindings in the accelerator system (Component <-> Signal relationships)._





URI: [pals_config:slot/signal_bindings](https://w3id.org/pals-config/slot/signal_bindings)
Alias: signal_bindings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SignalBinding](../classes/SignalBinding.md) |
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
| self | pals_config:signal_bindings |
| native | pals_config:signal_bindings |




## LinkML Source

<details>
```yaml
name: signal_bindings
description: A list of signal bindings in the accelerator system (Component <-> Signal
  relationships).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: signal_bindings
owner: Facility
domain_of:
- Facility
range: SignalBinding
multivalued: true
inlined: true
inlined_as_list: true

```
</details>