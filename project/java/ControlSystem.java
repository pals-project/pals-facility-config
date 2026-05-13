package None;

import java.util.List;
import lombok.*;






/**
  A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlSystem extends System {

  private String namingConvention;

}