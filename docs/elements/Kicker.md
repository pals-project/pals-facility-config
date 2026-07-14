
# Class: Kicker

A magnet primarily used to steer the beam.
Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. 
Only one of the electric or magnetic multipole components should be present, not both.

URI: [narad:Kicker](https://example.org/narad/Kicker)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MetadataEntry],[MagneticMultipoleP],[Magnet],[Kicker&#124;plane:PlaneEnum%20%3F;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[ElectricMultipoleP],[Kicker]uses%20-.->[MagneticMultipoleP],[Kicker]^-[ACKicker],[Magnet]^-[Kicker],[ElectricMultipoleP],[ACKicker])](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MetadataEntry],[MagneticMultipoleP],[Magnet],[Kicker&#124;plane:PlaneEnum%20%3F;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[ElectricMultipoleP],[Kicker]uses%20-.->[MagneticMultipoleP],[Kicker]^-[ACKicker],[Magnet]^-[Kicker],[ElectricMultipoleP],[ACKicker])

## Parents

 *  is_a: [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.

## Uses Mixin

 *  mixin: [ElectricMultipoleP](ElectricMultipoleP.md) - Mixin for electric multipole parameters,
 *  mixin: [MagneticMultipoleP](MagneticMultipoleP.md) - Mixin for magnetic multipole parameters,

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

### Mixed in from ElectricMultipoleP:

 * [➞components](electricMultipoleP__components.md)  <sub>0..\*</sub>
     * Description: Electric multipole components, one per order N.
     * Range: [MultipoleComponent](MultipoleComponent.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Corrector |
|  | | HCorrector |
|  | | VCorrector |
|  | | VDiagKicker |
|  | | HDiagKicker |
| **Broad Mappings:** | | pals:Kicker |
