

# Class: Component 


_A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [acc:class/Component](https://example.org/accelerator-core/class/Component)


```mermaid
erDiagram
AdditionalMetadata {
    DataTypeEnum datatype  
    string key  
    string value  
}
Component {
    stringList native_types  
    string id  
    stringList alias  
    string kind  
}
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}

Component ||--|o MetaParamGroup : "MetaP"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```




## Inheritance
* [Node](../classes/Node.md)
    * **Component** [ [HasMetaP](../classes/HasMetaP.md)]
        * [PhysicalComponent](../classes/PhysicalComponent.md) [ [HasFloorP](../classes/HasFloorP.md) [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md)]
        * [VirtualComponent](../classes/VirtualComponent.md) [ [HasFloorP](../classes/HasFloorP.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [native_types](../slots/native_types.md) | * <br/> [String](../types/String.md) | The native type of the component in the source system, which can be used to identify the component across different source systems. | direct |
| [MetaP](../slots/MetaP.md) | 0..1 <br/> [MetaParamGroup](../classes/MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasMetaP](../classes/HasMetaP.md) |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Node](../classes/Node.md) |
| [kind](../slots/kind.md) | 1 <br/> [String](../types/String.md) | The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor` (no prefix). | [Node](../classes/Node.md) |
| [alias](../slots/alias.md) | * <br/> [String](../types/String.md) | An alternative name or identifier for the instance. | [Node](../classes/Node.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](../classes/Facility.md) | [components](../slots/components.md) | range | [Component](../classes/Component.md) |
| [ComponentRelation](../classes/ComponentRelation.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [ComponentRelation](../classes/ComponentRelation.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [Precedes](../classes/Precedes.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [Precedes](../classes/Precedes.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [Contains](../classes/Contains.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [Contains](../classes/Contains.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [Controls](../classes/Controls.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [Controls](../classes/Controls.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [IsPartOf](../classes/IsPartOf.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [IsPartOf](../classes/IsPartOf.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [AdjacentTo](../classes/AdjacentTo.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [AdjacentTo](../classes/AdjacentTo.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [Overlaps](../classes/Overlaps.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [Overlaps](../classes/Overlaps.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [HasConnectingBranch](../classes/HasConnectingBranch.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [HasConnectingBranch](../classes/HasConnectingBranch.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [MountedOn](../classes/MountedOn.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [MountedOn](../classes/MountedOn.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [Intersects](../classes/Intersects.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [Intersects](../classes/Intersects.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |
| [NearestTo](../classes/NearestTo.md) | [subject](../slots/subject.md) | range | [Component](../classes/Component.md) |
| [NearestTo](../classes/NearestTo.md) | [object](../slots/object.md) | range | [Component](../classes/Component.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:Component |
| native | acc:Component |
| broad | pals:Element |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Component
description: A general class for accelerator components, which can be specialized
  into more specific types like AcceleratorDevice, Magnet, etc.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Element
is_a: Node
abstract: true
mixins:
- HasMetaP
attributes:
  native_types:
    name: native_types
    description: The native type of the component in the source system, which can
      be used to identify the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - Component
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Component
description: A general class for accelerator components, which can be specialized
  into more specific types like AcceleratorDevice, Magnet, etc.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Element
is_a: Node
abstract: true
mixins:
- HasMetaP
attributes:
  native_types:
    name: native_types
    description: The native type of the component in the source system, which can
      be used to identify the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: native_types
    owner: Component
    domain_of:
    - Component
    range: string
    multivalued: true
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MetaP
    owner: Component
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: Component
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true
  kind:
    name: kind
    description: The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor`
      (no prefix).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: rdf:type
    designates_type: true
    alias: kind
    owner: Component
    domain_of:
    - Node
    - PALSAccelerator
    range: string
    required: true
  alias:
    name: alias
    description: An alternative name or identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:alias
    rank: 1000
    alias: alias
    owner: Component
    domain_of:
    - Node
    - MetaParamGroup
    range: string
    multivalued: true

```
</details>