package None;

import java.util.List;
import lombok.*;






/**
  A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Beamline extends VirtualComponent {

  private boolean multipass;
  private Float length;
  private String zeroPoint;
  private boolean periodic;
  private Integer repeat;
  private Integer direction;

}