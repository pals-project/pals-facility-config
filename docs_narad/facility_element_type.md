

# Slot: facility_element_type 


_Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector). named facility_element_type here to avoid conflict with the LinkML metamodel 'type'  designator used for polymorphic class selection._





URI: [narad:facility_element_type](https://w3id.org/narad_linkml/schema/narad/facility_element_type)
Alias: facility_element_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilityParamSet](FacilityParamSet.md) | Facility-specific element parameters block for beamline elements |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* type


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:facility_element_type |
| native | narad:facility_element_type |




## LinkML Source

<details>
```yaml
name: facility_element_type
description: Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector).
  named facility_element_type here to avoid conflict with the LinkML metamodel 'type'  designator
  used for polymorphic class selection.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
aliases:
- type
rank: 1000
alias: facility_element_type
domain_of:
- FacilityParamSet
range: string

```
</details>