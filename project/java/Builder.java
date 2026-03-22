package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Represents the transitive closure of all software, hardware, and entities trusted to faithfully execute the build and record provenance. The builder.id is the primary basis for determining SLSA Build Level.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Builder  {

  private String id;
  private List<ResourceDescriptor> builderDependencies;
  private String version;
  private String versionTag;

}