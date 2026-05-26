package None;

import java.util.List;
import lombok.*;






/**
  A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph a Device is a subsystem of the Facility and a sibling to the ControlSystem. Also used in the SignalLayer to group signal bindings by device type. Aligned to ssn:System.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Device extends System {

  private String deviceType;
  private System subclassOf;
  private List<SignalBinding> isObservedBy;

}