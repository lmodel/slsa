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
  Details specific to this particular execution of the build, including the trusted builder and optional run-level metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RunDetails  {

  private Builder builder;
  private BuildMetadata buildMetadata;
  private List<ResourceDescriptor> byproducts;


}