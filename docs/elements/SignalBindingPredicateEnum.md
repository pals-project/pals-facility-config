# Enum: SignalBindingPredicateEnum 




_Controlled predicates for Component-to-Signal bindings._



URI: [pals:SignalBindingPredicateEnum](https://pals-project.readthedocs.io/SignalBindingPredicateEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| has_signal | None | Generic association between a component and one of its signals |
| has_status_signal | None | Subject has the given signal as its status indicator |
| has_setpoint_signal | None | Subject has the given signal as its setpoint |
| has_readback_signal | None | Subject has the given signal as its readback |
| has_command_signal | None | Subject has the given signal as a command trigger |
| has_limit_signal | None | Subject has the given signal as a limit/constraint value |




## Slots

| Name | Description |
| ---  | --- |
| [predicate](predicate.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: SignalBindingPredicateEnum
description: Controlled predicates for Component-to-Signal bindings.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  has_signal:
    text: has_signal
    description: Generic association between a component and one of its signals. The
      specific role (setpoint, readback, status, etc.) is carried by the Signal's
      own signal_role field, not the predicate.
  has_status_signal:
    text: has_status_signal
    description: Subject has the given signal as its status indicator.
  has_setpoint_signal:
    text: has_setpoint_signal
    description: Subject has the given signal as its setpoint.
  has_readback_signal:
    text: has_readback_signal
    description: Subject has the given signal as its readback.
  has_command_signal:
    text: has_command_signal
    description: Subject has the given signal as a command trigger.
  has_limit_signal:
    text: has_limit_signal
    description: Subject has the given signal as a limit/constraint value.

```
</details>