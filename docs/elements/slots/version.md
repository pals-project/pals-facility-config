

# Slot: version 


_Version of the representation of a particle accelerator and its operations._





URI: [acc:slot/version](https://example.org/accelerator-core/slot/version)
Alias: version

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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PALSAccelerator](../classes/PALSAccelerator.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:version |
| native | acc:version |




## LinkML Source

<details>
```yaml
name: version
description: Version of the representation of a particle accelerator and its operations.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: version
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: string
pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$

```
</details>