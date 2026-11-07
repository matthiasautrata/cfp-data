# Models, Policy and Governance

This document outlines a work area. It lists topics and open questions, not decisions.

## Scope

What data we model, how we name it, what it means, who owns it, and what rules apply to it.

## Sub-Areas

### Data Models

- Canonical models for core network entities (device, interface, circuit, VLAN, IP, service, customer, location, ...).
- Relationship model: how entities connect, contain, depend on each other.
- Extensibility: how teams add domain-specific attributes without breaking the core model.
- Versioning and evolution: how models change over time without breaking consumers.
- Time and modality: when a fact is true, when we recorded it, and how we know it (discovered, asserted, or planned). See the [idea](../ideas/bitemporal-modal-inventory.md).

### Metadata Registry

- What metadata exists, where it lives, what it means.
- Registry of registries: where to find each type of data.
- Cross-referencing: how the same device is identified across IPAM, monitoring, CMDB, and vendor tools.

### Policy Engine

- Policy as code: what rules apply to what data.
- Policy categories: naming conventions, classification, retention, access control, quality thresholds.
- Policy lifecycle: authoring, testing, deployment, auditing.
- Enforcement model: at ingestion, at query time, at reporting time.
- Sequencing (principle P6): the policy model is designed with the data model in Phase 0; enforcement comes later ([roadmap](../ways-of-working/01-roadmap.md)).

### Governance

- Data ownership: who is responsible for each domain's data quality.
- Stewardship: who curates and maintains the models.
- Review process: how model changes are proposed, reviewed, and approved.
- Dispute resolution: what happens when two systems disagree on a fact.

## Key Questions

- Do we adopt or adapt an existing model (for example OpenConfig, YANG, TM Forum SID, or the SNMP MIB structure), or define our own? The [standards landscape](../ideas/model-standards-landscape.md) collects the options.
- What is the minimum viable set of entities we must model to break the current fragmentation?
- How do we handle entities that exist in multiple sources with conflicting attributes?
