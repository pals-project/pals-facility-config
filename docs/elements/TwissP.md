
# Class: TwissP

Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

URI: [narad:TwissP](https://example.org/narad/TwissP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Marker]uses%20-.->[TwissP&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F],[Magnet]uses%20-.->[TwissP],[Cavity]uses%20-.->[TwissP],[BeamPositionMonitor]uses%20-.->[TwissP],[Marker],[Magnet],[Cavity],[BeamPositionMonitor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Marker]uses%20-.->[TwissP&#124;alpha_a:float%20%3F;alpha_b:float%20%3F;beta_a:float%20%3F;beta_b:float%20%3F;eta_x:float%20%3F;eta_y:float%20%3F;etap_x:float%20%3F;etap_y:float%20%3F;phi_a:float%20%3F;phi_b:float%20%3F],[Magnet]uses%20-.->[TwissP],[Cavity]uses%20-.->[TwissP],[BeamPositionMonitor]uses%20-.->[TwissP],[Marker],[Magnet],[Cavity],[BeamPositionMonitor])

## Mixin for

 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.
 * [Marker](Marker.md) (mixin)  - A virtual component used as a reference point or marker in the beamline structure.

## Referenced by Class


## Attributes


### Own

 * [➞alpha_a](twissP__alpha_a.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞alpha_b](twissP__alpha_b.md)  <sub>0..1</sub>
     * Description: Twiss alpha parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞beta_a](twissP__beta_a.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞beta_b](twissP__beta_b.md)  <sub>0..1</sub>
     * Description: Twiss beta parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞eta_x](twissP__eta_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞eta_y](twissP__eta_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞etap_x](twissP__etap_x.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞etap_y](twissP__etap_y.md)  <sub>0..1</sub>
     * Description: Twiss dispersion slope parameter in the vertical plane.
     * Range: [Float](types/Float.md)
 * [➞phi_a](twissP__phi_a.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the horizontal plane.
     * Range: [Float](types/Float.md)
 * [➞phi_b](twissP__phi_b.md)  <sub>0..1</sub>
     * Description: Twiss phase advance parameter in the vertical plane.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:TwissP |
