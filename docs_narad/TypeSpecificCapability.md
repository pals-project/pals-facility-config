

# Class: TypeSpecificCapability 


_An inline capability declared within a device-type profile, with its own identifier, a semantic class label, a description, and a list of signals. Distinct from the shared capabilities referenced by name; these are profile-local definitions._





URI: [https://w3id.org/narad_linkml/schema/narad/TypeSpecificCapability](https://w3id.org/narad_linkml/schema/narad/TypeSpecificCapability)





```mermaid
 classDiagram
    class TypeSpecificCapability
    click TypeSpecificCapability href "../TypeSpecificCapability/"
      CapabilityMixin <|-- TypeSpecificCapability
        click CapabilityMixin href "../CapabilityMixin/"
      
      TypeSpecificCapability : capability_class
        
      TypeSpecificCapability : class_curie
        
      TypeSpecificCapability : description
        
      TypeSpecificCapability : id
        
      TypeSpecificCapability : signals
        
          
    
        
        
        TypeSpecificCapability --> "*" Signal : signals
        click Signal href "../Signal/"
    

        
      
```





## Inheritance
* **TypeSpecificCapability** [ [CapabilityMixin](CapabilityMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Unique identifier for the entity | direct |
| [capability_class](capability_class.md) | 0..1 <br/> [String](String.md) | Semantic class label for a type-specific capability (e | direct |
| [class_curie](class_curie.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional machine-resolvable URI or CURIE for a TypeSpecificCapability class | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [CapabilityMixin](CapabilityMixin.md) |
| [signals](signals.md) | * <br/> [Signal](Signal.md) | Signals within a capability | [CapabilityMixin](CapabilityMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | [type_specific_capabilities](type_specific_capabilities.md) | range | [TypeSpecificCapability](TypeSpecificCapability.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/TypeSpecificCapability |
| native | https://w3id.org/narad_linkml/schema/narad/TypeSpecificCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TypeSpecificCapability
description: An inline capability declared within a device-type profile, with its
  own identifier, a semantic class label, a description, and a list of signals. Distinct
  from the shared capabilities referenced by name; these are profile-local definitions.
from_schema: https://w3id.org/narad_linkml/schema/narad/
mixins:
- CapabilityMixin
slots:
- id
- capability_class
- class_curie

```
</details>

### Induced

<details>
```yaml
name: TypeSpecificCapability
description: An inline capability declared within a device-type profile, with its
  own identifier, a semantic class label, a description, and a list of signals. Distinct
  from the shared capabilities referenced by name; these are profile-local definitions.
from_schema: https://w3id.org/narad_linkml/schema/narad/
mixins:
- CapabilityMixin
attributes:
  id:
    name: id
    description: Unique identifier for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    identifier: true
    alias: id
    owner: TypeSpecificCapability
    domain_of:
    - TypeSpecificCapability
    - Relationship
    range: string
    required: true
  capability_class:
    name: capability_class
    description: Semantic class label for a type-specific capability (e.g. QuadrupoleStrengthCapability).
      Serialized as 'class' in source YAML; renamed here to avoid conflict with reserved
      keywords.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    aliases:
    - class
    rank: 1000
    alias: capability_class
    owner: TypeSpecificCapability
    domain_of:
    - TypeSpecificCapability
    range: string
  class_curie:
    name: class_curie
    description: 'Optional machine-resolvable URI or CURIE for a TypeSpecificCapability
      class. Use the narad: prefix for NARAD-defined classes (e.g. narad:QuadrupoleStrengthCapability),
      or any registered prefix for externally defined capability types. New capability
      classes can be introduced freely by using a suitable namespace.'
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: class_curie
    owner: TypeSpecificCapability
    domain_of:
    - TypeSpecificCapability
    range: uriorcurie
  description:
    name: description
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: description
    owner: TypeSpecificCapability
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
    owner: TypeSpecificCapability
    domain_of:
    - CapabilityMixin
    range: Signal
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>