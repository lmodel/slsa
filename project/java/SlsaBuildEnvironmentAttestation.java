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
  Evidence of the state of a build environment when a build was dispatched to it: the image it came from and the measurements taken at boot.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildEnvironmentAttestation extends SlsaPredicate {

  private String buildEnvLevel;
  private String buildId;
  private SlsaBuildImage buildImage;
  private List<SlsaMeasurement> measurements;


}