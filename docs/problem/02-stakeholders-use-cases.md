# Stakeholders & Use Cases

## Stakeholders

| Role | Who | Interest |
|---|---|---|
| **Key stakeholder** | Core Foundational Platforms (CFP) management | Sponsor; owns outcome, scope, priorities |
| **First customer** | Network Services | First-domain consumers; validate use cases; set first thresholds |
| **AI agents** | Build-, design-, and run-time agents | See below |
| **Activity owners** | Owners of the activities below (TBD per activity) | Validate their use cases; own their thresholds |

## AI in Three Roles

| Role | Agents help to… | Implication |
|---|---|---|
| **Build** | Write docs, code, adapters, tests | Conventions and contracts machine-readable ([AGENTS.md](../../AGENTS.md)) |
| **Design** | Model, map sources, draft policy | Models and policies formal and versioned |
| **Use** | Analyse, decide, automate on live data | API + MCP for meaningful functions (P9); deterministic core (P10) |

## Activity Catalogue

Use cases are organised by activity. Names follow [ITIL 4](../references/itil4.md) practices, the vocabulary stakeholders already use; [FCAPS](../references/fcaps-m3400.md) is the network-specific crosswalk. ITIL's vocabulary is adopted, not its CMDB-as-single-truth doctrine ([source of truth dimensions](../ideas/source-of-truth-dimensions.md)). Two activities are outside ITIL.

| ID | Activity | ITIL 4 | FCAPS | Core question |
|---|---|---|---|---|
| AC-1 | Configuration | Service configuration management | C | What exists, how is it configured, how is it related? |
| AC-2 | Asset & lifecycle | IT asset management | A | Who owns it, where is it, when does support end? |
| AC-3 | Monitoring & events | Monitoring and event management | F, P | What is happening now? |
| AC-4 | Incident | Incident management | F | What is affected, and what changed? |
| AC-5 | Problem | Problem management | F | What was the state each time this recurred? |
| AC-6 | Change | Change enablement | C | What breaks if I change X? |
| AC-7 | Capacity & performance | Capacity and performance management | P | Where is headroom short, now and projected? |
| AC-8 | Availability & continuity | Availability; service continuity management | F | What supports critical functions; where are single points of failure? |
| AC-9 | Security | Information security management | S | What is unknown, exposed, or not as intended? |
| AC-10 | Provisioning | Deployment; infrastructure and platform management | C | What does the plan say; what is built? |
| AC-11 | Architecture & planning | Architecture management | — | What to buy, retire, consolidate? |
| AC-12 | Reporting & audit | Measurement and reporting | — | What did we know, and when? |
| AC-13 | Knowledge | Knowledge management | — | What data exists, where, and what does it mean? |
| AC-14 | Data stewardship & onboarding | — | — | Where do sources disagree; how does a new source join? |
| AC-15 | Agent analysis & automation | — | — | Answer, recommend, or act, with sources and policy |

Other frames considered: [eTOM](../references/tmf-etom.md) (operator scope, too heavy), FCAPS alone (no planning, lifecycle, or governance). Audit controls map via [COBIT 2019](../references/cobit2019.md).

## Use Cases

Each use case is a set of [competency questions](../references/competency-questions.md): questions the data must answer. Question text, entities, and data dimensions live in the [register](../data/competency-questions.yaml); this table references them. Each question doubles as an acceptance test and an agent evaluation item.

All use cases are candidates until validated with Network Services and the activity owners.

| ID | Activity | Actor | Need | Questions | Driver |
|---|---|---|---|---|---|
| UC-1 | AC-12 | Auditor | Customer-data devices, as of a date and as recorded then | CQ-1, CQ-2 | [Compliance](01-problem-statement.md#compliance--audit-risk) |
| UC-2 | AC-4 | Incident responder | Blast radius and recent changes for an affected device | CQ-3, CQ-4 | [Operational](01-problem-statement.md#operational-risk) |
| UC-3 | AC-13 | Engineer | What data exists, where, what it means; which count is authoritative | CQ-5, CQ-6 | [Discoverability](../ways-of-working/04-success-dimensions.md) |
| UC-4 | AC-6 | Change engineer | Impact of a planned change | CQ-7 | [Operational](01-problem-statement.md#operational-risk) |
| UC-5 | AC-7 | Capacity planner | Actual and planned capacity; projected shortfalls | CQ-8, CQ-9 | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) |
| UC-6 | AC-14 | Data steward | Disagreements across modalities, and who decides | CQ-10, CQ-11 | [Source of truth dimensions](../ideas/source-of-truth-dimensions.md) |
| UC-7 | AC-9 | Security | Unknown devices; segmentation not as intended | CQ-12, CQ-13 | [Security](01-problem-statement.md#security-risk) |
| UC-8 | AC-15 | AI agent | Answers with cited facts, sources, and policy | CQ-14 | [Features: AI](../solution/06-supporting-features.md) |
| UC-9 | AC-14 | Platform owner | Contracts in use, by source and consumer | CQ-15 | [P2](../solution/01-principles.md) |
| UC-10 | AC-3 | Operator | Current state and related events | CQ-16, CQ-17 | [Operational](01-problem-statement.md#operational-risk) |
| UC-11 | AC-5 | Problem manager | State at each recurrence of an incident class | CQ-18 | [Operational](01-problem-statement.md#operational-risk) |
| UC-12 | AC-8 | Resilience owner | Assets behind a critical function; single points of failure | CQ-19, CQ-20 | [DORA Art. 8](../references/dora-art8.md) |
| UC-13 | AC-2 | Asset owner | Assets nearing end of support, with owner and location | CQ-21 | [NYDFS 500.13](../references/nydfs-500-13.md) |
| UC-14 | AC-10 | Provisioning engineer | Planned vs built, per site | CQ-22 | [RFC 9315](../references/rfc9315-ibn.md) |
| UC-15 | AC-11 | Architect | Consolidation candidates | CQ-23 | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) |
| UC-16 | AC-1 | Network engineer | A device's configuration, now and as of a date, and its relationships | CQ-24, CQ-25 | [Problem statement](01-problem-statement.md) |
