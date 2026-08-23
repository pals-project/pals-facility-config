package None;

import java.util.List;
import lombok.*;






/**
  Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BeginningEle extends BookkeepingComponent {

  private ReferenceParamGroup referenceP;
  private TwissParamGroup twissP;

}