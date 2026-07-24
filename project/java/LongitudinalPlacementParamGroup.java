package None;

import java.util.List;
import lombok.*;






/**
  Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. 
Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
One (or both) `length` or `s_position` must be present.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LongitudinalPlacementParamGroup  {

  private Float length;
  private Float sPosition;

}