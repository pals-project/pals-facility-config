

# Class: SignalLayer 


_Signal-layer container for facility-specific signal bindings._





URI: [narad:SignalLayer](https://w3id.org/narad_linkml/schema/narad/SignalLayer)





```mermaid
 classDiagram
    class SignalLayer
    click SignalLayer href "../SignalLayer/"
      SignalLayer : facilities
        
          
    
        
        
        SignalLayer --> "*" FacilityConfig : facilities
        click FacilityConfig href "../FacilityConfig/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [facilities](facilities.md) | * <br/> [FacilityConfig](FacilityConfig.md) | Facility-specific signal binding configurations keyed by facility name | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradConfig](NaradConfig.md) | [signal_layer](signal_layer.md) | range | [SignalLayer](SignalLayer.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:SignalLayer |
| native | narad:SignalLayer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SignalLayer
description: Signal-layer container for facility-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- facilities

```
</details>

### Induced

<details>
```yaml
name: SignalLayer
description: Signal-layer container for facility-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  facilities:
    name: facilities
    description: Facility-specific signal binding configurations keyed by facility
      name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: facilities
    owner: SignalLayer
    domain_of:
    - SignalLayer
    range: FacilityConfig
    multivalued: true
    inlined: true

```
</details>