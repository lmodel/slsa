package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
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