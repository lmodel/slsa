<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# slsa

Supply-chain Levels for Software Artifacts (LinkML)

## Documentation Website

[https://lmodel.github.io/slsa](https://lmodel.github.io/slsa)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [slsa](src/slsa)
    * [schema/](src/slsa/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/slsa/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## License and attribution

The schema and the code in this repository are Apache-2.0
([LICENSE](LICENSE)). The schema models the
[SLSA specification](https://slsa.dev) and draws on two further sources,
named in [docs/about.md](docs/about.md). [NOTICE](NOTICE) lists the
third-party work this repository carries, and is included in the package.

* **The SLSA specification.** [src/slsa/schema/spec/](src/slsa/schema/spec)
  holds a copy of "Supply-chain Levels for Software Artifacts", the Working
  Draft as of version 1.2, by the SLSA Working Group (OpenSSF), retrieved
  from
  [slsa-framework/slsa at v1.2](https://github.com/slsa-framework/slsa/tree/v1.2/docs/spec/draft).
  Content contributed after the group adopted the Community Specification
  governance model is under the
  [Community Specification License 1.0](https://github.com/slsa-framework/slsa/blob/main/LICENSE.md),
  which asks every derivative work to name the material, its version and
  its source, as this paragraph does. Older portions are Apache-2.0. The
  copy is kept unmodified for reference; [NOTICE](NOTICE) says which files
  differ from that tree.
* **The Secure Software Factory whitepaper.**
  [docs/Secure_Software_Factory_Whitepaper.pdf](docs/Secure_Software_Factory_Whitepaper.pdf)
  is CNCF TAG-Security's whitepaper, copied unmodified from
  [cncf/tag-security](https://github.com/cncf/tag-security), whose
  documentation is under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

This is not an official SLSA release, and its use does not imply
endorsement by the SLSA Working Group, OpenSSF or the CNCF. Everything the
schema defines lives under `slsa:` (`https://w3id.org/lmodel/slsa/`).

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for a pull request and
for releasing. [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted
work. [SECURITY.md](SECURITY.md) says how to report a vulnerability.
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
