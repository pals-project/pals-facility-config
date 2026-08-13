
# Class: Kicker

A magnet primarily used to steer the beam.
Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. 
Only one of the electric or magnetic multipole components should be present, not both.

URI: [pals:Kicker](https://pals-project.readthedocs.io/Kicker)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[MetaParamGroup],[MagneticMultipoleParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[Kicker&#124;plane:PlaneEnum%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasElectricMultipoleP],[Kicker]uses%20-.->[HasMagneticMultipoleP],[Kicker]^-[ACKicker],[Magnet]^-[Kicker],[HasMagneticMultipoleP],[HasElectricMultipoleP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[ACKicker])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[MetaParamGroup],[MagneticMultipoleParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[Kicker&#124;plane:PlaneEnum%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasElectricMultipoleP],[Kicker]uses%20-.->[HasMagneticMultipoleP],[Kicker]^-[ACKicker],[Magnet]^-[Kicker],[HasMagneticMultipoleP],[HasElectricMultipoleP],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[ACKicker])

## Parents

 *  is_a: [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.

## Uses Mixin

 *  mixin: [HasElectricMultipoleP](HasElectricMultipoleP.md)
 *  mixin: [HasMagneticMultipoleP](HasMagneticMultipoleP.md)

## Children

 * [ACKicker](ACKicker.md) - An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.

## Referenced by Class


## Attributes


### Own

 * [➞plane](kicker__plane.md)  <sub>0..1</sub>
     * Description: The transverse plane in which the kicker operates, either horizontal or vertical.
     * Range: [PlaneEnum](PlaneEnum.md)

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
| **Aliases:** | | Corrector |
|  | | HCorrector |
|  | | VCorrector |
|  | | VDiagKicker |
|  | | HDiagKicker |
| **Broad Mappings:** | | pals:Kicker |
