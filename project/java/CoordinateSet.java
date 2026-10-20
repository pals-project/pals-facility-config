package None;

import java.util.List;
import lombok.*;






/**
  A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CoordinateSet  {

  private String coordinateSystem;
  private Float xCoord;
  private Float yCoord;
  private Float zCoord;
  private Float rCoord;
  private Float thetaCoord;
  private Float phiCoord;

}