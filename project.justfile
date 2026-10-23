## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/slsa.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the classes a knowledge concept may use as its `type`; a class with
# an identifier of its own is one of them, because the copy gives it LOKF's
# `id` in place of that identifier. `lokf adapt` is in lokf's main branch and
# not yet in a release, so LOKF_CMD points the recipes at a checkout until it
# is: LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root SlsaParty --root SlsaBuildPlatform --root SlsaControlPlane --root SlsaPackage --root SlsaPackageRegistry --root SlsaSourceControlSystem --root SlsaSourceRepository --root SlsaSourceRevision --root SlsaBuildImage"

# Rewrite .lokf/slsa.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/slsa.yaml

# Fail when .lokf/slsa.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/slsa.yaml --check

# ============ The merged schema for the docs site ============

# `just gen-doc` writes docs/schema/slsa.yaml with the modules' elements folded
# in but the `imports:` list kept, so a tool that loads it looks for the modules
# beside it. This file has no imports at all: the one to vendor or load offline.
# Run it after gen-doc.
[group('model development')]
gen-merged:
  uv run gen-linkml --mergeimports -f yaml {{source_schema_path}} > docs/schema/{{schema_name}}_merged.yaml
