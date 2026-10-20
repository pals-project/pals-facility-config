package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Overlaps extends ComponentRelation {

  private CoordinateSet coordinates;

}