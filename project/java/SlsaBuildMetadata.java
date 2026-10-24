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
  Metadata about one execution of a build: its identifier and when it started and finished.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildMetadata  {

  private String invocationId;
  private ZonedDateTime startedOn;
  private ZonedDateTime finishedOn;


}