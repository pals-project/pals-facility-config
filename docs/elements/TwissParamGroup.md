
# Class: TwissParamGroup

Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

URI: [pals:TwissParamGroup](https://pals-project.readthedocs.io/TwissParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[HasTwissP]++-%20TwissP%200..1>[TwissParamGroup&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;id(i):string],[ParamGroup]^-[TwissParamGroup],[ParamGroup],[HasTwissP])](https://yuml.me/diagram/nofunky;dir:TB/class/[HasTwissP]++-%20TwissP%200..1>[TwissParamGroup&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F;id(i):string],[ParamGroup]^-[TwissParamGroup],[ParamGroup],[HasTwissP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞TwissP](hasTwissP__TwissP.md)*  <sub>0..1</sub>  **[TwissParamGroup](TwissParamGroup.md)**

## Attributes


### Own

 * [➞alpha_a](twissParamGroup__alpha_a.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞alpha_b](twissParamGroup__alpha_b.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞beta_a](twissParamGroup__beta_a.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞beta_b](twissParamGroup__beta_b.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞eta_x](twissParamGroup__eta_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞eta_y](twissParamGroup__eta_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞etap_x](twissParamGroup__etap_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞etap_y](twissParamGroup__etap_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞phi_a](twissParamGroup__phi_a.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞phi_b](twissParamGroup__phi_b.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the vertical plane.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:TwissP |
