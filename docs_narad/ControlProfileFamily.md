

# Class: ControlProfileFamily 


_A reusable family of control profiles sharing common semantics and structure._





URI: [https://w3id.org/narad_linkml/schema/narad/ControlProfileFamily](https://w3id.org/narad_linkml/schema/narad/ControlProfileFamily)





```mermaid
 classDiagram
    class ControlProfileFamily
    click ControlProfileFamily href "../ControlProfileFamily/"
      ControlProfileFamily : description
        
      ControlProfileFamily : device_domain
        
          
    
        
        
        ControlProfileFamily --> "0..1" DeviceDomainEnum : device_domain
        click DeviceDomainEnum href "../DeviceDomainEnum/"
    

        
      ControlProfileFamily : graph_projection
        
          
    
        
        
        ControlProfileFamily --> "0..1" GraphProjection : graph_projection
        click GraphProjection href "../GraphProjection/"
    

        
      ControlProfileFamily : name
        
      ControlProfileFamily : shared_capabilities
        
          
    
        
        
        ControlProfileFamily --> "*" Capability : shared_capabilities
        click Capability href "../Capability/"
    

        
      ControlProfileFamily : type_profiles
        
          
    
        
        
        ControlProfileFamily --> "*" CapabilityProfile : type_profiles
        click CapabilityProfile href "../CapabilityProfile/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Name/identifier of the entity | direct |
| [device_domain](device_domain.md) | 0..1 <br/> [DeviceDomainEnum](DeviceDomainEnum.md) | High-level device domain that this profile family governs | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [shared_capabilities](shared_capabilities.md) | * <br/> [Capability](Capability.md) | Named shared capabilities reused by profile types in a family | direct |
| [type_profiles](type_profiles.md) | * <br/> [CapabilityProfile](CapabilityProfile.md) | Device-type profile definitions for this family, keyed by profile name | direct |
| [graph_projection](graph_projection.md) | 0..1 <br/> [GraphProjection](GraphProjection.md) | Optional per-family graph projection override | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapabilityLayer](CapabilityLayer.md) | [profiles](profiles.md) | range | [ControlProfileFamily](ControlProfileFamily.md) |
| [ElementNaradRef](ElementNaradRef.md) | [capability_profile_family](capability_profile_family.md) | range | [ControlProfileFamily](ControlProfileFamily.md) |






## Aliases


* capability_profile_family
* control_profile_family


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/ControlProfileFamily |
| native | https://w3id.org/narad_linkml/schema/narad/ControlProfileFamily |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ControlProfileFamily
description: A reusable family of control profiles sharing common semantics and structure.
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- capability_profile_family
- control_profile_family
slots:
- name
- device_domain
- description
- shared_capabilities
- type_profiles
- graph_projection
slot_usage:
  graph_projection:
    name: graph_projection
    description: Optional per-family graph projection override. If absent, the CapabilityLayer.default_graph_projection
      applies. Provide only when this family genuinely requires a different projection.

```
</details>

### Induced

<details>
```yaml
name: ControlProfileFamily
description: A reusable family of control profiles sharing common semantics and structure.
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- capability_profile_family
- control_profile_family
slot_usage:
  graph_projection:
    name: graph_projection
    description: Optional per-family graph projection override. If absent, the CapabilityLayer.default_graph_projection
      applies. Provide only when this family genuinely requires a different projection.
attributes:
  name:
    name: name
    description: Name/identifier of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    identifier: true
    alias: name
    owner: ControlProfileFamily
    domain_of:
    - Facility
    - SignalBinding
    - DeviceTypeSignalSet
    - Signal
    - Capability
    - CapabilityProfile
    - ControlProfileFamily
    - BeamlineElement
    - PVBinding
    range: string
    required: true
  device_domain:
    name: device_domain
    description: High-level device domain that this profile family governs.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: device_domain
    owner: ControlProfileFamily
    domain_of:
    - ControlProfileFamily
    range: DeviceDomainEnum
  description:
    name: description
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: description
    owner: ControlProfileFamily
    domain_of:
    - SignalBinding
    - CapabilityMixin
    - Signal
    - CapabilityProfile
    - ControlProfileFamily
    range: string
  shared_capabilities:
    name: shared_capabilities
    description: Named shared capabilities reused by profile types in a family.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: shared_capabilities
    owner: ControlProfileFamily
    domain_of:
    - ControlProfileFamily
    range: Capability
    multivalued: true
    inlined: true
  type_profiles:
    name: type_profiles
    description: Device-type profile definitions for this family, keyed by profile
      name. New device types are accommodated by adding a new entry without schema
      changes.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: type_profiles
    owner: ControlProfileFamily
    domain_of:
    - ControlProfileFamily
    range: CapabilityProfile
    multivalued: true
    inlined: true
  graph_projection:
    name: graph_projection
    description: Optional per-family graph projection override. If absent, the CapabilityLayer.default_graph_projection
      applies. Provide only when this family genuinely requires a different projection.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: graph_projection
    owner: ControlProfileFamily
    domain_of:
    - ControlProfileFamily
    range: GraphProjection
    inlined: true

```
</details>