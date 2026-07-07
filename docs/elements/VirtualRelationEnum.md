
# Enum: VirtualRelationEnum

Controlled values for virtual relation to the beamline.

URI: [narad:VirtualRelationEnum](https://example.org/narad/VirtualRelationEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| Inline | Beam passes through the virtual component. Used for virtual components like Markers that represent important locations on the beamline but don't have a physical instantiation. |  |  |
| AssociatedWithBeamline | Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the beamline structure and function but don't have a direct physical relationship to the beam path,  such as BeamlineSections or Markers that are not inline with the beam. |  |  |
| NotAssociatedWithBeamline | Not inline with the beamline and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the beamline, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the beamline structure. |  |  |
