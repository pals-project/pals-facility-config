package None;

import java.util.List;
import lombok.*;






/**
  A virtual component that represents a bookkeeping or organizational role in the accelerator system, 
such as a BeamlineSection, Marker or a Fork.
These can include BeamlineSections, Markers, Forks, 
and other virtual components that are important for understanding 
the structure and function of the accelerator system but are not physical devices.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BookkeepingComponent extends VirtualComponent {

  private Float xOffset;
  private Float yOffset;
  private Float zOffset;
  private Float xRot;
  private Float yRot;
  private Float zRot;

}