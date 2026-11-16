

# Slot: change_date 


_The date the change was made, in ISO 8601 format (YYYY-MM-DD)._





URI: [pals_config:slot/change_date](https://w3id.org/pals-config/slot/change_date)
Alias: change_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) | An individual entry in the change log, documenting a specific change to the data instance. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Isodate](../types/Isodate.md) |
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
| self | pals_config:change_date |
| native | pals_config:change_date |




## LinkML Source

<details>
```yaml
name: change_date
description: The date the change was made, in ISO 8601 format (YYYY-MM-DD).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: change_date
owner: ChangeLogEntryClass
domain_of:
- ChangeLogEntryClass
range: isodate
required: true

```
</details>