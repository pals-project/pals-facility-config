
# Class: Component

A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.

URI: [pals:Component](https://pals-project.readthedocs.io/Component)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[PhysicalComponent],[Node],[MetaParamGroup],[HasMetaP],[ComponentRelation],[ComponentRelation]-%20object%201..1>[Component&#124;native_types:string%20*;id(i):string;kind(i):string;alias(i):string%20*],[ComponentRelation]-%20subject%201..1>[Component],[Facility]++-%20components%200..*>[Component],[Component]uses%20-.->[HasMetaP],[Component]^-[VirtualComponent],[Component]^-[PhysicalComponent],[Node]^-[Component],[Facility])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[PhysicalComponent],[Node],[MetaParamGroup],[HasMetaP],[ComponentRelation],[ComponentRelation]-%20object%201..1>[Component&#124;native_types:string%20*;id(i):string;kind(i):string;alias(i):string%20*],[ComponentRelation]-%20subject%201..1>[Component],[Facility]++-%20components%200..*>[Component],[Component]uses%20-.->[HasMetaP],[Component]^-[VirtualComponent],[Component]^-[PhysicalComponent],[Node]^-[Component],[Facility])

## Parents

 *  is_a: [Node](Node.md) - Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology.

## Uses Mixin

 *  mixin: [HasMetaP](HasMetaP.md)

## Children

 * [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class

 *  **[ComponentRelation](ComponentRelation.md)** *[ComponentRelation➞object](ComponentRelation_object.md)*  <sub>1..1</sub>  **[Component](Component.md)**
 *  **[ComponentRelation](ComponentRelation.md)** *[ComponentRelation➞subject](ComponentRelation_subject.md)*  <sub>1..1</sub>  **[Component](Component.md)**
 *  **None** *[➞components](facility__components.md)*  <sub>0..\*</sub>  **[Component](Component.md)**

## Attributes


### Own

 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)

### Inherited from Node:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [kind](kind.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..\*</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)

### Mixed in from HasMetaP:

 * [➞MetaP](hasMetaP__MetaP.md)  <sub>0..1</sub>
     * Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [MetaParamGroup](MetaParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
