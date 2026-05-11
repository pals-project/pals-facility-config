

# Slot: device_type 


_The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM)._





URI: [narad:device_type](https://w3id.org/narad_linkml/schema/narad/device_type)
Alias: device_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |
| [SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |  no  |
| [InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |  no  |
| [MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |  no  |
| [DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |  no  |
| [CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |  no  |
| [ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |  no  |
| [CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |  no  |
| [QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |  no  |
| [BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |  no  |






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
- ControlCapability
- SignalDefinitions
- InstrumentSystem
- SystemCapability
range: ElementKindEnum

```
</details>