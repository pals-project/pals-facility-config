

# Slot: is_property_of 


_Inverse of for_property: links the Class Signal to the Class of SignalBinding Procedure that implements it. This can also link the Instance of a SignalBinding to the ControlSystem that implements it. This is the edge that connects the signal definitions to the facility-specific bindings in the graph. Values are typically the ControlSystem that implements this binding, e.g. narad:epics (for EPICS control system). NOTE: The value of this slot must match one of the values in narad_config.has_sub_system._

__





URI: [narad:is_property_of](https://example.org/narad_linkml/schema/narad/is_property_of)
Alias: is_property_of

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Capability](Capability.md) | A reusable device-type control profile that extends a generic shared capabili... |  yes  |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  yes  |






## Properties

* Range: [ControlSystem](ControlSystem.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:is_property_of |
| native | narad:is_property_of |
| broad | ssn:isPropertyOf |




## LinkML Source

<details>
```yaml
name: is_property_of
description: 'Inverse of for_property: links the Class Signal to the Class of SignalBinding
  Procedure that implements it. This can also link the Instance of a SignalBinding
  to the ControlSystem that implements it. This is the edge that connects the signal
  definitions to the facility-specific bindings in the graph. Values are typically
  the ControlSystem that implements this binding, e.g. narad:epics (for EPICS control
  system). NOTE: The value of this slot must match one of the values in narad_config.has_sub_system.

  '
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- ssn:isPropertyOf
rank: 1000
alias: is_property_of
domain_of:
- Capability
- InstanceSignalBinding
range: ControlSystem
multivalued: false

```
</details>