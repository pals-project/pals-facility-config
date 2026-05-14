package None;

import java.util.List;
import lombok.*;






/**
  A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Beamline extends NamedThing {

  private boolean multipass;
  private Float length;
  private BeamlineElement zeroPoint;
  private boolean periodic;
  private List<BeamlineElement> line;

}