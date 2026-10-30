

# Slot: RFP 


_A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [acc:slot/RFP](https://example.org/accelerator-core/slot/RFP)
Alias: RFP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFCavity](../classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |  no  |
| [HasRFP](../classes/HasRFP.md) |  |  no  |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting. |  no  |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is superconducting. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RFParamGroup](../classes/RFParamGroup.md) |
| Domain Of | [HasRFP](../classes/HasRFP.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HasRFP](../classes/HasRFP.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:RFP |
| native | acc:RFP |




## LinkML Source

<details>
```yaml
name: RFP
description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters)
  for interoperability with the Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: RFP
owner: HasRFP
domain_of:
- HasRFP
range: RFParamGroup
inlined: true

```
</details>