
# Class: Solenoid

A magnet with a primarily longitudinal magnetic field used for focusing.
A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis.

URI: [narad:Solenoid](https://example.org/narad/Solenoid)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SolenoidP],[Solenoid&#124;Ksol:float%20%3F;Bsol:float%20%3F;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[SolenoidP],[Magnet]^-[Solenoid],[MetadataEntry],[Magnet])](https://yuml.me/diagram/nofunky;dir:TB/class/[SolenoidP],[Solenoid&#124;Ksol:float%20%3F;Bsol:float%20%3F;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[SolenoidP],[Magnet]^-[Solenoid],[MetadataEntry],[Magnet])

## Parents

 *  is_a: [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.

## Uses Mixin

 *  mixin: [SolenoidP](SolenoidP.md) - Mixin for solenoid-specific parameters.

## Attributes


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

### Mixed in from SolenoidP:

 * [➞Ksol](solenoidP__Ksol.md)  <sub>0..1</sub>
     * Description: Normalized solenoid strength.
     * Range: [Float](types/Float.md)

### Mixed in from SolenoidP:

 * [➞Bsol](solenoidP__Bsol.md)  <sub>0..1</sub>
     * Description: Solenoid field.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:Solenoid |
