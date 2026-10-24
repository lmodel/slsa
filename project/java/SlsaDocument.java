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
  A document that holds SLSA attestations and the parties, platforms, packages, repositories and images they concern.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaDocument  {

  private List<InTotoStatement> attestations;
  private List<SlsaParty> parties;
  private List<SlsaBuildPlatform> buildPlatforms;
  private List<SlsaPackage> packages;
  private List<SlsaPackageRegistry> packageRegistries;
  private List<SlsaSourceControlSystem> sourceControlSystems;
  private List<SlsaSourceRepository> sourceRepositories;
  private List<SlsaSourceRevision> sourceRevisions;
  private List<SlsaNamedReference> namedReferences;
  private List<SlsaBuildImage> buildImages;
  private List<SlsaDependencyInventory> dependencyInventories;
  private SlsaAdoptionMetadata adoptionMetadata;


}