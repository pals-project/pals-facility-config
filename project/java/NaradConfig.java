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
  private DeployedSystem deployedSystem;
  private ControlSystem controlSystem;
  private List<Capability> capabilityLayer;
  private List<Device> deviceLayer;
  private SignalLayer signalLayer;

}