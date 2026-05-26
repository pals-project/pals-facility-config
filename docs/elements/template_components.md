

# Slot: template_components 


_Structured components of the naming convention template, for capturing the template in a more machine-actionable way than a raw string.  For example, you could have components for the device name, signal suffix, and any fixed parts of the naming convention._





URI: [narad:template_components](https://example.org/narad_linkml/schema/narad/template_components)
Alias: template_components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamingConvention](NamingConvention.md) | A template for constructing facility-specific signal names from a semantic si... |  no  |






## Properties

* Range: [TemplateComponent](TemplateComponent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:template_components |
| native | narad:template_components |




## LinkML Source

<details>
```yaml
name: template_components
description: Structured components of the naming convention template, for capturing
  the template in a more machine-actionable way than a raw string.  For example, you
  could have components for the device name, signal suffix, and any fixed parts of
  the naming convention.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: template_components
domain_of:
- NamingConvention
range: TemplateComponent
multivalued: true
inlined: true
inlined_as_list: true

```
</details>