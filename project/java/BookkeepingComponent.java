package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BookkeepingComponent extends VirtualComponent {

  private BodyShiftParamGroup bodyShiftP;

}