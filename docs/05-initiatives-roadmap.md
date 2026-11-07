# 5. Initiatives & Roadmap

## Initiatives

The raw list of things we need to do. These will be grouped into phases and assigned to workstreams.

### A. Define Data We Need

What entities, attributes, and relationships must we model to run the network? This is the foundational modelling exercise.

**Depends on**: Nothing — this is the first thing.
**Output**: Canonical model v1.0, covering 10-15 core entity types.

### B. Decide What Stays and What Goes

Inventory every current data source and classify: keep, migrate, retire, or deprecate.

**Depends on**: A (models define the target; we compare current state to target).
**Output**: Estate disposition matrix.

### C. Make Data Discoverable

Metadata registry + search/query interface so anyone can find what data exists and where to get it.

**Depends on**: A (models define what we index), B (we know what exists).
**Output**: Running metadata registry with pointers to current systems.

### D. Govern by Policy

Policy engine that defines naming, classification, retention, access, and quality rules — and enforces them.

**Depends on**: A, C (policy needs models and a registry to attach to).
**Output**: Policy framework, first set of enforceable policies.

### E. Trusted, Resilient Data

Data quality monitoring, reconciliation, drift detection, and automated remediation.

**Depends on**: C, D (quality needs a registry and policy framework).
**Output**: Data quality dashboards, reconciliation pipelines.

### F. Observe the Network

Telemetry and observability for both the network and the data ecosystem itself.

**Depends on**: E (quality baseline needed before observability is meaningful).
**Output**: Unified observability platform for network data health.

### G. Enable & Adopt

Training, documentation, self-service tooling, community model, onboarding process.

**Depends on**: C, D, E, F (need something to adopt before enabling adoption).
**Output**: Adoption program, onboarding playbook, self-service portal.

---

## Suggested Phasing

| Phase | Focus | Initiatives | Duration |
|---|---|---|---|
| **0: Foundation** | Models + Registry + Estate Map | A, B, C (partial) | 8-12 weeks |
| **1: First Domain** | Pick one domain, build target platform, migrate consumers | A+B+C applied to one domain, E (quality baseline) | 8-16 weeks |
| **2: Expand** | Repeat for 2-3 additional domains | A+B+C+E per domain | 16-24 weeks |
| **3: Govern + Observe** | Policy engine, telemetry, cross-domain integration | D, F, G | Ongoing |

> Note: These are working estimates. Each phase delivers a concrete, usable output before the next begins.
