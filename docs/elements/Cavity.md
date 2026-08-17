
# Class: Cavity

A cavity used for beam acceleration or manipulation.

URI: [pals:Cavity](https://pals-project.readthedocs.io/Cavity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[RFCavity],[PhysicalComponent],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasTwissP],[HasReferenceP],[HasMagneticMultipoleP],[HasElectricMultipoleP],[HasBodyShiftP],[FloorParamGroup],[ElectricMultipoleParamGroup],[CrabCavity],[Cavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasReferenceP],[Cavity]uses%20-.->[HasElectricMultipoleP],[Cavity]uses%20-.->[HasMagneticMultipoleP],[Cavity]uses%20-.->[HasBodyShiftP],[Cavity]uses%20-.->[HasTwissP],[Cavity]^-[RFCavity],[Cavity]^-[CrabCavity],[PhysicalComponent]^-[Cavity],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[ReferenceParamGroup],[RFCavity],[PhysicalComponent],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[HasTwissP],[HasReferenceP],[HasMagneticMultipoleP],[HasElectricMultipoleP],[HasBodyShiftP],[FloorParamGroup],[ElectricMultipoleParamGroup],[CrabCavity],[Cavity&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasReferenceP],[Cavity]uses%20-.->[HasElectricMultipoleP],[Cavity]uses%20-.->[HasMagneticMultipoleP],[Cavity]uses%20-.->[HasBodyShiftP],[Cavity]uses%20-.->[HasTwissP],[Cavity]^-[RFCavity],[Cavity]^-[CrabCavity],[PhysicalComponent]^-[Cavity],[BodyShiftParamGroup])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Uses Mixin

 *  mixin: [HasReferenceP](HasReferenceP.md)
 *  mixin: [HasElectricMultipoleP](HasElectricMultipoleP.md)
 *  mixin: [HasMagneticMultipoleP](HasMagneticMultipoleP.md)
 *  mixin: [HasBodyShiftP](HasBodyShiftP.md)
 *  mixin: [HasTwissP](HasTwissP.md)

## Children

 * [CrabCavity](CrabCavity.md) - A cavity used for transverse beam manipulation, such as crabbing or deflecting.
 * [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.

## Referenced by Class


## Attributes


### Inherited from PhysicalComponent:

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

### Mixed in from HasReferenceP:

 * [➞ReferenceP](hasReferenceP__ReferenceP.md)  <sub>0..1</sub>
     * Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [ReferenceParamGroup](ReferenceParamGroup.md)

### Mixed in from HasElectricMultipoleP:

 * [➞ElectricMultipoleP](hasElectricMultipoleP__ElectricMultipoleP.md)  <sub>0..1</sub>
     * Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md)

### Mixed in from HasMagneticMultipoleP:

 * [➞MagneticMultipoleP](hasMagneticMultipoleP__MagneticMultipoleP.md)  <sub>0..1</sub>
     * Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md)

### Mixed in from HasBodyShiftP:

 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BodyShiftParamGroup](BodyShiftParamGroup.md)

### Mixed in from HasTwissP:

 * [➞TwissP](hasTwissP__TwissP.md)  <sub>0..1</sub>
     * Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [TwissParamGroup](TwissParamGroup.md)
