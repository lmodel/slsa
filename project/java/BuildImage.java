package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
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