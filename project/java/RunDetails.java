package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Details specific to this particular execution of the build, including the trusted builder and optional run-level metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RunDetails  {

  private Builder builder;
  private BuildMetadata buildMetadata;
  private List<ResourceDescriptor> byproducts;

}