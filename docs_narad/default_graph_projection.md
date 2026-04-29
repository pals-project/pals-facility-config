

# Slot: default_graph_projection 


_The canonical graph projection for all profile families in this capability layer. Defines the full set of possible node labels (except device, which is derived from each family's device_domain) and the complete relationship vocabulary. Individual families may provide a graph_projection override when needed._





URI: [https://w3id.org/narad_linkml/schema/narad/default_graph_projection](https://w3id.org/narad_linkml/schema/narad/default_graph_projection)
Alias: default_graph_projection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityLayer](CapabilityLayer.md) | Capability-layer container for profile families and a shared default graph pr... |  no  |






## Properties

* Range: [GraphProjection](GraphProjection.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/default_graph_projection |
| native | https://w3id.org/narad_linkml/schema/narad/default_graph_projection |




## LinkML Source

<details>
```yaml
name: default_graph_projection
description: The canonical graph projection for all profile families in this capability
  layer. Defines the full set of possible node labels (except device, which is derived
  from each family's device_domain) and the complete relationship vocabulary. Individual
  families may provide a graph_projection override when needed.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: default_graph_projection
domain_of:
- CapabilityLayer
range: GraphProjection
inlined: true

```
</details>