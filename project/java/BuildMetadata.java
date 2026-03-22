package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Metadata about a specific invocation of the build, including timing information and a unique build identifier for log correlation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildMetadata  {

  private String invocationId;
  private String startedOn;
  private String finishedOn;

}