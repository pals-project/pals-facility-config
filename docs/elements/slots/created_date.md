

# Slot: created_date 


_The date the PALS/NARAD data instance of the facility configuration was first created, in ISO 8601 format (YYYY-MM-DD).  Provides temporal context for the data instance and can be used for tracking its age and relevance._





URI: [pals_config:slot/created_date](https://w3id.org/pals-config/slot/created_date)
Alias: created_date

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
| Required | Yes |
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
| self | pals_config:created_date |
| native | pals_config:created_date |




## LinkML Source

<details>
```yaml
name: created_date
description: The date the PALS/NARAD data instance of the facility configuration was
  first created, in ISO 8601 format (YYYY-MM-DD).  Provides temporal context for the
  data instance and can be used for tracking its age and relevance.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: created_date
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: isodate
required: true

```
</details>