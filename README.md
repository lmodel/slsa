<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# slsa

Supply-chain Levels for Software Artifacts (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/slsa](https://lmodel.github.io/slsa)

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema is `.lokf/slsa.yaml`, a copy that `lokf adapt` wrote from `src/slsa/schema/slsa.yaml`. Edit the source, never the copy.

`just lokf-adapt` rewrites the copy and `just lokf-adapt-check` says when it is stale; `project.justfile` says which classes the copy roots on `Concept`. A concept may name any of them, or a subclass, as its `type`. Obsidian users of the KTL Registrar and KTL Curator plugins should add them to the *Known LOKF types* setting:

```text
SlsaProducer, SlsaConsumer, SlsaVerifier, SlsaInfrastructureProvider, SlsaBuildImageProducer, SlsaBuildPlatform, SlsaControlPlane, SlsaPackage, SlsaPackageRegistry, SlsaSourceControlSystem, SlsaSourceRepository, SlsaSourceRevision, SlsaBuildImage
```

In the copy, LOKF's `id` stands in for each class's own identifier (`builder_id`, `repository_uri` and the like), so a concept writes `id`. Every other key keeps its SLSA name, because no top-level class, slot, enum or type in the schema has a name that `lokf.yaml` defines. `lokf adapt` does not compare class attributes, so `media_type` and `predicate` keep the names they share with LOKF slots.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)). The schema models the [SLSA specification](https://slsa.dev) and draws on two further sources, which [docs/about.md](docs/about.md) names.

The repository also carries the specification's pages in [src/slsa/schema/spec/](src/slsa/schema/spec) and the CNCF Secure Software Factory whitepaper in [docs/](docs/), each under its own license. See [NOTICE](NOTICE).

This is not an official SLSA release, and its use does not imply endorsement by the SLSA Working Group, OpenSSF or the CNCF.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for a pull request and
for releasing. [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted
work. [SECURITY.md](SECURITY.md) says how to report a vulnerability.
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
