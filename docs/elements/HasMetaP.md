
# Class: HasMetaP



URI: [pals:HasMetaP](https://pals-project.readthedocs.io/HasMetaP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup],[MetaParamGroup]<MetaP%200..1-++[HasMetaP],[Signal]uses%20-.->[HasMetaP],[Component]uses%20-.->[HasMetaP],[Signal],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup],[MetaParamGroup]<MetaP%200..1-++[HasMetaP],[Signal]uses%20-.->[HasMetaP],[Component]uses%20-.->[HasMetaP],[Signal],[Component])

## Mixin for

 * [Component](Component.md) (mixin)  - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
 * [Signal](Signal.md) (mixin)  - Semantic meaning of a control-system signal associated with a component.

## Referenced by Class


## Attributes


### Own

 * [➞MetaP](hasMetaP__MetaP.md)  <sub>0..1</sub>
     * Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [MetaParamGroup](MetaParamGroup.md)
