

# Slot: type_signal_sets 


_Signal suffix groups keyed by device type or device domain name. Domain-level keys (e.g. Magnet, RFCavity) represent signals shared across all types in that domain; device-type keys (e.g. Quadrupole, BPM) are type-specific. New device types require no schema changes._





URI: [https://w3id.org/narad_linkml/schema/narad/type_signal_sets](https://w3id.org/narad_linkml/schema/narad/type_signal_sets)
Alias: type_signal_sets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | EPICS signal suffix templates keyed by device type or device domain |  no  |






## Properties

* Range: [DeviceTypeSignalSet](DeviceTypeSignalSet.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/type_signal_sets |
| native | https://w3id.org/narad_linkml/schema/narad/type_signal_sets |




## LinkML Source

<details>
```yaml
name: type_signal_sets
description: Signal suffix groups keyed by device type or device domain name. Domain-level
  keys (e.g. Magnet, RFCavity) represent signals shared across all types in that domain;
  device-type keys (e.g. Quadrupole, BPM) are type-specific. New device types require
  no schema changes.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: type_signal_sets
domain_of:
- SignalDefinitions
range: DeviceTypeSignalSet
multivalued: true
inlined: true

```
</details>