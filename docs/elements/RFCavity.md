
# Class: RFCavity

A cavity used for RF acceleration or longitudinal manipulation.

URI: [pals:RFCavity](https://pals-project.readthedocs.io/RFCavity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SuperConductingRFCavity],[ReferenceParamGroup],[RFParamGroup],[RFCavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasRFP],[RFCavity]^-[SuperConductingRFCavity],[RFCavity]^-[NormalConductingRFCavity],[Cavity]^-[RFCavity],[NormalConductingRFCavity],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasRFP],[FloorParamGroup],[ElectricMultipoleParamGroup],[Cavity],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SuperConductingRFCavity],[ReferenceParamGroup],[RFParamGroup],[RFCavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasRFP],[RFCavity]^-[SuperConductingRFCavity],[RFCavity]^-[NormalConductingRFCavity],[Cavity]^-[RFCavity],[NormalConductingRFCavity],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasRFP],[FloorParamGroup],[ElectricMultipoleParamGroup],[Cavity],[BodyShiftParamGroup])

## Parents

 *  is_a: [Cavity](Cavity.md) - A cavity used for beam acceleration or manipulation.

## Uses Mixin

 *  mixin: [HasRFP](HasRFP.md)

## Children

 * [NormalConductingRFCavity](NormalConductingRFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
 * [SuperConductingRFCavity](SuperConductingRFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.

## Referenced by Class


## Attributes


### Inherited from Cavity:

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

### Mixed in from HasRFP:

 * [➞RFP](hasRFP__RFP.md)  <sub>0..1</sub>
     * Description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [RFParamGroup](RFParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:RFCavity |
