

# Class: CapabilityProfile 


_A device-type profile that reuses shared capabilities and adds type-specific ones (e.g. QuadrupoleProfile)._





URI: [narad:CapabilityProfile](https://w3id.org/narad_linkml/schema/narad/CapabilityProfile)





```mermaid
 classDiagram
    class CapabilityProfile
    click CapabilityProfile href "../CapabilityProfile/"
      NamedThing <|-- CapabilityProfile
        click NamedThing href "../NamedThing/"
      
      CapabilityProfile : description
        
      CapabilityProfile : device_type
        
          
    
        
        
        CapabilityProfile --> "0..1" ElementKindEnum : device_type
        click ElementKindEnum href "../ElementKindEnum/"
    

        
      CapabilityProfile : inherits_shared_capabilities
        
          
    
        
        
        CapabilityProfile --> "*" Capability : inherits_shared_capabilities
        click Capability href "../Capability/"
    

        
      CapabilityProfile : is_abstract
        
      CapabilityProfile : name
        
      CapabilityProfile : type_specific_capabilities
        
          
    
        
        
        CapabilityProfile --> "*" TypeSpecificCapability : type_specific_capabilities
        click TypeSpecificCapability href "../TypeSpecificCapability/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **CapabilityProfile**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [device_type](device_type.md) | 0..1 <br/> [ElementKindEnum](ElementKindEnum.md) | The specific device type this capability profile or system capability targets... | direct |
| [is_abstract](is_abstract.md) | 0..1 <br/> [Boolean](Boolean.md) | If true, this profile is a template not intended to be directly assigned to a... | direct |
| [inherits_shared_capabilities](inherits_shared_capabilities.md) | * <br/> [Capability](Capability.md) | Shared capabilities inherited by this profile, cross-referenced by name | direct |
| [type_specific_capabilities](type_specific_capabilities.md) | * <br/> [TypeSpecificCapability](TypeSpecificCapability.md) | Type-specific capabilities declared directly in a profile | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | [type_profiles](type_profiles.md) | range | [CapabilityProfile](CapabilityProfile.md) |
| [BeamlineElement](BeamlineElement.md) | [capability_profile](capability_profile.md) | range | [CapabilityProfile](CapabilityProfile.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:CapabilityProfile |
| native | narad:CapabilityProfile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CapabilityProfile
description: A device-type profile that reuses shared capabilities and adds type-specific
  ones (e.g. QuadrupoleProfile).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
slots:
- device_type
- is_abstract
- inherits_shared_capabilities
- type_specific_capabilities

```
</details>

### Induced

<details>
```yaml
name: CapabilityProfile
description: A device-type profile that reuses shared capabilities and adds type-specific
  ones (e.g. QuadrupoleProfile).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
attributes:
  device_type:
    name: device_type
    description: The specific device type this capability profile or system capability
      targets (e.g. Quadrupole, Corrector, BPM).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: device_type
    owner: CapabilityProfile
    domain_of:
    - CapabilityProfile
    - SystemCapability
    range: ElementKindEnum
  is_abstract:
    name: is_abstract
    description: If true, this profile is a template not intended to be directly assigned
      to a beamline element. Concrete profiles set this to false (default).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    ifabsent: 'false'
    alias: is_abstract
    owner: CapabilityProfile
    domain_of:
    - CapabilityProfile
    - SystemCapability
    range: boolean
  inherits_shared_capabilities:
    name: inherits_shared_capabilities
    description: Shared capabilities inherited by this profile, cross-referenced by
      name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: inherits_shared_capabilities
    owner: CapabilityProfile
    domain_of:
    - CapabilityProfile
    range: Capability
    multivalued: true
    inlined: false
  type_specific_capabilities:
    name: type_specific_capabilities
    description: Type-specific capabilities declared directly in a profile.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: type_specific_capabilities
    owner: CapabilityProfile
    domain_of:
    - CapabilityProfile
    range: TypeSpecificCapability
    multivalued: true
    inlined: true
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: CapabilityProfile
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
    owner: CapabilityProfile
    domain_of:
    - NamedThing
    - SignalBinding
    range: string

```
</details>