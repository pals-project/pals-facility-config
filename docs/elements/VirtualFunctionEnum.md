
# Enum: VirtualFunctionEnum

Broad virtual component functions or roles.

URI: [narad:VirtualFunctionEnum](https://example.org/narad/VirtualFunctionEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| BeamlineSection | A section of the beamline used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector. | pals:Beamline |  |
| Mark | A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device. | pals:Marker |  |
| Fork | A virtual component representing a branching point in the beamline,  such as a beamline fork or switchyard. | pals:Fork |  |
| Control | A virtual component representing a control system function or role that is important for understanding the overall accelerator system  but doesn't have a direct relationship to the beamline structure,  such as the EPICS control system that manages device process variables across the accelerator. |  |  |
