# Initiatives & Roadmap

Phasing lives here. How each domain migrates: [Migration Cycle](02-migration.md).

## Initiatives

### A. Define Data We Need

What entities, attributes, and relationships must we model to run the network? The foundational modelling exercise, including temporal and modal dimensions ([idea](../ideas/bitemporal-modal-inventory.md)).

**Depends on**: Nothing. Co-designed with D1.
**Output**: Canonical model v1 for the core entity types (expected 10–15).

### B. Decide What Stays and What Goes

Inventory every current data source and classify: keep, migrate, retire, or deprecate.

**Depends on**: A for the target. Runs alongside A: the estate first pass informs the model.
**Output**: Estate disposition matrix. First pass in Phase 0; refined per domain.

### C. Make Data Discoverable

Metadata registry + search/query interface so anyone can find what data exists and where to get it.

**Depends on**: A (what we index), B (what exists).
**Output**: Registry structure in Phase 0; populated per domain.

### D1. Policy Model

How policy is expressed, attached to entities and data elements, and evidenced. Categories: ownership, classification, naming, retention, access, quality.

**Depends on**: Co-designed with A (P6).
**Output**: Policy model v1; ownership and classification policies for the first domain.

### D2. Policy Enforcement

Evaluate and enforce policies at ingestion, query, and reporting time.

**Depends on**: D1, C.
**Output**: Enforcement for a first policy set.

### E. Trusted, Resilient Data

Data quality monitoring, reconciliation, drift detection, and automated remediation.

**Depends on**: C, D1.
**Output**: Quality baseline per domain; reconciliation pipelines.

### F. Observe the Network

Telemetry and observability for both the network and the data ecosystem itself.

**Depends on**: E (a quality baseline makes observability meaningful).
**Output**: Observability for network data health.

### G. Enable & Adopt

Training, documentation, self-service tooling, community model, onboarding process.

**Depends on**: Starts with the first domain's consumers; scales with C, D2, E, F.
**Output**: Onboarding playbook; self-service; adoption program.

---

## Phasing

| Phase | Focus | Initiatives | Exit criteria |
|---|---|---|---|
| **0: Foundation** | Shape: canonical model, policy model, registry structure, estate first pass | A, D1, B (first pass), C (structure) | Model v1 and policy model v1 drafted and reviewed; first domain chosen |
| **1: First Domain** | Migration cycle end to end on one domain | A, D1 applied; B, C for the domain; E (baseline); G (domain consumers) | Domain consumers on target; legacy read-only or retired; quality baseline measured |
| **2: Expand** | Migration cycle per further domain, by value and independence | A–E per domain; D2 (first policy set) | Per domain as Phase 1; first policies enforced |
| **3: Integrate, Govern, Observe** | Cross-domain integration, enforcement at scale, telemetry, adoption at scale | D2, F, G | Measured against [Success Dimensions](04-success-dimensions.md) |

Each phase delivers usable output before the next begins. Structure is designed early (P8, P6); detail arrives in increments.

## Sizing

Effort, not calendar time.

| Level | Unit | Set when |
|---|---|---|
| Phase, initiative | T-shirt (S, M, L, XL) | At phase start, after the estate first pass sizes scope |
| Backlog item | Points (team-relative) | At refinement |
| Calendar | Range derived from points ÷ measured velocity | After velocity is measured over several increments |

Estimates are conservative and revised at each phase gate.

## Choosing the First Domain

- Clear replacement candidate.
- Motivated consumers ([Risk Register](03-risk-register.md): adoption failure).
- Few dependencies on other domains.
- Visible value: reduced toil, a retired system.
