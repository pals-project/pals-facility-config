package None;

import java.util.List;
import lombok.*;






/**
  PALS element for an ordered sequence of beamline elements defining a beam path.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BeamLine extends VirtualComponent {

  private Float length;
  private String description;
  private boolean multipass;
  private boolean periodic;
  private Integer repeat;
  private Integer direction;

}