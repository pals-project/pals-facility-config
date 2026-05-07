

# Slot: role 


_The semantic role of the signal within its capability._





URI: [narad:role](https://w3id.org/narad_linkml/schema/narad/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |






## Properties

* Range: [SignalRoleEnum](SignalRoleEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:role |
| native | narad:role |




## LinkML Source

<details>
```yaml
name: role
description: The semantic role of the signal within its capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: role
domain_of:
- Signal
range: SignalRoleEnum

```
</details>