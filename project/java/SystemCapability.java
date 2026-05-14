package None;

import java.util.List;
import lombok.*;






/**
  A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs. type-specific signals) is expressed in CapabilityProfile, not here.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemCapability extends NamedThing {

  private List<String> forProperty;
  private String deviceType;

}