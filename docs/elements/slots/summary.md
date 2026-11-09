

# Slot: summary 


_A brief summary of the change._





URI: [pals_config:slot/summary](https://w3id.org/pals-config/slot/summary)
Alias: summary

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












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:summary |
| native | pals_config:summary |
| exact | skos:changeNote |




## LinkML Source

<details>
```yaml
name: summary
description: A brief summary of the change.
from_schema: https://w3id.org/pals-config
exact_mappings:
- skos:changeNote
rank: 1000
alias: summary
owner: ChangeLogEntryClass
domain_of:
- ChangeLogEntryClass
range: string
required: true

```
</details>