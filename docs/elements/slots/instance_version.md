

# Slot: instance_version 


_The version of the data instance that was changed. If this is the initial creation, it should be set to 0.0.0._





URI: [pals_config:slot/instance_version](https://w3id.org/pals-config/slot/instance_version)
Alias: instance_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) | An individual entry in the change log, documenting a specific change to the data instance. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:instance_version |
| native | pals_config:instance_version |




## LinkML Source

<details>
```yaml
name: instance_version
description: The version of the data instance that was changed. If this is the initial
  creation, it should be set to 0.0.0.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: instance_version
owner: ChangeLogEntryClass
domain_of:
- ChangeLogEntryClass
range: string
required: true
pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$

```
</details>