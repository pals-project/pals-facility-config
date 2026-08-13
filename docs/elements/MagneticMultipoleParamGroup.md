
# Class: MagneticMultipoleParamGroup

Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
  tilt: 0.7
- order: 3
  Bn: 27.3
- order: 2
  BnL: 3.47e1
- order: 1
  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
```

URI: [pals:MagneticMultipoleParamGroup](https://pals-project.readthedocs.io/MagneticMultipoleParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[MultipoleParameterGroup],[MultipoleParameterGroup]<mag_components%200..*-++[MagneticMultipoleParamGroup&#124;id(i):string],[HasMagneticMultipoleP]++-%20MagneticMultipoleP%200..1>[MagneticMultipoleParamGroup],[ParamGroup]^-[MagneticMultipoleParamGroup],[HasMagneticMultipoleP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[MultipoleParameterGroup],[MultipoleParameterGroup]<mag_components%200..*-++[MagneticMultipoleParamGroup&#124;id(i):string],[HasMagneticMultipoleP]++-%20MagneticMultipoleP%200..1>[MagneticMultipoleParamGroup],[ParamGroup]^-[MagneticMultipoleParamGroup],[HasMagneticMultipoleP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞MagneticMultipoleP](hasMagneticMultipoleP__MagneticMultipoleP.md)*  <sub>0..1</sub>  **[MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md)**

## Attributes


### Own

 * [➞mag_components](magneticMultipoleParamGroup__mag_components.md)  <sub>0..\*</sub>
     * Description: Magnetic multipole components, one per order N.
     * Range: [MultipoleParameterGroup](MultipoleParameterGroup.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:MagneticMultipoleP |
