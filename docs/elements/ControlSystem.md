

# Class: ControlSystem 


_A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility._

__





URI: [narad:ControlSystem](https://example.org/narad_linkml/schema/narad/ControlSystem)





```mermaid
 classDiagram
    class ControlSystem
    click ControlSystem href "../ControlSystem/"
      System <|-- ControlSystem
        click System href "../System/"
      
      ControlSystem : description
        
      ControlSystem : has_naming_convention
        
          
    
        
        
        ControlSystem --> "*" NamingConvention : has_naming_convention
        click NamingConvention href "../NamingConvention/"
    

        
      ControlSystem : has_sub_system
        
          
    
        
        
        ControlSystem --> "*" System : has_sub_system
        click System href "../System/"
    

        
      ControlSystem : has_system_capability
        
          
    
        
        
        ControlSystem --> "*" SystemCapability : has_system_capability
        click SystemCapability href "../SystemCapability/"
    

        
      ControlSystem : name
        
      ControlSystem : system_type
        
          
    
        
        
        ControlSystem --> "0..1" SystemTypeEnum : system_type
        click SystemTypeEnum href "../SystemTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [System](System.md)
        * **ControlSystem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_naming_convention](has_naming_convention.md) | * <br/> [NamingConvention](NamingConvention.md) | Signal naming conventions used by this control system defined in a machine ac... | direct |
| [system_type](system_type.md) | 0..1 <br/> [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying - set to ControlSystem... | [System](System.md) |
| [has_sub_system](has_sub_system.md) | * <br/> [System](System.md) | Relates a System to one of its subsystems (SSN alignment) | [System](System.md) |
| [has_system_capability](has_system_capability.md) | * <br/> [SystemCapability](SystemCapability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) | [System](System.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradConfig](NaradConfig.md) | [control_system](control_system.md) | range | [ControlSystem](ControlSystem.md) |
| [Capability](Capability.md) | [is_property_of](is_property_of.md) | range | [ControlSystem](ControlSystem.md) |
| [FacilitySystem](FacilitySystem.md) | [has_control_system](has_control_system.md) | range | [ControlSystem](ControlSystem.md) |
| [DeployedSystem](DeployedSystem.md) | [has_control_system](has_control_system.md) | range | [ControlSystem](ControlSystem.md) |
| [InstanceSignalBinding](InstanceSignalBinding.md) | [is_property_of](is_property_of.md) | range | [ControlSystem](ControlSystem.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:ControlSystem |
| native | narad:ControlSystem |
| exact | ssn:System |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ControlSystem
description: 'A control system (e.g. EPICS) that manages device process variables.
  In the SSN graph a ControlSystem is a subsystem of the Facility.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System
slots:
- has_naming_convention
slot_usage:
  has_naming_convention:
    name: has_naming_convention
    range: NamingConvention
    multivalued: true
    inlined: true
  system_type:
    name: system_type
    description: High-level system type for classification and querying - set to ControlSystem
      for all ControlSystem instances.
    range: SystemTypeEnum
  has_sub_system:
    name: has_sub_system
    required: false
  has_system_capability:
    name: has_system_capability
    required: false

```
</details>

### Induced

<details>
```yaml
name: ControlSystem
description: 'A control system (e.g. EPICS) that manages device process variables.
  In the SSN graph a ControlSystem is a subsystem of the Facility.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
exact_mappings:
- ssn:System
is_a: System
slot_usage:
  has_naming_convention:
    name: has_naming_convention
    range: NamingConvention
    multivalued: true
    inlined: true
  system_type:
    name: system_type
    description: High-level system type for classification and querying - set to ControlSystem
      for all ControlSystem instances.
    range: SystemTypeEnum
  has_sub_system:
    name: has_sub_system
    required: false
  has_system_capability:
    name: has_system_capability
    required: false
attributes:
  has_naming_convention:
    name: has_naming_convention
    description: Signal naming conventions used by this control system defined in
      a machine actionable manner.  This is where you would capture the patterns/templates
      for how control system PVs or signals are constructed for this control system,  for
      example, the EPICS convention of using suffixes like .R, .S, :GSET to indicate
      readback, status, and setpoint signals. Multiple naming conventions can be captured
      if a control system uses more than one convention for different device types
      or domains.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: has_naming_convention
    owner: ControlSystem
    domain_of:
    - ControlSystem
    range: NamingConvention
    multivalued: true
    inlined: true
    inlined_as_list: true
  system_type:
    name: system_type
    description: High-level system type for classification and querying - set to ControlSystem
      for all ControlSystem instances.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: system_type
    owner: ControlSystem
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
    owner: ControlSystem
    domain_of:
    - System
    - Device
    range: System
    required: false
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
    owner: ControlSystem
    domain_of:
    - System
    - Device
    range: SystemCapability
    required: false
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
    owner: ControlSystem
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
    owner: ControlSystem
    domain_of:
    - NamedThing
    - NamingConventionExample
    - TemplateExample
    range: string

```
</details>