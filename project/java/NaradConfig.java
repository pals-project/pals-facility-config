package None;

import java.util.List;
import lombok.*;






/**
  A top-level NARAD-system container for the: capability layer + signal layer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NaradConfig  {

  private String schemaVersion;
  private String intent;
  private FacilitySystem deployedSystem;
  private List<ControlSystem> hasSubSystem;
  private List<ControlCapability> controlCapabilityLayer;
  private List<DeviceSystem> deviceLayer;
  private SignalLayer signalLayer;

}