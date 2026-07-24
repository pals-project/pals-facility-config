

# Slot: description 


_A human-readable description of the instance._





URI: [pals:description](https://pals-project.readthedocs.io/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PALS](PALS.md) | Root container for accelerator core components, semantic signals, and local b... |  no  |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  no  |
| [MetaParamGroup](MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadat... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:description |
| native | pals:description |




## LinkML Source

<details>
```yaml
name: description
description: A human-readable description of the instance.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: description
domain_of:
- PALS
- MetaParamGroup
- BeamLine
range: string

```
</details>