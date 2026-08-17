
# Class: Author

Contains authorship information for a representation of an accelerator facility and its operations.

URI: [pals:Author](https://pals-project.readthedocs.io/Author)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Affiliation]<affiliation%200..1-++[Author&#124;name:string%20%3F;email:string%20%3F;orcid:string%20%3F],[PALSAccelerator]++-%20authors%200..*>[Author],[PALSAccelerator],[Affiliation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Affiliation]<affiliation%200..1-++[Author&#124;name:string%20%3F;email:string%20%3F;orcid:string%20%3F],[PALSAccelerator]++-%20authors%200..*>[Author],[PALSAccelerator],[Affiliation])

## Referenced by Class

 *  **None** *[➞authors](pALSAccelerator__authors.md)*  <sub>0..\*</sub>  **[Author](Author.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name of the entity. For example, the name of the person or organization.
     * Range: [String](types/String.md)
 * [affiliation](affiliation.md)  <sub>0..1</sub>
     * Description: The affiliation of the author or component, as a ROR.
     * Range: [Affiliation](Affiliation.md)
 * [➞email](author__email.md)  <sub>0..1</sub>
     * Description: The email address of the author.
     * Range: [String](types/String.md)
 * [➞orcid](author__orcid.md)  <sub>0..1</sub>
     * Description: The ORCID identifier of the author.
     * Range: [String](types/String.md)
