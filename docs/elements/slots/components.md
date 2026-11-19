

# Slot: components 


_A list of physical components in the accelerator system._





URI: [pals_config:slot/components](https://w3id.org/pals-config/slot/components)
Alias: components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Component](../classes/Component.md) |
| Domain Of | [Facility](../classes/Facility.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Facility](../classes/Facility.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:components |
| native | pals_config:components |




## LinkML Source

<details>
```yaml
name: components
description: A list of physical components in the accelerator system.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: components
owner: Facility
domain_of:
- Facility
range: Component
multivalued: true
inlined: true
inlined_as_list: true

```
</details>