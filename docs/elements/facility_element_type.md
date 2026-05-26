

# Slot: facility_element_type 


_capture the facility-specific or local designation (e.g., "QW", "WarmCavity", "HCorrector").  Isused for local naming, inventory, or legacy mapping of instances of facility elements (within elements:)  to the facility-specific type designations used in the control system or elsewhere at the facility._





URI: [narad:facility_element_type](https://example.org/narad_linkml/schema/narad/facility_element_type)
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
description: capture the facility-specific or local designation (e.g., "QW", "WarmCavity",
  "HCorrector").  Isused for local naming, inventory, or legacy mapping of instances
  of facility elements (within elements:)  to the facility-specific type designations
  used in the control system or elsewhere at the facility.
in_subset:
- label
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