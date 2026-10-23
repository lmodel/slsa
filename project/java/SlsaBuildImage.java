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
  The template a build environment is instantiated from, such as a VM or container image: root filesystem, guest OS and packages, build executor and build agent.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildImage  {

  private String buildEnvLevel;
  private URI imageUri;
  private SlsaBuildProvenance provenance;
  private SlsaBuildImageProducer producedBy;


}