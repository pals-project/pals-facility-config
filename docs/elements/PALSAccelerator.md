
# Class: PALSAccelerator

Root container for accelerator core components, semantic signals, and local bindings.

URI: [pals:PALSAccelerator](https://pals-project.readthedocs.io/PALSAccelerator)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Facility]<facility%200..1-++[PALSAccelerator&#124;kind:string;description:string%20%3F;version:string%20%3F;notes:string%20*],[Author]<authors%200..*-++[PALSAccelerator],[Affiliation]<affiliation%200..1-++[PALSAccelerator],[Facility],[Author],[Affiliation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Facility]<facility%200..1-++[PALSAccelerator&#124;kind:string;description:string%20%3F;version:string%20%3F;notes:string%20*],[Author]<authors%200..*-++[PALSAccelerator],[Affiliation]<affiliation%200..1-++[PALSAccelerator],[Facility],[Author],[Affiliation])

## Attributes


### Own

 * [kind](kind.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description of the instance.
     * Range: [String](types/String.md)
 * [affiliation](affiliation.md)  <sub>0..1</sub>
     * Description: The affiliation of the author or component, as a ROR.
     * Range: [Affiliation](Affiliation.md)
 * [➞version](pALSAccelerator__version.md)  <sub>0..1</sub>
     * Description: Version of the representation of a particle accelerator and its operations.
     * Range: [String](types/String.md)
 * [➞authors](pALSAccelerator__authors.md)  <sub>0..\*</sub>
     * Description: Contains the authorship information for this representation of an accelerator facility and its operations.
     * Range: [Author](Author.md)
 * [➞notes](pALSAccelerator__notes.md)  <sub>0..\*</sub>
     * Description: Additional notes or comments about the representation of a particle accelerator and its operations.
     * Range: [String](types/String.md)
 * [➞facility](pALSAccelerator__facility.md)  <sub>0..1</sub>
     * Description: A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc.
     * Range: [Facility](Facility.md)
