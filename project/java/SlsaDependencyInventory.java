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
  The inventory of every third-party build dependency, direct and transitive, of one artifact version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaDependencyInventory  {

  private InTotoResourceDescriptor artifact;
  private List<InTotoResourceDescriptor> dependencies;
  private String dependencyLevel;


}