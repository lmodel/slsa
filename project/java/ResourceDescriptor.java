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
  A reference to a software artifact including its location, digest, and optional metadata. Used throughout SLSA to describe inputs, outputs, and dependencies in provenance attestations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceDescriptor  {

  private String uri;
  private DigestSet digest;
  private String name;
  private String downloadLocation;
  private String mediaType;
  private List<String> annotations;


}