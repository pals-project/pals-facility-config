
# Class: Marker

A virtual component used as a reference point or marker in the beamline structure.

URI: [narad:Marker](https://example.org/narad/Marker)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissP],[MetadataEntry],[Marker&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[TwissP],[BookkeepingComponent]^-[Marker],[BookkeepingComponent])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissP],[MetadataEntry],[Marker&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[TwissP],[BookkeepingComponent]^-[Marker],[BookkeepingComponent])

## Parents

 *  is_a: [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,

## Uses Mixin

 *  mixin: [TwissP](TwissP.md) - Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

## Attributes


### Inherited from BookkeepingComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞functions](virtualComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:Marker |
