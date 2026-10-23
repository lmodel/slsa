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
  Optional structured metadata capturing the SLSA adoption challenges and mitigation strategies relevant to a given attestation or deployment context. Derived from empirical analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Use this class to document which challenge themes apply to the current deployment and which strategies are being employed or recommended. Attach via the adoptionMetadata slot on SlsaDocument.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AdoptionMetadata  {

  private List<String> challenges;
  private List<String> strategies;


}