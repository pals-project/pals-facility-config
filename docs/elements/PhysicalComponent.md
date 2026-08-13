
# Class: PhysicalComponent

A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

URI: [pals:PhysicalComponent](https://pals-project.readthedocs.io/PhysicalComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent],[SignalBinding],[SignalBinding]-%20subject%201..1>[PhysicalComponent&#124;functions:PhysicalFunctionEnum%20%2B;beamline_relation:PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[PhysicalComponent]uses%20-.->[HasFloorP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacementP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent]^-[Magnet],[PhysicalComponent]^-[DiagnosticDevice],[PhysicalComponent]^-[Cavity],[Component]^-[PhysicalComponent],[MetaParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP],[HasFloorP],[FloorParamGroup],[DiagnosticDevice],[Component],[Cavity])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent],[SignalBinding],[SignalBinding]-%20subject%201..1>[PhysicalComponent&#124;functions:PhysicalFunctionEnum%20%2B;beamline_relation:PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[PhysicalComponent]uses%20-.->[HasFloorP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacementP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent]^-[Magnet],[PhysicalComponent]^-[DiagnosticDevice],[PhysicalComponent]^-[Cavity],[Component]^-[PhysicalComponent],[MetaParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP],[HasFloorP],[FloorParamGroup],[DiagnosticDevice],[Component],[Cavity])

## Parents

 *  is_a: [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.

## Uses Mixin

 *  mixin: [HasFloorP](HasFloorP.md)
 *  mixin: [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)

## Children

 * [Cavity](Cavity.md) - A cavity used for beam acceleration or manipulation.
 * [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.
 * [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) - A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.

## Referenced by Class

 *  **[SignalBinding](SignalBinding.md)** *[SignalBinding➞subject](SignalBinding_subject.md)*  <sub>1..1</sub>  **[PhysicalComponent](PhysicalComponent.md)**

## Attributes


### Own

 * [➞functions](physicalComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the physical component,  which can be used to identify the component across different source systems.
     * Range: [PhysicalFunctionEnum](PhysicalFunctionEnum.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

### Inherited from Component:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [kind](kind.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..\*</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)

### Mixed in from HasFloorP:

 * [➞FloorP](hasFloorP__FloorP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [FloorParamGroup](FloorParamGroup.md)

### Mixed in from HasLongitudinalPlacementP:

 * [➞LongitudinalPlacementP](hasLongitudinalPlacementP__LongitudinalPlacementP.md)  <sub>0..1</sub>
     * Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
