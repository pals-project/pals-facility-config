

# Slot: has_system_capability 


_Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters._

__





URI: [narad:has_system_capability](https://w3id.org/narad_linkml/schema/narad/has_system_capability)
Alias: has_system_capability

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  yes  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  yes  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |






## Properties

* Range: [SystemCapability](SystemCapability.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:has_system_capability |
| native | narad:has_system_capability |
| exact | ssn-system:hasSystemCapability |




## LinkML Source

<details>
```yaml
name: has_system_capability
description: 'Relates a System to a SystemCapability it supports (SSN-System alignment).
  Prefer this over directly attaching signals to systems when capability context matters.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn-system:hasSystemCapability
rank: 1000
domain: System
alias: has_system_capability
domain_of:
- System
- InstrumentSystem
range: SystemCapability
multivalued: true

```
</details>