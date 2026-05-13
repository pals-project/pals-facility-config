package None;

import java.util.List;
import lombok.*;






/**
  Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics parameters.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FacilityParamSet  {

  private String facilityElementType;
  private String modeledAs;
  private AnyValue properties;

}