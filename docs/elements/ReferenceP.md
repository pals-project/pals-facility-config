
# Class: ReferenceP

Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [narad:ReferenceP](https://example.org/narad/ReferenceP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Magnet]uses%20-.->[ReferenceP&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F],[Cavity]uses%20-.->[ReferenceP],[BeamPositionMonitor]uses%20-.->[ReferenceP],[Magnet],[Cavity],[BeamPositionMonitor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Magnet]uses%20-.->[ReferenceP&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F],[Cavity]uses%20-.->[ReferenceP],[BeamPositionMonitor]uses%20-.->[ReferenceP],[Magnet],[Cavity],[BeamPositionMonitor])

## Mixin for

 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.

## Referenced by Class


## Attributes


### Own

 * [➞species_ref](referenceP__species_ref.md)  <sub>0..1</sub>
     * Description: A reference to a species or particle type, such as an ion, electron, or proton.
     * Range: [String](types/String.md)
 * [➞pc_ref](referenceP__pc_ref.md)  <sub>0..1</sub>
     * Description: [momentum*c] Reference momentum times speed of light.
     * Range: [Float](types/Float.md)
 * [➞E_tot_ref](referenceP__E_tot_ref.md)  <sub>0..1</sub>
     * Description: [eV] Reference total energy
     * Range: [Float](types/Float.md)
 * [➞time_ref](referenceP__time_ref.md)  <sub>0..1</sub>
     * Description: [s] Reference time
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:ReferenceP |
