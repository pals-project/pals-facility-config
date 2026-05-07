

# Slot: device_type 


_The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM)._





URI: [narad:device_type](https://w3id.org/narad_linkml/schema/narad/device_type)
Alias: device_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |  no  |
| [SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |  no  |
| [BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |  no  |
| [CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |  no  |
| [InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |  no  |
| [QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |  no  |
| [DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds type-specific ... |  no  |
| [CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |  no  |






## Properties

* Range: [ElementKindEnum](ElementKindEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:device_type |
| native | narad:device_type |




## LinkML Source

<details>
```yaml
name: device_type
description: The specific device type this capability profile or system capability
  targets (e.g. Quadrupole, Corrector, BPM).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: device_type
domain_of:
- CapabilityProfile
- SystemCapability
range: ElementKindEnum

```
</details>