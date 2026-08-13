package None;

import java.util.List;
import lombok.*;






/**
  A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasConnectingBranch extends ComponentRelation {

  private BeamLine beamlineContext;

}