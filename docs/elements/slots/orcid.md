

# Slot: orcid 


_The ORCID identifier of the author._





URI: [pals:slot/orcid](https://pals-project.readthedocs.io/slot/orcid)
Alias: orcid

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
| Regex Pattern | `^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[\dX]$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:orcid |
| native | pals:orcid |




## LinkML Source

<details>
```yaml
name: orcid
description: The ORCID identifier of the author.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: orcid
owner: Author
domain_of:
- Author
range: string
pattern: ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[\dX]$

```
</details>