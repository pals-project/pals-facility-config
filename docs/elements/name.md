

# Slot: name 


_The name of the entity. For example, the name of the person or organization._





URI: [pals:name](https://pals-project.readthedocs.io/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Author](Author.md) | Contains authorship information for a representation of an accelerator facili... |  no  |
| [Affiliation](Affiliation.md) | Contains affiliation information for an author or component, such as a ROR |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:name |
| native | pals:name |




## LinkML Source

<details>
```yaml
name: name
description: The name of the entity. For example, the name of the person or organization.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: name
domain_of:
- Author
- Affiliation
range: string

```
</details>