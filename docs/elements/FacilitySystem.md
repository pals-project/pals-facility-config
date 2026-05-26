

# Class: FacilitySystem 


_Facility-specific signal binding configuration._





URI: [narad:FacilitySystem](https://example.org/narad_linkml/schema/narad/FacilitySystem)





```mermaid
 classDiagram
    class FacilitySystem
    click FacilitySystem href "../FacilitySystem/"
      System <|-- FacilitySystem
        click System href "../System/"
      
      FacilitySystem : description
        
      FacilitySystem : has_control_system
        
          
    
        
        
        FacilitySystem --> "0..1" ControlSystem : has_control_system
        click ControlSystem href "../ControlSystem/"
    

        
      FacilitySystem : has_sub_system
        
          
    
        
        
        FacilitySystem --> "*" System : has_sub_system
        click System href "../System/"
    

        
      FacilitySystem : has_system_capability
        
          
    
        
        
        FacilitySystem --> "*" SystemCapability : has_system_capability
        click SystemCapability href "../SystemCapability/"
    

        
      FacilitySystem : hosts_device
        
          
    
        
        
        FacilitySystem --> "*" Device : hosts_device
        click Device href "../Device/"
    

        
      FacilitySystem : name
        
      FacilitySystem : system_type
        
          
    
        
        
        FacilitySystem --> "0..1" SystemTypeEnum : system_type
        click SystemTypeEnum href "../SystemTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [System](System.md)
        * **FacilitySystem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_control_system](has_control_system.md) | 0..1 <br/> [ControlSystem](ControlSystem.md) | Relates a System to one of its control systems (SSN alignment to sub system) | direct |
| [hosts_device](hosts_device.md) | * <br/> [Device](Device.md) | Structured container for facility-specific signal suffix templates | direct |
| [system_type](system_type.md) | 0..1 <br/> [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying | [System](System.md) |
| [has_sub_system](has_sub_system.md) | * <br/> [System](System.md) | Relates a System to one of its subsystems (SSN alignment) | [System](System.md) |
| [has_system_capability](has_system_capability.md) | * <br/> [SystemCapability](SystemCapability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) | [System](System.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SignalLayer](SignalLayer.md) | [facilities](facilities.md) | range | [FacilitySystem](FacilitySystem.md) |
| [FacilitySystem](FacilitySystem.md) | [hosts_device](hosts_device.md) | domain | [FacilitySystem](FacilitySystem.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:FacilitySystem |
| native | narad:FacilitySystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FacilitySystem
description: Facility-specific signal binding configuration.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: System
slots:
- has_control_system
- hosts_device

```
</details>

### Induced

<details>
```yaml
name: FacilitySystem
description: Facility-specific signal binding configuration.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: System
attributes:
  has_control_system:
    name: has_control_system
    description: 'Relates a System to one of its control systems (SSN alignment to
      sub system). Use for facility → control-system, facility → device, and device
      → component decomposition.

      '
    in_subset:
    - relationship
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    broad_mappings:
    - ssn-system:hasSubSystem
    rank: 1000
    domain: System
    alias: has_control_system
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    - DeployedSystem
    range: ControlSystem
    multivalued: false
  hosts_device:
    name: hosts_device
    description: Structured container for facility-specific signal suffix templates.
    in_subset:
    - relationship
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    domain: FacilitySystem
    alias: hosts_device
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    range: Device
    multivalued: true
    inlined: true
  system_type:
    name: system_type
    description: High-level system type for classification and querying.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: system_type
    owner: FacilitySystem
    domain_of:
    - System
    range: SystemTypeEnum
  has_sub_system:
    name: has_sub_system
    description: 'Relates a System to one of its subsystems (SSN alignment). Use for
      facility → control-system, facility → device, and device → component decomposition.

      '
    in_subset:
    - relationship
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn-system:hasSubSystem
    rank: 1000
    domain: System
    alias: has_sub_system
    owner: FacilitySystem
    domain_of:
    - System
    - Device
    range: System
    multivalued: true
    inlined_as_list: true
  has_system_capability:
    name: has_system_capability
    description: 'Relates a System to a SystemCapability it supports (SSN-System alignment).
      Prefer this over directly attaching signals to systems when capability context
      matters.

      '
    in_subset:
    - relationship
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn-system:hasSystemCapability
    rank: 1000
    domain: System
    alias: has_system_capability
    owner: FacilitySystem
    domain_of:
    - System
    - Device
    range: SystemCapability
    multivalued: true
    inlined: true
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: FacilitySystem
    domain_of:
    - NamedThing
    range: string
    required: true
  description:
    name: description
    description: Detailed description of the entity.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: description
    owner: FacilitySystem
    domain_of:
    - NamedThing
    - NamingConventionExample
    - TemplateExample
    range: string

```
</details>