

# Slot: datatype 


_Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string._





URI: [acc:slot/datatype](https://example.org/accelerator-core/slot/datatype)
Alias: datatype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdditionalMetadata](../classes/AdditionalMetadata.md) | A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DataTypeEnum](../enums/DataTypeEnum.md) |
| Domain Of | [AdditionalMetadata](../classes/AdditionalMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | acc:datatype |
| native | acc:datatype |




## LinkML Source

<details>
```yaml
name: datatype
description: Hint for the value's original type, so consumers can parse it back (e.g.
  float, integer, boolean) rather than treating everything as an opaque string.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: datatype
owner: AdditionalMetadata
domain_of:
- AdditionalMetadata
range: DataTypeEnum

```
</details>