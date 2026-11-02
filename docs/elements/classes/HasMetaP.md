

# Class: HasMetaP 



URI: [acc:class/HasMetaP](https://example.org/accelerator-core/class/HasMetaP)


```mermaid
erDiagram
AdditionalMetadata {
    DataTypeEnum datatype  
    string key  
    string value  
}
HasMetaP {

}
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}

HasMetaP ||--|o MetaParamGroup : "MetaP"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```



<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [MetaP](../slots/MetaP.md) | 0..1 <br/> [MetaParamGroup](../classes/MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Component](../classes/Component.md) | A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc. |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:HasMetaP |
| native | acc:HasMetaP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasMetaP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasMetaP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MetaP
    owner: HasMetaP
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>