

# Slot: is_hosted_by 


_Links an InstanceSignalBinding to the FacilitySystem it belongs to. This is the edge that connects the facility-specific bindings to the Facility node in the graph._

__





URI: [narad:is_hosted_by](https://example.org/narad_linkml/schema/narad/is_hosted_by)
Alias: is_hosted_by

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  yes  |






## Properties

* Range: [DeployedSystem](DeployedSystem.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:is_hosted_by |
| native | narad:is_hosted_by |
| broad | ssn-system:hasSubSystem, ssn:isHostedBy |




## LinkML Source

<details>
```yaml
name: is_hosted_by
description: 'Links an InstanceSignalBinding to the FacilitySystem it belongs to.
  This is the edge that connects the facility-specific bindings to the Facility node
  in the graph.

  '
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- ssn-system:hasSubSystem
- ssn:isHostedBy
rank: 1000
alias: is_hosted_by
domain_of:
- InstanceSignalBinding
range: DeployedSystem
multivalued: false

```
</details>