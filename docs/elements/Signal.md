

# Class: Signal 


_Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding._

__





URI: [narad:Signal](https://example.org/narad_linkml/schema/narad/Signal)





```mermaid
 classDiagram
    class Signal
    click Signal href "../Signal/"
      NamedThing <|-- Signal
        click NamedThing href "../NamedThing/"
      

      Signal <|-- ObservableSignal
        click ObservableSignal href "../ObservableSignal/"
      Signal <|-- ActuatableSignal
        click ActuatableSignal href "../ActuatableSignal/"
      

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





## Inheritance
* [NamedThing](NamedThing.md)
    * **Signal**
        * [ObservableSignal](ObservableSignal.md)
        * [ActuatableSignal](ActuatableSignal.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 0..1 <br/> [SignalRoleEnum](SignalRoleEnum.md) | The semantic role of the signal within its capability | direct |
| [data_type](data_type.md) | 0..1 <br/> [DataTypeEnum](DataTypeEnum.md) | The data type of the signal's value | direct |
| [units](units.md) | 0..1 <br/> [String](String.md) | Conventional unit symbol (e | direct |
| [units_uri](units_uri.md) | 0..1 <br/> [String](String.md) | Machine-resolvable QUDT unit reference (e | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Capability](Capability.md) | [has_signal](has_signal.md) | range | [Signal](Signal.md) |
| [InstanceSignalBinding](InstanceSignalBinding.md) | [is_instance_of](is_instance_of.md) | range | [Signal](Signal.md) |






## Aliases


* epics_pv
* pv
* process_variable
* EPICS Process Variable
* control signal
* control-system signal


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:Signal |
| native | narad:Signal |
| broad | sosa:Property, ssn:Property, qudt:QuantityKind |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Signal
description: 'Domain term for a control-system signal. A Signal represents an identifiable
  quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD
  Signals are treated as properties of systems (ssn:forProperty). The concrete facility
  binding is captured in SignalBinding.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
aliases:
- epics_pv
- pv
- process_variable
- EPICS Process Variable
- control signal
- control-system signal
broad_mappings:
- sosa:Property
- ssn:Property
- qudt:QuantityKind
is_a: NamedThing
slots:
- role
- data_type
- units
- units_uri

```
</details>

### Induced

<details>
```yaml
name: Signal
description: 'Domain term for a control-system signal. A Signal represents an identifiable
  quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD
  Signals are treated as properties of systems (ssn:forProperty). The concrete facility
  binding is captured in SignalBinding.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
aliases:
- epics_pv
- pv
- process_variable
- EPICS Process Variable
- control signal
- control-system signal
broad_mappings:
- sosa:Property
- ssn:Property
- qudt:QuantityKind
is_a: NamedThing
attributes:
  role:
    name: role
    description: The semantic role of the signal within its capability.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: role
    owner: Signal
    domain_of:
    - Signal
    range: SignalRoleEnum
  data_type:
    name: data_type
    description: The data type of the signal's value.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: data_type
    owner: Signal
    domain_of:
    - Signal
    range: DataTypeEnum
  units:
    name: units
    description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: units
    owner: Signal
    domain_of:
    - Signal
    range: string
  units_uri:
    name: units_uri
    description: 'Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere).
      The si-unit: prefix maps to http://qudt.org/vocab/unit/.'
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: units_uri
    owner: Signal
    domain_of:
    - Signal
    range: string
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: Signal
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
    owner: Signal
    domain_of:
    - NamedThing
    - NamingConventionExample
    - TemplateExample
    range: string

```
</details>