

# Slot: native_unit 


_The native unit of the signal in the source system._





URI: [pals_config:slot/native_unit](https://w3id.org/pals-config/slot/native_unit)
Alias: native_unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [UnitEnum](../enums/UnitEnum.md) |
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
| self | pals_config:native_unit |
| native | pals_config:native_unit |




## LinkML Source

<details>
```yaml
name: native_unit
description: The native unit of the signal in the source system.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: native_unit
owner: Signal
domain_of:
- Signal
range: UnitEnum
required: true

```
</details>