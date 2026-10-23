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
  A distribution platform that resolves package names to immutable package artifacts within an ecosystem.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaPackageRegistry  {

  private String ecosystem;
  private URI registryUri;


}