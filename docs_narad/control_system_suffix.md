

# Slot: control_system_suffix 


_Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET._

__





URI: [narad:control_system_suffix](https://w3id.org/narad_linkml/schema/narad/control_system_suffix)
Alias: control_system_suffix

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
| self | narad:control_system_suffix |
| native | narad:control_system_suffix |




## LinkML Source

<details>
```yaml
name: control_system_suffix
description: 'Facility-specific control-system (e.g. EPICS) naming suffix used to
  derive or interpret the signal binding, e.g. .S, M, :GSET.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: control_system_suffix
domain_of:
- SignalBinding
range: string

```
</details>