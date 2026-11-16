

# Slot: signal_role 


_The role of the signal in the control system, such as setpoint, readback, status, command, or limit._





URI: [pals_config:slot/signal_role](https://w3id.org/pals-config/slot/signal_role)
Alias: signal_role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SignalRoleEnum](../enums/SignalRoleEnum.md) |
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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:signal_role |
| native | pals_config:signal_role |




## LinkML Source

<details>
```yaml
name: signal_role
description: The role of the signal in the control system, such as setpoint, readback,
  status, command, or limit.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: signal_role
owner: Signal
domain_of:
- Signal
range: SignalRoleEnum
required: true

```
</details>