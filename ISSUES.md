# Status and Issues

The status of every document, and the open issues that affect more than one document.

## Status

| Symbol | Meaning |
|---|---|
| 🟢 Stable | Reviewed, agreed; changes need an ADR |
| 🟡 Draft | Written, not yet reviewed |
| 🔴 Not started | Skeleton; little or no content |

| Document | Status | Owner |
|---|---|---|
| [Vision](docs/problem/00-vision.md) | 🟡 Draft | TBD |
| [Problem Statement](docs/problem/01-problem-statement.md) | 🟡 Draft | TBD |
| [Stakeholders & Use Cases](docs/problem/02-stakeholders-use-cases.md) | 🟡 Draft — use cases are candidates | TBD |
| [Requirements](docs/problem/03-requirements.md) | 🟡 Draft — candidates | TBD |
| [Current State & Constraints](docs/problem/04-current-state-constraints.md) | 🔴 Not started | TBD |
| [Principles](docs/solution/01-principles.md) | 🟡 Draft | TBD |
| [Conceptual Model](docs/solution/02-conceptual-model.md) | 🔴 Not started — dimensions are ideas | TBD |
| [Models, Policy & Governance](docs/solution/03-models-policy-governance.md) | 🔴 Not started | TBD |
| [Process, Rules & Activities](docs/solution/04-process-rules-activities.md) | 🔴 Not started | TBD |
| [Core Platforms](docs/solution/05-core-platforms.md) | 🔴 Not started | TBD |
| [Supporting Features](docs/solution/06-supporting-features.md) | 🔴 Not started | TBD |
| [Roadmap](docs/ways-of-working/01-roadmap.md) | 🟡 Draft | TBD |
| [Migration](docs/ways-of-working/02-migration.md) | 🔴 Not started | TBD |
| [Risk Register](docs/ways-of-working/03-risk-register.md) | 🔴 Not started | TBD |
| [Success Dimensions](docs/ways-of-working/04-success-dimensions.md) | 🟡 Draft — thresholds `[T]` | TBD |
| [Glossary](docs/glossary.md) | 🟡 Draft | TBD |
| [Estate disposition](docs/data/estate-disposition.csv) | 🔴 Header only | TBD |
| [Use cases & competency questions](docs/data/use-cases.yaml) | 🟡 Draft — 16 use cases, 25 questions, all candidates | TBD |
| ADRs | — None yet | — |
| [Idea: Discovery decoupled from inventory](docs/ideas/discovery-decoupled-from-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Bitemporal, modal inventory](docs/ideas/bitemporal-modal-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Source of truth dimensions](docs/ideas/source-of-truth-dimensions.md) | 🟡 Idea | Matthias |
| [Idea: Multi-agent coordination](docs/ideas/multi-agent-coordination.md) | 🟡 Idea | Matthias |
| [Idea: Model and interface standards landscape](docs/ideas/model-standards-landscape.md) | 🟡 Idea — verdicts per layer, no decisions | Matthias |

## Open Issues

Only issues that affect more than one document are listed here; questions about a single document stay in that document. Gaps in the numbering are retired IDs.

We are currently working on structure: the shape of the solution, the models, and our conventions. Facts about today's systems, owners, and domains will come from the first pass over the estate. Issues that depend on those facts are marked *deferred*.

| ID | Issue | Where | Next step |
|---|---|---|---|
| I-1 | Use cases (UC-1…16) are candidates, not validated | [Use cases](docs/problem/02-stakeholders-use-cases.md) | Review with Network Services |
| I-2 | Thresholds not set | [Success Dimensions](docs/ways-of-working/04-success-dimensions.md) | Baseline in Phase 1 |
| I-3 | Domains, owners, and current systems unknown | [Current State](docs/problem/04-current-state-constraints.md) | Estate first pass |
| I-4 | Constraints (firm-wide standards, platforms, regulatory) not captured | [Current State](docs/problem/04-current-state-constraints.md) | Collect from CFP management |
| I-5 | R-7, Q-4 trace to no principle | [Requirements](docs/problem/03-requirements.md) | Decide: add principle or accept |
| I-6 | Effort sizes not set | [Roadmap](docs/ways-of-working/01-roadmap.md) | Size at Phase 0 start |
| I-7 | Precedence when modalities or oracles disagree | [Ideas](docs/ideas/source-of-truth-dimensions.md) | Discuss |
| I-8 | Knowledge Platform history: derived or snapshots? | [Core Platforms](docs/solution/05-core-platforms.md) | Discuss |
| I-9 | The principles mix two kinds: properties of the system (P1, P2, P4, P6, P7, P9, P10) and rules for how we decide or sequence work (P3, P5, P8). The requirements table treats them alike, which produces weak links, for example R-2 to P8, R-6 to P7, and Q-1 to P1. | [Requirements](docs/problem/03-requirements.md), [Principles](docs/solution/01-principles.md) | Split the principles table into two groups, or add a trace strength column |
| I-10 | Actors map to stakeholders through activity owners (AC-n); owners not yet named. **Deferred** — needs organizational facts. | [Use cases](docs/problem/02-stakeholders-use-cases.md) | Map during use-case validation with Network Services |
| I-12 | Policy language not chosen. Important; decide after the policy model (D1) is drafted. | [Standards landscape](docs/ideas/model-standards-landscape.md) | Evaluate candidates against D1 |
| I-13 | Vision claims not yet covered by requirements: quality and lineage alongside data, answer assembly (access modes: R-11; freshness: R-14) | [Vision](docs/problem/00-vision.md), [Requirements](docs/problem/03-requirements.md) | Add requirements traced to vision claims |
