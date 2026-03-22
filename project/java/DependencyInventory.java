package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A comprehensive inventory of all third-party build dependencies for an artifact, capturing direct and transitive dependencies. Supports vulnerability management and incident response.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DependencyInventory  {

  private ResourceDescriptor artifact;
  private List<ResourceDescriptor> dependencies;
  private String dependencyLevel;

}