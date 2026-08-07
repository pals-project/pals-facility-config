

# Slot: identifiers 


_A unique and ideally persistent identifier for the facility, such as a DOI or ROR._





URI: [pals:slot/identifiers](https://pals-project.readthedocs.io/slot/identifiers)
Alias: identifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Affiliation](../classes/Affiliation.md) | Contains affiliation information for an author or component, such as a ROR. |  no  |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifier](../classes/Identifier.md) |
| Domain Of | [Facility](../classes/Facility.md), [Affiliation](../classes/Affiliation.md) |

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