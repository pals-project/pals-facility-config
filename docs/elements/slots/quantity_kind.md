

# Slot: quantity_kind 


_The physical quantity kind of the signal._





URI: [pals:slot/quantity_kind](https://pals-project.readthedocs.io/slot/quantity_kind)
Alias: quantity_kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuantityKindEnum](../enums/QuantityKindEnum.md) |
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:quantity_kind |
| native | pals:quantity_kind |




## LinkML Source

<details>
```yaml
name: quantity_kind
description: The physical quantity kind of the signal.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: quantity_kind
owner: Signal
domain_of:
- Signal
range: QuantityKindEnum
required: true

```
</details>