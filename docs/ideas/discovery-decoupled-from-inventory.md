# Idea: Discovery Decoupled from Inventory

## Status

Idea — under discussion. Promote to an ADR when agreed.

## Context

Discovery observes the network (LLDP/CDP, SNMP, APIs, cloud APIs). Inventory is the curated record of what exists, existed, or is planned. Tools often fuse them. Then discovery capability defines the inventory, observations overwrite records, and non-discoverable assets (air-gapped, third-party managed, planned) have no home.

Options:

| # | Option | Problem |
|---|---|---|
| 1 | Fused: discovery writes inventory directly | Tool defines the model; no place for asserted or planned facts |
| 2 | Decoupled, shared canonical model | — |
| 3 | Decoupled, separate models with translation | Two models of one thing; translation drifts |

## Proposal

Option 2. Discovery and inventory are separate components that share the canonical model ([4.1](../04-major-areas-of-work/04-01-models-policy-governance.md)). Discovery emits observations through a defined contract. Inventory records them with modality `discovered` ([idea](bitemporal-modal-inventory.md)), alongside `asserted` and `planned` facts.

## Rationale

- P1 (one thing, one task): observing and recording are different jobs.
- P3, P4 (no vendor dependency, plug-and-play): a discovery tool is replaceable without touching inventory.
- Option 3 contradicts the canonical-model definition ([glossary](../07-glossary.md)).

## Consequences

- Easier: adding discovery sources; holding non-discoverable assets; drift detection as `discovered` ≠ `asserted`.
- Harder: identity resolution between observations and records (cross-reference index, [4.3.1](../04-major-areas-of-work/04-03-core-platforms-mapping.md)); one more contract to version.

## How We Would Check

Discovery writes to inventory only through the observation contract. Checked in design review; detected by write-path audit on inventory.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [4.4.1 Discovery](../04-major-areas-of-work/04-04-supporting-features.md), [Idea: bitemporal, modal inventory](bitemporal-modal-inventory.md)
