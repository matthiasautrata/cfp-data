# Stakeholders & Use Cases

> Use cases and competency questions live in [`use-cases.yaml`](../data/use-cases.yaml). The tables under *Use Cases* are generated from it and refresh on commit (pre-commit hook); by hand: `uv run tools/render_use_cases.py`. If they differ, the YAML wins.

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

Use cases are organised by activity. Names follow [ITIL 4](../references/itil4.md) practices, the vocabulary stakeholders already use; [FCAPS](../references/fcaps-m3400.md) is the network-specific crosswalk. ITIL's vocabulary is adopted, not its CMDB-as-single-truth doctrine ([source of truth dimensions](../ideas/source-of-truth-dimensions.md)). Two activities are outside ITIL. FCAPS has no asset function: its A is accounting (usage, cost, billing); inventory sits under Configuration, hence AC-2 → C.

| ID | Activity | ITIL 4 | FCAPS | Core question |
|---|---|---|---|---|
| AC-1 | Configuration | Service configuration management | C | What exists, how is it configured, how is it related? |
| AC-2 | Asset & lifecycle | IT asset management | C | Who owns it, where is it, when does support end? |
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

Each use case is a set of [competency questions](../references/competency-questions.md): questions the data must answer. Each question doubles as an acceptance test and an agent evaluation item. Questions name the *fact dimensions* they need (from the [conceptual model](../solution/02-conceptual-model.md)) separately from *answer requirements* (dependency traversal, freshness), which constrain the answer, not the fact. All are candidates until validated with Network Services and the activity owners.

<!-- BEGIN GENERATED: tools/render_use_cases.py from docs/data/use-cases.yaml. Do not edit. -->
### Use Cases

| ID | Activity | Actor | Need | Questions | Driver | Status |
|---|---|---|---|---|---|---|
| UC-1 | AC-12 | Auditor | Customer-data devices, as of a date and as recorded then | CQ-1, CQ-2 | [Compliance](01-problem-statement.md#compliance--audit-risk) | candidate |
| UC-2 | AC-4 | Incident responder | Blast radius and recent changes for an affected device | CQ-3, CQ-4 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-3 | AC-13 | Engineer | What data exists, where, what it means; which count is authoritative | CQ-5, CQ-6 | [Discoverability](../ways-of-working/04-success-dimensions.md) | candidate |
| UC-4 | AC-6 | Change engineer | Impact of a planned change | CQ-7 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-5 | AC-7 | Capacity planner | Actual and planned capacity; projected shortfalls | CQ-8, CQ-9 | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) | candidate |
| UC-6 | AC-14 | Data steward | Disagreements across modalities, and who decides | CQ-10, CQ-11 | [Source of truth dimensions](../ideas/source-of-truth-dimensions.md) | candidate |
| UC-7 | AC-9 | Security | Unknown devices; segmentation not as intended | CQ-12, CQ-13 | [Security](01-problem-statement.md#security-risk) | candidate |
| UC-8 | AC-15 | AI agent | Answers with cited facts, sources, and policy | CQ-14 | [Features: AI](../solution/06-supporting-features.md) | candidate |
| UC-9 | AC-14 | Platform owner | Contracts in use, by source and consumer | CQ-15 | [P2](../solution/01-principles.md) | candidate |
| UC-10 | AC-3 | Operator | Current state and related events | CQ-16, CQ-17 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-11 | AC-5 | Problem manager | State at each recurrence of an incident class | CQ-18 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-12 | AC-8 | Resilience owner | Assets behind a critical function; single points of failure | CQ-19, CQ-20 | [DORA Art. 8](../references/dora-art8.md) | candidate |
| UC-13 | AC-2 | Asset owner | Assets nearing end of support, with owner and location | CQ-21 | [NYDFS 500.13](../references/nydfs-500-13.md) | candidate |
| UC-14 | AC-10 | Provisioning engineer | Planned vs built, per site | CQ-22 | [RFC 9315](../references/rfc9315-ibn.md) | candidate |
| UC-15 | AC-11 | Architect | Consolidation candidates | CQ-23 | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) | candidate |
| UC-16 | AC-1 | Network engineer | A device's configuration, now and as of a date, and its relationships | CQ-24, CQ-25 | [Problem statement](01-problem-statement.md) | candidate |

### Competency Questions

