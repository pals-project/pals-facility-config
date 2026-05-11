# Enum: ElementKindEnum 




_Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile device_type values in sync with element kind values without circular imports. Values must stay aligned with CapabilityProfile.device_type._



URI: [narad:ElementKindEnum](https://w3id.org/narad_linkml/schema/narad/ElementKindEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Drift | None | A field-free drift space between elements |
| Marker | None | A zero-length reference point or survey marker |
| BPM | None | Beam Position Monitor |
| Corrector | None | Dipole corrector magnet for orbit correction |
| Dipole | None | Dipole bending magnet |
| Quadrupole | None | Quadrupole focusing/defocusing magnet |
| Solenoid | None | Solenoid magnet |
| CavityGradient | None | Accelerating or bunching cavity |
| RFCavity | None | Radio-frequency accelerating or bunching cavity |
| Instrument | None | Generic beam diagnostic instrument (halo monitor, viewer, etc |
| Magnet | None | Generic powered magnet device (supertype for all magnet kinds) |




## Slots

| Name | Description |
| ---  | --- |
| [device_type](device_type.md) | The specific device type this capability profile or system capability targets... |
| [element_kind](element_kind.md) | The type of this beamline element (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system






## LinkML Source

<details>
```yaml
name: ElementKindEnum
description: Controlled vocabulary for beamline element types, shared between the
  capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind).
  Keeping the enum here keeps profile device_type values in sync with element kind
  values without circular imports. Values must stay aligned with CapabilityProfile.device_type.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
permissible_values:
  Drift:
    text: Drift
    description: A field-free drift space between elements.
  Marker:
    text: Marker
    description: A zero-length reference point or survey marker.
  BPM:
    text: BPM
    description: Beam Position Monitor.
  Corrector:
    text: Corrector
    description: Dipole corrector magnet for orbit correction.
  Dipole:
    text: Dipole
    description: Dipole bending magnet.
  Quadrupole:
    text: Quadrupole
    description: Quadrupole focusing/defocusing magnet.
  Solenoid:
    text: Solenoid
    description: Solenoid magnet.
  CavityGradient:
    text: CavityGradient
    description: Accelerating or bunching cavity.
  RFCavity:
    text: RFCavity
    description: Radio-frequency accelerating or bunching cavity.
  Instrument:
    text: Instrument
    description: Generic beam diagnostic instrument (halo monitor, viewer, etc.).
  Magnet:
    text: Magnet
    description: Generic powered magnet device (supertype for all magnet kinds).

```
</details>