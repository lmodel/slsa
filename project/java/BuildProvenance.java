package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An attestation predicate (predicateType "https://slsa.dev/provenance/v1") that describes how a set of output artifacts was produced by a build platform. Consumers use this to verify artifact authenticity and trace artifacts back through the supply chain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildProvenance extends Statement {

  private BuildDefinition buildDefinition;
  private RunDetails runDetails;

}