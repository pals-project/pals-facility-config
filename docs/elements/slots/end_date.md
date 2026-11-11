

# Slot: end_date 


_End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SS±hh:mm for offset or YYYY-MM-DDTHH:MM:SSZ for UTC)._





URI: [pals_config:slot/end_date](https://w3id.org/pals-config/slot/end_date)
Alias: end_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TemporalCoverageClass](../classes/TemporalCoverageClass.md) | Temporal coverage for time-based datasets, if applicable.<br>  Container for elements describing the start_date and end_date of the data instance's temporal coverage <br>  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SS±hh:mm for offset (e.g., 2024-06-05T14:30:00-04:00) or YYYY-MM-DDTHH:MM:SSZ for UTC (e.g., 2024-06-05T14:30:00Z).<br>  Use temporal_coverage when the dataset describes a specific historical or projected time period.<br>  This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Iso8601Datetime](../types/Iso8601Datetime.md) |
| Domain Of | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:end_date |
| native | pals_config:end_date |
| narrow | dcterms:date |
| related | schema:temporalCoverage |




## LinkML Source

<details>
```yaml
name: end_date
description: End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SS±hh:mm
  for offset or YYYY-MM-DDTHH:MM:SSZ for UTC).
from_schema: https://w3id.org/pals-config
related_mappings:
- schema:temporalCoverage
narrow_mappings:
- dcterms:date
rank: 1000
alias: end_date
owner: TemporalCoverageClass
domain_of:
- TemporalCoverageClass
range: iso8601_datetime

```
</details>