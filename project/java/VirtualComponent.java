package None;

import java.util.List;
import lombok.*;






/**
  A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VirtualComponent extends Component {

  private String function;
  private String beamlineRelation;
  private Float x;
  private Float y;
  private Float z;
  private Float theta;
  private Float phi;
  private Float psi;

}