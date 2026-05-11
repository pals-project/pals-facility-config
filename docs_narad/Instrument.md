

# Class: Instrument 


_A generic beam diagnostic instrument._





URI: [narad:Instrument](https://w3id.org/narad_linkml/schema/narad/Instrument)





```mermaid
 classDiagram
    class Instrument
    click Instrument href "../Instrument/"
      System <|-- Instrument
        click System href "../System/"
      
      Instrument : description
        
      Instrument : has_sub_system
        
          
    
        
        
        Instrument --> "*" System : has_sub_system
        click System href "../System/"
    

        
      Instrument : has_system_capability
        
          
    
        
        
        Instrument --> "*" SystemCapability : has_system_capability
        click SystemCapability href "../SystemCapability/"
    

        
      Instrument : name
        
      Instrument : system_type
        
          
    
        
        
        Instrument --> "0..1" SystemTypeEnum : system_type
        click SystemTypeEnum href "../SystemTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [System](System.md)
        * **Instrument**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [system_type](system_type.md) | 0..1 <br/> [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying | [System](System.md) |
| [has_sub_system](has_sub_system.md) | * <br/> [System](System.md) | Relates a System to one of its subsystems (SSN alignment) | [System](System.md) |
| [has_system_capability](has_system_capability.md) | * <br/> [SystemCapability](SystemCapability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) | [System](System.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:Instrument |
| native | narad:Instrument |
| exact | ssn:System |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Instrument
description: A generic beam diagnostic instrument.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System

```
</details>

### Induced

<details>
```yaml
name: Instrument
description: A generic beam diagnostic instrument.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System
attributes:
  system_type:
    name: system_type
    description: High-level system type for classification and querying.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: system_type
    owner: Instrument
    domain_of:
    - System
    range: SystemTypeEnum
  has_sub_system:
    name: has_sub_system
    description: 'Relates a System to one of its subsystems (SSN alignment). Use for
      facility → control-system, facility → device, and device → component decomposition.

      '
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn-system:hasSubSystem
    rank: 1000
    domain: System
    alias: has_sub_system
    owner: Instrument
    domain_of:
    - NaradConfig
    - System
    - InstrumentSystem
    range: System
    multivalued: true
    inlined_as_list: true
  has_system_capability:
    name: has_system_capability
    description: 'Relates a System to a SystemCapability it supports (SSN-System alignment).
      Prefer this over directly attaching signals to systems when capability context
      matters.

      '
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn-system:hasSystemCapability
    rank: 1000
    domain: System
    alias: has_system_capability
    owner: Instrument
    domain_of:
    - System
    - InstrumentSystem
    range: SystemCapability
    multivalued: true
    inlined: true
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: Instrument
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
    owner: Instrument
    domain_of:
    - NamedThing
    range: string

```
</details>