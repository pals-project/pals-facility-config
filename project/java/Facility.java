package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A facility that houses one or more accelerators.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Facility  {

  private List<Identifier> identifiers;
  private List<Component> components;
  private List<BeamLine> beamlines;
  private List<Signal> signals;
  private List<SignalBinding> signalBindings;
  private List<ComponentRelation> componentRelations;

}