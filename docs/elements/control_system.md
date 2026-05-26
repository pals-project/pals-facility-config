

# Slot: control_system 


_Identifier of the control system (e.g. epics)._





URI: [narad:control_system](https://example.org/narad_linkml/schema/narad/control_system)
Alias: control_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  yes  |






## Properties

* Range: [ControlSystem](ControlSystem.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:control_system |
| native | narad:control_system |




## LinkML Source

<details>
```yaml
name: control_system
description: Identifier of the control system (e.g. epics).
in_subset:
- instance
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: control_system
domain_of:
- NaradConfig
range: ControlSystem
inlined: true

```
</details>