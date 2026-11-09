

# Slot: updated_date 


_The date the data instance for the facility configuration was last updated, in ISO 8601 format (YYYY-MM-DD). Date of most recent update; revise on every change/version to the data instance, including minor edits and version updates.  This provides temporal context for the data instance and can be used for tracking its currency and maintenance._





URI: [pals_config:slot/updated_date](https://w3id.org/pals-config/slot/updated_date)
Alias: updated_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Isodate](../types/Isodate.md) |
| Domain Of | [PALSAccelerator](../classes/PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | pals_config:updated_date |
| native | pals_config:updated_date |




## LinkML Source

<details>
```yaml
name: updated_date
description: The date the data instance for the facility configuration was last updated,
  in ISO 8601 format (YYYY-MM-DD). Date of most recent update; revise on every change/version
  to the data instance, including minor edits and version updates.  This provides
  temporal context for the data instance and can be used for tracking its currency
  and maintenance.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: updated_date
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: isodate

```
</details>