

# Slot: beamline_context 


_The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order)._





URI: [pals:slot/beamline_context](https://pals-project.readthedocs.io/slot/beamline_context)
Alias: beamline_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentRelation](../classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BeamLine](../classes/BeamLine.md) |
| Domain Of | [ComponentRelation](../classes/ComponentRelation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ComponentRelation](../classes/ComponentRelation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:beamline_context |
| native | pals:beamline_context |




## LinkML Source

<details>
```yaml
name: beamline_context
description: The specific BeamLine this relationship is defined with respect to (relevant
  when context=beamline_order).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: beamline_context
owner: ComponentRelation
domain_of:
- ComponentRelation
range: BeamLine

```
</details>