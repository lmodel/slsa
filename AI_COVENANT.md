# AI Covenant

This covenant establishes community norms for responsible AI use in the project. It aims to maintain trust, quality, and accountability while embracing AI as a useful tool.

It applies to this repository, <https://github.com/lmodel/slsa>.

## Core Principle: You Own Your Contributions

**Everything you contribute is yours, regardless of what tools helped create it.**

When you submit code, documentation, issues, or comments with AI assistance, you are the author. You are responsible for:

- Understanding what you are submitting
- Verifying correctness and appropriateness
- Defending and explaining your choices during review
- Ensuring it meets project standards

Do not submit anything you cannot fully stand behind.

## A note specific to this project

This repository models someone else's specification. SLSA is the work of the SLSA Working Group at OpenSSF; this project renders its tracks, levels and attestation formats as a LinkML schema, with elements drawn from a CNCF whitepaper and a published study. That makes one failure mode worse here than elsewhere: a description, level or requirement that a model produced, presented as what SLSA says. A reader cannot tell it from the specification's own text.

So:

- **A description says what its source says.** Every class, slot and enum value in `src/slsa/schema/slsa.yaml` renders a passage of the SLSA specification, the Secure Software Factory whitepaper or the adoption study. Cite that passage in the pull request, and never give a SLSA term a meaning its source does not carry. "The model said so" is not a source.
- **The specification copy is upstream text.** `src/slsa/schema/spec/` is SLSA's own pages, kept for reference. Never edit it; replace it from the upstream tag and commit that [NOTICE](NOTICE) records, and `upstream-watch.yaml` checks it still matches.
- **The namespace is this project's.** Everything the schema defines lives under `slsa:` (`https://w3id.org/lmodel/slsa/`). SLSA's own identifiers, such as predicate types under `https://slsa.dev/`, appear only as values the schema documents.

## AI-Assisted Code Reviews

AI review tools (Claude, Copilot, CodeRabbit, etc.) provide **automated quality checks, not human reviews**.

- AI comments are suggestions, not requirements
- PR owners may close AI comments without response
- Human reviewers may use AI feedback to inform their own review
- A PR still requires human approval regardless of AI feedback

## AI-Assisted Discussions

AI tools can be helpful **thinking aids** when preparing to participate in [issues](https://github.com/lmodel/slsa/issues).

They may be used to:

- Clarify your own thinking before engaging
- Explore alternative framings or options
- Help draft *your* contribution for clarity and structure

However, discussions exist to **surface, negotiate, and consolidate human judgement**. They are not a channel for autonomous or proxy AI participation.

**AI systems MUST NOT be used to directly post comments, replies, or messages** in:

- GitHub issues or discussions
- Shared Slack channels
- Project mailing lists or email threads

All discussion contributions must reflect a **human position** that the author is prepared to explain, revise, and defend. Posting AI-generated commentary as an independent "voice" undermines trust, accountability, and the purpose of deliberation.

In short:

- AI may *support* participation
- Humans must *own* participation

## Repository-Owned Agent Automation

Some of what runs here isn't "a person using an AI tool". It is a scheduled agent (this repo's `knowledge-librarian.yaml` workflow, running the `ktl-librarian` skill) that reads the repository and proposes changes on its own initiative, with no one drafting alongside it in real time. The core principle above still applies; here is what it means in that case:

- **Identity.** Such an agent commits as either a clearly labeled bot identity (here, `knowledge-librarian[bot]`) or the maintainer who invoked it interactively, never both. A bot identity already discloses what produced the change, so it carries no further trailer; a commit made under a maintainer's identity carries no AI co-authorship trailer either, for the same reason the "Not required" section below discourages one generally.
- **Review, always.** Every change such an agent proposes is opened as a pull request, never a direct push to the default branch, and requires a human maintainer's approval before merge. An agent's own review of its own work, or one agent approving another's, does not satisfy it.
- **Least privilege, enforced.** The agent runs in a read-only job with no git credentials on disk and hands its proposed change to a separate privileged job that runs no agent code. The "edit only `.lokf/knowledge/`" contract is checked after the agent runs, not merely requested of it.
- **Verdicts must be real.** A skill that records a person's judgment (for instance, `ktl-curator` writing a `verified: human:<id>` event) may write only what that person actually said about that specific item, in that session: never inferred, batched, or supplied by the agent itself.

None of this relaxes anything above: an agent's output is nobody's contribution until a human has reviewed and approved it into the repository.

## When to Disclose AI Assistance

**Required disclosure:**

- When proposing bug fixes or changes to code you don't fully understand, attribute the idea to AI so reviewers can assess appropriately.
- When a schema description under `src/slsa/schema/` was drafted by AI, as described above, along with the passage it rests on.

**Appreciated transparency:**

- When brainstorming solutions, distinguish between "AI suggests X" and "I recommend X based on my expertise". This helps the community prioritize ideas.

**Not required:**

- Routine use of AI for writing code, issues, or PR descriptions.
- AI co-authorship in commit messages. This is actively discouraged.

## What This Means in Practice

| Situation | Guidance |
| --- | --- |
| Writing code with Copilot/Claude | No disclosure needed; you own the result |
| Submitting AI-suggested fix you fully understand | No disclosure needed |
| Submitting AI-suggested fix in unfamiliar code | Disclose AI origin for reviewer context |
| Adding or changing a description in `src/slsa/schema/slsa.yaml` | Cite the passage it renders, whoever drafted it |
| Drafting issue or PR description with AI | No disclosure needed; ensure it's accurate |
| Brainstorming in discussions | Be clear about AI-generated vs. expert ideas |
| Receiving AI review comments | Address or close at your discretion |

## Trust and Accountability

This covenant is built on trust. By contributing, you agree that:

1. You will not submit AI-generated content without reviewing it
2. You will take responsibility for any issues arising from your contributions
3. You will be honest about the origins of ideas when it matters for review quality

---

*This covenant may evolve as AI tools and community needs change. It is adapted from the [Knowledge Trust Ladder AI Covenant](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/AI_COVENANT.md), itself adapted from the [LinkML AI Covenant](https://github.com/linkml/linkml/blob/main/AI_COVENANT.md). Feedback and suggestions are welcome.*
