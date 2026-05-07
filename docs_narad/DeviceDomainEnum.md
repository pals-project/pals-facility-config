# Enum: DeviceDomainEnum 




_High-level device domain for a control profile family. Use: groups profile families, not individual elements._



URI: [narad:DeviceDomainEnum](https://w3id.org/narad_linkml/schema/narad/DeviceDomainEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Magnet | None | Magnet devices: dipoles, quadrupoles, correctors, solenoids |
| Instrument | None | Beam diagnostic instruments: BPMs, screens, viewers, etc |
| RFCavity | None | RF cavity and RF-related devices |




## Slots

| Name | Description |
| ---  | --- |
| [device_domain](device_domain.md) | High-level device domain that this profile family governs |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system






## LinkML Source

<details>
```yaml
name: DeviceDomainEnum
description: 'High-level device domain for a control profile family. Use: groups profile
  families, not individual elements.'
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
permissible_values:
  Magnet:
    text: Magnet
    description: 'Magnet devices: dipoles, quadrupoles, correctors, solenoids.'
  Instrument:
    text: Instrument
    description: 'Beam diagnostic instruments: BPMs, screens, viewers, etc.'
  RFCavity:
    text: RFCavity
    description: RF cavity and RF-related devices.

```
</details>