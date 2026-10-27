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
  The predicate in which a verifier records that it evaluated artifacts against a policy and the SLSA levels they met, so consumers can rely on the verifier instead of reading every underlying attestation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaVerificationSummary extends SlsaPredicate {

  private URI resourceUri;
  private SlsaVerifier verifier;
  private ZonedDateTime timeVerified;
  private SlsaVerificationSummaryPolicy policy;
  private List<SlsaVerificationSummaryInputAttestation> inputAttestations;
  private String verificationResult;
  private List<String> verifiedLevels;
  private List<String> organizationProperties;
  private List<SlsaDependencyLevelCount> dependencyLevels;
  private String slsaVersion;


}