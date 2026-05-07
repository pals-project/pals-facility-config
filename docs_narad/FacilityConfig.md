

# Class: FacilityConfig 


_Facility-specific signal binding configuration._





URI: [narad:FacilityConfig](https://w3id.org/narad_linkml/schema/narad/FacilityConfig)





```mermaid
 classDiagram
    class FacilityConfig
    click FacilityConfig href "../FacilityConfig/"
      NamedThing <|-- FacilityConfig
        click NamedThing href "../NamedThing/"
      
      FacilityConfig : control_system
        
      FacilityConfig : description
        
      FacilityConfig : facility_identifier
        
          
    
        
        
        FacilityConfig --> "*" FacilityIdentifier : facility_identifier
        click FacilityIdentifier href "../FacilityIdentifier/"
    

        
      FacilityConfig : name
        
      FacilityConfig : naming_convention
        
      FacilityConfig : signal_definitions
        
          
    
        
        
        FacilityConfig --> "0..1" SignalDefinitions : signal_definitions
        click SignalDefinitions href "../SignalDefinitions/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **FacilityConfig**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [facility_identifier](facility_identifier.md) | * <br/> [FacilityIdentifier](FacilityIdentifier.md) | Globally unique identifier for the facility, with specified type and value | direct |
| [control_system](control_system.md) | 0..1 <br/> [String](String.md) | Identifier of the control system (e | direct |
| [naming_convention](naming_convention.md) | 0..1 <br/> [String](String.md) | Signal naming convention template (e | direct |
| [signal_definitions](signal_definitions.md) | 0..1 <br/> [SignalDefinitions](SignalDefinitions.md) | Signal suffix templates for this facility | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SignalLayer](SignalLayer.md) | [facilities](facilities.md) | range | [FacilityConfig](FacilityConfig.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:FacilityConfig |
| native | narad:FacilityConfig |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FacilityConfig
description: Facility-specific signal binding configuration.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
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
name: FacilityConfig
description: Facility-specific signal binding configuration.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
attributes:
  facility_identifier:
    name: facility_identifier
    description: Globally unique identifier for the facility, with specified type
      and value.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: facility_identifier
    owner: FacilityConfig
    domain_of:
    - FacilityConfig
    range: FacilityIdentifier
    multivalued: true
    inlined: false
  control_system:
    name: control_system
    description: Identifier of the control system (e.g. epics).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: control_system
    owner: FacilityConfig
    domain_of:
    - NaradConfig
    - FacilityConfig
    range: string
  naming_convention:
    name: naming_convention
    description: Signal naming convention template (e.g. <device><signal_code>).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: naming_convention
    owner: FacilityConfig
    domain_of:
    - FacilityConfig
    range: string
  signal_definitions:
    name: signal_definitions
    description: Signal suffix templates for this facility.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: signal_definitions
    owner: FacilityConfig
    domain_of:
    - FacilityConfig
    range: SignalDefinitions
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: FacilityConfig
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
    owner: FacilityConfig
    domain_of:
    - NamedThing
    - SignalBinding
    range: string

```
</details>