

# Slot: schema_version 


_Version of the schema used for this representation of a particle accelerator and its operations. Should follow the semantic versioning convention (MAJOR.MINOR.PATCH). Should match the schema version of the NARAD/PALS instance configuration schema being used._





URI: [pals_config:slot/schema_version](https://w3id.org/pals-config/slot/schema_version)
Alias: schema_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [PALSAccelerator](../classes/PALSAccelerator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `(0.0.1)` |
| Owner | [PALSAccelerator](../classes/PALSAccelerator.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:schema_version |
| native | pals_config:schema_version |




## LinkML Source

<details>
```yaml
name: schema_version
description: Version of the schema used for this representation of a particle accelerator
  and its operations. Should follow the semantic versioning convention (MAJOR.MINOR.PATCH).
  Should match the schema version of the NARAD/PALS instance configuration schema
  being used.
from_schema: https://w3id.org/pals-config
rank: 1000
ifabsent: (0.0.1)
alias: schema_version
owner: PALSAccelerator
domain_of:
- PALSAccelerator
range: string
required: false
pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$

```
</details>