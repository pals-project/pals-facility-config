
# Class: MetaP

Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [narad:MetaP](https://example.org/narad/MetaP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataEntry],[MetadataEntry]<additional_metadata%200..*-++[MetaP&#124;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[Signal]uses%20-.->[MetaP],[Component]uses%20-.->[MetaP],[Signal],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataEntry],[MetadataEntry]<additional_metadata%200..*-++[MetaP&#124;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[Signal]uses%20-.->[MetaP],[Component]uses%20-.->[MetaP],[Signal],[Component])

## Mixin for

 * [Component](Component.md) (mixin)  - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
 * [Signal](Signal.md) (mixin)  - Semantic meaning of a control-system signal associated with a component.

## Referenced by Class


## Attributes


### Own

 * [➞description](metaP__description.md)  <sub>0..1</sub>
     * Description: Human-readable description.
     * Range: [String](types/String.md)
 * [➞label](metaP__label.md)  <sub>0..1</sub>
     * Description: A label string.
     * Range: [String](types/String.md)
 * [➞alias](metaP__alias.md)  <sub>0..1</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)
 * [➞additional_metadata](metaP__additional_metadata.md)  <sub>0..\*</sub>
     * Description: Additional metadata or annotations for the instance.
     * Range: [MetadataEntry](MetadataEntry.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:MetaP |
