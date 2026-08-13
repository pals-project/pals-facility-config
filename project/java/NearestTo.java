package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NearestTo extends ComponentRelation {

  private Float distanceValue;
  private String distanceUnit;
  private Float toleranceValue;
  private String toleranceUnit;
  private CoordinateSet coordinates;

}