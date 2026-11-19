

# Slot: temporal_coverage 


_Temporal coverage for time-based datasets, if applicable. Container for elements describing the start_date and end_date of the data instance's temporal coverage  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SS±hh:mm for offset (e.g., 2024-06-05T14:30:00-04:00) or YYYY-MM-DDTHH:MM:SSZ for UTC (e.g., 2024-06-05T14:30:00Z). Use temporal_coverage when the dataset describes a specific historical or projected time period. This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant._





URI: [pals_config:slot/temporal_coverage](https://w3id.org/pals-config/slot/temporal_coverage)
Alias: temporal_coverage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |
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
| self | pals_config:temporal_coverage |
| native | pals_config:temporal_coverage |
| related | dcterms:temporal, schema:temporalCoverage |




## LinkML Source

<details>
```yaml
name: temporal_coverage
description: Temporal coverage for time-based datasets, if applicable. Container for
  elements describing the start_date and end_date of the data instance's temporal
  coverage  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SS±hh:mm for offset (e.g.,
  2024-06-05T14:30:00-04:00) or YYYY-MM-DDTHH:MM:SSZ for UTC (e.g., 2024-06-05T14:30:00Z).
  Use temporal_coverage when the dataset describes a specific historical or projected
  time period. This may not apply to simulations where temporal coverage of a specific
  facility during a specific time is not relevant.
from_schema: https://w3id.org/pals-config
related_mappings:
- dcterms:temporal
- schema:temporalCoverage
rank: 1000
alias: temporal_coverage
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: TemporalCoverageClass
required: false

```
</details>