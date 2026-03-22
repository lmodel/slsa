package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The build platform component that orchestrates each independent build execution and generates provenance. Managed by an admin and trusted to be outside of tenant control. Responsible for generating and signing provenance at SLSA Build L2+.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlPlane  {


}