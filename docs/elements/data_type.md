

# Slot: data_type 


_The data type of the signal's value._





URI: [narad:data_type](https://example.org/narad_linkml/schema/narad/data_type)
Alias: data_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |






## Properties

* Range: [DataTypeEnum](DataTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:data_type |
| native | narad:data_type |




## LinkML Source

<details>
```yaml
name: data_type
description: The data type of the signal's value.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: data_type
domain_of:
- Signal
range: DataTypeEnum

```
</details>