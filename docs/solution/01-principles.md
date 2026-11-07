# Architecture Principles

These principles guide every decision in this program. A proposal that violates a principle carries a heavy burden of proof.

Each principle covers one concern. Which requirements each principle serves is recorded once, in the [trace matrix](../problem/03-requirements.md).

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
| P11 | Question-Driven Modelling | Model scope |

---

### P1. Separation of Concerns

Each component does one thing well. A metadata registry does not also serve time-series data. A topology service does not also enforce policy. No single database, service, or vendor owns all network data.

> **Rationale**: Focused components are replaceable, testable, and understandable. A monolith follows from violating this principle; it also concentrates control in one team, which becomes a bottleneck.

---

### P2. Contract-First Interfaces

Every interface is defined by contract, not by product. Adapters live at the boundaries, not in the core. A new source or consumer connects through a contract, not custom code. A platform that cannot expose its data and functions through open, documented interfaces is disqualified.

> **Rationale**: The network lifecycle is longer than any product's. Contracts let us swap components and absorb growth without proportional complexity.

---

### P3. Acquire Where It Fits, Build Where It Matters

Prefer proven platforms over custom development, unless the requirement is differentiating. Build only:
- Core models that reflect unique network semantics.
- Adapters that bridge incompatible standards.
- Policy logic that embodies proprietary operational knowledge.

> **Rationale**: Building what you can buy is wasteful. Buying what must be owned is irresponsible.

---

### P4. Declarative State and Intent

Systems declare desired state; platforms reconcile. Imperative workflows are the exception.

> **Rationale**: Declarative models are auditable, testable, and repeatable. They separate *what* from *how*.

---

### P5. Standards-Based, Hype-Resistant

Adopt a standard only if it:
1. Solves a real problem we have.
2. Reduces coupling or increases portability.
3. Has an operational cost we accept.

> **Rationale**: Hype-driven architecture produces complexity without value. We are effective adopters, not early adopters.

---

### P6. Policy-Driven, Designed In

What data is collected, retained, transformed, and exposed is determined by policy, not by what a tool supports. The policy model — how policy is expressed, attached to data, and evidenced — is foundation work, designed with the data model. Enforcement may follow later; the model may not.

> **Rationale**: Tool-driven governance produces accidental architecture. Retrofitting policy re-touches every model, pipeline, and consumer.

---

### P7. Data Is a Product

Network data has users, owners, SLAs, quality metrics, and lifecycle management. It is designed, not accumulated.

> **Rationale**: Data treated as a byproduct fragments, degrades, and costs without control.

---

### P8. Structure First, Detail Later

Get the shape right early: entities, dimensions, boundaries, interfaces. Fill in detail in small increments. Each increment ships value; none forces a redesign.

> **Rationale**: Structural rework is expensive; detail is cheap to add. Small increments inside a sound structure show value early without running in the wrong direction. Standards and prior art (P5) are the cheapest route to a sound structure.

---

### P9. API-First, Agent-Accessible

Every meaningful function is exposed through a versioned API. Agent access (MCP today) is an adapter generated from or layered on that API, not a separate path.

> **Rationale**: Agents build, design, and use this system. A function without an API is invisible to them. Treating MCP as an adapter keeps us protocol-independent (P2, P5).

---

### P10. Deterministic Core, Agentic Edge

Core processing — ingestion, storage, reconciliation execution, policy evaluation — is deterministic, fast, and reliable. Agents work at the edge: analysis, decisions, automation. Agents act through the same APIs and policies as humans, and their actions are audited.

> **Rationale**: Core paths need predictable latency and repeatable results. Agents add value where judgement and synthesis are needed. Coordination model: [idea: multi-agent coordination](../ideas/multi-agent-coordination.md).

---

### P11. Question-Driven Modelling

Every entity, attribute, and dimension in the model is needed by at least one [competency question](../data/competency-questions.yaml). An element no question needs is removed, or parked in `ideas/`. The questions are the model's acceptance tests.

> **Rationale**: Questions ground (meta-)data design in use. They favour useful designs over theoretically complete ones, and give every model review a concrete test: which question needs this?
