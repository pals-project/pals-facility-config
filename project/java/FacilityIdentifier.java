package None;

import java.util.List;
import lombok.*;






/**
  A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FacilityIdentifier  {

  private String identifierType;
  private String identifierValue;

}