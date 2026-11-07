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

Each use case is a set of [competency questions](../references/competency-questions.md): questions the data must answer. Each question doubles as an acceptance test and an agent evaluation item.

Data needs: **VT** valid time · **RT** record time · **M** modality · **Dep** dependencies · **Auth** authority and provenance · **Fr** freshness `[T]` · **Life** lifecycle dates.

All use cases are candidates until validated with Network Services and the activity owners.

| ID | Activity | Actor | Competency question | Data needs | Driver |
|---|---|---|---|---|---|
| UC-1 | AC-12 | Auditor | Which devices held customer data on date *d*, and what did our records say then? | VT, RT, Auth | [Compliance](01-problem-statement.md#compliance--audit-risk) |
| UC-2 | AC-4 | Incident responder | For device *X*: what is connected, what depends on it, what changed in the last *h* hours? | Dep, RT, Fr | [Operational](01-problem-statement.md#operational-risk) |
| UC-3 | AC-13 | Engineer | What data exists about entity type *E*, where does it live, what does it mean, and which count is authoritative? | Auth | [Discoverability](../ways-of-working/04-success-dimensions.md) |
| UC-4 | AC-6 | Change engineer | If I change IP, link, or device *X*, which devices and services are affected? | Dep, M | [Operational](01-problem-statement.md#operational-risk) |
| UC-5 | AC-7 | Capacity planner | What capacity exists and is planned per site; where and when does projected demand exceed it? | VT, M | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) |
| UC-6 | AC-14 | Data steward | Where do discovered, asserted, and planned state disagree, and which authority decides? | M, Auth | [Source of truth dimensions](../ideas/source-of-truth-dimensions.md) |
| UC-7 | AC-9 | Security | Which devices are discovered but unknown to inventory? Where does actual segmentation differ from intent? | M | [Security](01-problem-statement.md#security-risk) |
| UC-8 | AC-15 | AI agent | Given question *Q*, what is the answer, which facts and sources support it, and which policy applies? | all | [Features: AI](../solution/06-supporting-features.md) |
| UC-9 | AC-14 | Platform owner | Can source or consumer *S* connect through a published contract, without core code? | — | [P2](../solution/01-principles.md) |
| UC-10 | AC-3 | Operator | What is the current operational state of *X*, and which events relate to it? | M, Fr | [Operational](01-problem-statement.md#operational-risk) |
| UC-11 | AC-5 | Problem manager | What were configuration and topology each time incident class *Y* recurred? | VT, RT, Dep | [Operational](01-problem-statement.md#operational-risk) |
| UC-12 | AC-8 | Resilience owner | Which assets and dependencies support critical function *F*; where are single points of failure? | Dep, VT | [DORA Art. 8](../references/dora-art8.md) |
| UC-13 | AC-2 | Asset owner | Which assets reach end of support within horizon *h*; who owns them and where are they? | VT, Life | [NYDFS 500.13](../references/nydfs-500-13.md) |
| UC-14 | AC-10 | Provisioning engineer | For site *S*: what does the plan say, and what is built so far? | M, VT | [RFC 9315](../references/rfc9315-ibn.md) |
| UC-15 | AC-11 | Architect | Which assets or functions are duplicated or under-used, and are candidates to consolidate? | Dep, VT | [Untrusted decisions](01-problem-statement.md#untrusted-decisions) |
| UC-16 | AC-1 | Network engineer | What is device *X*, how is it configured now and as of date *d*, and how is it related to others? | VT, RT, M, Dep | [Problem statement](01-problem-statement.md) |
