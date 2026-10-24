---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/slsa/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: SLSA Knowledge Bundle
description: Supply-chain Levels for Software Artifacts (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/slsa/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# SLSA Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for SLSA. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [slsa documentation site](services/documentation-site.md) - The MkDocs site at `https://lmodel.github.io/slsa`, generated from the slsa schema and deployed to GitHub Pages on every push to main, with a preview built for each pull request from a branch of this repository.

# References

* [SLSA specification](references/slsa-specification.md) - Supply-chain Levels for Software Artifacts (SLSA), the OpenSSF specification of tracks and levels for supply chain security; the slsa LinkML schema renders version 1.2, its Build and Source tracks, and the working draft's Dependency and Build Environment tracks.
* [CNCF Secure Software Factory whitepaper](references/secure-software-factory.md) - The CNCF TAG-Security Secure Software Factory whitepaper (2022), which describes a pipeline of version control, build service, artifact registry, signing service and policy engine; the schema's slsa_ssf subset takes five slots from it.
* [SLSA adoption study (Tamanna et al., 2024)](references/slsa-adoption-study.md) - An empirical study by Tamanna et al. (2024, arXiv:2409.05014) of 1,523 SLSA-related GitHub issues from 233 repositories; the schema's slsa_adoption module encodes its four challenge and five strategy themes as enums on SlsaAdoptionMetadata.
* [OpenSSF Supply Chain Integrity Working Group](references/openssf-supply-chain.md) - The OpenSSF Supply Chain Integrity Working Group, whose software supply chain projects include SLSA, Sigstore, GUAC, gittuf and Security Insights; the schema's guac_uri and security_insights_uri slots point at GUAC and Security Insights.

# Datasets

* [slsa LinkML schema](datasets/slsa-linkml-schema.md) - The modular LinkML schema of the SLSA specification v1.2 (schema id `https://w3id.org/lmodel/slsa`): `slsa.yaml` imports a core module and one module per track, predicate or study, covering the Build, Source, Dependency and Build Environment tracks and the in-toto statement layer; its `lokf adapt` copy in `.lokf/slsa.yaml` is the bundle's domain schema.
* [SLSA specification copy](datasets/slsa-spec-copy.md) - The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`: all 39 files are identical to `docs/spec/draft/` at SLSA tag v1.2, and a weekly workflow watches for a newer release.
* [Generated artifacts](datasets/generated-artefacts.md) - Files generated from the slsa schema and never edited by hand, committed or git-ignored: the two merged schemas in docs/schema/, the Python data models, project/ (JSON Schema, OWL, SHACL, Java and more), docs/elements/ and the bundle's domain schema .lokf/slsa.yaml.
* [Test data](datasets/test-data.md) - Example YAML instances of the slsa schema in tests/data/, valid and invalid, named ClassName-###.yaml after the class they instantiate (InTotoStatement, SlsaBuildPlatform and the rest); pytest and linkml-run-examples check them.

# Explanations

* [Schema subsets](explanations/schema-subsets.md) - Why the slsa schema tags its elements with six subsets (one per SLSA track: Build, Source, Dependency and Build Environment, plus slsa_ssf and slsa_adoption_study for what two outside sources add), and what each subset covers.

# Glossary

* [SLSA track](glossary/slsa-track.md) - A SLSA track focuses on one aspect of a software supply chain (Build, Source, Dependency or Build Environment), with its own levels, threats and requirements; the schema gives each track a subset and a level enum.
* [SLSA level](glossary/slsa-level.md) - A rung within a SLSA track, such as Build L2 or Source L3; higher levels give better guarantees against supply chain threats at a higher cost to implement. The schema names them in its four level enums, such as SlsaBuildLevel.

# Playbooks

* [Regenerate and test the schema](playbooks/regenerate-and-test.md) - How to change the slsa schema and its modules, regenerate the artifacts, the docs and the bundle's domain schema with just (gen-project, gen-doc, gen-merged, lokf-adapt), then run the tests CI runs (just test) on Python 3.10 to 3.14.
* [Release the slsa package](playbooks/release.md) - How a releasing commit merged to main makes semantic-release promote the changelog, tag vX.Y.Z and publish a GitHub Release, and how pypi-publish.yaml then publishes slsa-linkml to PyPI once PYPI_RELEASE_ENABLED is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external URL this bundle derives concepts from, and how to re-verify each on a refresh run.

# Org

* [SLSA project (OpenSSF)](org/slsa-project.md) - The OpenSSF project that publishes the SLSA specification from the slsa-framework/slsa repository, governed by a steering committee and licensed under the Community Specification License 1.0.
* [CNCF TAG-Security](org/cncf-tag-security.md) - The CNCF Security Technical Advisory Group, publisher of the Secure Software Factory whitepaper from its cncf/tag-security repository (now archived), which licenses its documentation under CC BY 4.0.

# Policies

* [License and attribution](policies/license-and-attribution.md) - Which license covers what in the slsa repository: Apache-2.0 for the schema and code, the SLSA specification copy under the Community Specification License 1.0 (older portions Apache-2.0) with its name, version and source given in NOTICE, the whitepaper under CC BY 4.0, and what else NOTICE lists.
