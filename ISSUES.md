# Status & Issues

## Status

| Symbol | Meaning |
|---|---|
| 🟢 Stable | Reviewed, agreed; changes need an ADR |
| 🟡 Draft | Written, not yet reviewed |
| 🔴 Not started | Skeleton; little or no content |

| Document | Status | Owner |
|---|---|---|
| [Problem Statement](docs/problem/01-problem-statement.md) | 🟡 Draft | TBD |
| [Risks & Importance](docs/problem/02-risks-and-importance.md) | 🟡 Draft | TBD |
| [Stakeholders & Use Cases](docs/problem/03-stakeholders-use-cases.md) | 🟡 Draft — use cases are candidates | TBD |
| [Requirements](docs/problem/04-requirements.md) | 🟡 Draft — candidates | TBD |
| [Current State & Constraints](docs/problem/05-current-state-constraints.md) | 🔴 Not started | TBD |
| [Principles](docs/solution/01-principles.md) | 🟡 Draft | TBD |
| [Conceptual Model](docs/solution/02-conceptual-model.md) | 🔴 Not started — dimensions are ideas | TBD |
| [Models, Policy & Governance](docs/solution/03-models-policy-governance.md) | 🔴 Not started | TBD |
| [Process, Rules & Activities](docs/solution/04-process-rules-activities.md) | 🔴 Not started | TBD |
| [Core Platforms](docs/solution/05-core-platforms.md) | 🔴 Not started | TBD |
| [Supporting Features](docs/solution/06-supporting-features.md) | 🔴 Not started | TBD |
| [Roadmap](docs/delivery/01-roadmap.md) | 🟡 Draft | TBD |
| [Migration](docs/delivery/02-migration.md) | 🔴 Not started | TBD |
| [Risk Register](docs/delivery/03-risk-register.md) | 🔴 Not started | TBD |
| [Success Dimensions](docs/delivery/04-success-dimensions.md) | 🟡 Draft — thresholds `[T]` | TBD |
| [Glossary](docs/glossary.md) | 🟡 Draft | TBD |
| [Estate disposition](docs/data/estate-disposition.csv) | 🔴 Header only | TBD |
| ADRs | — None yet | — |
| [Idea: Discovery decoupled from inventory](docs/ideas/discovery-decoupled-from-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Bitemporal, modal inventory](docs/ideas/bitemporal-modal-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Source of truth dimensions](docs/ideas/source-of-truth-dimensions.md) | 🟡 Idea | Matthias |
| [Idea: Multi-agent coordination](docs/ideas/multi-agent-coordination.md) | 🟡 Idea | Matthias |

## Open Issues

Cross-cutting issues only. Questions local to one document stay in that document's Key Questions.

| ID | Issue | Where | Next step |
|---|---|---|---|
| I-1 | Use cases are candidates, not validated | [Use cases](docs/problem/03-stakeholders-use-cases.md) | Review with Network Services |
| I-2 | Thresholds not set | [Success Dimensions](docs/delivery/04-success-dimensions.md) | Baseline in Phase 1 |
| I-3 | Domains, owners, and current systems unknown | [Current State](docs/problem/05-current-state-constraints.md) | Estate first pass |
| I-4 | Constraints (firm-wide standards, platforms, regulatory) not captured | [Current State](docs/problem/05-current-state-constraints.md) | Collect from CFP management |
| I-5 | R-7, Q-4 trace to no principle | [Requirements](docs/problem/04-requirements.md) | Decide: add principle or accept |
| I-6 | Effort sizes not set | [Roadmap](docs/delivery/01-roadmap.md) | Size at Phase 0 start |
| I-7 | Precedence when modalities or oracles disagree | [Ideas](docs/ideas/source-of-truth-dimensions.md) | Discuss |
| I-8 | Knowledge Platform history: derived or snapshots? | [Core Platforms](docs/solution/05-core-platforms.md) | Discuss |
| I-9 | Trace matrix mixes two kinds of principle. System properties (P1, P2, P4, P6, P7, P9, P10) and decision/sequencing rules (P3, P5, P8) are traced uniformly, producing weak traces: R-2 → P8, R-6 → P7, Q-1 → P1. | [Requirements](docs/problem/04-requirements.md), [Principles](docs/solution/01-principles.md) | Split the principles table into two groups, or add a trace strength column |
| I-10 | Nine use-case actors, three named stakeholders; no actor-to-stakeholder mapping | [Use cases](docs/problem/03-stakeholders-use-cases.md) | Map actors to stakeholder roles during validation |
| I-11 | P-numbers were reassigned during the last restructure (P7, P8 changed meaning). The ID-stability rule in [AGENTS.md](AGENTS.md) now forbids this; earlier citations may be stale. | [Principles](docs/solution/01-principles.md) | Freeze P-numbers; anchor future traceability on concern names |
