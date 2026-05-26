

# Slot: has_control_system 


_Relates a System to one of its control systems (SSN alignment to sub system). Use for facility → control-system, facility → device, and device → component decomposition._

__





URI: [narad:has_control_system](https://example.org/narad_linkml/schema/narad/has_control_system)
Alias: has_control_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeployedSystem](DeployedSystem.md) | A deployed system, with an identified facility, that is the subject of a NARA... |  yes  |
| [FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |  no  |






## Properties

* Range: [ControlSystem](ControlSystem.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:has_control_system |
| native | narad:has_control_system |
| broad | ssn-system:hasSubSystem |




## LinkML Source

<details>
```yaml
name: has_control_system
description: 'Relates a System to one of its control systems (SSN alignment to sub
  system). Use for facility → control-system, facility → device, and device → component
  decomposition.

  '
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- ssn-system:hasSubSystem
rank: 1000
domain: System
alias: has_control_system
domain_of:
- FacilitySystem
- DeployedSystem
range: ControlSystem
multivalued: false

```
</details>