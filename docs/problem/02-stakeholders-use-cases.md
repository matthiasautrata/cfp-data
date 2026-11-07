# Stakeholders and Use Cases

> The use cases and their questions are kept in one file, [`use-cases.yaml`](../data/use-cases.yaml). The two tables at the end of this document are generated from it. They refresh automatically when you commit; to refresh them by hand, run `uv run tools/render_use_cases.py`. If a table and the file disagree, the file is correct.

## Stakeholders

| Role | Who | Interest |
|---|---|---|
| **Key stakeholder** | Core Foundational Platforms (CFP) management | Sponsors the program; owns its outcome, scope, and priorities |
| **First customer** | Network Services | Uses the first domain; reviews the use cases; helps set the first thresholds |
| **Activity owners** | The owner of each activity listed below (not yet named) | Review the use cases for their activity; own its thresholds |
| **AI agents** | Agents that help build, design, and use the system | See the next section |

## AI in Three Roles

AI matters here in three distinct ways.

| Role | Agents help to… | What this asks of the design |
|---|---|---|
| **Build** | Write documents, code, adapters, and tests | Conventions and contracts that a machine can read ([AGENTS.md](../../AGENTS.md)) |
| **Design** | Model data, map sources, draft policies | Models and policies kept in a formal, versioned form |
| **Use** | Analyze, decide, and automate on live data | Every meaningful function available through an API and MCP (principle P9); a deterministic core, with agents at the edge (principle P10) |

## Activity Catalog

We group use cases by the activity they support. Activity names follow [ITIL 4](../references/itil4.md), because that is the vocabulary our stakeholders already use. We adopt ITIL's names, not its assumption that a single configuration management database is the source of truth ([idea: source of truth dimensions](../ideas/source-of-truth-dimensions.md)).

For network specialists, the table also shows [FCAPS](../references/fcaps-m3400.md), the classic set of network management functions: Fault, Configuration, Accounting, Performance, and Security. FCAPS has no separate asset function. Its A stands for accounting (usage, cost, and billing), and inventory belongs under Configuration, so asset management maps to C. Two activities, data stewardship and agent analysis, fall outside ITIL.

| ID | Activity | ITIL 4 practice | FCAPS | Core question |
|---|---|---|---|---|
| AC-1 | Configuration | Service configuration management | C | What exists, how is it configured, and how is it related? |
| AC-2 | Asset and lifecycle | IT asset management | C | Who owns it, where is it, and when does support end? |
| AC-3 | Monitoring and events | Monitoring and event management | F, P | What is happening now? |
| AC-4 | Incident | Incident management | F | What is affected, and what changed? |
| AC-5 | Problem | Problem management | F | What was the state each time this happened? |
| AC-6 | Change | Change enablement | C | What breaks if I change this? |
| AC-7 | Capacity and performance | Capacity and performance management | P | Where is capacity short, now and in future? |
| AC-8 | Availability and continuity | Availability management; service continuity management | F | What supports critical functions, and where are the single points of failure? |
| AC-9 | Security | Information security management | S | What is unknown, exposed, or not as intended? |
| AC-10 | Provisioning | Deployment management; infrastructure and platform management | C | What does the plan say, and what has been built? |
| AC-11 | Architecture and planning | Architecture management | — | What should we buy, retire, or consolidate? |
| AC-12 | Reporting and audit | Measurement and reporting | — | What did we know, and when? |
| AC-13 | Knowledge | Knowledge management | — | What data exists, where is it, and what does it mean? |
| AC-14 | Data stewardship and onboarding | — | — | Where do sources disagree, and how does a new source join? |
| AC-15 | Agent analysis and automation | — | — | Answer, recommend, or act, citing sources and policy |

We considered two other frameworks. TM Forum [eTOM](../references/tmf-etom.md) is written for telecom operators and is too heavy for an internal network. FCAPS on its own has no planning, lifecycle, or governance activities. Audit controls map to [COBIT 2019](../references/cobit2019.md).

## Use Cases

Each use case is described by one or more [competency questions](../references/competency-questions.md): concrete questions the data must be able to answer. Later, each question becomes an acceptance test for the platform and a test item for AI agents.

For each question we note what it needs:

- **Fact dimensions**: information kept with every fact, such as when it was true or how we know it. These are defined in the [conceptual model](../solution/02-conceptual-model.md).
- **Answer requirements**: needs that apply to the answer rather than to the stored facts, such as following dependencies, or a limit on how old the data may be.

These are early candidates. We are still collecting questions, and details such as which dimensions a question needs will be added or corrected as we learn more. A dash means "not yet identified", not "none". All use cases will be reviewed with Network Services and the activity owners.

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
| UC-8 | AC-15 | AI agent | Answers with cited facts, sources, and policy | CQ-14 | [Consumers: AI agents](../solution/06-producers-consumers.md) | candidate |
| UC-9 | AC-14 | Platform owner | Contracts in use, by source and consumer | CQ-15 | [P2](../solution/01-principles.md) | candidate |
| UC-10 | AC-3 | Operator | Current state and related events | CQ-16, CQ-17 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-11 | AC-5 | Problem manager | State at each recurrence of an incident class | CQ-18 | [Operational](01-problem-statement.md#operational-risk) | candidate |
| UC-12 | AC-8 | Resilience owner | Assets behind a critical function; single points of failure | CQ-19, CQ-20 | [DORA Art. 8](../references/dora-art8.md) | candidate |
| UC-13 | AC-2 | Asset owner | Assets nearing end of support, with owner and location | CQ-21 | [NYDFS 500.13](../references/nydfs-500-13.md) | candidate |
| UC-14 | AC-10 | Provisioning engineer | Planned vs built, per site | CQ-22 | [RFC 9315](../references/rfc9315-ibn.md) | candidate |
| UC-15 | AC-11 | Architect | Consolidation candidates | CQ-23 | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) | candidate |
| UC-16 | AC-1 | Network engineer | A device's configuration, now and as of a date, and its relationships | CQ-24, CQ-25 | [Problem statement](01-problem-statement.md) | candidate |

