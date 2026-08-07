

# Slot: authors 


_Contains the authorship information for this representation of an accelerator facility and its operations._





URI: [pals:authors](https://pals-project.readthedocs.io/authors)
Alias: authors

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local b... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Author](Author.md) |
| Domain Of | [PALSAccelerator](PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PALSAccelerator](PALSAccelerator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:authors |
| native | pals:authors |




## LinkML Source

<details>
```yaml
name: authors
description: Contains the authorship information for this representation of an accelerator
  facility and its operations.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: authors
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: Author
multivalued: true
inlined: true
inlined_as_list: true

```
</details>