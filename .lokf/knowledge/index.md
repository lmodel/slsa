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

* [SLSA specification](references/slsa-specification.md) - Supply-chain Levels for Software Artifacts (SLSA), the OpenSSF specification of tracks and levels for supply chain security that the slsa LinkML schema encodes; the schema's docs name v1.2 as the target.
* [CNCF Secure Software Factory whitepaper](references/secure-software-factory.md) - The CNCF TAG-Security Secure Software Factory whitepaper (2022), a reference architecture for an end-to-end SLSA pipeline; the schema's slsa_ssf subset draws on it.
* [SLSA adoption study (Tamanna et al., 2024)](references/slsa-adoption-study.md) - An empirical study of SLSA adoption in open source projects (arXiv:2409.05014), whose challenge and strategy themes the schema's slsa_adoption_study subset encodes as enums and slots.
* [OpenSSF Software Supply Chain working group](references/openssf-supply-chain.md) - The OpenSSF working group that coordinates SLSA, Sigstore, GUAC, gittuf, Security Insights and related projects; the schema cross-references them in notes and see_also annotations.

# Datasets

* [slsa LinkML schema](datasets/slsa-linkml-schema.md) - The LinkML schema for SLSA attestations and adoption metadata (schema id `https://w3id.org/lmodel/slsa`), covering the Build, Source, Dependency and Build Environment tracks, the in-toto Statement layer, and the SSF and adoption-study subsets.
* [SLSA specification copy](datasets/slsa-spec-copy.md) - The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`; 38 of its 42 files match `docs/spec/draft/` at SLSA tag v1.2.
* [Generated artifacts](datasets/generated-artefacts.md) - Files generated from the slsa schema and never edited by hand, committed or git-ignored: the merged schema in docs/schema/, the Python data models, project/ (JSON Schema, OWL, SHACL, Java and more) and docs/elements/.
* [Test data](datasets/test-data.md) - Example YAML instances of the slsa schema in tests/data/, valid and invalid, named after the class they instantiate; pytest and linkml-run-examples check them.

# Explanations

* [Schema subsets](explanations/schema-subsets.md) - Why the slsa schema tags its elements with six subsets (one per SLSA track, plus slsa_ssf and slsa_adoption_study), and what each subset covers.

# Glossary

* [SLSA track](glossary/slsa-track.md) - A track groups SLSA levels that measure one aspect of supply chain security (Build, Source, Dependency or Build Environment), so progress on one aspect is recognised without blocking on another.
* [SLSA level](glossary/slsa-level.md) - A rung within a SLSA track, such as Build L2 or Source L3, each giving a stronger supply chain security guarantee than the one below; the schema names them in its four level enums.

# Playbooks

* [Regenerate and test the schema](playbooks/regenerate-and-test.md) - How to change the slsa schema and regenerate its artifacts and docs with just (gen-project, gen-doc), then run the tests CI runs (just test) on Python 3.9 to 3.13.
* [Release the slsa package](playbooks/release.md) - How a releasing commit merged to main makes semantic-release promote the changelog, tag vX.Y.Z and publish a GitHub Release, and how pypi-publish.yaml then publishes slsa-linkml to PyPI once PYPI_RELEASE_ENABLED is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external URL this bundle derives concepts from, and how to re-verify each on a refresh run.

# Org

* [SLSA project (OpenSSF)](org/slsa-project.md) - The OpenSSF project that publishes the SLSA specification from the slsa-framework/slsa repository, governed by a steering committee and licensed under the Community Specification License 1.0.
* [CNCF TAG-Security](org/cncf-tag-security.md) - The CNCF Security Technical Advisory Group, publisher of the Secure Software Factory whitepaper from its cncf/tag-security repository (now archived), which licenses its documentation under CC BY 4.0.

# Policies

* [License and attribution](policies/license-and-attribution.md) - Which license covers what in the slsa repository: Apache-2.0 for the schema and code, the SLSA specification copy under the Community Specification License 1.0 with its name, version and source attribution, the whitepaper under CC BY 4.0, and what NOTICE lists.
