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
  What is specific to one execution of a build: the platform that ran it, metadata about the run and its by-products.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaRunDetails  {

  private SlsaBuildPlatform builder;
  private SlsaBuildMetadata buildMetadata;
  private List<InTotoResourceDescriptor> byproducts;


}