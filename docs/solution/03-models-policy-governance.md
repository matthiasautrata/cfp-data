# Models, Policy & Governance

## Scope

What data we model, how we name it, what it means, who owns it, and what rules apply to it.

## Sub-Areas

### Data Models

- Canonical models for core network entities (device, interface, circuit, VLAN, IP, service, customer, location, ...).
- Relationship model: how entities connect, contain, depend on each other.
- Extensibility: how teams add domain-specific attributes without breaking the core model.
- Versioning and evolution: how models change over time without breaking consumers.
- Temporal and modal dimensions: valid time, record time, and basis (discovered, asserted, planned). See [idea](../ideas/bitemporal-modal-inventory.md).

### Metadata Registry

- What metadata exists, where it lives, what it means.
- Registry of registries: the system that tells you where to find each data type.
- Cross-referencing: how the same device is identified across IPAM, monitoring, CMDB, and vendor tools.

### Policy Engine

- Policy as code: what rules apply to what data.
- Policy categories: naming conventions, classification, retention, access control, quality thresholds.
- Policy lifecycle: authoring, testing, deployment, auditing.
- Enforcement model: at ingestion, at query time, at reporting time.
- Sequencing (P6): the policy model is designed with the data model in Phase 0; enforcement follows ([Initiatives & Roadmap](../delivery/01-roadmap.md)).

### Governance

- Data ownership: who is responsible for each domain's data quality.
- Stewardship: who curates and maintains the models.
- Review process: how model changes are proposed, reviewed, and approved.
- Dispute resolution: what happens when two systems disagree on a fact.

## Key Questions

- Do we adopt or adapt an existing model (e.g., OpenConfig, YANG, TMF SID, SNMP MIB structure) or define our own?
- What is the minimum viable set of entities we must model to break the current fragmentation?
- How do we handle entities that exist in multiple sources with conflicting attributes?
