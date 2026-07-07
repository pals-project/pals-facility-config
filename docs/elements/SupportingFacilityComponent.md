
# Class: SupportingFacilityComponent

A physical component that supports accelerator operation 
without a specific beam-pipe placement, 
such as a power supply, control rack, or radiation detector.
These can include Girders, Racks, Power Supplies, 
and other physical infrastructure components that are important for understanding 
the structure and function of the accelerator system but are not inline with the beamline.

URI: [narad:SupportingFacilityComponent](https://example.org/narad/SupportingFacilityComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NARAD]++-%20supporting_facility_components%200..*>[SupportingFacilityComponent&#124;function:FacilityFunctionEnum;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[SupportingFacilityComponent]uses%20-.->[FloorP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacement],[SupportingFacilityComponent]uses%20-.->[BodyShiftP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent],[NARAD],[MetadataEntry],[HasLongitudinalPlacement],[FloorP],[BodyShiftP])](https://yuml.me/diagram/nofunky;dir:TB/class/[NARAD]++-%20supporting_facility_components%200..*>[SupportingFacilityComponent&#124;function:FacilityFunctionEnum;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[SupportingFacilityComponent]uses%20-.->[FloorP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacement],[SupportingFacilityComponent]uses%20-.->[BodyShiftP],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent],[NARAD],[MetadataEntry],[HasLongitudinalPlacement],[FloorP],[BodyShiftP])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Uses Mixin

 *  mixin: [FloorP](FloorP.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 *  mixin: [HasLongitudinalPlacement](HasLongitudinalPlacement.md) - Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.
 *  mixin: [BodyShiftP](BodyShiftP.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

## Referenced by Class

 *  **None** *[➞supporting_facility_components](nARAD__supporting_facility_components.md)*  <sub>0..\*</sub>  **[SupportingFacilityComponent](SupportingFacilityComponent.md)**

## Attributes


### Own

 * [➞function](supportingFacilityComponent__function.md)  <sub>1..1</sub>
     * Description: The function of the supporting facility component,  which can be used to identify the component across different source systems.
     * Range: [FacilityFunctionEnum](FacilityFunctionEnum.md)

### Inherited from PhysicalComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

### Mixed in from FloorP:

 * [➞x](floorP__x.md)  <sub>0..1</sub>
     * Description: Global X coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞y](floorP__y.md)  <sub>0..1</sub>
     * Description: Global Y coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞z](floorP__z.md)  <sub>0..1</sub>
     * Description: Global Z coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞theta](floorP__theta.md)  <sub>0..1</sub>
     * Description: Orientation angle around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞phi](floorP__phi.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞psi](floorP__psi.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from HasLongitudinalPlacement:

 * [➞length](hasLongitudinalPlacement__length.md)  <sub>0..1</sub>
     * Description: Length of the element (arc length for bends).
     * Range: [Float](types/Float.md)

### Mixed in from HasLongitudinalPlacement:

 * [➞s_position](hasLongitudinalPlacement__s_position.md)  <sub>0..1</sub>
     * Description: Longitudinal position of the element along the beamline.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞x_offset](bodyShiftP__x_offset.md)  <sub>0..1</sub>
     * Description: Shift in the X direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_offset](bodyShiftP__y_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Y direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_offset](bodyShiftP__z_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Z direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞x_rot](bodyShiftP__x_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_rot](bodyShiftP__y_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_rot](bodyShiftP__z_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:StructuralElement |
