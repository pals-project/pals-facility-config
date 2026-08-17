
# Class: Multipole

A general magnet with a higher-order multipole field, such as a sextupole or octupole.
Only one of the electric or magnetic multipole components should be present, not both.

URI: [pals:Multipole](https://pals-project.readthedocs.io/Multipole)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[Sextupole],[ReferenceParamGroup],[Quadrupole],[Octupole],[Multipole&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasElectricMultipoleP],[Multipole]uses%20-.->[HasMagneticMultipoleP],[Multipole]^-[Sextupole],[Multipole]^-[Quadrupole],[Multipole]^-[Octupole],[Multipole]^-[Bend],[Magnet]^-[Multipole],[MetaParamGroup],[MagneticMultipoleParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasMagneticMultipoleP],[HasElectricMultipoleP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[Bend])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[Sextupole],[ReferenceParamGroup],[Quadrupole],[Octupole],[Multipole&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasElectricMultipoleP],[Multipole]uses%20-.->[HasMagneticMultipoleP],[Multipole]^-[Sextupole],[Multipole]^-[Quadrupole],[Multipole]^-[Octupole],[Multipole]^-[Bend],[Magnet]^-[Multipole],[MetaParamGroup],[MagneticMultipoleParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasMagneticMultipoleP],[HasElectricMultipoleP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[Bend])

## Parents

 *  is_a: [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.

## Uses Mixin

 *  mixin: [HasElectricMultipoleP](HasElectricMultipoleP.md)
 *  mixin: [HasMagneticMultipoleP](HasMagneticMultipoleP.md)

## Children

 * [Bend](Bend.md) - Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
 * [Octupole](Octupole.md) - A magnet primarily used to focus or defocus the beam. 8 poles.
 * [Quadrupole](Quadrupole.md) - A magnet primarily used to focus or defocus the beam. 4 poles.
 * [Sextupole](Sextupole.md) - A magnet primarily used to focus or defocus the beam. 6 poles.

## Referenced by Class


## Attributes


### Inherited from Magnet:

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

### Mixed in from HasElectricMultipoleP:

 * [➞ElectricMultipoleP](hasElectricMultipoleP__ElectricMultipoleP.md)  <sub>0..1</sub>
     * Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md)

### Mixed in from HasMagneticMultipoleP:

 * [➞MagneticMultipoleP](hasMagneticMultipoleP__MagneticMultipoleP.md)  <sub>0..1</sub>
     * Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Multipole |
