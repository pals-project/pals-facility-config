package None;

import java.util.List;
import lombok.*;






/**
  A slot that can take any value, used for fields where a controlled vocabulary is not necessary or not yet established. Use when the field can contain a wide range of values that do not fit into a predefined set, or when flexibility is needed for future expansion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnyValue  {

  private String value;

}