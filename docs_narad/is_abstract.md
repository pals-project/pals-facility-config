

# Slot: is_abstract 


_If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default)._





URI: [narad:is_abstract](https://w3id.org/narad_linkml/schema/narad/is_abstract)
Alias: is_abstract

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds type-specific ... |  no  |
| [CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |  no  |
| [MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |  no  |
| [QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |  no  |
| [DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |  no  |
| [InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |  no  |
| [SystemCapability](SystemCapability.md) | A capability of a system |  no  |
| [BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |  no  |
| [SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |  no  |
| [CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:is_abstract |
| native | narad:is_abstract |




## LinkML Source

<details>
```yaml
name: is_abstract
description: If true, this profile is a template not intended to be directly assigned
  to a beamline element. Concrete profiles set this to false (default).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
ifabsent: 'false'
alias: is_abstract
domain_of:
- CapabilityProfile
- SystemCapability
range: boolean

```
</details>