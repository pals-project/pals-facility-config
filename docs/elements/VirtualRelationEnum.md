# Enum: VirtualRelationEnum 




_Controlled values for virtual relation to the beamline._



URI: [pals:VirtualRelationEnum](https://pals-project.readthedocs.io/VirtualRelationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Inline | None | Beam passes through the virtual component |
| AssociatedWithBeamLine | None | Not inline with the beamline but still operationally associated with it |
| NotAssociatedWithBeamLine | None | Not inline with the BeamLine and not operationally associated with it |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: VirtualRelationEnum
description: Controlled values for virtual relation to the beamline.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  Inline:
    text: Inline
    description: Beam passes through the virtual component. Used for virtual components
      like Markers that represent important locations on the beamline but don't have
      a physical instantiation.
  AssociatedWithBeamLine:
    text: AssociatedWithBeamLine
    description: Not inline with the beamline but still operationally associated with
      it.  Used for virtual components that are important for understanding the BeamLine
      structure and function but don't have a direct physical relationship to the
      beam path,  such as BeamLineSections or Markers that are not inline with the
      beam.
  NotAssociatedWithBeamLine:
    text: NotAssociatedWithBeamLine
    description: Not inline with the BeamLine and not operationally associated with
      it.  Used for virtual components that are more abstract and don't have a specific
      relationship  to the BeamLine, such as a virtual component representing a control
      system function  or role that is important for understanding the overall accelerator
      system but doesn't have a direct relationship to the BeamLine structure.

```
</details>