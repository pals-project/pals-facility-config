package None;

import java.util.List;
import lombok.*;






/**
  A cavity used for RF acceleration or longitudinal manipulation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class RFCavity extends Cavity {

  private RFParamGroup rFP;

}