

# Slot: identifier_type 


_The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK._





URI: [acc:slot/identifier_type](https://example.org/accelerator-core/slot/identifier_type)
Alias: identifier_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identifier](../classes/Identifier.md) | A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IdentifierTypeEnum](../enums/IdentifierTypeEnum.md) |
| Domain Of | [Identifier](../classes/Identifier.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Identifier](../classes/Identifier.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:identifier_type |
| native | acc:identifier_type |




## LinkML Source

<details>
```yaml
name: identifier_type
description: The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: identifier_type
owner: Identifier
domain_of:
- Identifier
range: IdentifierTypeEnum

```
</details>