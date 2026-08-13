package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MountedOn extends ComponentRelation {

  private CoordinateSet coordinates;

}