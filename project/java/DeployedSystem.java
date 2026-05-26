package None;

import java.util.List;
import lombok.*;






/**
  A deployed system, with an identified facility, that is the subject of a NARAD configuration.  This is the child of the target of the narad_config.deployed_system slot. In the SSN graph a DeployedSystem is a broad mapping to the ssn:Deployment and also is equivalent to the signal_layers.facilities entries.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DeployedSystem extends System {

  private List<FacilityIdentifier> facilityIdentifier;
  private ControlSystem hasControlSystem;

}