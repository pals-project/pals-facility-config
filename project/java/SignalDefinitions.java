package None;

import java.util.List;
import lombok.*;






/**
  Signal binding set scoped to a device type or device domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SignalDefinitions extends NamedThing {

  private String deviceType;
  private List<SignalBinding> signalBindings;

}