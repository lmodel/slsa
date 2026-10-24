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
  The template for a build environment, such as a VM or container image. Comprises the root filesystem, pre-installed guest OS and packages, the build executor, and the build agent. Created by a build image producer and consumed by the hosted build platform.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildImage  {

  private String id;
  private BuildProvenance provenance;
  private String buildEnvLevel;


}