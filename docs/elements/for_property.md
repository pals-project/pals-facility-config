

# Slot: for_property 


_SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal._

__





URI: [narad:for_property](https://example.org/narad_linkml/schema/narad/for_property)
Alias: for_property

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SystemCapability](SystemCapability.md) | A capability of a system |  yes  |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  yes  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:for_property |
| native | narad:for_property |
| exact | ssn:forProperty |




## LinkML Source

<details>
```yaml
name: for_property
description: 'SystemCapability → Signal: the capability can expose, monitor, control,
  or actuate that signal.

  '
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:forProperty
rank: 1000
alias: for_property
domain_of:
- SystemCapability
- InstanceSignalBinding
range: string
multivalued: true

```
</details>