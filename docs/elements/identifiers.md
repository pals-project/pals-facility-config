

# Slot: identifiers 


_A unique and ideally persistent identifier for the facility, such as a DOI or ROR._





URI: [pals:identifiers](https://pals-project.readthedocs.io/identifiers)
Alias: identifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Affiliation](Affiliation.md) | Contains affiliation information for an author or component, such as a ROR |  no  |
| [Facility](Facility.md) | A facility that houses one or more accelerators |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifier](Identifier.md) |
| Domain Of | [Facility](Facility.md), [Affiliation](Affiliation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:identifiers |
| native | pals:identifiers |




## LinkML Source

<details>
```yaml
name: identifiers
description: A unique and ideally persistent identifier for the facility, such as
  a DOI or ROR.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: identifiers
domain_of:
- Facility
- Affiliation
range: Identifier
multivalued: true

```
</details>