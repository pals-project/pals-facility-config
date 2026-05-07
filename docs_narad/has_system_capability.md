

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
range: SystemCapability
multivalued: true

```
</details>