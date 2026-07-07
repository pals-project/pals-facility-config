package None;

import java.util.List;
import lombok.*;






/**
  A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhysicalComponent extends Component {

  private String function;
  private String beamlineRelation;
  private Float x;
  private Float y;
  private Float z;
  private Float theta;
  private Float phi;
  private Float psi;
  private Float length;
  private Float sPosition;

}