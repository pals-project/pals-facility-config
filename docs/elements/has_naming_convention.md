

# Slot: has_naming_convention 


_Signal naming conventions used by this control system defined in a machine actionable manner.  This is where you would capture the patterns/templates for how control system PVs or signals are constructed for this control system,  for example, the EPICS convention of using suffixes like .R, .S, :GSET to indicate readback, status, and setpoint signals. Multiple naming conventions can be captured if a control system uses more than one convention for different device types or domains._





URI: [narad:has_naming_convention](https://example.org/narad_linkml/schema/narad/has_naming_convention)
Alias: has_naming_convention

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlSystem](ControlSystem.md) | A control system (e |  yes  |






## Properties

* Range: [NamingConvention](NamingConvention.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:has_naming_convention |
| native | narad:has_naming_convention |




## LinkML Source

<details>
```yaml
name: has_naming_convention
description: Signal naming conventions used by this control system defined in a machine
  actionable manner.  This is where you would capture the patterns/templates for how
  control system PVs or signals are constructed for this control system,  for example,
  the EPICS convention of using suffixes like .R, .S, :GSET to indicate readback,
  status, and setpoint signals. Multiple naming conventions can be captured if a control
  system uses more than one convention for different device types or domains.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: has_naming_convention
domain_of:
- ControlSystem
range: NamingConvention
multivalued: true
inlined: true
inlined_as_list: true

```
</details>