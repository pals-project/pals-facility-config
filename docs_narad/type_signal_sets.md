

# Slot: type_signal_sets 


_Signal suffix groups keyed by device type or device domain name. Domain-level keys cover signals shared across all types in that domain; device-type keys are type-specific._





URI: [narad:type_signal_sets](https://w3id.org/narad_linkml/schema/narad/type_signal_sets)
Alias: type_signal_sets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | Control system signal suffix templates keyed by device type or device domain |  no  |






## Properties

* Range: [TypeSignalSet](TypeSignalSet.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:type_signal_sets |
| native | narad:type_signal_sets |




## LinkML Source

<details>
```yaml
name: type_signal_sets
description: Signal suffix groups keyed by device type or device domain name. Domain-level
  keys cover signals shared across all types in that domain; device-type keys are
  type-specific.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: type_signal_sets
domain_of:
- SignalDefinitions
range: TypeSignalSet
multivalued: false
inlined: true

```
</details>