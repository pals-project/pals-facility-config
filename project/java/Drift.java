package None;

import java.util.List;
import lombok.*;






/**
  A field-free space between beamline components. A Drift is a virtual beamline component whose longitudinal extent preserves the separation between adjacent physical or virtual components.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Drift extends VirtualComponent {

  private LongitudinalPlacementParamGroup longitudinalPlacementP;

}