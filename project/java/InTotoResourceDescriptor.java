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
  A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoResourceDescriptor  {

  private URI resourceUri;
  private InTotoDigestSet digest;
  private String resourceName;
  private URI downloadLocation;
  private String mediaType;
  private String content;
  private List<InTotoAnnotation> annotations;


}