

# Slot: full_pattern 


_A regex pattern that the full resolved value (e.g. after template substitution) must match for validation._





URI: [narad:full_pattern](https://example.org/narad_linkml/schema/narad/full_pattern)
Alias: full_pattern

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
| self | narad:full_pattern |
| native | narad:full_pattern |




## LinkML Source

<details>
```yaml
name: full_pattern
description: A regex pattern that the full resolved value (e.g. after template substitution)
  must match for validation.
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: full_pattern
domain_of:
- NamingConvention
range: string

```
</details>