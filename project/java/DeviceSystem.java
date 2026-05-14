package None;

import java.util.List;
import lombok.*;






/**
  A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph a DeviceSystem is a subsystem of the Facility and a sibling to the ControlSystem.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DeviceSystem extends System {

  private String deviceType;
  private System subclassOf;

}