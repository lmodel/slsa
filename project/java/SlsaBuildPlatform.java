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
  The system that runs builds and records their provenance: the transitive closure of software, hardware, people and organizations trusted to do so. Provenance names it as the builder.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildPlatform  {

  private List<SlsaComponentVersion> componentVersions;
  private URI builderId;
  private String buildLevel;
  private Boolean hosted;
  private List<InTotoResourceDescriptor> builderDependencies;


}