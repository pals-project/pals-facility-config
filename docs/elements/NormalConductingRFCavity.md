
# Class: NormalConductingRFCavity

A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.

URI: [pals:NormalConductingRFCavity](https://pals-project.readthedocs.io/NormalConductingRFCavity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[RFParamGroup],[RFCavity],[RFCavity]^-[NormalConductingRFCavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[RFParamGroup],[RFCavity],[RFCavity]^-[NormalConductingRFCavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup])

## Parents

 *  is_a: [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.

## Attributes


### Inherited from RFCavity:

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
 * [➞functions](physicalComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the physical component,  which can be used to identify the component across different source systems.
     * Range: [PhysicalFunctionEnum](PhysicalFunctionEnum.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:RFCavity |
