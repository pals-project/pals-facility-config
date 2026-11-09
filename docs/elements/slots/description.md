

# Slot: description 


_A human-readable description of the instance._





URI: [pals_config:slot/description](https://w3id.org/pals-config/slot/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetaParamGroup](../classes/MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |
| [PALSAccelerator](../classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |  no  |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [PALSAccelerator](../classes/PALSAccelerator.md), [MetaParamGroup](../classes/MetaParamGroup.md), [BeamLine](../classes/BeamLine.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:description |
| native | pals_config:description |




## LinkML Source

<details>
```yaml
name: description
description: A human-readable description of the instance.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: description
domain_of:
- PALSAccelerator
- MetaParamGroup
- BeamLine
range: string

```
</details>