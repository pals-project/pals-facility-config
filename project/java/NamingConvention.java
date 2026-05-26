package None;

import java.util.List;
import lombok.*;






/**
  A template for constructing facility-specific signal names from a semantic signal name and a control-system-specific suffix.  The template is used to generate the full control system PV name for a given device instance and semantic signal by substituting the device name and signal code suffix into the template.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamingConvention extends NamedThing {

  private String template;
  private List<TemplateComponent> templateComponents;
  private String fullPattern;
  private List<NamingConventionExample> examples;

}