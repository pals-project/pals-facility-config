# Enum: SignalRoleEnum 




_Controlled vocabulary for the semantic role of a signal within a capability._



URI: [narad:SignalRoleEnum](https://w3id.org/narad_linkml/schema/narad/SignalRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| control | None | A writable signal that commands a device setpoint |
| readback | None | A readable signal that reports a measured or monitored quantity |
| constraint | None | A signal that defines an operational limit or boundary on a control quantity |
| status | None | A signal reporting the device or system operational state |




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | The semantic role of the signal within its capability |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system






## LinkML Source

<details>
```yaml
name: SignalRoleEnum
description: Controlled vocabulary for the semantic role of a signal within a capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
permissible_values:
  control:
    text: control
    description: A writable signal that commands a device setpoint.
    broad_mappings:
    - sosa:ActuatableProperty
  readback:
    text: readback
    description: A readable signal that reports a measured or monitored quantity.
    broad_mappings:
    - sosa:ObservableProperty
  constraint:
    text: constraint
    description: A signal that defines an operational limit or boundary on a control
      quantity.
  status:
    text: status
    description: A signal reporting the device or system operational state.
    broad_mappings:
    - sosa:ObservableProperty

```
</details>