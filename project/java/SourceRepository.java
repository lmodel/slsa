package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A self-contained unit that holds the content and complete revision history for a set of files, along with metadata such as branches and tags. Hosted and governed by a Source Control System.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SourceRepository  {

  private String id;
  private String description;
  private String sourceLevel;

}