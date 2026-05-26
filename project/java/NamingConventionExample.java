package None;

import java.util.List;
import lombok.*;






/**
  An example of a control system naming convention, illustrating how the template is used to generate full control system PV names from semantic signal names and device instance information.  This can be used to provide concrete examples of the expected PV naming convention for different device types and signals based on the defined NamingConvention template.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamingConventionExample  {

  private String example;
  private String description;

}