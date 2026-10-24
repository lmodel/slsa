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
  The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their accuracy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildDefinition  {

  private URI buildType;
  private List<SlsaBuildParameter> externalParameters;
  private List<SlsaBuildParameter> internalParameters;
  private List<InTotoResourceDescriptor> resolvedDependencies;
  private Boolean hermetic;
  private URI provenanceGenerationTool;
  private URI pipelineOrchestrator;


}