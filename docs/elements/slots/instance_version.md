

# Slot: instance_version 


_The version of the data instance that was changed._





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
| If Absent | `string(0.0.0)` |
| Owner | [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+\.\d+(\.\d+)?$` |












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
description: The version of the data instance that was changed.
from_schema: https://w3id.org/pals-config
rank: 1000
ifabsent: string(0.0.0)
alias: instance_version
owner: ChangeLogEntryClass
domain_of:
- ChangeLogEntryClass
range: string
required: true
pattern: ^\d+\.\d+(\.\d+)?$

```
</details>