package None;

import java.util.List;
import lombok.*;






/**
  A magnet primarily used to steer the beam.
Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. 
Only one of the electric or magnetic multipole components should be present, not both.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Kicker extends Magnet {

  private String plane;
  private List<MultipoleComponent> components;

}