### Competency Questions

| ID | Use case | Question | Entities | Fact dimensions | Answer requirements | Expected answer | Status |
|---|---|---|---|---|---|---|---|
| CQ-1 | UC-1 | Which devices held customer data on `<date>`? | device, data classification | valid time, source authority, provenance | — | list of devices with classification and source | candidate |
| CQ-2 | UC-1 | What did our records say about which devices held customer data, as recorded on `<date>`? | device, data classification | record time, source authority, provenance | — | list of devices as recorded, with provenance | candidate |
| CQ-3 | UC-2 | What is connected to `<device>`, and what depends on it? | device, interface, link, service | — | dependencies, freshness | dependency graph rooted at the device | candidate |
| CQ-4 | UC-2 | What changed on or around `<device>` in the last `<hours>`? | device, change, configuration | record time | dependencies, freshness | ordered list of changes with source and time | candidate |
| CQ-5 | UC-3 | What data exists about `<entity type>`, where does it live, and what does it mean? | entity type, source, definition | source authority, provenance | — | registry entries with locations and definitions | candidate |
| CQ-6 | UC-3 | Which count of `<entity type>` is authoritative, and on whose authority? | entity type, source | oracle authority, source authority, provenance | — | count with source authority and provenance | candidate |
| CQ-7 | UC-4 | If `<IP | link | device>` changes, which devices and services are affected? | ip address, link, device, service | modality | dependencies | impacted set with dependency paths | candidate |
| CQ-8 | UC-5 | What capacity exists and is planned, per site? | site, device, capacity metric | valid time, modality | — | capacity per site, actual and planned | candidate |
| CQ-9 | UC-5 | Where and when does projected demand exceed capacity? | site, capacity metric | valid time, modality | — | list of site, resource, and date of shortfall | candidate |
| CQ-10 | UC-6 | Where do discovered, asserted, and planned state disagree for `<entity type>`? | entity type | modality, source authority, provenance | — | list of disagreements with values per modality | candidate |
| CQ-11 | UC-6 | Which authority decides each disagreement? | entity type, source | oracle authority, source authority, provenance | — | per disagreement, the deciding oracle or source authority | candidate |
| CQ-12 | UC-7 | Which devices are discovered but unknown to inventory? | device | modality | — | list of discovered-only devices with discovery provenance | candidate |
| CQ-13 | UC-7 | Where does actual segmentation differ from intended segmentation? | segment, policy, device | modality | — | list of segment violations, intended vs observed | candidate |
| CQ-14 | UC-8 | For question `<Q>`, what is the answer, which facts and sources support it, and which policy applies? | any | valid time, record time, modality, source authority, provenance | — | answer with cited facts, sources, and applicable policy | candidate |
| CQ-15 | UC-9 | Which contracts exist, in which versions, and which sources and consumers use each? | contract, source, consumer | valid time | — | contract catalog with users per version | candidate |
| CQ-16 | UC-10 | What is the current operational state of `<entity>`? | device, interface, link | modality | freshness | state with observation time | candidate |
| CQ-17 | UC-10 | Which events relate to `<entity>` within `<window>`? | event, device | valid time | freshness | ordered list of events | candidate |
| CQ-18 | UC-11 | What were configuration and topology of `<affected set>` at each occurrence of incident class `<Y>`? | incident, device, configuration, link | valid time, record time | dependencies | per occurrence, configuration and topology snapshot views | candidate |
| CQ-19 | UC-12 | Which assets and dependencies support critical function `<F>`? | business function, asset, service | valid time | dependencies | dependency graph from function to assets | candidate |
| CQ-20 | UC-12 | Which of those assets or links are single points of failure? | asset, link | — | dependencies | list of single points of failure per function | candidate |
| CQ-21 | UC-13 | Which assets reach end of support within `<horizon>`, who owns them, and where are they? | asset, owner, site; attributes: owner, location, support expiration date | valid time | — | list of asset, owner, location, support end date | candidate |
| CQ-22 | UC-14 | For site `<S>`, what is planned, and what is built? | site, device, link | modality, valid time | — | planned vs built, per element | candidate |
| CQ-23 | UC-15 | Which assets or functions are duplicated or under-used? | asset, service, capacity metric | valid time | dependencies | consolidation candidates with evidence | candidate |
| CQ-24 | UC-16 | What is `<device>`, and how is it configured, now and as of `<date>`? | device, configuration | valid time, record time, modality | — | device record with configuration per modality | candidate |
| CQ-25 | UC-16 | How is `<device>` related to other entities? | device, interface, link, site, service | — | dependencies | relationship graph | candidate |
<!-- END GENERATED -->
