package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Precedes extends ComponentRelation {

  private BeamLine beamlineContext;

}