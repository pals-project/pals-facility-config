package None;

import java.util.List;
import lombok.*;






/**
  A single element in a beamline with its kind and optional NARAD capability annotations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BeamlineElement extends NamedThing {

  private String isInstanceOf;
  private Float length;
  private List<InstanceSignalBinding> isObservedBy;
  private ElementParamSet paramSet;

}