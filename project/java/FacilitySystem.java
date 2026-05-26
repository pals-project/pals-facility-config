package None;

import java.util.List;
import lombok.*;






/**
  Facility-specific signal binding configuration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FacilitySystem extends System {

  private ControlSystem hasControlSystem;
  private List<Device> hostsDevice;

}