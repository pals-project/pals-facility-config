
# Class: Bend

Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.

URI: [pals:Bend](https://pals-project.readthedocs.io/Bend)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[Multipole],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasBendP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[BendParamGroup],[Bend&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasBendP],[Multipole]^-[Bend])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[Multipole],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasBendP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[BendParamGroup],[Bend&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasBendP],[Multipole]^-[Bend])

## Parents

 *  is_a: [Multipole](Multipole.md) - A general magnet with a higher-order multipole field, such as a sextupole or octupole.

## Uses Mixin

 *  mixin: [HasBendP](HasBendP.md)

## Attributes


### Inherited from Multipole:

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

### Mixed in from HasBendP:

 * [➞BendP](hasBendP__BendP.md)  <sub>0..1</sub>
     * Description: A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BendParamGroup](BendParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Dipole |
| **Exact Mappings:** | | pals:Bend |
