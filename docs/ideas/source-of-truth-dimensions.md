# Idea: Source of Truth Splits into Dimensions

## Status

Idea — under discussion. Promote to an ADR when agreed.

## Context

"Every element has exactly one source of truth" conflates three questions. A fact can be authoritative in one sense and not in another.

Example — configured memory of a host. It can come from Linux config, Windows config, or one of several cloud config systems. The host or its control plane decides the value. The inventory system is where consumers get it. The path differs per host.

## Proposal

| Dimension | Question | Example (configured memory) |
|---|---|---|
| **Oracle authority** | Who decides what is true? | The host OS, hypervisor, or cloud control plane |
| **Source authority** | Which system is authoritative for holding and serving the fact? | The inventory system |
| **Provenance** | Exactly how did this value get here? | Collector X read Linux config on host H at time *t*; or cloud API Y for instance I |

Authority is declared per entity type and attribute, and may differ per modality ([idea: bitemporal, modal inventory](bitemporal-modal-inventory.md)):

| Modality | Typical oracle |
|---|---|
| `discovered` | The device or control plane |
| `asserted` | A person or system of record |
| `planned` | The planning or intent system |

Provenance is recorded per fact, not per entity type.

## Trade-offs

- Gains: conflicts become explainable (which oracle, which path); one attribute can have several legitimate origins; source authority can move during migration without losing provenance.
- Costs: authority declarations to maintain in the registry ([4.3.1](../04-major-areas-of-work/04-03-core-platforms-mapping.md)); per-fact provenance adds volume.
- Prior art: [W3C PROV](../references/prov.md) (entity, activity, agent) for the provenance dimension.

## Open Questions

- Granularity of provenance: per fact, per batch, or per collection run?
- Precedence when two oracles disagree for the same modality.
- Is oracle authority policy (D1), model (A), or both?

## How We Would Check

Every attribute in the schema registry declares its oracle and source authority. Every fact carries a provenance reference.
