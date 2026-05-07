

# Slot: units 


_Conventional unit symbol (e.g. A, MV/m, T*m, G/cm)._





URI: [narad:units](https://w3id.org/narad_linkml/schema/narad/units)
Alias: units

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:units |
| native | narad:units |




## LinkML Source

<details>
```yaml
name: units
description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: units
domain_of:
- Signal
range: string

```
</details>