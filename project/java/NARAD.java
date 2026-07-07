package None;

import java.util.List;
import lombok.*;






/**
  Root container for accelerator core components, semantic signals, and local bindings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NARAD  {

  private String type;
  private String description;
  private List<PhysicalComponent> physicalComponents;
  private List<VirtualComponent> virtualComponents;
  private List<Beamline> beamlines;
  private List<SupportingFacilityComponent> supportingFacilityComponents;
  private List<Signal> signals;
  private List<SignalBinding> signalBindings;
  private List<ComponentRelation> componentRelations;

}