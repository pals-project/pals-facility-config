package None;

import java.util.List;
import lombok.*;






/**
  A virtual component used as a reference point or marker in the beamline structure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Marker extends BookkeepingComponent {

  private TwissParamGroup twissP;

}