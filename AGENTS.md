# Agents — Working Conventions for This Repository

This file defines how we work in this repo. It is the operating agreement for anyone (human or agent) contributing documents here.

## Purpose of This Repo

`cfp-data/` houses, under `docs/`, the working documents for the Network Data Target State program: vision, use cases, requirements, principles, architecture, designs, and roadmap. It is a living document set, not a deliverable. Status is always honest; perfection is not required to commit.

## Language & Style

- **Precise engineering language.** Favour short words, short sentences, short paragraphs. If a concept needs a paragraph to explain, the concept needs rewriting — not the paragraph.
- **Assume a knowledgeable audience.** No background primers on networking, databases, or architecture. Define only terms that are genuinely ambiguous or contested within the team (see [`glossary.md`](docs/glossary.md)).
- **No filler.** Every paragraph, every sentence, every word earns its place. If it does not add signal, delete it.
- **Readable in 5 minutes.** Detail goes into linked sub-documents or ADRs.
- **No unqualified absolutes in estimates or targets.** Size work as effort: T-shirt for phases and initiatives, points for backlog items. Calendar ranges derive from measured velocity. Every KPI needs a threshold; until baselined, write `[T]` rather than a number.
- **Standards-first, hype-last.** See principle P5 in [`01-principles.md`](docs/solution/01-principles.md).
- **Tables over prose** for enumerations (risks, principles, success dimensions, platform capabilities). One row per item, concrete values where possible.
- **Cross-reference by relative path**, never by absolute URL. The document tree is the navigation system.

## Document Types

| Type | Purpose | Lives in |
|---|---|---|
| **Problem** | Why, for whom, what: problem, risks of inaction, stakeholders, use cases, requirements, current state, constraints | `docs/problem/` |
| **Solution** | How: principles, conceptual model, design areas, platforms, features | `docs/solution/` |
| **Delivery** | When and how we know: roadmap, migration cycle, risk register, success dimensions | `docs/delivery/` |
| **Glossary** | Terms that cause ambiguity | `docs/glossary.md` |
| **Data** | Structured registers (estate matrix, etc.) | `docs/data/*.csv`, `*.yaml` |
| **Idea** | Early thinking: options, sketches, open questions. Not binding. | `docs/ideas/short-name.md` |
| **ADR** | A specific architectural decision: context, options, choice, rationale, consequences | `docs/adr/NNNN-title.md` |
| **Reference** | External standard, paper, tool, or pattern that informed a decision | `docs/references/short-name.md` |

## Decision Log

Every architectural decision gets an ADR in `docs/adr/`. Number sequentially (0001, 0002...). The ADR template is at [`decision-record.md`](docs/templates/decision-record.md).

Most early thinking is not yet a decision. Capture it in `docs/ideas/` first. Ideas may be revised, merged, or dropped. Promote an idea to an ADR only when the team agrees; the idea's status then reads `Promoted to ADR-NNNN`.

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

One file per reference. Keep it minimal — a few lines, not an essay. Link from ADRs, ideas, and solution docs by relative path.

## Traceability

Use case (`UC-n`) → requirement (`R-n`, `Q-n`) → principle (`Pn`). Links are recorded once, in the trace matrix in [`04-requirements.md`](docs/problem/04-requirements.md); reverse views are derived. IDs are stable and never reused; a retired ID stays retired.

## Status & Issues

Document status and cross-cutting open issues live in [`ISSUES.md`](ISSUES.md). Questions local to one document stay in its Key Questions.

Push status forward alongside content. A draft merged and reviewed becomes 🟢. A superseded ADR becomes "Superseded by ADR-NNNN".

## File Conventions

- **Layout.** Document set lives in `docs/`. Root holds only `README.md`, `AGENTS.md`, `CLAUDE.md`, `ISSUES.md`. Docs are banded: `problem/`, `solution/`, `delivery/`.
- **Plain-text formats.** Documents in markdown; structured data in CSV or YAML. No Word, PDF, Google Docs, or other office formats.
- **One thing per file.** A monolith document is a sign of undiscovered structure. Split when a section could stand alone and be cross-referenced.
- **Files are numbered** (`01-`, `02-`...) within a band, only for reading order. Directories are unnumbered.
- **Relative links** (`../02-risks-and-importance.md`), never `https://github.com/...` links within the doc set. External links are fine.

## Agent Behaviour

When an agent (any agent) works in this repo:

1. **Read the current state first.** Load `ISSUES.md` for status and open issues, then the file you need to modify.
2. **Check existing ADRs and ideas.** Before proposing a decision, verify it has not already been made or explored.
3. **Leave status honest.** If you add content to a 🟡 draft, leave it 🟡 unless the user explicitly approves. If you create something new, mark it 🔴 or 🟡 as appropriate.
4. **Cross-reference.** When you add content that relates to another file, add the relative link. Add new files to `ISSUES.md` (status) and the README map.
5. **Record thinking as you go.** Write substantive choices down the same session: as an idea while open, as an ADR once agreed. Do not create an ADR without the user's agreement.
6. **Prefer append to rewrite.** Additions are safer than deletions. Rewrite only when the old content is clearly wrong, not just when you would phrase it differently.
7. **Commit with meaningful messages.** One commit per logical change. The message says what changed, not why the change matters (that lives in the document body).
8. **Agent instructions live here.** Updates to agent/LLM instructions go into this file. Tool-specific files (`CLAUDE.md`, etc.) only point here.
