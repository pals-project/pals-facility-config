

# Slot: email 


_The email address of the author._





URI: [pals:email](https://pals-project.readthedocs.io/email)
Alias: email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Author](Author.md) | Contains authorship information for a representation of an accelerator facili... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[^@]+@[^@]+\.[^@]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:email |
| native | pals:email |




## LinkML Source

<details>
```yaml
name: email
description: The email address of the author.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: email
owner: Author
domain_of:
- Author
range: string
pattern: ^[^@]+@[^@]+\.[^@]+$

```
</details>