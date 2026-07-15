
# Class: NormalConductingRFCavity

A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.

URI: [narad:NormalConductingRFCavity](https://example.org/narad/NormalConductingRFCavity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RFCavity],[RFCavity]^-[NormalConductingRFCavity&#124;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[MultipoleComponent],[MetadataEntry],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[RFCavity],[RFCavity]^-[NormalConductingRFCavity&#124;species_ref(i):string%20%3F;pc_ref(i):float%20%3F;E_tot_ref(i):float%20%3F;time_ref(i):float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;alpha_a(i):float%20%3F;alpha_b(i):float%20%3F;beta_a(i):float%20%3F;beta_b(i):float%20%3F;eta_x(i):float%20%3F;eta_y(i):float%20%3F;etap_x(i):float%20%3F;etap_y(i):float%20%3F;phi_a(i):float%20%3F;phi_b(i):float%20%3F;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[MultipoleComponent],[MetadataEntry],[Component])

## Parents

 *  is_a: [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.

## Attributes


### Inherited from RFCavity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [Component](Component.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞functions](physicalComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the physical component,  which can be used to identify the component across different source systems.
     * Range: [PhysicalFunctionEnum](PhysicalFunctionEnum.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:RFCavity |
