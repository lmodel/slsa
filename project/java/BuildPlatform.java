package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The infrastructure (software, hardware, people, and organizations) used to transform source code into package artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant build service.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildPlatform  {

  private String id;
  private String buildLevel;
  private boolean isHosted;

}