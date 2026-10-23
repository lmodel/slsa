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
  A unit of software distributed under a package name, which is the primary security boundary SLSA protects. Its artifacts are the outputs of builds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaPackage  {

  private String ecosystem;
  private String packageName;
  private SlsaPackageRegistry registry;
  private List<InTotoResourceDescriptor> packageArtifacts;
  private URI guacUri;
  private URI securityInsightsUri;


}