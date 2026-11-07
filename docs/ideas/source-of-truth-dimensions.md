# Idea: Source of Truth Splits into Dimensions

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

The rule "every element has exactly one source of truth" mixes up three different questions. A system can be authoritative in one sense and not in another.

Example: the configured memory of a host. It can come from Linux configuration, Windows configuration, or one of several cloud configuration systems. The host, or its control plane, decides the value. The inventory system is where consumers get it. The path by which it arrives differs from host to host.

## Proposal

| Dimension | Question | Example (configured memory) |
|---|---|---|
| **Oracle authority** | Who decides what is true? | The host OS, hypervisor, or cloud control plane |
| **Source authority** | Which system is authoritative for holding and serving the fact? | The inventory system |
| **Provenance** | Exactly how did this value get here? | Collector X read Linux config on host H at time *t*; or cloud API Y for instance I |

Authority is declared for each entity type and attribute, and may differ by modality ([idea: record time and modality](bitemporal-modal-inventory.md)):

| Modality | Typical oracle |
|---|---|
| `discovered` | The device or control plane |
| `asserted` | A person or system of record |
| `planned` | The planning or intent system |

Provenance is recorded per fact, not per entity type.

## Trade-offs

- Gains: conflicts can be explained (which authority, which path); one attribute can legitimately come from several places; source authority can move during migration without losing provenance.
- Costs: authority declarations must be maintained in the registry ([Core Platforms](../solution/05-core-platforms.md)); provenance for every fact adds volume.
- Prior art: [W3C PROV](../references/prov.md) (entity, activity, agent) for the provenance dimension.

## Open Questions

- How fine-grained should provenance be: per fact, per batch, or per collection run?
- Which oracle wins when two disagree for the same modality?
- Is oracle authority part of the policy model (initiative D1), the data model (initiative A), or both?

## How We Would Check

Every attribute in the schema registry declares its oracle and source authority. Every fact carries a provenance reference.
