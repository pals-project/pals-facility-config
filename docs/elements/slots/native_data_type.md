

# Slot: native_data_type 


_The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean._





URI: [pals_config:slot/native_data_type](https://w3id.org/pals-config/slot/native_data_type)
Alias: native_data_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DataTypeEnum](../enums/DataTypeEnum.md) |
| Domain Of | [Signal](../classes/Signal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Signal](../classes/Signal.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:native_data_type |
| native | pals_config:native_data_type |




## LinkML Source

<details>
```yaml
name: native_data_type
description: The native data type of the signal in the source system,  such as String,
  Integer, Float, or Boolean.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: native_data_type
owner: Signal
domain_of:
- Signal
range: DataTypeEnum
required: true

```
</details>