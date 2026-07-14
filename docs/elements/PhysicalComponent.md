
# Class: PhysicalComponent

A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

URI: [narad:PhysicalComponent](https://example.org/narad/PhysicalComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent],[SignalBinding],[SignalBinding]-%20subject%201..1>[PhysicalComponent&#124;functions:PhysicalFunctionEnum%20%2B;beamline_relation:PhysicalRelationEnum;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;length:float%20%3F;s_position:float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[NARAD]++-%20physical_components%200..*>[PhysicalComponent],[PhysicalComponent]uses%20-.->[FloorP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacement],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent]^-[Magnet],[PhysicalComponent]^-[DiagnosticDevice],[PhysicalComponent]^-[Cavity],[Component]^-[PhysicalComponent],[NARAD],[MetadataEntry],[Magnet],[HasLongitudinalPlacement],[FloorP],[DiagnosticDevice],[Component],[Cavity])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent],[SignalBinding],[SignalBinding]-%20subject%201..1>[PhysicalComponent&#124;functions:PhysicalFunctionEnum%20%2B;beamline_relation:PhysicalRelationEnum;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;length:float%20%3F;s_position:float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[NARAD]++-%20physical_components%200..*>[PhysicalComponent],[PhysicalComponent]uses%20-.->[FloorP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacement],[PhysicalComponent]^-[SupportingFacilityComponent],[PhysicalComponent]^-[Magnet],[PhysicalComponent]^-[DiagnosticDevice],[PhysicalComponent]^-[Cavity],[Component]^-[PhysicalComponent],[NARAD],[MetadataEntry],[Magnet],[HasLongitudinalPlacement],[FloorP],[DiagnosticDevice],[Component],[Cavity])

## Parents

 *  is_a: [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.

## Uses Mixin

 *  mixin: [FloorP](FloorP.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 *  mixin: [HasLongitudinalPlacement](HasLongitudinalPlacement.md) - Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.

## Children

 * [Cavity](Cavity.md) - A cavity used for beam acceleration or manipulation.
 * [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.
 * [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) - A physical component that supports accelerator operation

## Referenced by Class

 *  **[SignalBinding](SignalBinding.md)** *[SignalBinding➞subject](SignalBinding_subject.md)*  <sub>1..1</sub>  **[PhysicalComponent](PhysicalComponent.md)**
 *  **None** *[➞physical_components](nARAD__physical_components.md)*  <sub>0..\*</sub>  **[PhysicalComponent](PhysicalComponent.md)**

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
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
