
# Enum: SignalBindingPredicateEnum

Controlled predicates for Component-to-Signal bindings.

URI: [narad:SignalBindingPredicateEnum](https://example.org/narad/SignalBindingPredicateEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| has_signal | Generic association between a component and one of its signals. The specific role (setpoint, readback, status, etc.) is carried by the Signal's own signal_role field, not the predicate. |  |  |
| has_status_signal | Subject has the given signal as its status indicator. |  |  |
| has_setpoint_signal | Subject has the given signal as its setpoint. |  |  |
| has_readback_signal | Subject has the given signal as its readback. |  |  |
| has_command_signal | Subject has the given signal as a command trigger. |  |  |
| has_limit_signal | Subject has the given signal as a limit/constraint value. |  |  |
