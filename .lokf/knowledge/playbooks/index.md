# Playbooks

* [Regenerate and test the schema](regenerate-and-test.md) - How to change the slsa schema and its modules, regenerate the artifacts, the docs and the bundle's domain schema with just (gen-project, gen-doc, gen-merged, lokf-adapt), then run the checks CI runs: just test on Python 3.10 to 3.14, and just lint and just lokf-adapt-check on 3.13.
* [Release the slsa package](release.md) - How a releasing commit merged to main makes semantic-release promote the changelog, tag vX.Y.Z and publish a GitHub Release, and how pypi-publish.yaml then publishes slsa-linkml to PyPI once PYPI_RELEASE_ENABLED is true.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external URL this bundle derives concepts from, and how to re-verify each on a refresh run.
