

# Slot: start_date 


_Start date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm )._





URI: [pals_config:slot/start_date](https://w3id.org/pals-config/slot/start_date)
Alias: start_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TemporalCoverageClass](../classes/TemporalCoverageClass.md) | Temporal coverage for time-based datasets, if applicable.<br>  Container for elements describing the start_date and end_date of the data instance's temporal coverage <br>  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SSZ±hh:mm (e.g., 2024-06-05T14:30:00Z+05:00).<br>  Use temporal_coverage when the dataset describes a specific historical or projected time period.<br>  This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `iso8601_datetime` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:start_date |
| native | pals_config:start_date |
| narrow | dcterms:date |
| related | schema:temporalCoverage |




## LinkML Source

<details>
```yaml
name: start_date
description: Start date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm
  ).
from_schema: https://w3id.org/pals-config
related_mappings:
- schema:temporalCoverage
narrow_mappings:
- dcterms:date
rank: 1000
alias: start_date
owner: TemporalCoverageClass
domain_of:
- TemporalCoverageClass
range: string
pattern: iso8601_datetime

```
</details>