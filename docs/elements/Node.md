
# Class: Node

Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology.

URI: [pals:Node](https://pals-project.readthedocs.io/Node)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal],[Node&#124;id:string;kind:string;alias:string%20*]^-[Signal],[Node]^-[Component],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal],[Node&#124;id:string;kind:string;alias:string%20*]^-[Signal],[Node]^-[Component],[Component])

## Children

 * [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
 * [Signal](Signal.md) - Semantic meaning of a control-system signal associated with a component.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [kind](kind.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..\*</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)
