

# Slot: notes 


_Additional notes or comments about the representation of a particle accelerator and its operations._





URI: [acc:slot/notes](https://example.org/accelerator-core/slot/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:notes |
| native | acc:notes |




## LinkML Source

<details>
```yaml
name: notes
description: Additional notes or comments about the representation of a particle accelerator
  and its operations.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: notes
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>