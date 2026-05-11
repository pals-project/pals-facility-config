

# Class: InstrumentSystem 


_A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph an InstrumentSystem is a subsystem of the Facility and a sibling to the ControlSystem._

__





URI: [narad:InstrumentSystem](https://w3id.org/narad_linkml/schema/narad/InstrumentSystem)





```mermaid
 classDiagram
    class InstrumentSystem
    click InstrumentSystem href "../InstrumentSystem/"
      System <|-- InstrumentSystem
        click System href "../System/"
      
      InstrumentSystem : description
        
      InstrumentSystem : device_type
        
          
    
        
        
        InstrumentSystem --> "0..1" ElementKindEnum : device_type
        click ElementKindEnum href "../ElementKindEnum/"
    

        
      InstrumentSystem : has_sub_system
        
          
    
        
        
        InstrumentSystem --> "*" System : has_sub_system
        click System href "../System/"
    

        
      InstrumentSystem : has_system_capability
        
          
    
        
        
        InstrumentSystem --> "0..1" SystemCapability : has_system_capability
        click SystemCapability href "../SystemCapability/"
    

        
      InstrumentSystem : name
        
      InstrumentSystem : system_type
        
          
    
        
        
        InstrumentSystem --> "0..1" SystemTypeEnum : system_type
        click SystemTypeEnum href "../SystemTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [System](System.md)
        * **InstrumentSystem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [device_type](device_type.md) | 0..1 <br/> [ElementKindEnum](ElementKindEnum.md) | The specific device type this capability profile or system capability targets... | direct |
| [has_sub_system](has_sub_system.md) | * <br/> [System](System.md) | Relates a System to one of its subsystems (SSN alignment) | direct |
| [has_system_capability](has_system_capability.md) | 0..1 <br/> [SystemCapability](SystemCapability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) | direct |
| [system_type](system_type.md) | 0..1 <br/> [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying | [System](System.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradConfig](NaradConfig.md) | [instrument_layer](instrument_layer.md) | range | [InstrumentSystem](InstrumentSystem.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:InstrumentSystem |
| native | narad:InstrumentSystem |
| exact | ssn:System |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstrumentSystem
description: 'A system representing a beam diagnostic instrument, magnet, or other
  non-magnet device. It represents the instrument as a whole rather than the control
  system for that instrument. In the SSN graph an InstrumentSystem is a subsystem
  of the Facility and a sibling to the ControlSystem.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System
slots:
- device_type
- has_sub_system
- has_system_capability
slot_usage:
  has_sub_system:
    name: has_sub_system
    range: System
    multivalued: true
    inlined_as_list: true
  has_system_capability:
    name: has_system_capability
    range: SystemCapability
    multivalued: false
    inlined: false

```
</details>

### Induced

<details>
```yaml
name: InstrumentSystem
description: 'A system representing a beam diagnostic instrument, magnet, or other
  non-magnet device. It represents the instrument as a whole rather than the control
  system for that instrument. In the SSN graph an InstrumentSystem is a subsystem
  of the Facility and a sibling to the ControlSystem.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System
slot_usage:
  has_sub_system:
    name: has_sub_system
    range: System
    multivalued: true
    inlined_as_list: true
  has_system_capability:
    name: has_system_capability
    range: SystemCapability
    multivalued: false
    inlined: false
attributes:
  device_type:
    name: device_type
    description: The specific device type this capability profile or system capability
      targets (e.g. Quadrupole, Corrector, BPM).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: device_type
    owner: InstrumentSystem
    domain_of:
    - ControlCapability
    - SignalDefinitions
    - InstrumentSystem
    - SystemCapability
    range: ElementKindEnum
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
    owner: InstrumentSystem
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
    owner: InstrumentSystem
    domain_of:
    - System
    - InstrumentSystem
    range: SystemCapability
    multivalued: false
    inlined: false
  system_type:
    name: system_type
    description: High-level system type for classification and querying.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: system_type
    owner: InstrumentSystem
    domain_of:
    - System
    range: SystemTypeEnum
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: InstrumentSystem
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
    owner: InstrumentSystem
    domain_of:
    - NamedThing
    range: string

```
</details>