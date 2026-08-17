
# Class: CoordinateSet

A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis.

URI: [pals:CoordinateSet](https://pals-project.readthedocs.io/CoordinateSet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AdjacentTo]++-%20coordinates%200..1>[CoordinateSet&#124;coordinate_system:CoordinateSystemEnum%20%3F;x_coord:float%20%3F;y_coord:float%20%3F;z_coord:float%20%3F;r_coord:float%20%3F;theta_coord:float%20%3F;phi_coord:float%20%3F],[Overlaps]++-%20coordinates%200..1>[CoordinateSet],[MountedOn]++-%20coordinates%200..1>[CoordinateSet],[NearestTo]++-%20coordinates%200..1>[CoordinateSet],[Overlaps],[NearestTo],[MountedOn],[AdjacentTo])](https://yuml.me/diagram/nofunky;dir:TB/class/[AdjacentTo]++-%20coordinates%200..1>[CoordinateSet&#124;coordinate_system:CoordinateSystemEnum%20%3F;x_coord:float%20%3F;y_coord:float%20%3F;z_coord:float%20%3F;r_coord:float%20%3F;theta_coord:float%20%3F;phi_coord:float%20%3F],[Overlaps]++-%20coordinates%200..1>[CoordinateSet],[MountedOn]++-%20coordinates%200..1>[CoordinateSet],[NearestTo]++-%20coordinates%200..1>[CoordinateSet],[Overlaps],[NearestTo],[MountedOn],[AdjacentTo])

## Referenced by Class

 *  **None** *[coordinates](coordinates.md)*  <sub>0..1</sub>  **[CoordinateSet](CoordinateSet.md)**

## Attributes


### Own

 * [➞coordinate_system](coordinateSet__coordinate_system.md)  <sub>0..1</sub>
     * Description: The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical).
     * Range: [CoordinateSystemEnum](CoordinateSystemEnum.md)
 * [➞x_coord](coordinateSet__x_coord.md)  <sub>0..1</sub>
     * Description: The x-coordinate in the specified coordinate system.
     * Range: [Float](types/Float.md)
 * [➞y_coord](coordinateSet__y_coord.md)  <sub>0..1</sub>
     * Description: The y-coordinate in the specified coordinate system.
     * Range: [Float](types/Float.md)
 * [➞z_coord](coordinateSet__z_coord.md)  <sub>0..1</sub>
     * Description: The z-coordinate in the specified coordinate system.
     * Range: [Float](types/Float.md)
 * [➞r_coord](coordinateSet__r_coord.md)  <sub>0..1</sub>
     * Description: The radial distance in cylindrical coordinates.
     * Range: [Float](types/Float.md)
 * [➞theta_coord](coordinateSet__theta_coord.md)  <sub>0..1</sub>
     * Description: The angular coordinate in cylindrical coordinates (in radians).
     * Range: [Float](types/Float.md)
 * [➞phi_coord](coordinateSet__phi_coord.md)  <sub>0..1</sub>
     * Description: The azimuthal angle in spherical coordinates (in radians).
     * Range: [Float](types/Float.md)
