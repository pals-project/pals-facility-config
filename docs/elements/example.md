

# Slot: example 


_A single example of how this naming convention is applied to a specific device instance and signal._





URI: [narad:example](https://example.org/narad_linkml/schema/narad/example)
Alias: example

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamingConventionExample](NamingConventionExample.md) | An example of a control system naming convention, illustrating how the templa... |  yes  |
| [TemplateExample](TemplateExample.md) | An example of a control system PV name generated from a naming convention tem... |  yes  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:example |
| native | narad:example |




## LinkML Source

<details>
```yaml
name: example
description: A single example of how this naming convention is applied to a specific
  device instance and signal.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: example
domain_of:
- NamingConventionExample
- TemplateExample
range: string

```
</details>