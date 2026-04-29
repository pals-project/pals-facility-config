

# Slot: is_abstract 


_If true, this profile is a template or abstract definition not intended to be directly assigned to a beamline element. Concrete profiles that refine a template should set this to false (the default)._





URI: [https://w3id.org/narad_linkml/schema/narad/is_abstract](https://w3id.org/narad_linkml/schema/narad/is_abstract)
Alias: is_abstract

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/is_abstract |
| native | https://w3id.org/narad_linkml/schema/narad/is_abstract |




## LinkML Source

<details>
```yaml
name: is_abstract
description: If true, this profile is a template or abstract definition not intended
  to be directly assigned to a beamline element. Concrete profiles that refine a template
  should set this to false (the default).
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
ifabsent: 'false'
alias: is_abstract
domain_of:
- CapabilityProfile
range: boolean

```
</details>