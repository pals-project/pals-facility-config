

# Slot: rfp 


_A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:rfp](https://pals-project.readthedocs.io/rfp)
Alias: rfp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [HasRFP](HasRFP.md) |  |  no  |






## Properties

* Range: [RFP](RFP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:rfp |
| native | pals:rfp |




## LinkML Source

<details>
```yaml
name: rfp
description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters)
  for interoperability with the Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: rfp
owner: HasRFP
domain_of:
- HasRFP
range: RFP

```
</details>