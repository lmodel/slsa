package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An attestation predicate (predicateType "https://slsa.dev/verification_summary/v1") issued by a trusted verifier stating that one or more artifacts were evaluated against a policy and the SLSA level at which they were verified. Allows consumers to trust the verifier's determination without needing access to all underlying provenance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VerificationSummaryAttestation extends Statement {

  private Verifier verifier;
  private String timeVerified;
  private String resourceUri;
  private ResourceDescriptor policy;
  private List<ResourceDescriptor> inputAttestations;
  private String verificationResult;
  private List<String> verifiedLevels;
  private String dependencyLevels;
  private String slsaVersion;

}