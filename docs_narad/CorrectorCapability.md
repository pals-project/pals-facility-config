

# Class: CorrectorCapability 


_Corrector-specific capability extending MagnetCapability with kick signals._





URI: [narad:CorrectorCapability](https://w3id.org/narad_linkml/schema/narad/CorrectorCapability)





```mermaid
 classDiagram
    class CorrectorCapability
    click CorrectorCapability href "../CorrectorCapability/"
      MagnetCapability <|-- CorrectorCapability
        click MagnetCapability href "../MagnetCapability/"
      
      CorrectorCapability : description
        
      CorrectorCapability : device_type
        
          
    
        
        
        CorrectorCapability --> "0..1" ElementKindEnum : device_type
        click ElementKindEnum href "../ElementKindEnum/"
    

        
      CorrectorCapability : for_property
        
          
    
        
        
        CorrectorCapability --> "*" Signal : for_property
        click Signal href "../Signal/"
    

        
      CorrectorCapability : is_abstract
        
      CorrectorCapability : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [SystemCapability](SystemCapability.md)
        * [MagnetCapability](MagnetCapability.md)
            * **CorrectorCapability**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [for_property](for_property.md) | * <br/> [Signal](Signal.md) | SystemCapability → Signal: the capability can expose, monitor, control, or ac... | [SystemCapability](SystemCapability.md) |
| [device_type](device_type.md) | 0..1 <br/> [ElementKindEnum](ElementKindEnum.md) | The specific device type this capability profile or system capability targets... | [SystemCapability](SystemCapability.md) |
| [is_abstract](is_abstract.md) | 0..1 <br/> [Boolean](Boolean.md) | If true, this profile is a template not intended to be directly assigned to a... | [SystemCapability](SystemCapability.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:CorrectorCapability |
| native | narad:CorrectorCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CorrectorCapability
description: Corrector-specific capability extending MagnetCapability with kick signals.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: MagnetCapability

```
</details>

### Induced

<details>
```yaml
name: CorrectorCapability
description: Corrector-specific capability extending MagnetCapability with kick signals.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: MagnetCapability
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
    owner: CorrectorCapability
    domain_of:
    - SystemCapability
    range: Signal
    multivalued: true
  device_type:
    name: device_type
    description: The specific device type this capability profile or system capability
      targets (e.g. Quadrupole, Corrector, BPM).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: device_type
    owner: CorrectorCapability
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
    owner: CorrectorCapability
    domain_of:
    - CapabilityProfile
    - SystemCapability
    range: boolean
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: CorrectorCapability
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
    owner: CorrectorCapability
    domain_of:
    - NamedThing
    - SignalBinding
    range: string

```
</details>