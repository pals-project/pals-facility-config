

# Slot: system_type 


_High-level system type for classification and querying._





URI: [narad:system_type](https://w3id.org/narad_linkml/schema/narad/system_type)
Alias: system_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  no  |






## Properties

* Range: [SystemTypeEnum](SystemTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:system_type |
| native | narad:system_type |




## LinkML Source

<details>
```yaml
name: system_type
description: High-level system type for classification and querying.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: system_type
domain_of:
- System
range: SystemTypeEnum

```
</details>