

# Class: Capability 


_A named, shared grouping of semantically related signals for a control aspect._





URI: [https://w3id.org/narad_linkml/schema/narad/Capability](https://w3id.org/narad_linkml/schema/narad/Capability)





```mermaid
 classDiagram
    class Capability
    click Capability href "../Capability/"
      CapabilityMixin <|-- Capability
        click CapabilityMixin href "../CapabilityMixin/"
      
      Capability : description
        
      Capability : name
        
      Capability : signals
        
          
    
        
        
        Capability --> "*" Signal : signals
        click Signal href "../Signal/"
    

        
      
```





## Inheritance
* **Capability** [ [CapabilityMixin](CapabilityMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Name/identifier of the entity | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [CapabilityMixin](CapabilityMixin.md) |
| [signals](signals.md) | * <br/> [Signal](Signal.md) | Signals within a capability | [CapabilityMixin](CapabilityMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | [inherits_shared_capabilities](inherits_shared_capabilities.md) | range | [Capability](Capability.md) |
| [ControlProfileFamily](ControlProfileFamily.md) | [shared_capabilities](shared_capabilities.md) | range | [Capability](Capability.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/Capability |
| native | https://w3id.org/narad_linkml/schema/narad/Capability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Capability
description: A named, shared grouping of semantically related signals for a control
  aspect.
from_schema: https://w3id.org/narad_linkml/schema/narad/
mixins:
- CapabilityMixin
slots:
- name

```
</details>

### Induced

<details>
```yaml
name: Capability
description: A named, shared grouping of semantically related signals for a control
  aspect.
from_schema: https://w3id.org/narad_linkml/schema/narad/
mixins:
- CapabilityMixin
attributes:
  name:
    name: name
    description: Name/identifier of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    identifier: true
    alias: name
    owner: Capability
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
  description:
    name: description
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: description
    owner: Capability
    domain_of:
    - SignalBinding
    - CapabilityMixin
    - Signal
    - CapabilityProfile
    - ControlProfileFamily
    range: string
  signals:
    name: signals
    description: Signals within a capability.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: signals
    owner: Capability
    domain_of:
    - CapabilityMixin
    range: Signal
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>