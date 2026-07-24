

# Class: Affiliation 


_Contains affiliation information for an author or component, such as a ROR._





URI: [pals:Affiliation](https://pals-project.readthedocs.io/Affiliation)





```mermaid
 classDiagram
    class Affiliation
    click Affiliation href "../Affiliation/"
      Affiliation : id
        
      Affiliation : identifiers
        
          
    
        
        
        Affiliation --> "*" Identifier : identifiers
        click Identifier href "../Identifier/"
    

        
      Affiliation : name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the instance | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | The name of the entity | direct |
| [identifiers](identifiers.md) | * <br/> [Identifier](Identifier.md) | A unique and ideally persistent identifier for the facility, such as a DOI or... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PALS](PALS.md) | [affiliation](affiliation.md) | range | [Affiliation](Affiliation.md) |
| [Author](Author.md) | [affiliation](affiliation.md) | range | [Affiliation](Affiliation.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:Affiliation |
| native | pals:Affiliation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Affiliation
description: Contains affiliation information for an author or component, such as
  a ROR.
from_schema: https://w3id.org/accelerator-core
slots:
- id
- name
- identifiers

```
</details>

### Induced

<details>
```yaml
name: Affiliation
description: Contains affiliation information for an author or component, such as
  a ROR.
from_schema: https://w3id.org/accelerator-core
attributes:
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: Affiliation
    domain_of:
    - Affiliation
    - Component
    - Signal
    - Relationship
    range: string
    required: true
  name:
    name: name
    description: The name of the entity. For example, the name of the person or organization.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: name
    owner: Affiliation
    domain_of:
    - Author
    - Affiliation
    range: string
  identifiers:
    name: identifiers
    description: A unique and ideally persistent identifier for the facility, such
      as a DOI or ROR.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: identifiers
    owner: Affiliation
    domain_of:
    - Facility
    - Affiliation
    range: Identifier
    multivalued: true

```
</details>