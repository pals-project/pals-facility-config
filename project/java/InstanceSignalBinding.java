package None;

import java.util.List;
import lombok.*;






/**
  A facility-specific binding between a NARAD Signal and an implementation interface (e.g. an EPICS process variable). Modeled as sosa:Sensor because it describes how a signal is observed, monitored, or actuated. ssn:forProperty → Signal; narad:isInstanceOf → the capability class.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InstanceSignalBinding extends NamedThing {

  private String pvName;
  private String isInstanceOf;
  private String forProperty;
  private String isHostedBy;
  private String isPropertyOf;

}