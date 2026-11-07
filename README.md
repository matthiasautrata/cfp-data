# Network Data — Target State Architecture & Migration

Working conventions for humans and agents: [`AGENTS.md`](AGENTS.md).

## Document Map

```
cfp-data/
├── README.md                          # This file — document map, status
├── AGENTS.md                          # Working conventions (humans + agents)
├── CLAUDE.md                          # Pointer to AGENTS.md
└── docs/
    ├── 01-problem-statement.md        # The problem we're solving (short, pithy, precise)
    ├── 02-risks-and-importance.md     # Why this matters — risk categories
    ├── 03-architecture-principles.md  # Guiding principles for the target state
    ├── 04-major-areas-of-work/
    │   ├── 04-01-models-policy-governance.md
    │   ├── 04-02-process-rules-activities.md
    │   ├── 04-03-core-platforms-mapping.md
    │   ├── 04-04-supporting-features.md
    │   ├── 04-05-migration-strategy.md
    │   └── 04-06-risks-mitigations.md
    ├── 05-initiatives-roadmap.md      # Initiatives, priorities, sequencing
    ├── 06-success-dimensions.md       # How we measure success
    ├── 07-glossary.md                 # Terms, acronyms, conventions
    ├── adr/                           # Architecture Decision Records (NNNN-title.md)
    ├── ideas/                         # Early, non-binding thinking; promoted to ADRs when agreed
    ├── references/                    # External sources (short-name.md)
    └── templates/
        └── decision-record.md         # ADR template
```

---

## Status

| Section | Status | Owner |
|---|---|---|
| [Problem Statement](docs/problem/01-problem-statement.md) | 🟡 Draft | TBD |
| [Risks & Importance](docs/problem/02-risks-and-importance.md) | 🟡 Draft | TBD |
| [Architecture Principles](docs/solution/01-principles.md) | 🟡 Draft | TBD |
| [Models, Policy, Governance](docs/solution/03-models-policy-governance.md) | 🔴 Not started | TBD |
| [Process, Rules, Activities](docs/solution/04-process-rules-activities.md) | 🔴 Not started | TBD |
| [Core Platforms Mapping](docs/solution/05-core-platforms.md) | 🔴 Not started | TBD |
| [Supporting Features](docs/solution/06-supporting-features.md) | 🔴 Not started | TBD |
| [Migration Strategy](docs/delivery/02-migration.md) | 🔴 Not started | TBD |
| [Risks & Mitigations](docs/delivery/03-risk-register.md) | 🔴 Not started | TBD |
| [Initiatives Roadmap](docs/delivery/01-roadmap.md) | 🟡 Draft | TBD |
| [Success Dimensions](docs/delivery/04-success-dimensions.md) | 🟡 Draft | TBD |
| [Glossary](docs/glossary.md) | 🟡 Draft | TBD |
| ADRs | 🔴 None yet | — |
| [Idea: Discovery decoupled from inventory](docs/ideas/discovery-decoupled-from-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Bitemporal, modal inventory](docs/ideas/bitemporal-modal-inventory.md) | 🟡 Idea | Matthias |
| [Idea: Source of truth dimensions](docs/ideas/source-of-truth-dimensions.md) | 🟡 Idea | Matthias |

---

## Key Relationships

```mermaid
flowchart LR
    P[Principles] --> M[Models & Policy]
    P --> R[Rules & Activities]
    M --> C[Core Platforms]
    R --> C
    C --> F[Supporting Features]
    C --> S[Migration Strategy]
    S --> L[Legacy Platforms]
    L --> F
    F --> D[Success Dimensions]
    R --> D
```

---

## Quick Reference — Inputs Mapped to Structure

| Your input | Lives in |
|---|---|
| "Define data we need" | [Models, Policy & Governance](docs/solution/03-models-policy-governance.md) |
| "Decide what stays and what goes" | [Migration Strategy](docs/delivery/02-migration.md) + [Success Dimensions](docs/delivery/04-success-dimensions.md) (Estate Decisions) |
| "Make data discoverable" | [Supporting Features](docs/solution/06-supporting-features.md) (Discovery) |
| "Govern by policy" | [Models, Policy & Governance](docs/solution/03-models-policy-governance.md) |
| "Trusted, resilient data" | [Mapping to Core Platforms](docs/solution/05-core-platforms.md) + [Success Dimensions](docs/delivery/04-success-dimensions.md) (Resilience, Quality) |
| "Observe the network" | [Supporting Features](docs/solution/06-supporting-features.md) (Telemetry) |
| "Enabler and adoption" | [Process, Rules & Activities](docs/solution/04-process-rules-activities.md) + [Success Dimensions](docs/delivery/04-success-dimensions.md) (Adoption) |
| Topology | [Mapping to Core Platforms](docs/solution/05-core-platforms.md) (Instances: static + time-series) |
| Infrastructure assets | [Mapping to Core Platforms](docs/solution/05-core-platforms.md) (Instances: static) |
| Registry for meta-data | [Mapping to Core Platforms](docs/solution/05-core-platforms.md) (Meta-data platform) |
| Keep existing infrastructure alive | [Migration Strategy](docs/delivery/02-migration.md) |
| State and intent is declarative | [Architecture Principles](docs/solution/01-principles.md) (P6) |
| Policy drive | [Models, Policy & Governance](docs/solution/03-models-policy-governance.md) |
