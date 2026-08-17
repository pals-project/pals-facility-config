
# Class: SupportingFacilityComponent

A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.

URI: [pals:SupportingFacilityComponent](https://pals-project.readthedocs.io/SupportingFacilityComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent&#124;functions:FacilityFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasFloorP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacementP],[SupportingFacilityComponent]uses%20-.->[HasBodyShiftP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent],[MetaParamGroup],[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP],[HasFloorP],[HasBodyShiftP],[FloorParamGroup],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent&#124;functions:FacilityFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasFloorP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacementP],[SupportingFacilityComponent]uses%20-.->[HasBodyShiftP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent],[MetaParamGroup],[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP],[HasFloorP],[HasBodyShiftP],[FloorParamGroup],[BodyShiftParamGroup])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Uses Mixin

 *  mixin: [HasFloorP](HasFloorP.md)
 *  mixin: [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)
 *  mixin: [HasBodyShiftP](HasBodyShiftP.md)

## Attributes


### Own

 * [➞functions](supportingFacilityComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the supporting facility component,  which can be used to identify the component across different source systems.
     * Range: [FacilityFunctionEnum](FacilityFunctionEnum.md)

### Inherited from PhysicalComponent:

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
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

### Mixed in from HasFloorP:

 * [➞FloorP](hasFloorP__FloorP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [FloorParamGroup](FloorParamGroup.md)

### Mixed in from HasLongitudinalPlacementP:

 * [➞LongitudinalPlacementP](hasLongitudinalPlacementP__LongitudinalPlacementP.md)  <sub>0..1</sub>
     * Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md)

### Mixed in from HasBodyShiftP:

 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BodyShiftParamGroup](BodyShiftParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:StructuralElement |
