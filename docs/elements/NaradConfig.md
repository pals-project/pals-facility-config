

# Class: NaradConfig 


_A top-level NARAD-system container for the: capability layer + signal layer._





URI: [narad:NaradConfig](https://example.org/narad_linkml/schema/narad/NaradConfig)





```mermaid
 classDiagram
    class NaradConfig
    click NaradConfig href "../NaradConfig/"
      NaradConfig : capability_layer
        
          
    
        
        
        NaradConfig --> "1..*" Capability : capability_layer
        click Capability href "../Capability/"
    

        
      NaradConfig : control_system
        
          
    
        
        
        NaradConfig --> "1" ControlSystem : control_system
        click ControlSystem href "../ControlSystem/"
    

        
      NaradConfig : deployed_system
        
          
    
        
        
        NaradConfig --> "1" DeployedSystem : deployed_system
        click DeployedSystem href "../DeployedSystem/"
    

        
      NaradConfig : device_layer
        
          
    
        
        
        NaradConfig --> "1..*" Device : device_layer
        click Device href "../Device/"
    

        
      NaradConfig : intent
        
      NaradConfig : schema_version
        
      NaradConfig : signal_layer
        
          
    
        
        
        NaradConfig --> "1" SignalLayer : signal_layer
        click SignalLayer href "../SignalLayer/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [schema_version](schema_version.md) | 1 <br/> [String](String.md) | Version of the NARAD schema used in this document | direct |
| [intent](intent.md) | 0..1 <br/> [String](String.md) | A human-readable statement of the intended use or purpose of this NARAD confi... | direct |
| [deployed_system](deployed_system.md) | 1 <br/> [DeployedSystem](DeployedSystem.md) | Identifier of the deployed system this configuration describes | direct |
| [control_system](control_system.md) | 1 <br/> [ControlSystem](ControlSystem.md) | Identifier of the control system (e | direct |
| [capability_layer](capability_layer.md) | 1..* <br/> [Capability](Capability.md) | Control Capability definitions for this facility | direct |
| [device_layer](device_layer.md) | 1..* <br/> [Device](Device.md) | Device Capability definitions keyed by capability name | direct |
| [signal_layer](signal_layer.md) | 1 <br/> [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradModel](NaradModel.md) | [narad_config](narad_config.md) | range | [NaradConfig](NaradConfig.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:NaradConfig |
| native | narad:NaradConfig |
| broad | ssn:Deployment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NaradConfig
description: 'A top-level NARAD-system container for the: capability layer + signal
  layer.'
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- ssn:Deployment
slots:
- schema_version
- intent
- deployed_system
- control_system
- capability_layer
- device_layer
- signal_layer
slot_usage:
  schema_version:
    name: schema_version
    description: Version of the NARAD schema used in this document.
    range: string
    required: true
  deployed_system:
    name: deployed_system
    description: Identifier of the deployed system this configuration describes.
    range: DeployedSystem
    required: true
    multivalued: false
    inlined: true
  control_system:
    name: control_system
    description: Identifier of the control system (e.g. epics) this configuration
      describes.
    range: ControlSystem
    required: true
    multivalued: false
  device_layer:
    name: device_layer
    description: Device Capability definitions keyed by capability name.
    range: Device
    required: true
    multivalued: true
    inlined: true
  signal_layer:
    name: signal_layer
    description: Signal-layer container for facility-specific signal bindings.
    range: SignalLayer
    required: true
    inlined: false

```
</details>

### Induced

<details>
```yaml
name: NaradConfig
description: 'A top-level NARAD-system container for the: capability layer + signal
  layer.'
from_schema: https://w3id.org/narad_linkml/schema/narad/system
broad_mappings:
- ssn:Deployment
slot_usage:
  schema_version:
    name: schema_version
    description: Version of the NARAD schema used in this document.
    range: string
    required: true
  deployed_system:
    name: deployed_system
    description: Identifier of the deployed system this configuration describes.
    range: DeployedSystem
    required: true
    multivalued: false
    inlined: true
  control_system:
    name: control_system
    description: Identifier of the control system (e.g. epics) this configuration
      describes.
    range: ControlSystem
    required: true
    multivalued: false
  device_layer:
    name: device_layer
    description: Device Capability definitions keyed by capability name.
    range: Device
    required: true
    multivalued: true
    inlined: true
  signal_layer:
    name: signal_layer
    description: Signal-layer container for facility-specific signal bindings.
    range: SignalLayer
    required: true
    inlined: false
attributes:
  schema_version:
    name: schema_version
    description: Version of the NARAD schema used in this document.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: schema_version
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: string
    required: true
  intent:
    name: intent
    description: A human-readable statement of the intended use or purpose of this
      NARAD configuration.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: intent
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: string
  deployed_system:
    name: deployed_system
    description: Identifier of the deployed system this configuration describes.
    in_subset:
    - instance
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: deployed_system
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: DeployedSystem
    required: true
    multivalued: false
    inlined: true
  control_system:
    name: control_system
    description: Identifier of the control system (e.g. epics) this configuration
      describes.
    in_subset:
    - instance
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: control_system
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: ControlSystem
    required: true
    multivalued: false
    inlined: true
  capability_layer:
    name: capability_layer
    description: Control Capability definitions for this facility.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: capability_layer
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: Capability
    required: true
    multivalued: true
    inlined: true
  device_layer:
    name: device_layer
    description: Device Capability definitions keyed by capability name.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: device_layer
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: Device
    required: true
    multivalued: true
    inlined: true
  signal_layer:
    name: signal_layer
    description: Signal-layer container for facility-specific signal bindings.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: signal_layer
    owner: NaradConfig
    domain_of:
    - NaradConfig
    range: SignalLayer
    required: true
    inlined: false

```
</details>