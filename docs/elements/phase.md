

# Slot: phase 


_RF phase in degrees._





URI: [narad:phase](https://example.org/narad_linkml/schema/narad/phase)
Alias: phase

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
| self | narad:phase |
| native | narad:phase |




## LinkML Source

<details>
```yaml
name: phase
description: RF phase in degrees.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: phase
domain_of:
- ElementParamSet
range: float

```
</details>