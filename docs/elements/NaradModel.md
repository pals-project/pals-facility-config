

# Class: NaradModel 


_Top-level NARAD document container._





URI: [narad:NaradModel](https://example.org/narad_linkml/schema/narad/NaradModel)





```mermaid
 classDiagram
    class NaradModel
    click NaradModel href "../NaradModel/"
      NaradModel : beamlines
        
          
    
        
        
        NaradModel --> "*" Beamline : beamlines
        click Beamline href "../Beamline/"
    

        
      NaradModel : elements
        
          
    
        
        
        NaradModel --> "*" BeamlineElement : elements
        click BeamlineElement href "../BeamlineElement/"
    

        
      NaradModel : narad_config
        
          
    
        
        
        NaradModel --> "0..1" NaradConfig : narad_config
        click NaradConfig href "../NaradConfig/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [narad_config](narad_config.md) | 0..1 <br/> [NaradConfig](NaradConfig.md) | Top-level NARAD configuration block (capability_layer + signal_layer) | direct |
| [beamlines](beamlines.md) | * <br/> [Beamline](Beamline.md) | A top-level NARAD-system container for the ordered beamline definitions keyed... | direct |
| [elements](elements.md) | * <br/> [BeamlineElement](BeamlineElement.md) | Beamline element definitions referenced by name from beamline sequences | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:NaradModel |
| native | narad:NaradModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NaradModel
description: Top-level NARAD document container.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- narad_config
- beamlines
- elements
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: NaradModel
description: Top-level NARAD document container.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  narad_config:
    name: narad_config
    description: Top-level NARAD configuration block (capability_layer + signal_layer).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    aliases:
    - narad
    rank: 1000
    alias: narad_config
    owner: NaradModel
    domain_of:
    - NaradModel
    range: NaradConfig
    inlined: true
  beamlines:
    name: beamlines
    description: A top-level NARAD-system container for the ordered beamline definitions
      keyed by beamline name. Serializes as a keyed map by beamline name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: beamlines
    owner: NaradModel
    domain_of:
    - NaradModel
    range: Beamline
    multivalued: true
    inlined: true
  elements:
    name: elements
    description: Beamline element definitions referenced by name from beamline sequences.
      Serializes as a keyed map by element name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: elements
    owner: NaradModel
    domain_of:
    - NaradModel
    range: BeamlineElement
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>