

# Slot: RFP 


_A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:RFP](https://pals-project.readthedocs.io/RFP)
Alias: RFP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasRFP](HasRFP.md) |  |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |






## Properties

* Range: [RFParamGroup](RFParamGroup.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:RFP |
| native | pals:RFP |




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