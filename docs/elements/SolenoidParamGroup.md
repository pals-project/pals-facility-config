
# Class: SolenoidParamGroup

Mixin for solenoid-specific parameters.

URI: [pals:SolenoidParamGroup](https://pals-project.readthedocs.io/SolenoidParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[HasSolenoidP]++-%20SolenoidP%200..1>[SolenoidParamGroup&#124;Ksol:float%20%3F;Bsol:float%20%3F;id(i):string],[ParamGroup]^-[SolenoidParamGroup],[ParamGroup],[HasSolenoidP])](https://yuml.me/diagram/nofunky;dir:TB/class/[HasSolenoidP]++-%20SolenoidP%200..1>[SolenoidParamGroup&#124;Ksol:float%20%3F;Bsol:float%20%3F;id(i):string],[ParamGroup]^-[SolenoidParamGroup],[ParamGroup],[HasSolenoidP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞SolenoidP](hasSolenoidP__SolenoidP.md)*  <sub>0..1</sub>  **[SolenoidParamGroup](SolenoidParamGroup.md)**

## Attributes


### Own

 * [➞Ksol](solenoidParamGroup__Ksol.md)  <sub>0..1</sub>
     * Description: Normalized solenoid strength.
     * Range: [Float](types/Float.md)
 * [➞Bsol](solenoidParamGroup__Bsol.md)  <sub>0..1</sub>
     * Description: Solenoid field.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:SolenoidP |
