# Enum: SignalRoleEnum 




_Roles for control-system signals._



URI: [pals:enum/SignalRoleEnum](https://pals-project.readthedocs.io/enum/SignalRoleEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Setpoint | sosa:ActuatableProperty | Requested or configured value. |
| Readback | sosa:ObservableProperty | Measured or reported value. |
| Status | None | State or condition indicator. |
| Command | sosa:ActuatableProperty | Command or action trigger. |
| MinimumLimit | xsd:minInclusive | Minimum allowed signal value. |
| MaximumLimit | xsd:maxInclusive | Maximum allowed signal value. |




## Slots

| Name | Description |
| ---  | --- |
| [signal_role](../slots/signal_role.md) | The role of the signal in the control system, such as setpoint, readback, status, command, or limit. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: SignalRoleEnum
description: Roles for control-system signals.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  Setpoint:
    text: Setpoint
    description: Requested or configured value.
    meaning: sosa:ActuatableProperty
  Readback:
    text: Readback
    description: Measured or reported value.
    meaning: sosa:ObservableProperty
  Status:
    text: Status
    description: State or condition indicator.
  Command:
    text: Command
    description: Command or action trigger.
    meaning: sosa:ActuatableProperty
  MinimumLimit:
    text: MinimumLimit
    description: Minimum allowed signal value.
    meaning: xsd:minInclusive
  MaximumLimit:
    text: MaximumLimit
    description: Maximum allowed signal value.
    meaning: xsd:maxInclusive

```
</details>