

# Class: CavityGradientCapability 


_RF cavity capability with gradient control, readback, and status signals._





URI: [narad:CavityGradientCapability](https://w3id.org/narad_linkml/schema/narad/CavityGradientCapability)





```mermaid
 classDiagram
    class CavityGradientCapability
    click CavityGradientCapability href "../CavityGradientCapability/"
      SystemCapability <|-- CavityGradientCapability
        click SystemCapability href "../SystemCapability/"
      
      CavityGradientCapability : description
        
      CavityGradientCapability : device_type
        
          
    
        
        
        CavityGradientCapability --> "0..1" ElementKindEnum : device_type
        click ElementKindEnum href "../ElementKindEnum/"
    

        
      CavityGradientCapability : for_property
        
      CavityGradientCapability : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [SystemCapability](SystemCapability.md)
        * **CavityGradientCapability**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [for_property](for_property.md) | * <br/> [String](String.md) | SystemCapability → Signal: the capability can expose, monitor, control, or ac... | [SystemCapability](SystemCapability.md) |
| [device_type](device_type.md) | 0..1 <br/> [ElementKindEnum](ElementKindEnum.md) | The specific device type this capability profile or system capability targets... | [SystemCapability](SystemCapability.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:CavityGradientCapability |
| native | narad:CavityGradientCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CavityGradientCapability
description: RF cavity capability with gradient control, readback, and status signals.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: SystemCapability

```
</details>

### Induced

<details>
```yaml
name: CavityGradientCapability
description: RF cavity capability with gradient control, readback, and status signals.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: SystemCapability
attributes:
  for_property:
    name: for_property
    description: 'SystemCapability → Signal: the capability can expose, monitor, control,
      or actuate that signal.

      '
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn:forProperty
    rank: 1000
    alias: for_property
    owner: CavityGradientCapability
    domain_of:
    - SystemCapability
    - InstanceSignalBinding
    range: string
    multivalued: true
  device_type:
    name: device_type
    description: The specific device type this capability profile or system capability
      targets (e.g. Quadrupole, Corrector, BPM).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: device_type
    owner: CavityGradientCapability
    domain_of:
    - ControlCapability
    - SignalDefinitions
    - InstrumentSystem
    - SystemCapability
    range: ElementKindEnum
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: CavityGradientCapability
    domain_of:
    - NamedThing
    range: string
    required: true
  description:
    name: description
    description: Detailed description of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: description
    owner: CavityGradientCapability
    domain_of:
    - NamedThing
    range: string

```
</details>