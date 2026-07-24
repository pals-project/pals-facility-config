package None;

import java.util.List;
import lombok.*;






/**
  A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SupportingFacilityComponent extends PhysicalComponent {

  private BodyShiftParamGroup bodyShiftP;

}