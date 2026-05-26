

# Slot: voltage 


_RF voltage in volts._





URI: [narad:voltage](https://example.org/narad_linkml/schema/narad/voltage)
Alias: voltage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ElementParamSet](ElementParamSet.md) | Named physics-parameter block for a beamline element |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:voltage |
| native | narad:voltage |




## LinkML Source

<details>
```yaml
name: voltage
description: RF voltage in volts.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: voltage
domain_of:
- ElementParamSet
range: float

```
</details>