package None;

import java.util.List;
import lombok.*;






/**
  Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Signal extends NamedThing {

  private String role;
  private String dataType;
  private String units;
  private String unitsUri;

}