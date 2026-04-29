

# Class: Identifier 


_A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local)._





URI: [https://w3id.org/narad_linkml/schema/narad/Identifier](https://w3id.org/narad_linkml/schema/narad/Identifier)





```mermaid
 classDiagram
    class Identifier
    click Identifier href "../Identifier/"
      Identifier : identifier_type
        
          
    
        
        
        Identifier --> "0..1" IdentifierTypeEnum : identifier_type
        click IdentifierTypeEnum href "../IdentifierTypeEnum/"
    

        
      Identifier : identifier_value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [identifier_type](identifier_type.md) | 0..1 <br/> [IdentifierTypeEnum](IdentifierTypeEnum.md) | The type of identifier used in the identifier slot (e | direct |
| [identifier_value](identifier_value.md) | 0..1 <br/> [String](String.md) | The value of the identifier (e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](Facility.md) | [identifier](identifier.md) | range | [Identifier](Identifier.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/Identifier |
| native | https://w3id.org/narad_linkml/schema/narad/Identifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identifier
description: A globally unique identifier for an entity (e.g., facility), with a specified
  type (e.g. DOI, ROR, ARK, local).
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- identifier_type
- identifier_value

```
</details>

### Induced

<details>
```yaml
name: Identifier
description: A globally unique identifier for an entity (e.g., facility), with a specified
  type (e.g. DOI, ROR, ARK, local).
from_schema: https://w3id.org/narad_linkml/schema/narad/
attributes:
  identifier_type:
    name: identifier_type
    description: The type of identifier used in the identifier slot (e.g. DOI, ARK,
      URL, local).
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: identifier_type
    owner: Identifier
    domain_of:
    - Identifier
    range: IdentifierTypeEnum
  identifier_value:
    name: identifier_value
    description: The value of the identifier (e.g. the DOI string, ARK string, URL
      string, or local ID).
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: identifier_value
    owner: Identifier
    domain_of:
    - Identifier
    range: string

```
</details>