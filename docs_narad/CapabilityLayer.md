

# Class: CapabilityLayer 


_Capability-layer container for profile families and a shared default graph projection._





URI: [https://w3id.org/narad_linkml/schema/narad/CapabilityLayer](https://w3id.org/narad_linkml/schema/narad/CapabilityLayer)





```mermaid
 classDiagram
    class CapabilityLayer
    click CapabilityLayer href "../CapabilityLayer/"
      CapabilityLayer : default_graph_projection
        
          
    
        
        
        CapabilityLayer --> "0..1" GraphProjection : default_graph_projection
        click GraphProjection href "../GraphProjection/"
    

        
      CapabilityLayer : profiles
        
          
    
        
        
        CapabilityLayer --> "*" ControlProfileFamily : profiles
        click ControlProfileFamily href "../ControlProfileFamily/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [default_graph_projection](default_graph_projection.md) | 0..1 <br/> [GraphProjection](GraphProjection.md) | The canonical graph projection for all profile families in this capability la... | direct |
| [profiles](profiles.md) | * <br/> [ControlProfileFamily](ControlProfileFamily.md) | Control profile families keyed by family name | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradConfig](NaradConfig.md) | [capability_layer](capability_layer.md) | range | [CapabilityLayer](CapabilityLayer.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/CapabilityLayer |
| native | https://w3id.org/narad_linkml/schema/narad/CapabilityLayer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CapabilityLayer
description: Capability-layer container for profile families and a shared default
  graph projection.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- default_graph_projection
- profiles

```
</details>

### Induced

<details>
```yaml
name: CapabilityLayer
description: Capability-layer container for profile families and a shared default
  graph projection.
from_schema: https://w3id.org/narad_linkml/schema/narad/
attributes:
  default_graph_projection:
    name: default_graph_projection
    description: The canonical graph projection for all profile families in this capability
      layer. Defines the full set of possible node labels (except device, which is
      derived from each family's device_domain) and the complete relationship vocabulary.
      Individual families may provide a graph_projection override when needed.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: default_graph_projection
    owner: CapabilityLayer
    domain_of:
    - CapabilityLayer
    range: GraphProjection
    inlined: true
  profiles:
    name: profiles
    description: Control profile families keyed by family name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: profiles
    owner: CapabilityLayer
    domain_of:
    - CapabilityLayer
    range: ControlProfileFamily
    multivalued: true
    inlined: true

```
</details>