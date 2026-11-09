

# Class: TemporalCoverageClass 


_Temporal coverage for time-based datasets, if applicable._

_  Container for elements describing the start_date and end_date of the data instance's temporal coverage _

_  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SSZ±hh:mm (e.g., 2024-06-05T14:30:00Z+05:00)._

_  Use temporal_coverage when the dataset describes a specific historical or projected time period._

_  This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant._





URI: [pals_config:class/TemporalCoverageClass](https://w3id.org/pals-config/class/TemporalCoverageClass)


```mermaid
erDiagram
TemporalCoverageClass {
    string end_date  
    string slot_usage  
    string slots  
    string start_date  
}



```



<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [start_date](../slots/start_date.md) | 0..1 <br/> [String](../types/String.md) | Start date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm ). | direct |
| [end_date](../slots/end_date.md) | 0..1 <br/> [String](../types/String.md) | End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm ). | direct |
| [slots](../slots/slots.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [slot_usage](../slots/slot_usage.md) | 0..1 <br/> [String](../types/String.md) | JsonObj(description='Detailed description of the temporal coverage.') | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | [temporal_coverage](../slots/temporal_coverage.md) | range | [TemporalCoverageClass](../classes/TemporalCoverageClass.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:TemporalCoverageClass |
| native | pals_config:TemporalCoverageClass |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TemporalCoverageClass
description: "Temporal coverage for time-based datasets, if applicable.\n  Container\
  \ for elements describing the start_date and end_date of the data instance's temporal\
  \ coverage \n  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SSZ±hh:mm (e.g., 2024-06-05T14:30:00Z+05:00).\n\
  \  Use temporal_coverage when the dataset describes a specific historical or projected\
  \ time period.\n  This may not apply to simulations where temporal coverage of a\
  \ specific facility during a specific time is not relevant."
from_schema: https://w3id.org/pals-config
attributes:
  start_date:
    name: start_date
    description: Start date of the dataset's temporal coverage in ISO 8601 format
      (YYYY-MM-DDTHH:MM:SSZ±hh:mm ).
    from_schema: https://w3id.org/pals-config
    related_mappings:
    - schema:temporalCoverage
    narrow_mappings:
    - dcterms:date
    rank: 1000
    domain_of:
    - TemporalCoverageClass
    range: string
    pattern: iso8601_datetime
  end_date:
    name: end_date
    description: End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm
      ).
    from_schema: https://w3id.org/pals-config
    related_mappings:
    - schema:temporalCoverage
    narrow_mappings:
    - dcterms:date
    rank: 1000
    domain_of:
    - TemporalCoverageClass
    range: string
    pattern: iso8601_datetime
  slots:
    name: slots
    id_prefixes:
    - description
    from_schema: https://w3id.org/pals-config
    rank: 1000
    domain_of:
    - TemporalCoverageClass
  slot_usage:
    name: slot_usage
    description: JsonObj(description='Detailed description of the temporal coverage.')
    from_schema: https://w3id.org/pals-config
    rank: 1000
    domain_of:
    - TemporalCoverageClass

```
</details>

### Induced

<details>
```yaml
name: TemporalCoverageClass
description: "Temporal coverage for time-based datasets, if applicable.\n  Container\
  \ for elements describing the start_date and end_date of the data instance's temporal\
  \ coverage \n  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SSZ±hh:mm (e.g., 2024-06-05T14:30:00Z+05:00).\n\
  \  Use temporal_coverage when the dataset describes a specific historical or projected\
  \ time period.\n  This may not apply to simulations where temporal coverage of a\
  \ specific facility during a specific time is not relevant."
from_schema: https://w3id.org/pals-config
attributes:
  start_date:
    name: start_date
    description: Start date of the dataset's temporal coverage in ISO 8601 format
      (YYYY-MM-DDTHH:MM:SSZ±hh:mm ).
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
  end_date:
    name: end_date
    description: End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ±hh:mm
      ).
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
    range: string
    pattern: iso8601_datetime
  slots:
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
  slot_usage:
    name: slot_usage
    description: JsonObj(description='Detailed description of the temporal coverage.')
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: slot_usage
    owner: TemporalCoverageClass
    domain_of:
    - TemporalCoverageClass
    range: string

```
</details>