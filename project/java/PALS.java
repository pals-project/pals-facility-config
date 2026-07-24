package None;

import java.util.List;
import lombok.*;






/**
  Root container for accelerator core components, semantic signals, and local bindings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PALS  {

  private String kind;
  private String description;
  private Affiliation affiliation;
  private String version;
  private List<Author> authors;
  private List<String> notes;
  private Facility facility;

}