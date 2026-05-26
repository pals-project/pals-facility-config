

# Slot: template 


_A template string for constructing control system PV names based on the semantic signal name and device instance. This can include placeholders for the device name and signal suffix, e.g. {device_name}{signal_suffix}._





URI: [narad:template](https://example.org/narad_linkml/schema/narad/template)
Alias: template

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamingConvention](NamingConvention.md) | A template for constructing facility-specific signal names from a semantic si... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:template |
| native | narad:template |




## LinkML Source

<details>
```yaml
name: template
description: A template string for constructing control system PV names based on the
  semantic signal name and device instance. This can include placeholders for the
  device name and signal suffix, e.g. {device_name}{signal_suffix}.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: template
domain_of:
- NamingConvention
range: string

```
</details>