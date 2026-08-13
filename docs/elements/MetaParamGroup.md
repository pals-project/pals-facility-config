
# Class: MetaParamGroup

Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:MetaParamGroup](https://pals-project.readthedocs.io/MetaParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[AdditionalMetadata]<additional_metadata%200..*-++[MetaParamGroup&#124;description:string%20%3F;alias:string%20*;label:string%20%3F;id(i):string],[HasMetaP]++-%20MetaP%200..1>[MetaParamGroup],[ParamGroup]^-[MetaParamGroup],[HasMetaP],[AdditionalMetadata])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[AdditionalMetadata]<additional_metadata%200..*-++[MetaParamGroup&#124;description:string%20%3F;alias:string%20*;label:string%20%3F;id(i):string],[HasMetaP]++-%20MetaP%200..1>[MetaParamGroup],[ParamGroup]^-[MetaParamGroup],[HasMetaP],[AdditionalMetadata])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞MetaP](hasMetaP__MetaP.md)*  <sub>0..1</sub>  **[MetaParamGroup](MetaParamGroup.md)**

## Attributes


### Own

 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description of the instance.
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..\*</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)
 * [➞label](metaParamGroup__label.md)  <sub>0..1</sub>
     * Description: A label string.
     * Range: [String](types/String.md)
 * [➞additional_metadata](metaParamGroup__additional_metadata.md)  <sub>0..\*</sub>
     * Description: Additional metadata or annotations for the instance.
     * Range: [AdditionalMetadata](AdditionalMetadata.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:MetaP |
