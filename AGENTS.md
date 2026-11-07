# Agents — Working Conventions for This Repository

This file defines how we work in this repo. It is the operating agreement for anyone (human or agent) contributing documents here.

## Purpose of This Repo

`cfp-data/` houses, under `docs/`, the working documents for the Network Data Target State program: vision, requirements, strategy, architecture, designs, and roadmap. It is a living document set, not a deliverable. Status is always honest; perfection is not required to commit.

## Language & Style

- **Precise engineering language.** Favour short words, short sentences, short paragraphs. If a concept needs a paragraph to explain, the concept needs rewriting — not the paragraph.
- **Assume a knowledgeable audience.** No background primers on networking, databases, or architecture. Define only terms that are genuinely ambiguous or contested within the team (see [`docs/07-glossary.md`](docs/07-glossary.md)).
- **No filler.** Every paragraph, every sentence, every word earns its place. If it does not add signal, delete it.
- **Readable in 5 minutes.** Detail goes into linked sub-documents or ADRs.
- **Standards-first, hype-last.** See principle P7 in [`docs/03-architecture-principles.md`](docs/03-architecture-principles.md).
- **Tables over prose** for enumerations (risks, principles, success dimensions, platform capabilities). One row per item, concrete values where possible.
- **Cross-reference by relative path**, never by absolute URL. The document tree is the navigation system.

## Document Types

| Type | Purpose | Lives in |
|---|---|---|
| **Vision / Problem** | Why this exists, what we are solving, what we are not solving | `docs/01-*.md` |
| **Risk / Context** | Why it matters, what happens if we fail | `docs/02-*.md` |
| **Principles** | Non-negotiable constraints that guide every decision | `docs/03-*.md` |
| **Area of work** | Scope, sub-areas, open questions for one workstream | `docs/04-major-areas-of-work/*.md` |
| **Roadmap / Plan** | Phasing, dependencies, sequencing | `docs/05-*.md` |
| **Success criteria** | How we know it worked — concrete, measurable | `docs/06-*.md` |
| **Glossary** | Terms that cause ambiguity | `docs/07-*.md` |
| **ADR** | A specific architectural decision: context, options, choice, rationale, consequences | `docs/adr/NNNN-title.md` |
| **Reference** | External standard, paper, tool, or pattern that informed a decision | `docs/references/short-name.md` |

## Decision Log

Every architectural decision gets an ADR in `docs/adr/`. Number sequentially (0001, 0002...). The ADR template is at [`docs/templates/decision-record.md`](docs/templates/decision-record.md).

Do not record:
- Project management decisions (sprint scope, meeting cadence).
- Implementation details that may change week-to-week.
- Trivial choices with no lasting impact.

## References

When a decision references an external source (standard, RFC, paper, tool, blog post), capture it in `docs/references/`:

```markdown
# docs/references/openconfig.md

## OpenConfig

- **Home**: https://openconfig.net/
- **Key documents**: [Model catalog](https://openconfig.net/models/)
- **Relevance**: Primary candidate for device model standardisation
- **Used by**: ADR-0003 (device model format)
```

One file per reference. Keep it minimal — a few lines, not an essay. Link from ADRs and area-of-work docs by relative path.

## Status Tracking

Every document has a status in `README.md`:

| Symbol | Meaning |
|---|---|
| 🟢 Stable | Reviewed, agreed, unlikely to change without an ADR |
| 🟡 Draft | Written but not yet reviewed; expected to change |
| 🔴 Not started | Skeleton exists, little or no content |

Push status-forward alongside content. A draft merged and reviewed becomes 🟢. A superseded ADR becomes "Superseded by ADR-NNNN".

## File Conventions

- **Layout.** Document set lives in `docs/`. Root holds only `README.md`, `AGENTS.md`, `CLAUDE.md`.
- **Markdown only.** No Word, no PDF, no Google Docs. If it cannot be written in markdown it does not belong here.
- **One thing per file.** A monolith document is a sign of undiscovered structure. Split when a section could stand alone and be cross-referenced.
- **Files are numbered** (`01-`, `02-`...) only for reading order. Sub-directories (`04-major-areas-of-work/`, `adr/`, `references/`, `templates/`) are unnumbered.
- **Relative links** (`../02-risks-and-importance.md`), never `https://github.com/...` links within the doc set. External links are fine.

## Agent Behaviour

When an agent (any agent) works in this repo:

1. **Read the current state first.** Load `README.md` for status, then the file you need to modify.
2. **Check existing ADRs.** Before proposing a decision, verify it has not already been made.
3. **Leave status honest.** If you add content to a 🟡 draft, leave it 🟡 unless the user explicitly approves. If you create something new, mark it 🔴 or 🟡 as appropriate.
4. **Cross-reference.** When you add content that relates to another file, add the relative link. Update the README's status table if you add a new file.
5. **Record decisions as you go.** If you make a substantive choice, write the ADR the same session. Do not accumulate undocumented decisions.
6. **Prefer append to rewrite.** Additions are safer than deletions. Rewrite only when the old content is clearly wrong, not just when you would phrase it differently.
7. **Commit with meaningful messages.** One commit per logical change. The message says what changed, not why the change matters (that lives in the document body).
8. **Agent instructions live here.** Updates to agent/LLM instructions go into this file. Tool-specific files (`CLAUDE.md`, etc.) only point here.