| ID | Use case | Question | Entities | Fact dimensions | Answer requirements | Answer | Status |
|---|---|---|---|---|---|---|---|
| CQ-1 | UC-1 | Which devices held customer data on `<date>`? | device, data_classification | valid_time, source_authority, provenance | — | list of devices with classification and source | candidate |
| CQ-2 | UC-1 | What did our records say about which devices held customer data, as recorded on `<date>`? | device, data_classification | record_time, source_authority, provenance | — | list of devices as recorded, with provenance | candidate |
| CQ-3 | UC-2 | What is connected to `<device>`, and what depends on it? | device, interface, link, service | — | dependencies, freshness | dependency graph rooted at the device | candidate |
| CQ-4 | UC-2 | What changed on or around `<device>` in the last `<hours>`? | device, change, configuration | record_time | dependencies, freshness | ordered list of changes with source and time | candidate |
| CQ-5 | UC-3 | What data exists about `<entity type>`, where does it live, and what does it mean? | entity_type, source, definition | source_authority, provenance | — | registry entries with locations and definitions | candidate |
| CQ-6 | UC-3 | Which count of `<entity type>` is authoritative, and on whose authority? | entity_type, source | oracle_authority, source_authority, provenance | — | count with source authority and provenance | candidate |
| CQ-7 | UC-4 | If `<IP | link | device>` changes, which devices and services are affected? | ip_address, link, device, service | modality | dependencies | impacted set with dependency paths | candidate |
| CQ-8 | UC-5 | What capacity exists and is planned, per site? | site, device, capacity_metric | valid_time, modality | — | capacity per site, actual and planned | candidate |
| CQ-9 | UC-5 | Where and when does projected demand exceed capacity? | site, capacity_metric | valid_time, modality | — | list of site, resource, and date of shortfall | candidate |
| CQ-10 | UC-6 | Where do discovered, asserted, and planned state disagree for `<entity type>`? | entity_type | modality, source_authority, provenance | — | list of disagreements with values per modality | candidate |
| CQ-11 | UC-6 | Which authority decides each disagreement? | entity_type, source | oracle_authority, source_authority, provenance | — | per disagreement, the deciding oracle or source authority | candidate |
| CQ-12 | UC-7 | Which devices are discovered but unknown to inventory? | device | modality | — | list of discovered-only devices with discovery provenance | candidate |
| CQ-13 | UC-7 | Where does actual segmentation differ from intended segmentation? | segment, policy, device | modality | — | list of segment violations, intended vs observed | candidate |
| CQ-14 | UC-8 | For question `<Q>`, what is the answer, which facts and sources support it, and which policy applies? | any | valid_time, record_time, modality, source_authority, provenance | — | answer with cited facts, sources, and applicable policy | candidate |
| CQ-15 | UC-9 | Which contracts exist, in which versions, and which sources and consumers use each? | contract, source, consumer | valid_time | — | contract catalogue with users per version | candidate |
| CQ-16 | UC-10 | What is the current operational state of `<entity>`? | device, interface, link | modality | freshness | state with observation time | candidate |
| CQ-17 | UC-10 | Which events relate to `<entity>` within `<window>`? | event, device | valid_time | freshness | ordered list of events | candidate |
| CQ-18 | UC-11 | What were configuration and topology of `<affected set>` at each occurrence of incident class `<Y>`? | incident, device, configuration, link | valid_time, record_time | dependencies | per occurrence, configuration and topology snapshot views | candidate |
| CQ-19 | UC-12 | Which assets and dependencies support critical function `<F>`? | business_function, asset, service | valid_time | dependencies | dependency graph from function to assets | candidate |
| CQ-20 | UC-12 | Which of those assets or links are single points of failure? | asset, link | — | dependencies | list of single points of failure per function | candidate |
| CQ-21 | UC-13 | Which assets reach end of support within `<horizon>`, who owns them, and where are they? | asset, owner, site · attributes: owner, location, support_expiration_date | valid_time | — | list of asset, owner, location, support end date | candidate |
| CQ-22 | UC-14 | For site `<S>`, what is planned, and what is built? | site, device, link | modality, valid_time | — | planned vs built, per element | candidate |
| CQ-23 | UC-15 | Which assets or functions are duplicated or under-used? | asset, service, capacity_metric | valid_time | dependencies | consolidation candidates with evidence | candidate |
| CQ-24 | UC-16 | What is `<device>`, and how is it configured, now and as of `<date>`? | device, configuration | valid_time, record_time, modality | — | device record with configuration per modality | candidate |
| CQ-25 | UC-16 | How is `<device>` related to other entities? | device, interface, link, site, service | — | dependencies | relationship graph | candidate |
<!-- END GENERATED -->
