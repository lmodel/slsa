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
  Describes all inputs to the build in enough detail to initialise and reproduce the build. The accuracy and completeness are implied by the builder identified in runDetails.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildDefinition  {

  private String buildType;
  private String externalParameters;
  private String internalParameters;
  private List<ResourceDescriptor> resolvedDependencies;
  private Boolean hermeticBuild;
  private String provenanceGenerationTool;
  private String pipelineOrchestrator;


}