
# Class: AdditionalMetadata

A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.

URI: [pals:AdditionalMetadata](https://pals-project.readthedocs.io/AdditionalMetadata)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup]++-%20additional_metadata%200..*>[AdditionalMetadata&#124;key:string;value:string;datatype:DataTypeEnum%20%3F],[MetaParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup]++-%20additional_metadata%200..*>[AdditionalMetadata&#124;key:string;value:string;datatype:DataTypeEnum%20%3F],[MetaParamGroup])

## Referenced by Class

 *  **None** *[➞additional_metadata](metaParamGroup__additional_metadata.md)*  <sub>0..\*</sub>  **[AdditionalMetadata](AdditionalMetadata.md)**

## Attributes


### Own

 * [➞key](additionalMetadata__key.md)  <sub>1..1</sub>
     * Description: The metadata field name.
     * Range: [String](types/String.md)
 * [➞value](additionalMetadata__value.md)  <sub>1..1</sub>
     * Description: The metadata value, serialized as a string.
     * Range: [String](types/String.md)
 * [➞datatype](additionalMetadata__datatype.md)  <sub>0..1</sub>
     * Description: Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string.
     * Range: [DataTypeEnum](DataTypeEnum.md)
