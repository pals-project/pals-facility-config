
# Class: RFParamGroup

Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:RFParamGroup](https://pals-project.readthedocs.io/RFParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[HasRFP]++-%20RFP%200..1>[RFParamGroup&#124;frequency:float%20%3F;harmon:integer%20%3F;voltage:float%20%3F;phase:float%20%3F;multipass_phase:float%20%3F;cavity_type:CavityTypeEnum%20%3F;num_cells:integer%20%3F;zero_phase:ZeroPhaseEnum%20%3F;L_active:float%20%3F;dE_ref:float%20%3F;id(i):string],[ParamGroup]^-[RFParamGroup],[ParamGroup],[HasRFP])](https://yuml.me/diagram/nofunky;dir:TB/class/[HasRFP]++-%20RFP%200..1>[RFParamGroup&#124;frequency:float%20%3F;harmon:integer%20%3F;voltage:float%20%3F;phase:float%20%3F;multipass_phase:float%20%3F;cavity_type:CavityTypeEnum%20%3F;num_cells:integer%20%3F;zero_phase:ZeroPhaseEnum%20%3F;L_active:float%20%3F;dE_ref:float%20%3F;id(i):string],[ParamGroup]^-[RFParamGroup],[ParamGroup],[HasRFP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞RFP](hasRFP__RFP.md)*  <sub>0..1</sub>  **[RFParamGroup](RFParamGroup.md)**

## Attributes


### Own

 * [➞frequency](rFParamGroup__frequency.md)  <sub>0..1</sub>
     * Description: RF frequency.
     * Range: [Float](types/Float.md)
 * [➞harmon](rFParamGroup__harmon.md)  <sub>0..1</sub>
     * Description: RF harmonic number.
     * Range: [Integer](types/Integer.md)
 * [➞voltage](rFParamGroup__voltage.md)  <sub>0..1</sub>
     * Description: RF voltage.
     * Range: [Float](types/Float.md)
 * [➞phase](rFParamGroup__phase.md)  <sub>0..1</sub>
     * Description: RF phase. rad/2pi RF phase in 0 to 2*pi
     * Range: [Float](types/Float.md)
 * [➞multipass_phase](rFParamGroup__multipass_phase.md)  <sub>0..1</sub>
     * Description: rad/2pi RF Phase added to multipass elements
     * Range: [Float](types/Float.md)
 * [➞cavity_type](rFParamGroup__cavity_type.md)  <sub>0..1</sub>
     * Description: Cavity type
     * Range: [CavityTypeEnum](CavityTypeEnum.md)
 * [➞num_cells](rFParamGroup__num_cells.md)  <sub>0..1</sub>
     * Description: Number of cells in the cavity
     * Range: [Integer](types/Integer.md)
 * [➞zero_phase](rFParamGroup__zero_phase.md)  <sub>0..1</sub>
     * Description: Sets what phase = 0 means.
     * Range: [ZeroPhaseEnum](ZeroPhaseEnum.md)
 * [➞L_active](rFParamGroup__L_active.md)  <sub>0..1</sub>
     * Description: Active acceleration length.
     * Range: [Float](types/Float.md)
 * [➞dE_ref](rFParamGroup__dE_ref.md)  <sub>0..1</sub>
     * Description: Reference energy gain.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:RFP |
