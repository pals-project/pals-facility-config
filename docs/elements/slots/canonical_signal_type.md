

# Slot: canonical_signal_type 


_The canonical semantic meaning of the signal._





URI: [pals:slot/canonical_signal_type](https://pals-project.readthedocs.io/slot/canonical_signal_type)
Alias: canonical_signal_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](../classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CanonicalSignalTypeEnum](../enums/CanonicalSignalTypeEnum.md) |
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
| self | pals:canonical_signal_type |
| native | pals:canonical_signal_type |




## LinkML Source

<details>
```yaml
name: canonical_signal_type
description: The canonical semantic meaning of the signal.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: canonical_signal_type
owner: Signal
domain_of:
- Signal
range: CanonicalSignalTypeEnum
required: true

```
</details>