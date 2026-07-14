
# Class: Cavity

A cavity used for beam acceleration or manipulation.

URI: [narad:Cavity](https://example.org/narad/Cavity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissP],[ReferenceP],[RFCavity],[PhysicalComponent],[MultipoleComponent],[MetadataEntry],[MagneticMultipoleP],[ElectricMultipoleP],[CrabCavity],[Cavity&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[ReferenceP],[Cavity]uses%20-.->[ElectricMultipoleP],[Cavity]uses%20-.->[MagneticMultipoleP],[Cavity]uses%20-.->[BodyShiftP],[Cavity]uses%20-.->[TwissP],[Cavity]^-[RFCavity],[Cavity]^-[CrabCavity],[PhysicalComponent]^-[Cavity],[BodyShiftP])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissP],[ReferenceP],[RFCavity],[PhysicalComponent],[MultipoleComponent],[MetadataEntry],[MagneticMultipoleP],[ElectricMultipoleP],[CrabCavity],[Cavity&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[ReferenceP],[Cavity]uses%20-.->[ElectricMultipoleP],[Cavity]uses%20-.->[MagneticMultipoleP],[Cavity]uses%20-.->[BodyShiftP],[Cavity]uses%20-.->[TwissP],[Cavity]^-[RFCavity],[Cavity]^-[CrabCavity],[PhysicalComponent]^-[Cavity],[BodyShiftP])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Uses Mixin

 *  mixin: [ReferenceP](ReferenceP.md) - Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 *  mixin: [ElectricMultipoleP](ElectricMultipoleP.md) - Mixin for electric multipole parameters,
 *  mixin: [MagneticMultipoleP](MagneticMultipoleP.md) - Mixin for magnetic multipole parameters,
 *  mixin: [BodyShiftP](BodyShiftP.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 *  mixin: [TwissP](TwissP.md) - Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

## Children

 * [CrabCavity](CrabCavity.md) - A cavity used for transverse beam manipulation, such as crabbing or deflecting.
 * [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.

## Referenced by Class


## Attributes


### Inherited from PhysicalComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
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

### Mixed in from ReferenceP:

 * [➞species_ref](referenceP__species_ref.md)  <sub>0..1</sub>
     * Description: A reference to a species or particle type, such as an ion, electron, or proton.
     * Range: [String](types/String.md)

### Mixed in from ReferenceP:

 * [➞pc_ref](referenceP__pc_ref.md)  <sub>0..1</sub>
     * Description: [momentum*c] Reference momentum times speed of light.
     * Range: [Float](types/Float.md)

### Mixed in from ReferenceP:

 * [➞E_tot_ref](referenceP__E_tot_ref.md)  <sub>0..1</sub>
     * Description: [eV] Reference total energy
     * Range: [Float](types/Float.md)

### Mixed in from ReferenceP:

 * [➞time_ref](referenceP__time_ref.md)  <sub>0..1</sub>
     * Description: [s] Reference time
     * Range: [Float](types/Float.md)

### Mixed in from ElectricMultipoleP:

 * [➞components](electricMultipoleP__components.md)  <sub>0..\*</sub>
     * Description: Electric multipole components, one per order N.
     * Range: [MultipoleComponent](MultipoleComponent.md)

### Mixed in from BodyShiftP:

 * [➞x_offset](bodyShiftP__x_offset.md)  <sub>0..1</sub>
     * Description: Shift in the X direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_offset](bodyShiftP__y_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Y direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_offset](bodyShiftP__z_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Z direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞x_rot](bodyShiftP__x_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_rot](bodyShiftP__y_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_rot](bodyShiftP__z_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞alpha_a](twissP__alpha_a.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the horizontal plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞alpha_b](twissP__alpha_b.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the vertical plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞beta_a](twissP__beta_a.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the horizontal plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞beta_b](twissP__beta_b.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the vertical plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞eta_x](twissP__eta_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the horizontal plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞eta_y](twissP__eta_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the vertical plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞etap_x](twissP__etap_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the horizontal plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞etap_y](twissP__etap_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the vertical plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞phi_a](twissP__phi_a.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the horizontal plane.
     * Range: [Float](types/Float.md)

### Mixed in from TwissP:

 * [➞phi_b](twissP__phi_b.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the vertical plane.
     * Range: [Float](types/Float.md)
