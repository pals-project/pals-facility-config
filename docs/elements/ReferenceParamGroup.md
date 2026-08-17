
# Class: ReferenceParamGroup

Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:ReferenceParamGroup](https://pals-project.readthedocs.io/ReferenceParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[HasReferenceP]++-%20ReferenceP%200..1>[ReferenceParamGroup&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F;id(i):string],[ParamGroup]^-[ReferenceParamGroup],[ParamGroup],[HasReferenceP])](https://yuml.me/diagram/nofunky;dir:TB/class/[HasReferenceP]++-%20ReferenceP%200..1>[ReferenceParamGroup&#124;species_ref:string%20%3F;pc_ref:float%20%3F;E_tot_ref:float%20%3F;time_ref:float%20%3F;id(i):string],[ParamGroup]^-[ReferenceParamGroup],[ParamGroup],[HasReferenceP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞ReferenceP](hasReferenceP__ReferenceP.md)*  <sub>0..1</sub>  **[ReferenceParamGroup](ReferenceParamGroup.md)**

## Attributes


### Own

 * [➞species_ref](referenceParamGroup__species_ref.md)  <sub>0..1</sub>
     * Description: A reference to a species or particle type, such as an ion, electron, or proton.
     * Range: [String](types/String.md)
 * [➞pc_ref](referenceParamGroup__pc_ref.md)  <sub>0..1</sub>
     * Description: [momentum*c] Reference momentum times speed of light.
     * Range: [Float](types/Float.md)
 * [➞E_tot_ref](referenceParamGroup__E_tot_ref.md)  <sub>0..1</sub>
     * Description: [eV] Reference total energy
     * Range: [Float](types/Float.md)
 * [➞time_ref](referenceParamGroup__time_ref.md)  <sub>0..1</sub>
     * Description: [s] Reference time
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:ReferenceP |
