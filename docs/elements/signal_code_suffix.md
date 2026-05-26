

# Slot: signal_code_suffix 


_Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET._

__





URI: [narad:signal_code_suffix](https://example.org/narad_linkml/schema/narad/signal_code_suffix)
Alias: signal_code_suffix

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalBinding](SignalBinding.md) | A named control system suffix definition for one semantic signal |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:signal_code_suffix |
| native | narad:signal_code_suffix |




## LinkML Source

<details>
```yaml
name: signal_code_suffix
description: 'Facility-specific control-system (e.g. EPICS) naming suffix used to
  derive or interpret the signal binding, e.g. .S, M, :GSET.

  '
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: signal_code_suffix
domain_of:
- SignalBinding
range: string

```
</details>