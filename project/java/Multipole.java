package None;

import java.util.List;
import lombok.*;






/**
  A general magnet with a higher-order multipole field, such as a sextupole or octupole.
Only one of the electric or magnetic multipole components should be present, not both.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Multipole extends Magnet {

  private List<MultipoleComponent> components;

}