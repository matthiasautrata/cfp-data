# 3. Architecture Principles

These principles guide every decision in this program. A proposal that violates a principle carries a heavy burden of proof.

---

### P1. One Thing, One Task

Each component does one thing well. A metadata registry does not also serve time-series data. A topology service does not also enforce policy. Boundaries are explicit and respected.

> **Rationale**: Focused components are replaceable, testable, and understandable. A system that does everything does nothing reliably.

---

### P2. No Monoliths

The target architecture is a set of interoperating platforms, not a single platform. No single database, no single service, no single vendor owns all network data.

> **Rationale**: Monoliths create coupling, single points of failure, and vendor lock-in. They also concentrate power in one team — which becomes a bottleneck.

---

### P3. No Vendor Dependency

Every interface is defined by contract, not by product. Where we acquire a platform, it must expose data and functions through open, documented interfaces. Proprietary lock-in is a disqualifier.

> **Rationale**: The network lifecycle is longer than any vendor's product lifecycle. We must be able to swap components without rebuilding everything.

---

### P4. Design for Plug-and-Play

Components define clear, stable interfaces. Adapters and transformers live at the boundaries, not in the core. A new data source or consumer connects through a defined contract, not through custom code.

> **Rationale**: The set of data sources and consumers will grow. A plug-and-play architecture absorbs growth without proportional complexity increase.

---

### P5. Acquire Where It Fits, Build Where It Matters

We prefer proven platforms over custom development — *unless* the requirement is truly differentiating. Custom code is justified only for:
- Core models that reflect unique network semantics.
- Integration adapters that bridge incompatible standards.
- Policy logic that embodies proprietary operational knowledge.

> **Rationale**: Building what you can buy is wasteful. But buying what must be owned is irresponsible.

---

### P6. Declarative State and Intent

Wherever possible, systems declare desired state and let the platform reconcile. Imperative workflows are the exception, not the default.

> **Rationale**: Declarative models are auditable, testable, and repeatable. They separate *what* from *how*.

---

### P7. Standards-Based, Hype-Resistant

We adopt standards that reduce risk, friction, or cost. We do not adopt a standard because it is popular, loudly marketed, or "what everyone is doing." Every standard choice must be rationally motivated against:
1. Does it solve a real problem we have?
2. Does it reduce coupling or increase portability?
3. What is the operational cost of adopting it?

> **Rationale**: Hype-driven architecture produces complexity without commensurate value. We are not early adopters; we are effective adopters.

---

### P8. Policy-Driven, Not Tool-Driven

What data is collected, retained, transformed, and exposed is determined by policy — not by what a given tool happens to support. Tools serve policy; policy does not bend to tools.

> **Rationale**: Tool-driven governance produces accidental architecture. Policy-driven governance produces intentional architecture.

---

### P9. Data Is a Product, Not a Byproduct

Network data has users, owners, SLAs, quality metrics, and lifecycle management — just like any product. It is designed, not accumulated.

> **Rationale**: Treating data as a byproduct guarantees fragmentation, quality issues, and unmanaged cost.

---

### P10. Resilience by Default

The data plane must survive failures in the control plane. A metadata registry being down should not break topology queries that could be served from a cached copy.

> **Rationale**: If the data architecture is less reliable than the network it describes, operators will bypass it.
