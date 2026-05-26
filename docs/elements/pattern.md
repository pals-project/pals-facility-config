

# Slot: pattern 


_A regex pattern that the value of this slot must match for validation._





URI: [narad:pattern](https://example.org/narad_linkml/schema/narad/pattern)
Alias: pattern

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TemplateComponent](TemplateComponent.md) | A component of a naming convention template, representing a variable part of ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:pattern |
| native | narad:pattern |




## LinkML Source

<details>
```yaml
name: pattern
description: A regex pattern that the value of this slot must match for validation.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: pattern
domain_of:
- TemplateComponent
range: string

```
</details>