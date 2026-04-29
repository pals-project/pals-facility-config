

# Class: Signal 


_A named semantic signal used by a capability._





URI: [sosa:ObservableProperty](http://www.w3.org/ns/sosa/ObservableProperty)





```mermaid
 classDiagram
    class Signal
    click Signal href "../Signal/"
      Signal : data_type
        
          
    
        
        
        Signal --> "0..1" DataTypeEnum : data_type
        click DataTypeEnum href "../DataTypeEnum/"
    

        
      Signal : description
        
      Signal : name
        
      Signal : role
        
          
    
        
        
        Signal --> "0..1" SignalRoleEnum : role
        click SignalRoleEnum href "../SignalRoleEnum/"
    

        
      Signal : units
        
      Signal : units_uri
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Name/identifier of the entity | direct |
| [role](role.md) | 0..1 <br/> [SignalRoleEnum](SignalRoleEnum.md) | The semantic role of the signal within its capability | direct |
| [data_type](data_type.md) | 0..1 <br/> [DataTypeEnum](DataTypeEnum.md) | The data type of the signal's value | direct |
| [units](units.md) | 0..1 <br/> [String](String.md) | Conventional unit symbol (e | direct |
| [units_uri](units_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Machine-resolvable QUDT unit reference (e | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapabilityMixin](CapabilityMixin.md) | [signals](signals.md) | range | [Signal](Signal.md) |
| [Capability](Capability.md) | [signals](signals.md) | range | [Signal](Signal.md) |
| [TypeSpecificCapability](TypeSpecificCapability.md) | [signals](signals.md) | range | [Signal](Signal.md) |






## Aliases


* epics_pv
* pv
* process_variable
* EPICS Process Variable


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sosa:ObservableProperty |
| native | https://w3id.org/narad_linkml/schema/narad/Signal |
| broad | qudt:QuantityKind |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Signal
description: A named semantic signal used by a capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- epics_pv
- pv
- process_variable
- EPICS Process Variable
broad_mappings:
- qudt:QuantityKind
slots:
- name
- role
- data_type
- units
- units_uri
- description
class_uri: sosa:ObservableProperty

```
</details>

### Induced

<details>
```yaml
name: Signal
description: A named semantic signal used by a capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- epics_pv
- pv
- process_variable
- EPICS Process Variable
broad_mappings:
- qudt:QuantityKind
attributes:
  name:
    name: name
    description: Name/identifier of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    identifier: true
    alias: name
    owner: Signal
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
  role:
    name: role
    description: The semantic role of the signal within its capability.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: role
    owner: Signal
    domain_of:
    - Signal
    range: SignalRoleEnum
  data_type:
    name: data_type
    description: The data type of the signal's value.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    broad_mappings:
    - ncit:C42645
    - qudt:Datatype
    rank: 1000
    alias: data_type
    owner: Signal
    domain_of:
    - Signal
    range: DataTypeEnum
  units:
    name: units
    description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    broad_mappings:
    - si-unit:Unit
    rank: 1000
    alias: units
    owner: Signal
    domain_of:
    - Signal
    range: string
  units_uri:
    name: units_uri
    description: 'Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere,
      si-unit:MegaV-PER-M for MV/m, si-unit:T-M for T*m). The si-unit: prefix maps
      to http://qudt.org/vocab/unit/. Companion to the human-readable symbol in the
      units slot. Use the narad:CustomUnit for user-defined units not in QUDT; these
      should be defined in the graph projection with a narad:CustomUnit class and
      linked to signals via the units_uri slot.'
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    broad_mappings:
    - si-unit:Unit
    rank: 1000
    alias: units_uri
    owner: Signal
    domain_of:
    - Signal
    range: uriorcurie
  description:
    name: description
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: description
    owner: Signal
    domain_of:
    - SignalBinding
    - CapabilityMixin
    - Signal
    - CapabilityProfile
    - ControlProfileFamily
    range: string
class_uri: sosa:ObservableProperty

```
</details>