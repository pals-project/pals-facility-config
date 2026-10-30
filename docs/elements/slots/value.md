

# Slot: value 


_The metadata value, serialized as a string._





URI: [acc:slot/value](https://example.org/accelerator-core/slot/value)
Alias: value

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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:value |
| native | acc:value |




## LinkML Source

<details>
```yaml
name: value
description: The metadata value, serialized as a string.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: value
owner: AdditionalMetadata
domain_of:
- AdditionalMetadata
range: string
required: true

```
</details>