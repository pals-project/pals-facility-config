
# Class: Magnet

An accelerator device that produces a magnetic field for beam control.

URI: [pals:Magnet](https://pals-project.readthedocs.io/Magnet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[Solenoid],[ReferenceParamGroup],[PhysicalComponent],[Multipole],[MetaParamGroup],[Magnet&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasReferenceP],[Magnet]uses%20-.->[HasBodyShiftP],[Magnet]uses%20-.->[HasTwissP],[Magnet]^-[Solenoid],[Magnet]^-[Multipole],[Magnet]^-[Kicker],[PhysicalComponent]^-[Magnet],[LongitudinalPlacementParamGroup],[Kicker],[HasTwissP],[HasReferenceP],[HasBodyShiftP],[FloorParamGroup],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[Solenoid],[ReferenceParamGroup],[PhysicalComponent],[Multipole],[MetaParamGroup],[Magnet&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasReferenceP],[Magnet]uses%20-.->[HasBodyShiftP],[Magnet]uses%20-.->[HasTwissP],[Magnet]^-[Solenoid],[Magnet]^-[Multipole],[Magnet]^-[Kicker],[PhysicalComponent]^-[Magnet],[LongitudinalPlacementParamGroup],[Kicker],[HasTwissP],[HasReferenceP],[HasBodyShiftP],[FloorParamGroup],[BodyShiftParamGroup])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Uses Mixin

 *  mixin: [HasReferenceP](HasReferenceP.md)
 *  mixin: [HasBodyShiftP](HasBodyShiftP.md)
 *  mixin: [HasTwissP](HasTwissP.md)

## Children

 * [Kicker](Kicker.md) - A magnet primarily used to steer the beam.
 * [Multipole](Multipole.md) - A general magnet with a higher-order multipole field, such as a sextupole or octupole.
 * [Solenoid](Solenoid.md) - A magnet with a primarily longitudinal magnetic field used for focusing.

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

### Mixed in from HasBodyShiftP:

 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BodyShiftParamGroup](BodyShiftParamGroup.md)

### Mixed in from HasTwissP:

 * [➞TwissP](hasTwissP__TwissP.md)  <sub>0..1</sub>
     * Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [TwissParamGroup](TwissParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
