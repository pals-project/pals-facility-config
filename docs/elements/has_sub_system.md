

# Slot: has_sub_system 


_Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition._

__





URI: [narad:has_sub_system](https://example.org/narad_linkml/schema/narad/has_sub_system)
Alias: has_sub_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeployedSystem](DeployedSystem.md) | A deployed system, with an identified facility, that is the subject of a NARA... |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  yes  |
| [Device](Device.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  yes  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [ControlSystem](ControlSystem.md) | A control system (e |  yes  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |






## Properties

* Range: [System](System.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:has_sub_system |
| native | narad:has_sub_system |
| exact | ssn-system:hasSubSystem |




## LinkML Source

<details>
```yaml
name: has_sub_system
description: 'Relates a System to one of its subsystems (SSN alignment). Use for facility
  → control-system, facility → device, and device → component decomposition.

  '
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn-system:hasSubSystem
rank: 1000
domain: System
alias: has_sub_system
domain_of:
- System
- Device
range: System
multivalued: true

```
</details>