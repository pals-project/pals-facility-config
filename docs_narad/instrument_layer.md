

# Slot: instrument_layer 


_Instrument definitions for this facility._





URI: [narad:instrument_layer](https://w3id.org/narad_linkml/schema/narad/instrument_layer)
Alias: instrument_layer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  yes  |






## Properties

* Range: [InstrumentSystem](InstrumentSystem.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:instrument_layer |
| native | narad:instrument_layer |




## LinkML Source

<details>
```yaml
name: instrument_layer
description: Instrument definitions for this facility.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: instrument_layer
domain_of:
- NaradConfig
range: InstrumentSystem
multivalued: true
inlined: true

```
</details>