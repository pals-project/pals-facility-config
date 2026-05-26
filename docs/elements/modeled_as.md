

# Slot: modeled_as 


_Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK)._





URI: [narad:modeled_as](https://example.org/narad_linkml/schema/narad/modeled_as)
Alias: modeled_as

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilityParamSet](FacilityParamSet.md) | Facility-specific element parameters block for beamline elements |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:modeled_as |
| native | narad:modeled_as |




## LinkML Source

<details>
```yaml
name: modeled_as
description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: modeled_as
domain_of:
- FacilityParamSet
range: string

```
</details>