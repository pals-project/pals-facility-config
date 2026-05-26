package None;

import java.util.List;
import lombok.*;






/**
  A component of a naming convention template, representing a variable part of the control system PV name that is substituted based on the device instance and signal definition.  For example, in the template "{device_name}{signal_code_suffix}", "device_name" and "signal_code_suffix" would be TemplateComponents that are replaced with the actual device name and signal code suffix for each specific binding.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TemplateComponent extends NamedThing {

  private boolean required;
  private String pattern;

}