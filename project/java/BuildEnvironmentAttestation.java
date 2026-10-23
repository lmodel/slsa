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
  An attestation describing the integrity of a build environment at the time a specific build was dispatched and executed. Used to verify that a build ran in the expected, untampered environment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildEnvironmentAttestation extends Statement {

  private String buildId;
  private BuildImage buildImage;
  private List<String> measurements;
  private String buildEnvLevel;


}