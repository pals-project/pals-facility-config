
# Class: Affiliation

Contains affiliation information for an author or component, such as a ROR.

URI: [pals:Affiliation](https://pals-project.readthedocs.io/Affiliation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Identifier],[Identifier]<identifiers%200..*-++[Affiliation&#124;id:string;name:string%20%3F],[PALSAccelerator]++-%20affiliation%200..1>[Affiliation],[Author]++-%20affiliation%200..1>[Affiliation],[PALSAccelerator],[Author])](https://yuml.me/diagram/nofunky;dir:TB/class/[Identifier],[Identifier]<identifiers%200..*-++[Affiliation&#124;id:string;name:string%20%3F],[PALSAccelerator]++-%20affiliation%200..1>[Affiliation],[Author]++-%20affiliation%200..1>[Affiliation],[PALSAccelerator],[Author])

## Referenced by Class

 *  **None** *[affiliation](affiliation.md)*  <sub>0..1</sub>  **[Affiliation](Affiliation.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: The name of the entity. For example, the name of the person or organization.
     * Range: [String](types/String.md)
 * [identifiers](identifiers.md)  <sub>0..\*</sub>
     * Description: A unique and ideally persistent identifier for the facility, such as a DOI or ROR.
     * Range: [Identifier](Identifier.md)
