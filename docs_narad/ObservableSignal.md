

# Class: ObservableSignal 


_A NARAD signal that is read, monitored, observed, or exposed by a system. Examples: current_readback, status, horizontal_beam_position, gradient_readback. Aligned to sosa:ObservableProperty._

__





URI: [narad:ObservableSignal](https://w3id.org/narad_linkml/schema/narad/ObservableSignal)





```mermaid
 classDiagram
    class ObservableSignal
    click ObservableSignal href "../ObservableSignal/"
      Signal <|-- ObservableSignal
        click Signal href "../Signal/"
      
      ObservableSignal : data_type
        
          
    
        
        
        ObservableSignal --> "0..1" DataTypeEnum : data_type
        click DataTypeEnum href "../DataTypeEnum/"
    

        
      ObservableSignal : description
        
      ObservableSignal : name
        
      ObservableSignal : role
        
          
    
        
        
        ObservableSignal --> "0..1" SignalRoleEnum : role
        click SignalRoleEnum href "../SignalRoleEnum/"
    

        
      ObservableSignal : units
        
      ObservableSignal : units_uri
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Signal](Signal.md)
        * **ObservableSignal**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 0..1 <br/> [SignalRoleEnum](SignalRoleEnum.md) | The semantic role of the signal within its capability | [Signal](Signal.md) |
| [data_type](data_type.md) | 0..1 <br/> [DataTypeEnum](DataTypeEnum.md) | The data type of the signal's value | [Signal](Signal.md) |
| [units](units.md) | 0..1 <br/> [String](String.md) | Conventional unit symbol (e | [Signal](Signal.md) |
| [units_uri](units_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Machine-resolvable QUDT unit reference (e | [Signal](Signal.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:ObservableSignal |
| native | narad:ObservableSignal |
| broad | sosa:ObservableProperty |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ObservableSignal
description: 'A NARAD signal that is read, monitored, observed, or exposed by a system.
  Examples: current_readback, status, horizontal_beam_position, gradient_readback.
  Aligned to sosa:ObservableProperty.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- sosa:ObservableProperty
is_a: Signal

```
</details>

### Induced

<details>
```yaml
name: ObservableSignal
description: 'A NARAD signal that is read, monitored, observed, or exposed by a system.
  Examples: current_readback, status, horizontal_beam_position, gradient_readback.
  Aligned to sosa:ObservableProperty.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- sosa:ObservableProperty
is_a: Signal
attributes:
  role:
    name: role
    description: The semantic role of the signal within its capability.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: role
    owner: ObservableSignal
    domain_of:
    - Signal
    range: SignalRoleEnum
  data_type:
    name: data_type
    description: The data type of the signal's value.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: data_type
    owner: ObservableSignal
    domain_of:
    - Signal
    range: DataTypeEnum
  units:
    name: units
    description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: units
    owner: ObservableSignal
    domain_of:
    - Signal
    range: string
  units_uri:
    name: units_uri
    description: 'Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere).
      The si-unit: prefix maps to http://qudt.org/vocab/unit/.'
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: units_uri
    owner: ObservableSignal
    domain_of:
    - Signal
    range: uriorcurie
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: ObservableSignal
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
    owner: ObservableSignal
    domain_of:
    - NamedThing
    - SignalBinding
    range: string

```
</details>