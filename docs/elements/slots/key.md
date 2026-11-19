

# Slot: key 


_The metadata field name._





URI: [pals_config:slot/key](https://w3id.org/pals-config/slot/key)
Alias: key

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdditionalMetadata](../classes/AdditionalMetadata.md) | A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AdditionalMetadata](../classes/AdditionalMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdditionalMetadata](../classes/AdditionalMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:key |
| native | pals_config:key |




## LinkML Source

<details>
```yaml
name: key
description: The metadata field name.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: key
owner: AdditionalMetadata
domain_of:
- AdditionalMetadata
range: string
required: true

```
</details>