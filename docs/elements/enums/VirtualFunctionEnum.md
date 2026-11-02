# Enum: VirtualFunctionEnum 




_Broad virtual component functions or roles._



URI: [acc:enum/VirtualFunctionEnum](https://example.org/accelerator-core/enum/VirtualFunctionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| BeamLineSection | None | A section of the BeamLine used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector. |
| Mark | None | A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device. |
| DriftSpace | None | A field-free longitudinal interval separating beamline components. |
| Fork | None | A virtual component representing a branching point in the beamline,  such as a beamline fork or switchyard. |
| Control | None | A virtual component representing a control system function or role that is important for understanding the overall accelerator system  but doesn't have a direct relationship to the beamline structure,  such as the EPICS control system that manages device process variables across the accelerator. |













## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: VirtualFunctionEnum
description: Broad virtual component functions or roles.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  BeamLineSection:
    text: BeamLineSection
    description: A section of the BeamLine used for organizational or functional grouping
      of components, such as a linac section, transfer line, or ring sector.
    exact_mappings:
    - pals:BeamLine
  Mark:
    text: Mark
    description: A virtual component representing an important location on the beamline,  such
      as a reference point for beam-based alignment, a location of a known aperture
      restriction,  or a location of a critical diagnostic device.
    exact_mappings:
    - pals:Marker
  DriftSpace:
    text: DriftSpace
    description: A field-free longitudinal interval separating beamline components.
    exact_mappings:
    - pals:Drift
  Fork:
    text: Fork
    description: A virtual component representing a branching point in the beamline,  such
      as a beamline fork or switchyard.
    exact_mappings:
    - pals:Fork
  Control:
    text: Control
    description: A virtual component representing a control system function or role
      that is important for understanding the overall accelerator system  but doesn't
      have a direct relationship to the beamline structure,  such as the EPICS control
      system that manages device process variables across the accelerator.

```
</details>