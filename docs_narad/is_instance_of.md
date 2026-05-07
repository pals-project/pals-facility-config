

# Slot: is_instance_of 


_NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Procedure class that implements the signal binding, e.g. narad:CavityGradientControlCapability._

__





URI: [narad:is_instance_of](https://w3id.org/narad_linkml/schema/narad/is_instance_of)
Alias: is_instance_of

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  yes  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:is_instance_of |
| native | narad:is_instance_of |
| exact | rdf:type |




## LinkML Source

<details>
```yaml
name: is_instance_of
description: 'NARAD alias for rdf:type. Links a facility-specific instance node to
  the LinkML class or semantic class it instantiates. In the graph this edge is labelled
  narad:isInstanceOf. Values are typically the rdf:type of the Procedure class that
  implements the signal binding, e.g. narad:CavityGradientControlCapability.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- rdf:type
rank: 1000
alias: is_instance_of
domain_of:
- InstanceSignalBinding
range: uriorcurie
multivalued: true

```
</details>