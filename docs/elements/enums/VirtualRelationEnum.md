# Enum: VirtualRelationEnum 




_Controlled values for virtual relation to the beamline._



URI: [pals_config:enum/VirtualRelationEnum](https://w3id.org/pals-config/enum/VirtualRelationEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Inline | None | Beam passes through the virtual component. Used for virtual components like Markers that represent important locations on the beamline but don't have a physical instantiation. |
| AssociatedWithBeamLine | None | Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the BeamLine structure and function but don't have a direct physical relationship to the beam path,  such as BeamLineSections or Markers that are not inline with the beam. |
| NotAssociatedWithBeamLine | None | Not inline with the BeamLine and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the BeamLine, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the BeamLine structure. |




## Slots

| Name | Description |
| ---  | --- |
| [beamline_relation](../slots/beamline_relation.md) | The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config






## LinkML Source

<details>
```yaml
name: VirtualRelationEnum
description: Controlled values for virtual relation to the beamline.
from_schema: https://w3id.org/pals-config
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