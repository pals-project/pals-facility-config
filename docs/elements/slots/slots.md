

# Slot: slots 



URI: [pals_config:slot/slots](https://w3id.org/pals-config/slot/slots)
Alias: slots

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












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* description







### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:slots |
| native | pals_config:slots |




## LinkML Source

<details>
```yaml
name: slots
id_prefixes:
- description
from_schema: https://w3id.org/pals-config
rank: 1000
alias: slots
owner: TemporalCoverageClass
domain_of:
- TemporalCoverageClass
range: string

```
</details>