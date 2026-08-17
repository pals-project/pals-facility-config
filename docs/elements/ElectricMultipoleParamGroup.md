
# Class: ElectricMultipoleParamGroup

Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
  tilt: 0.7
- order: 3
  En: 27.3
- order: 2
  EnL: 3.47e1
```

URI: [pals:ElectricMultipoleParamGroup](https://pals-project.readthedocs.io/ElectricMultipoleParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[MultipoleParameterGroup],[MultipoleParameterGroup]<elec_components%200..*-++[ElectricMultipoleParamGroup&#124;id(i):string],[HasElectricMultipoleP]++-%20ElectricMultipoleP%200..1>[ElectricMultipoleParamGroup],[ParamGroup]^-[ElectricMultipoleParamGroup],[HasElectricMultipoleP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[MultipoleParameterGroup],[MultipoleParameterGroup]<elec_components%200..*-++[ElectricMultipoleParamGroup&#124;id(i):string],[HasElectricMultipoleP]++-%20ElectricMultipoleP%200..1>[ElectricMultipoleParamGroup],[ParamGroup]^-[ElectricMultipoleParamGroup],[HasElectricMultipoleP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞ElectricMultipoleP](hasElectricMultipoleP__ElectricMultipoleP.md)*  <sub>0..1</sub>  **[ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md)**

## Attributes


### Own

 * [➞elec_components](electricMultipoleParamGroup__elec_components.md)  <sub>0..\*</sub>
     * Description: Electric multipole components, one per order N.
     * Range: [MultipoleParameterGroup](MultipoleParameterGroup.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:ElectricMultipoleP |
| **Broad Mappings:** | | pals:ElectricMultipoleP |
