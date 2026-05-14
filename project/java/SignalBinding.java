package None;

import java.util.List;
import lombok.*;






/**
  A named control system suffix definition for one semantic signal. The suffix is used within in a template naming convention to construct the full control system PV name for a given device instance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SignalBinding extends NamedThing {

  private String controlSystemSuffix;

}