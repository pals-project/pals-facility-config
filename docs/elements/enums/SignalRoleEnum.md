# Enum: SignalRoleEnum 




_Roles for control-system signals._



URI: [pals_config:enum/SignalRoleEnum](https://w3id.org/pals-config/enum/SignalRoleEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Setpoint | None | Requested or configured value. |
| Readback | None | Measured or reported value. |
| Status | None | State or condition indicator. |
| Command | None | Command or action trigger. |
| MinimumLimit | None | Minimum allowed signal value. |
| MaximumLimit | None | Maximum allowed signal value. |
| RangeLimit | None | A signal containing both upper and lower allowed limits. |




## Slots

| Name | Description |
| ---  | --- |
| [signal_role](../slots/signal_role.md) | The role of the signal in the control system, such as setpoint, readback, status, command, or limit. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config






## LinkML Source

<details>
```yaml
name: SignalRoleEnum
description: Roles for control-system signals.
from_schema: https://w3id.org/pals-config
rank: 1000
permissible_values:
  Setpoint:
    text: Setpoint
    description: Requested or configured value.
    exact_mappings:
    - sosa:ActuatableProperty
  Readback:
    text: Readback
    description: Measured or reported value.
    exact_mappings:
    - sosa:ObservableProperty
  Status:
    text: Status
    description: State or condition indicator.
  Command:
    text: Command
    description: Command or action trigger.
    exact_mappings:
    - sosa:ActuatableProperty
  MinimumLimit:
    text: MinimumLimit
    description: Minimum allowed signal value.
    exact_mappings:
    - xsd:minInclusive
  MaximumLimit:
    text: MaximumLimit
    description: Maximum allowed signal value.
    exact_mappings:
    - xsd:maxInclusive
  RangeLimit:
    text: RangeLimit
    description: A signal containing both upper and lower allowed limits.

```
</details>