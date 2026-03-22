package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An identifiable unit of software intended for distribution. In the SLSA model, a package is always the output of a build process (which may be a no-op). The package name is the primary security boundary within a package ecosystem.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Package  {

  private String name;
  private String ecosystem;
  private String registry;
  private ResourceDescriptor artifact;

}