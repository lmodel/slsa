package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A party who creates software and provides it to others. Responsible for choosing an appropriate build platform, following a consistent build process, and distributing provenance to consumers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Producer  {

  private String name;
  private String buildPlatformId;

}