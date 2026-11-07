# Idea: Discovery Decoupled from Inventory

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

Discovery observes the network (through LLDP and CDP, SNMP, device APIs, and cloud APIs). Inventory is the curated record of what exists, what has existed, and what is planned. Many tools combine the two. When they do, what the tool can discover defines the inventory, observations overwrite records, and assets that cannot be discovered (air-gapped, managed by third parties, or not yet built) have no place.

Options:

| # | Option | Problem |
|---|---|---|
| 1 | Combined: discovery writes directly to inventory | The tool defines the model; there is no place for asserted or planned facts |
| 2 | Separate, sharing one canonical model | — |
| 3 | Separate, each with its own model, plus a translation | Two models of one thing; the translation drifts |

## Proposal

Option 2. Discovery and inventory are separate components that share the canonical model ([Models, Policy and Governance](../solution/03-models-policy-governance.md)). Discovery publishes observations through a defined contract. Inventory records them with the modality `discovered` ([idea](bitemporal-modal-inventory.md)), alongside asserted and planned facts.

## Rationale

- Principle P1, separation of concerns: observing and recording are different jobs.
- Principle P2, contract-first interfaces: a discovery tool can be replaced without touching inventory.
- Option 3 contradicts the canonical-model definition ([glossary](../glossary.md)).

## Consequences

- Easier: adding discovery sources; holding assets that cannot be discovered; finding drift as a difference between discovered and asserted values.
- Harder: matching observations to records (the cross-reference index in [Core Platforms](../solution/05-core-platforms.md)); one more contract to version.

## How We Would Check

Discovery writes to inventory only through the observation contract. This is checked in design reviews, and violations are caught by auditing writes to inventory.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Discovery](../solution/06-supporting-features.md), [Idea: bitemporal, modal inventory](bitemporal-modal-inventory.md)
