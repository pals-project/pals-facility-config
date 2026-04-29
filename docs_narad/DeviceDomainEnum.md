# Enum: DeviceDomainEnum 




_High-level device domain for a control profile family. Intentionally kept small;  ADD new values here as the NARAD schema evolves._



URI: [https://w3id.org/narad_linkml/schema/narad/DeviceDomainEnum](https://w3id.org/narad_linkml/schema/narad/DeviceDomainEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Magnet | None | Magnet devices: dipoles, quadrupoles, correctors, solenoids |
| Instrument | None | Beam diagnostic instruments: BPMs, screens, halos, viewers, etc |
| RFCavity | None | RF cavity and RF-related devices |




## Slots

| Name | Description |
| ---  | --- |
| [device_domain](device_domain.md) | High-level device domain that this profile family governs |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/






## LinkML Source

<details>
```yaml
name: DeviceDomainEnum
description: High-level device domain for a control profile family. Intentionally
  kept small;  ADD new values here as the NARAD schema evolves.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
permissible_values:
  Magnet:
    text: Magnet
    description: 'Magnet devices: dipoles, quadrupoles, correctors, solenoids.'
  Instrument:
    text: Instrument
    description: 'Beam diagnostic instruments: BPMs, screens, halos, viewers, etc.'
  RFCavity:
    text: RFCavity
    description: RF cavity and RF-related devices.

```
</details>