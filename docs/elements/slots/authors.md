

# Slot: authors 


_Contains the authorship information for this representation of an accelerator facility and its operations._





URI: [pals_config:slot/authors](https://w3id.org/pals-config/slot/authors)
Alias: authors

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Author](../classes/Author.md) |
| Domain Of | [PALSAccelerator](../classes/PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PALSAccelerator](../classes/PALSAccelerator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:authors |
| native | pals_config:authors |




## LinkML Source

<details>
```yaml
name: authors
description: Contains the authorship information for this representation of an accelerator
  facility and its operations.
from_schema: https://w3id.org/pals-config
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