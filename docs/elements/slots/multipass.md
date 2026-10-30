

# Slot: multipass 


_Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass._





URI: [acc:slot/multipass](https://example.org/accelerator-core/slot/multipass)
Alias: multipass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLine](../classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [BeamLine](../classes/BeamLine.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BeamLine](../classes/BeamLine.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:multipass |
| native | acc:multipass |
| close | pals:multipass |




## LinkML Source

<details>
```yaml
name: multipass
description: Indicates whether the BeamLine is a multipass BeamLine, where the beam
  passes through the same physical elements multiple times. If not provided, the default
  assumption is that the BeamLine is single-pass.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:multipass
rank: 1000
alias: multipass
owner: BeamLine
domain_of:
- BeamLine
range: boolean

```
</details>