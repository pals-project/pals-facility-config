

# Class: FacilitySystem 


_Facility-specific signal binding configuration._





URI: [narad:FacilitySystem](https://w3id.org/narad_linkml/schema/narad/FacilitySystem)





```mermaid
 classDiagram
    class FacilitySystem
    click FacilitySystem href "../FacilitySystem/"
      System <|-- FacilitySystem
        click System href "../System/"
      
      FacilitySystem : control_system
        
          
    
        
        
        FacilitySystem --> "0..1" ControlSystem : control_system
        click ControlSystem href "../ControlSystem/"
    

        
      FacilitySystem : description
        
      FacilitySystem : facility_identifier
        
          
    
        
        
        FacilitySystem --> "*" FacilityIdentifier : facility_identifier
        click FacilityIdentifier href "../FacilityIdentifier/"
    

        
      FacilitySystem : has_sub_system
        
          
    
        
        
        FacilitySystem --> "*" System : has_sub_system
        click System href "../System/"
    

        
      FacilitySystem : has_system_capability
        
          
    
        
        
        FacilitySystem --> "*" SystemCapability : has_system_capability
        click SystemCapability href "../SystemCapability/"
    

        
      FacilitySystem : name
        
      FacilitySystem : naming_convention
        
      FacilitySystem : signal_definitions
        
          
    
        
        
        FacilitySystem --> "*" SignalDefinitions : signal_definitions
        click SignalDefinitions href "../SignalDefinitions/"
    

        
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
| [facility_identifier](facility_identifier.md) | * <br/> [FacilityIdentifier](FacilityIdentifier.md) | Globally unique identifier for the facility, with specified type and value | direct |
| [control_system](control_system.md) | 0..1 <br/> [ControlSystem](ControlSystem.md) | Identifier of the control system (e | direct |
| [naming_convention](naming_convention.md) | 0..1 <br/> [String](String.md) | Signal naming convention template (e | direct |
| [signal_definitions](signal_definitions.md) | * <br/> [SignalDefinitions](SignalDefinitions.md) | Structured container for facility-specific signal suffix templates | direct |
| [system_type](system_type.md) | 0..1 <br/> [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying | [System](System.md) |
| [has_sub_system](has_sub_system.md) | * <br/> [System](System.md) | Relates a System to one of its subsystems (SSN alignment) | [System](System.md) |
| [has_system_capability](has_system_capability.md) | * <br/> [SystemCapability](SystemCapability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) | [System](System.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradConfig](NaradConfig.md) | [deployed_system](deployed_system.md) | range | [FacilitySystem](FacilitySystem.md) |
| [SignalLayer](SignalLayer.md) | [facilities](facilities.md) | range | [FacilitySystem](FacilitySystem.md) |







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
- facility_identifier
- control_system
- naming_convention
- signal_definitions

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
  facility_identifier:
    name: facility_identifier
    description: Globally unique identifier for the facility, with specified type
      and value.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: facility_identifier
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    range: FacilityIdentifier
    multivalued: true
    inlined: false
  control_system:
    name: control_system
    description: Identifier of the control system (e.g. epics).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: control_system
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    range: ControlSystem
    inlined: true
  naming_convention:
    name: naming_convention
    description: Signal naming convention template (e.g. <device><signal_code>).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: naming_convention
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    - ControlSystem
    range: string
  signal_definitions:
    name: signal_definitions
    description: Structured container for facility-specific signal suffix templates.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: signal_definitions
    owner: FacilitySystem
    domain_of:
    - FacilitySystem
    range: SignalDefinitions
    multivalued: true
    inlined: true
  system_type:
    name: system_type
    description: High-level system type for classification and querying.
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
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    exact_mappings:
    - ssn-system:hasSubSystem
    rank: 1000
    domain: System
    alias: has_sub_system
    owner: FacilitySystem
    domain_of:
    - NaradConfig
    - System
    - DeviceSystem
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
    owner: FacilitySystem
    domain_of:
    - System
    - DeviceSystem
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
    owner: FacilitySystem
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
    owner: FacilitySystem
    domain_of:
    - NamedThing
    range: string

```
</details>