package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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