package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
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
  private boolean hermeticBuild;
  private String provenanceGenerationTool;
  private String pipelineOrchestrator;

}