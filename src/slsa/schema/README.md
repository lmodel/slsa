# Schema directory

The LinkML schema, as `slsa.yaml` and the modules it imports:

| File | Holds |
| --- | --- |
| `slsa.yaml` | The umbrella: imports every module and adds the `SlsaDocument` root. The project names this file. |
| `slsa_core.yaml` | What every track shares: the in-toto statement layer and resource descriptors, the roles, the build platform and the package model. Imports only `linkml:types`. |
| `slsa_build.yaml` | The Build track's provenance predicate. |
| `slsa_verification.yaml` | The Verification Summary Attestation predicate, `SlsaResult` and the `slsa_result_value` type that verified levels take, which also admits an issuer's own results. |
| `slsa_source.yaml` | The Source track: source control systems, repositories, revisions, named references and source provenance. |
| `slsa_dependency.yaml` | The Dependency track (working draft). |
| `slsa_build_environment.yaml` | The Build Environment track (working draft); imports `slsa_build` for the image's provenance. |
| `slsa_adoption.yaml` | The adoption study's challenge and strategy themes. |
| `spec/` | A copy of the SLSA specification's pages at tag `v1.2`, as `NOTICE` records. Never edited here. |

Each module imports the core and lints alone; no module imports the umbrella.
