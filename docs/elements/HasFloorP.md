
# Class: HasFloorP



URI: [pals:HasFloorP](https://pals-project.readthedocs.io/HasFloorP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[FloorParamGroup]<FloorP%200..1-++[HasFloorP],[VirtualComponent]uses%20-.->[HasFloorP],[SupportingFacilityComponent]uses%20-.->[HasFloorP],[PhysicalComponent]uses%20-.->[HasFloorP],[BeamLineSection]uses%20-.->[HasFloorP],[VirtualComponent],[SupportingFacilityComponent],[PhysicalComponent],[FloorParamGroup],[BeamLineSection])](https://yuml.me/diagram/nofunky;dir:TB/class/[FloorParamGroup]<FloorP%200..1-++[HasFloorP],[VirtualComponent]uses%20-.->[HasFloorP],[SupportingFacilityComponent]uses%20-.->[HasFloorP],[PhysicalComponent]uses%20-.->[HasFloorP],[BeamLineSection]uses%20-.->[HasFloorP],[VirtualComponent],[SupportingFacilityComponent],[PhysicalComponent],[FloorParamGroup],[BeamLineSection])

## Mixin for

 * [BeamLineSection](BeamLineSection.md) (mixin)  - A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.
 * [PhysicalComponent](PhysicalComponent.md) (mixin)  - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
 * [VirtualComponent](VirtualComponent.md) (mixin)  - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class


## Attributes


### Own

 * [➞FloorP](hasFloorP__FloorP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [FloorParamGroup](FloorParamGroup.md)
