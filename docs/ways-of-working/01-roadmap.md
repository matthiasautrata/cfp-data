# Initiatives & Roadmap

A draft plan. It sets out the initiatives and the phases in which we expect to deliver them. Initiatives, phases, and exit criteria will change as the use cases and the estate become better understood. How each domain migrates is described in [Migration](02-migration.md).

## Initiatives

### A. Define Data We Need

Which entities, attributes, and relationships must we model to run the network? This is the foundational modeling work, including how we record time and modality ([idea](../ideas/bitemporal-modal-inventory.md)).

**Depends on**: Nothing. Co-designed with D1.
**Output**: Canonical model v1 for the core entity types (first estimate: 10 to 15).

### B. Decide What Stays and What Goes

List every current data source and decide for each: keep, migrate, retire, or deprecate.

**Depends on**: A, for the target. Runs alongside A, because the first pass over the estate informs the model.
**Output**: The estate register, with a decision per source. First pass in Phase 0; refined domain by domain.

### C. Make Data Discoverable

A metadata registry, with search and query, so that anyone can find what data exists and where to get it.

**Depends on**: A (what we index), B (what exists).
**Output**: Registry structure in Phase 0; populated per domain.

### D1. Policy Model

How policy is expressed, attached to entities and data elements, and evidenced. Categories: ownership, classification, naming, retention, access, quality.

**Depends on**: Designed together with A (principle P6).
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

Connect the time-series subsystem, which we source rather than build (principle P12), and observe the health of the data layer itself.

**Depends on**: E, because observability means little without a quality baseline.
**Output**: Observability for network data health.

### G. Enable & Adopt

Training, documentation, self-service tooling, community model, onboarding process.

**Depends on**: Starts with the first domain's consumers; scales with C, D2, E, F.
**Output**: Onboarding playbook; self-service; adoption program.

### H. Source Modules

Define the protocols and the capabilities that modules must provide, then evaluate candidate products against them and against the competency questions, in proofs of concept ([idea: build versus buy](../ideas/market-landscape-build-vs-buy.md)).

**Depends on**: A (the competency questions), and a first draft of the fact protocol.
**Output**: A capability map; evaluation results; sourcing recommendations for the first domain.

---

## Phasing

| Phase | Focus | Initiatives | Exit criteria |
|---|---|---|---|
| **0: Foundation** | Shape: canonical model, policy model, registry structure, estate first pass; protocols and capabilities defined | A, D1, B (first pass), C (structure), H (definitions) | Model v1 and policy model v1 drafted and reviewed; protocols and capabilities drafted; first domain chosen |
| **1: First Domain** | Migration cycle end to end on one domain | A, D1 applied; B, C for the domain; E (baseline); G (domain consumers); H (evaluation and sourcing for the domain) | Domain consumers on target; legacy read-only or retired; quality baseline measured |
| **2: Expand** | Migration cycle per further domain, by value and independence | A–E per domain; D2 (first policy set) | Per domain as Phase 1; first policies enforced |
| **3: Integrate, Govern, Observe** | Cross-domain integration, enforcement at scale, telemetry, adoption at scale | D2, F, G | Measured against [Success Dimensions](04-success-dimensions.md) |

Each phase delivers something usable before the next begins. Structure is designed early (principles P8 and P6); detail is added in increments.

## Sizing

We estimate effort, not calendar time.

| Level | Unit | Set when |
|---|---|---|
| Phase, initiative | T-shirt (S, M, L, XL) | At phase start, after the estate first pass sizes scope |
| Backlog item | Points (team-relative) | At refinement |
| Calendar | A range, derived from points and measured velocity | Once velocity has been measured over several increments |

Estimates are conservative and are revised at the end of each phase.

## Choosing the First Domain

- Clear replacement candidate.
- Motivated consumers ([Risk Register](03-risk-register.md): adoption failure).
- Few dependencies on other domains.
- Visible value: reduced toil, a retired system.
