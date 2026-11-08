# Architecture Principles

These principles guide the decisions in this program. A proposal that breaks a principle needs a strong argument.

The principles are drafts. Each covers one concern. Which requirements each principle supports is recorded once, in the [requirements](../problem/03-requirements.md) table.

| ID | Principle | Concern |
|---|---|---|
| P1 | Separation of Concerns | Component boundaries |
| P2 | Contract-First Interfaces | Coupling, replaceability |
| P3 | Acquire Where It Fits, Build Where It Matters | Sourcing |
| P4 | Declarative State and Intent | Desired vs actual state |
| P5 | Standards-Based, Hype-Resistant | Adoption of standards |
| P6 | Policy-Driven, Designed In | Governance |
| P7 | Data Is a Product | Ownership, lifecycle |
| P8 | Structure First, Detail Later | Design sequencing |
| P9 | API-First, Agent-Accessible | Access |
| P10 | Deterministic Core, Agentic Edge | Where agents act |
| P11 | Question-Driven Modeling | Model scope |
| P12 | Enable, Don't Build | Program scope |
| P13 | Self-Describing Data Layer | Metadata |
| P14 | Thin Core | What we build |

---

### P1. Separation of Concerns

Each component does one job well. A metadata registry does not also serve time-series data; a topology service does not also enforce policy. No single database, service, or vendor holds all network data.

> **Rationale**: Focused components are easier to understand, test, and replace. A monolith is what happens when this principle is ignored, and it concentrates control in one team, which then becomes a bottleneck.

---

### P2. Contract-First Interfaces

Every interface is defined by a contract, not by a product. Adapters sit at the boundaries, not in the core. A new source or consumer connects through a contract, not through custom code. A platform that cannot expose its data and functions through open, documented interfaces is not a candidate.

> **Rationale**: The network outlives any product. Contracts let us replace components, and absorb growth without a matching growth in complexity.

---

### P3. Acquire Where It Fits, Build Where It Matters

Prefer proven platforms to custom development, unless the requirement sets us apart. Build only:
- Core models that reflect unique network semantics.
- Adapters that bridge incompatible standards.
- Policy logic that embodies proprietary operational knowledge.

> **Rationale**: Building what you can buy is wasteful. Buying what must be owned is irresponsible.

---

### P4. Declarative State and Intent

Systems describe the state they want, and the platform works to bring the actual state into line. Step-by-step (imperative) workflows are the exception.

> **Rationale**: Declarative models can be audited, tested, and repeated. They separate *what* we want from *how* it is achieved.

---

### P5. Standards-Based, Hype-Resistant

Adopt a standard only if it:
1. Solves a real problem we have.
2. Reduces coupling or increases portability.
3. Has an operational cost we accept.

> **Rationale**: Architecture driven by fashion adds complexity without adding value. We aim to adopt effectively, not early.

---

### P6. Policy-Driven, Designed In

Policy decides what data is collected, kept, transformed, and exposed, not the features of a tool. The policy model, which defines how policy is written, attached to data, and evidenced, is foundation work and is designed together with the data model. Enforcement can come later; the model cannot.

> **Rationale**: Governance driven by tools produces accidental architecture. Adding policy afterwards means reworking every model, pipeline, and consumer.

---

### P7. Data Is a Product

Network data has users, owners, service levels, quality measures, and a managed lifecycle. It is designed, not accumulated.

> **Rationale**: Data treated as a byproduct fragments, degrades, and generates cost that nobody controls.

---

### P8. Structure First, Detail Later

Get the shape right early: entities, dimensions, boundaries, and interfaces. Add detail in small increments. Each increment delivers value, and none should force a redesign.

> **Rationale**: Reworking structure is expensive; adding detail is cheap. Small increments inside a sound structure show value early without heading in the wrong direction. Standards and prior art (P5) are the cheapest way to a sound structure.

---

### P9. API-First, Agent-Accessible

Every meaningful function is available through a versioned API. Access for AI agents (through MCP, today) is an adapter built on that API, not a separate path.

> **Rationale**: Agents help build, design, and use this system, and a function without an API is invisible to them. Treating MCP as an adapter keeps us independent of any one protocol (P2, P5).

---

### P10. Deterministic Core, Agentic Edge

Core processing, meaning ingestion, storage, running reconciliation, and evaluating policy, is deterministic, fast, and reliable. AI agents work at the edge, on analysis, decisions, and automation. They act through the same APIs and policies as people, and their actions are audited.

> **Rationale**: Core processing needs predictable speed and repeatable results. Agents add value where judgment and synthesis are needed. How agents might coordinate: [idea: multi-agent coordination](../ideas/multi-agent-coordination.md).

---

### P11. Question-Driven Modeling

Every entity, attribute, and dimension in the model must be needed by at least one [competency question](../data/use-cases.yaml). An element that no question needs is removed, or parked in `ideas/`. The questions are the model's acceptance tests.

> **Rationale**: Questions keep data and metadata design grounded in real use. They favor useful designs over theoretically complete ones, and give every model review a simple test: which question needs this?

---

### P12. Enable, Don't Build

This program builds the data layer: the models, the protocols, and the storage and serving of data. Operational capabilities, such as discovery, monitoring, event management, and analysis, connect to it as modules that are bought or built elsewhere. We define how they connect; we do not build them. If a needed subsystem has no suitable source, building it is a separate, later decision.

> **Rationale**: Our value is consistent, trusted data. Building operational tools would spread our effort, duplicate products that already exist, and tie the data layer to one tool's view of the world. See [Producers, Consumers, and Extension Points](06-producers-consumers.md).

---

### P13. Self-Describing Data Layer

The structure of the data, the flows that move it, and the rules and policies that act on it are described as metadata. That metadata is itself data: versioned in time, governed by policy, queryable through the same access paths as the data, and covered by competency questions. The meta-model has a small, fixed core and grows toward the leaves.

> **Rationale**: A data layer that describes itself can be understood, audited, and extended by people and agents, without separate documentation drifting away from reality. See [idea: three layers of metadata](../ideas/metadata-layers.md).

---

### P14. Thin Core

The core holds only what must be shared and consistent: the fact protocol and contracts, the meta-model, identity, the store of facts with their time, modality, and provenance, and the consistent access paths. Everything else is a module. Modules are measured against the protocols, the capabilities they must provide, and the competency questions. Anything proposed for the core must be justified by a competency question that no module can answer.

> **Rationale**: A thin core is cheaper to build, easier to keep consistent, and leaves every module replaceable. It also turns build-versus-buy into a measurement rather than a matter of taste. See [idea: market landscape and build versus buy](../ideas/market-landscape-build-vs-buy.md).

