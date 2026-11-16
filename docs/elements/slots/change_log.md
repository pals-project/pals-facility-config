

# Slot: change_log 


_Running history of meaningful changes to a data instance of a facility's configuration. Add a new entry every time the instance is updated. Do not overwrite or delete prior entries. If there have been no changes since creation, include a single entry with the creation date and the summary 'Initial creation'._





URI: [pals_config:slot/change_log](https://w3id.org/pals-config/slot/change_log)
Alias: change_log

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChangeLogEntryClass](../classes/ChangeLogEntryClass.md) |
| Domain Of | [PALSAccelerator](../classes/PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | pals_config:change_log |
| native | pals_config:change_log |




## LinkML Source

<details>
```yaml
name: change_log
description: Running history of meaningful changes to a data instance of a facility's
  configuration. Add a new entry every time the instance is updated. Do not overwrite
  or delete prior entries. If there have been no changes since creation, include a
  single entry with the creation date and the summary 'Initial creation'.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: change_log
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: ChangeLogEntryClass
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>