

# Slot: has_sub_system 


_Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition._

__





URI: [narad:has_sub_system](https://w3id.org/narad_linkml/schema/narad/has_sub_system)
Alias: has_sub_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlSystem](ControlSystem.md) | A control system (e |  no  |
| [Magnet](Magnet.md) | A powered magnet device (generic supertype for all magnet kinds) |  no  |
| [BPM](BPM.md) | A Beam Position Monitor |  no  |
| [Quadrupole](Quadrupole.md) | A quadrupole focusing/defocusing magnet |  no  |
| [Marker](Marker.md) | A zero-length reference point, drift space, or survey marker |  no  |
| [Instrument](Instrument.md) | A generic beam diagnostic instrument |  no  |
| [System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |  yes  |
| [RFCavity](RFCavity.md) | A radio-frequency accelerating or bunching cavity |  no  |
| [Dipole](Dipole.md) | A dipole bending magnet |  no  |
| [Corrector](Corrector.md) | A dipole corrector magnet for orbit correction |  no  |
| [Solenoid](Solenoid.md) | A solenoid magnet |  no  |






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
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn-system:hasSubSystem
rank: 1000
domain: System
alias: has_sub_system
domain_of:
- System
range: System
multivalued: true

```
</details>