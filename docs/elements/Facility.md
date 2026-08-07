

# Slot: facility 


_A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc._





URI: [pals:facility](https://pals-project.readthedocs.io/facility)
Alias: facility

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local b... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Facility](Facility.md) |
| Domain Of | [PALSAccelerator](PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PALSAccelerator](PALSAccelerator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:facility |
| native | pals:facility |




## LinkML Source

<details>
```yaml
name: facility
description: A facility that contains lattice elements (physical and virtual), beamlines,
  parameter set commands, signals, etc.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: facility
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: Facility

```
</details>