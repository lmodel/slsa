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