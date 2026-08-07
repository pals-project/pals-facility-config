

# Slot: email 


_The email address of the author._





URI: [pals:slot/email](https://pals-project.readthedocs.io/slot/email)
Alias: email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Author](../classes/Author.md) | Contains authorship information for a representation of an accelerator facility and its operations. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Author](../classes/Author.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Author](../classes/Author.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[^@]+@[^@]+\.[^@]+$` |












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