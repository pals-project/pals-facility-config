

# Slot: facility_element_type 


_Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector). named facility_element_type here to avoid conflict with the LinkML metamodel 'type' designator used for polymorphic class selection._





URI: [https://w3id.org/narad_linkml/schema/narad/facility_element_type](https://w3id.org/narad_linkml/schema/narad/facility_element_type)
Alias: facility_element_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FacilityParams](FacilityParams.md) | Facility-specific element parameters: type designation, accelerator model nam... |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* type


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/facility_element_type |
| native | https://w3id.org/narad_linkml/schema/narad/facility_element_type |




## LinkML Source

<details>
```yaml
name: facility_element_type
description: Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector).
  named facility_element_type here to avoid conflict with the LinkML metamodel 'type'
  designator used for polymorphic class selection.
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- type
rank: 1000
alias: facility_element_type
domain_of:
- FacilityParams
range: string

```
</details>