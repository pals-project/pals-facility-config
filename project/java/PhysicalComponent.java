package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhysicalComponent extends Component {

  private List<String> functions;
  private String beamlineRelation;
  private FloorParamGroup floorP;
  private LongitudinalPlacementParamGroup longitudinalPlacementP;

}