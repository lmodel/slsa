<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# slsa

Supply-chain Levels for Software Artifacts (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/slsa](https://lmodel.github.io/slsa)

## What it models

The schema models the [SLSA specification](https://slsa.dev/spec/v1.2/), version 1.2: the Build and Source tracks, the build provenance and Verification Summary Attestation predicates, and the roles, build platform and package model. The in-toto statement layer comes from [lmodel/in-toto](https://github.com/lmodel/in-toto)'s core module, vendored in [src/slsa/schema/in_toto/](src/slsa/schema/in_toto). The Dependency and Build Environment tracks follow the working draft at 1.2. The copy in [src/slsa/schema/spec/](src/slsa/schema/spec) matches the `v1.2` tag, and a weekly workflow opens an issue when the SLSA Working Group tags a newer version.

## Influences

Two sources add elements of their own, each in a subset: the CNCF *Secure Software Factory* whitepaper (`slsa_ssf`) and the SLSA adoption study by Tamanna et al. (`slsa_adoption_study`). [docs/about.md](docs/about.md) says what each adds.

## Mappings

SLSA publishes no alignment, so every mapping but the first is this project's own.

* **Predicate types**: the two predicate classes map exactly to `https://slsa.dev/provenance/v1` and `https://slsa.dev/verification_summary/v1`.
* **[SPDX 3.0.1](https://spdx.org/rdf/3.0.1/terms/)**: Build profile, Core and Software terms. SPDX's build `environment` and `configSource` map where SLSA's migration table from 0.2 puts those fields.
* **[DOAP](https://github.com/ewilderj/doap)** and **[W3C PROV-O](https://www.w3.org/TR/prov-o/)**: the nearest terms.
* **[W3C EARL 1.0](https://www.w3.org/TR/EARL10-Schema/)**: the results `PASSED` and `FAILED` mean EARL's outcomes of those names.

[tests/test_schema_rules.py](tests/test_schema_rules.py) lists each term the mappings name and the file it was checked in.

## Repository Structure

* [docs/](docs/): the documentation pages the website shows
  * [elements/](docs/elements/): generated schema documentation
* [examples/](examples/): examples of using the schema
* [project/](project/): project files (these files are auto-generated, do not edit)
* [src/](src/): source files (edit these)
  * [slsa](src/slsa)
    * [schema/](src/slsa/schema): the LinkML schema, `slsa.yaml` and
      the modules it imports (edit these)
    * [datamodel/](src/slsa/datamodel): generated
      Python datamodel
* [tests/](tests/): Python tests
  * [data/](tests/data): example data
* [website/](website/): the documentation website, an Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Several pre-defined command-recipes are available using [just](https://github.com/casey/just/). To see the list, run `just` or `just --list`.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/slsa.yaml`, is the copy `just lokf-adapt` writes from `src/slsa/schema/slsa.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy.

The copy roots these classes on `Concept`, so a concept may name any of them, or a subclass, as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
SlsaProducer, SlsaConsumer, SlsaVerifier, SlsaInfrastructureProvider, SlsaBuildImageProducer, SlsaBuildPlatform, SlsaControlPlane, SlsaPackage, SlsaPackageRegistry, SlsaSourceControlSystem, SlsaSourceRepository, SlsaSourceRevision, SlsaBuildImage
```

In the copy, LOKF's `id` stands in for each class's own identifier (`builder_id`, `repository_uri` and the like), so a concept writes `id`. LOKF 0.9.0 defines `revision` and `predicate`, so the copy renames them `slsa_revision`, with its IRI still `slsa:revision`, and `slsa_predicate`, with in-toto's IRI. A slsa document keeps both keys. `media_type` keeps its name, because `lokf adapt` does not compare class attributes, and takes LOKF's IRI, `dcat:mediaType`.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)). The specification's pages in [src/slsa/schema/spec/](src/slsa/schema/spec) and the CNCF Secure Software Factory whitepaper in [docs/](docs/) keep their own licences: see [NOTICE](NOTICE). This is not an official SLSA release, and its use does not imply endorsement by the SLSA Working Group, OpenSSF or the CNCF.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for a pull request and
for releasing. [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted
work. [SECURITY.md](SECURITY.md) says how to report a vulnerability.
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
