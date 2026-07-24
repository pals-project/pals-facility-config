

# Class: Signal 


_Semantic meaning of a control-system signal associated with a component._





URI: [pals:Signal](https://pals-project.readthedocs.io/Signal)





```mermaid
 classDiagram
    class Signal
    click Signal href "../Signal/"
      HasMetaP <|-- Signal
        click HasMetaP href "../HasMetaP/"
      
      Signal : access_protocol
        
      Signal : alias
        
      Signal : archive_identifier
        
      Signal : canonical_signal_type
        
          
    
        
        
        Signal --> "1" CanonicalSignalTypeEnum : canonical_signal_type
        click CanonicalSignalTypeEnum href "../CanonicalSignalTypeEnum/"
    

        
      Signal : id
        
      Signal : kind
        
      Signal : MetaP
        
          
    
        
        
        Signal --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      Signal : native_data_type
        
          
    
        
        
        Signal --> "1" DataTypeEnum : native_data_type
        click DataTypeEnum href "../DataTypeEnum/"
    

        
      Signal : native_description
        
      Signal : native_unit
        
          
    
        
        
        Signal --> "1" UnitEnum : native_unit
        click UnitEnum href "../UnitEnum/"
    

        
      Signal : quantity_kind
        
          
    
        
        
        Signal --> "1" QuantityKindEnum : quantity_kind
        click QuantityKindEnum href "../QuantityKindEnum/"
    

        
      Signal : signal_role
        
          
    
        
        
        Signal --> "1" SignalRoleEnum : signal_role
        click SignalRoleEnum href "../SignalRoleEnum/"
    

        
      Signal : source_system
        
          
    
        
        
        Signal --> "1" SourceSystemEnum : source_system
        click SourceSystemEnum href "../SourceSystemEnum/"
    

        
      
```





## Inheritance
* **Signal** [ [HasMetaP](HasMetaP.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the instance | direct |
| [kind](kind.md) | 1 <br/> [String](String.md) | The LinkML class name of this instance | direct |
| [alias](alias.md) | 0..1 <br/> [String](String.md) | An alternative name or identifier for the instance | direct |
| [signal_role](signal_role.md) | 1 <br/> [SignalRoleEnum](SignalRoleEnum.md) | The role of the signal in the control system, such as setpoint, readback, sta... | direct |
| [source_system](source_system.md) | 1 <br/> [SourceSystemEnum](SourceSystemEnum.md) | The source system from which the signal originates, such as EPICS, PALS-Ext, ... | direct |
| [native_description](native_description.md) | 0..1 <br/> [String](String.md) | A human-readable description of the signal in the source system | direct |
| [canonical_signal_type](canonical_signal_type.md) | 1 <br/> [CanonicalSignalTypeEnum](CanonicalSignalTypeEnum.md) | The canonical semantic meaning of the signal | direct |
| [quantity_kind](quantity_kind.md) | 1 <br/> [QuantityKindEnum](QuantityKindEnum.md) | The physical quantity kind of the signal | direct |
| [native_data_type](native_data_type.md) | 1 <br/> [DataTypeEnum](DataTypeEnum.md) | The native data type of the signal in the source system,  such as String, Int... | direct |
| [native_unit](native_unit.md) | 1 <br/> [UnitEnum](UnitEnum.md) | The native unit of the signal in the source system | direct |
| [access_protocol](access_protocol.md) | 0..1 <br/> [String](String.md) | The protocol used to access the signal in the source system,  such as EPICS C... | direct |
| [archive_identifier](archive_identifier.md) | 0..1 <br/> [String](String.md) | The identifier used to reference the signal in an archival system | direct |
| [MetaP](MetaP.md) | 0..1 <br/> [MetaParamGroup](MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Pa... | [HasMetaP](HasMetaP.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](Facility.md) | [signals](signals.md) | range | [Signal](Signal.md) |
| [SignalBinding](SignalBinding.md) | [object](object.md) | range | [Signal](Signal.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:Signal |
| native | pals:Signal |
| broad | sosa:Sensor, sosa:Actuator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Signal
description: Semantic meaning of a control-system signal associated with a component.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- sosa:Sensor
- sosa:Actuator
mixins:
- HasMetaP
slots:
- id
- kind
- alias
attributes:
  signal_role:
    name: signal_role
    description: The role of the signal in the control system, such as setpoint, readback,
      status, command, or limit.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: SignalRoleEnum
    required: true
  source_system:
    name: source_system
    description: The source system from which the signal originates, such as EPICS,
      PALS-Ext, MYA, an element database, a channel database, or a simulation service.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: SourceSystemEnum
    required: true
  native_description:
    name: native_description
    description: A human-readable description of the signal in the source system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: string
  canonical_signal_type:
    name: canonical_signal_type
    description: The canonical semantic meaning of the signal.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: CanonicalSignalTypeEnum
    required: true
  quantity_kind:
    name: quantity_kind
    description: The physical quantity kind of the signal.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: QuantityKindEnum
    required: true
  native_data_type:
    name: native_data_type
    description: The native data type of the signal in the source system,  such as
      String, Integer, Float, or Boolean.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: DataTypeEnum
    required: true
  native_unit:
    name: native_unit
    description: The native unit of the signal in the source system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: UnitEnum
    required: true
  access_protocol:
    name: access_protocol
    description: The protocol used to access the signal in the source system,  such
      as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: string
  archive_identifier:
    name: archive_identifier
    description: The identifier used to reference the signal in an archival system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Signal
    range: string

```
</details>

### Induced

<details>
```yaml
name: Signal
description: Semantic meaning of a control-system signal associated with a component.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- sosa:Sensor
- sosa:Actuator
mixins:
- HasMetaP
attributes:
  signal_role:
    name: signal_role
    description: The role of the signal in the control system, such as setpoint, readback,
      status, command, or limit.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: signal_role
    owner: Signal
    domain_of:
    - Signal
    range: SignalRoleEnum
    required: true
  source_system:
    name: source_system
    description: The source system from which the signal originates, such as EPICS,
      PALS-Ext, MYA, an element database, a channel database, or a simulation service.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: source_system
    owner: Signal
    domain_of:
    - Signal
    range: SourceSystemEnum
    required: true
  native_description:
    name: native_description
    description: A human-readable description of the signal in the source system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: native_description
    owner: Signal
    domain_of:
    - Signal
    range: string
  canonical_signal_type:
    name: canonical_signal_type
    description: The canonical semantic meaning of the signal.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: canonical_signal_type
    owner: Signal
    domain_of:
    - Signal
    range: CanonicalSignalTypeEnum
    required: true
  quantity_kind:
    name: quantity_kind
    description: The physical quantity kind of the signal.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: quantity_kind
    owner: Signal
    domain_of:
    - Signal
    range: QuantityKindEnum
    required: true
  native_data_type:
    name: native_data_type
    description: The native data type of the signal in the source system,  such as
      String, Integer, Float, or Boolean.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: native_data_type
    owner: Signal
    domain_of:
    - Signal
    range: DataTypeEnum
    required: true
  native_unit:
    name: native_unit
    description: The native unit of the signal in the source system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: native_unit
    owner: Signal
    domain_of:
    - Signal
    range: UnitEnum
    required: true
  access_protocol:
    name: access_protocol
    description: The protocol used to access the signal in the source system,  such
      as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: access_protocol
    owner: Signal
    domain_of:
    - Signal
    range: string
  archive_identifier:
    name: archive_identifier
    description: The identifier used to reference the signal in an archival system.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: archive_identifier
    owner: Signal
    domain_of:
    - Signal
    range: string
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: Signal
    domain_of:
    - Affiliation
    - Component
    - Signal
    - Relationship
    range: string
    required: true
  kind:
    name: kind
    description: The LinkML class name of this instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:kind
    alias: kind
    owner: Signal
    domain_of:
    - PALS
    - Component
    - Signal
    range: string
    required: true
  alias:
    name: alias
    description: An alternative name or identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:alias
    alias: alias
    owner: Signal
    domain_of:
    - MetaParamGroup
    - Signal
    range: string
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MetaP
    owner: Signal
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>