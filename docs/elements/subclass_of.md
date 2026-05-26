

# Slot: subclass_of 


_-> NARAD alias for rdfs:subClassOf. Links a type-specific capability to the generic capability it extends. In the graph this edge is labelled narad:subclassOf._





URI: [narad:subclass_of](https://example.org/narad_linkml/schema/narad/subclass_of)
Alias: subclass_of

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Capability](Capability.md) | A reusable device-type control profile that extends a generic shared capabili... |  yes  |
| [Device](Device.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |  no  |






## Properties

* Range: [System](System.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:subclass_of |
| native | narad:subclass_of |
| exact | rdfs:subClassOf |




## LinkML Source

<details>
```yaml
name: subclass_of
description: -> NARAD alias for rdfs:subClassOf. Links a type-specific capability
  to the generic capability it extends. In the graph this edge is labelled narad:subclassOf.
in_subset:
- relationship
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- rdfs:subClassOf
rank: 1000
alias: subclass_of
domain_of:
- Capability
- Device
range: System
multivalued: false

```
</details>