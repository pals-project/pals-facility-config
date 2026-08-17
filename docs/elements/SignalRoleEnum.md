
# Enum: SignalRoleEnum

Roles for control-system signals.

URI: [pals:SignalRoleEnum](https://pals-project.readthedocs.io/SignalRoleEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| Setpoint | Requested or configured value. | sosa:ActuatableProperty |  |
| Readback | Measured or reported value. | sosa:ObservableProperty |  |
| Status | State or condition indicator. |  |  |
| Command | Command or action trigger. | sosa:ActuatableProperty |  |
| MinimumLimit | Minimum allowed signal value. | xsd:minInclusive |  |
| MaximumLimit | Maximum allowed signal value. | xsd:maxInclusive |  |
