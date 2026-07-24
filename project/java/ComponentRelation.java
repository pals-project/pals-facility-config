package None;

import java.util.List;
import lombok.*;






/**
  Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentRelation extends Relationship {

  private String context;
  private BeamLine beamlineContext;
  private String referenceFrame;
  private Float distanceValue;
  private String distanceUnit;
  private String axis;
  private String componentDirection;
  private Float toleranceValue;
  private String toleranceUnit;

}