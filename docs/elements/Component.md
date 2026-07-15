
# Class: Component

A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.

URI: [narad:Component](https://example.org/narad/Component)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[PhysicalComponent],[MetadataEntry],[MetaP],[ComponentRelation],[Component]<type%201..1-%20[Component&#124;id:string;native_types:string%20*;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[ComponentRelation]-%20object%201..1>[Component],[ComponentRelation]-%20subject%201..1>[Component],[Component]uses%20-.->[MetaP],[Component]^-[VirtualComponent],[Component]^-[PhysicalComponent])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[PhysicalComponent],[MetadataEntry],[MetaP],[ComponentRelation],[Component]<type%201..1-%20[Component&#124;id:string;native_types:string%20*;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[ComponentRelation]-%20object%201..1>[Component],[ComponentRelation]-%20subject%201..1>[Component],[Component]uses%20-.->[MetaP],[Component]^-[VirtualComponent],[Component]^-[PhysicalComponent])

## Uses Mixin

 *  mixin: [MetaP](MetaP.md) - Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).

## Children

 * [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class

 *  **[ComponentRelation](ComponentRelation.md)** *[ComponentRelation➞object](ComponentRelation_object.md)*  <sub>1..1</sub>  **[Component](Component.md)**
 *  **[ComponentRelation](ComponentRelation.md)** *[ComponentRelation➞subject](ComponentRelation_subject.md)*  <sub>1..1</sub>  **[Component](Component.md)**
 *  **None** *[type](type.md)*  <sub>1..1</sub>  **[Component](Component.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [Component](Component.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞description](metaP__description.md)  <sub>0..1</sub>
     * Description: Human-readable description.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞label](metaP__label.md)  <sub>0..1</sub>
     * Description: A label string.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞alias](metaP__alias.md)  <sub>0..1</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞additional_metadata](metaP__additional_metadata.md)  <sub>0..\*</sub>
     * Description: Additional metadata or annotations for the instance.
     * Range: [MetadataEntry](MetadataEntry.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
