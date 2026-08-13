
# Class: ParamGroup

Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

URI: [pals:ParamGroup](https://pals-project.readthedocs.io/ParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SolenoidParamGroup],[ReferenceParamGroup],[RFParamGroup],[ParamGroup&#124;id:string]^-[TwissParamGroup],[ParamGroup]^-[SolenoidParamGroup],[ParamGroup]^-[ReferenceParamGroup],[ParamGroup]^-[RFParamGroup],[ParamGroup]^-[MetaParamGroup],[ParamGroup]^-[MagneticMultipoleParamGroup],[ParamGroup]^-[LongitudinalPlacementParamGroup],[ParamGroup]^-[FloorParamGroup],[ParamGroup]^-[ElectricMultipoleParamGroup],[ParamGroup]^-[BodyShiftParamGroup],[ParamGroup]^-[BendParamGroup],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[BendParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SolenoidParamGroup],[ReferenceParamGroup],[RFParamGroup],[ParamGroup&#124;id:string]^-[TwissParamGroup],[ParamGroup]^-[SolenoidParamGroup],[ParamGroup]^-[ReferenceParamGroup],[ParamGroup]^-[RFParamGroup],[ParamGroup]^-[MetaParamGroup],[ParamGroup]^-[MagneticMultipoleParamGroup],[ParamGroup]^-[LongitudinalPlacementParamGroup],[ParamGroup]^-[FloorParamGroup],[ParamGroup]^-[ElectricMultipoleParamGroup],[ParamGroup]^-[BodyShiftParamGroup],[ParamGroup]^-[BendParamGroup],[MetaParamGroup],[MagneticMultipoleParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[ElectricMultipoleParamGroup],[BodyShiftParamGroup],[BendParamGroup])

## Children

 * [BendParamGroup](BendParamGroup.md) - Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
 * [BodyShiftParamGroup](BodyShiftParamGroup.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md) - Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
 * [FloorParamGroup](FloorParamGroup.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md) - Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present.
 * [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) - Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
 * [MetaParamGroup](MetaParamGroup.md) - Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [RFParamGroup](RFParamGroup.md) - Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
 * [ReferenceParamGroup](ReferenceParamGroup.md) - Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [SolenoidParamGroup](SolenoidParamGroup.md) - Mixin for solenoid-specific parameters.
 * [TwissParamGroup](TwissParamGroup.md) - Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
