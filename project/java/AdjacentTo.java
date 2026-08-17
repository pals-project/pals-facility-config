package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component is adjacent to the object component and not overlapping
 in a specified context, such as radiation detector and a magnet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AdjacentTo extends ComponentRelation {

  private Float distanceValue;
  private String distanceUnit;
  private Float toleranceValue;
  private String toleranceUnit;
  private CoordinateSet coordinates;

}