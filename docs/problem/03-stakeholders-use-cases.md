# Stakeholders & Use Cases

## Stakeholders

| Role | Who | Interest |
|---|---|---|
| **Key stakeholder** | Core Foundational Platforms (CFP) management | Sponsor; owns outcome, scope, priorities |
| **First customer** | Network Services | First-domain consumers; validate use cases; set first thresholds |
| **AI agents** | Build-, design-, and run-time agents | See below |
| **Others** | TBD (audit, security, capacity planning, operations) | TBD |

## AI in Three Roles

| Role | Agents help to… | Implication |
|---|---|---|
| **Build** | Write docs, code, adapters, tests | Conventions and contracts machine-readable ([AGENTS.md](../../AGENTS.md)) |
| **Design** | Model, map sources, draft policy | Models and policies formal and versioned |
| **Use** | Analyse, decide, automate on live data | API + MCP for meaningful functions (P9); deterministic core (P10) |

## Use Cases

Candidates derived from the existing documents. Each is validated with Network Services before it drives requirements beyond Phase 0.

| ID | Actor | Use case | Derived from | Status |
|---|---|---|---|---|
| UC-1 | Auditor | Which devices hold customer data — now, and as of a past date? | [Risks: Compliance](02-risks-and-importance.md) | Candidate |
| UC-2 | Incident responder | Find topology, config, and dependencies for an affected device during an incident | [Risks: Operational](02-risks-and-importance.md) | Candidate |
| UC-3 | Engineer | Find what data exists, where it lives, what it means (e.g. authoritative device count) | [Success: Discoverability](../ways-of-working/04-success-dimensions.md) | Candidate |
| UC-4 | Change engineer | Impact analysis: if I change this IP, link, or device, what breaks? | [Process](../solution/04-process-rules-activities.md) | Candidate |
| UC-5 | Capacity planner | Know existing and planned capacity before buying | [Risks: Bad Decisions](02-risks-and-importance.md) | Candidate |
| UC-6 | Data steward | Detect and resolve drift between discovered, asserted, and planned state | [Idea: bitemporal, modal inventory](../ideas/bitemporal-modal-inventory.md) | Candidate |
| UC-7 | Security | Find unknown devices; check segmentation intent against actual | [Risks: Security](02-risks-and-importance.md) | Candidate |
| UC-8 | AI agent | Analyse, recommend, or automate on network data and policy, citing sources | [Features: AI](../solution/06-supporting-features.md) | Candidate |
| UC-9 | Platform owner | Onboard a new source or consumer through a contract, without core code | [P2](../solution/01-principles.md) | Candidate |
