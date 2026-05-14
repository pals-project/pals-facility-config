package None;

import java.util.List;
import lombok.*;






/**
  Top-level NARAD document container.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NaradModel  {

  private NaradConfig naradConfig;
  private List<Beamline> beamlines;
  private List<BeamlineElement> elements;

}