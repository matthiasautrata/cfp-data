# Idea: Inventory Is Bitemporal and Modal

## Status

Idea — under discussion. Promote to an ADR when agreed.

## Context

Inventory changes. We must answer:

- What was true in the network at time *t*? (incident review, what-if)
- What did we believe at time *t*? (audit — see [Compliance & Audit Risk](../problem/02-risks-and-importance.md))
- What is planned?

Facts also differ by basis: observed by discovery, asserted by a person or system of record, or planned as intent.

Options:

| # | Option | Problem |
|---|---|---|
| 1 | Current state + change log | History is a reconstruction, not a query |
| 2 | Periodic snapshots | Coarse; costly; misses changes between snapshots |
| 3 | Uni-temporal (valid time) + modality | Cannot answer "what did we believe when" |
| 4 | Bitemporal (valid + record time) + modality | — |

## Proposal

Option 4. Every inventory fact carries three dimensions:

| Dimension | Values | Answers |
|---|---|---|
| **Valid time** | interval | When is/was/will this be true in the network? |
| **Record time** | interval | When did we hold this fact? |
| **Modality** | `discovered`, `asserted`, `planned` | On what basis do we hold it? |

Current state is a view over these dimensions, not the store.

## Rationale

- Audit needs record time; option 3 loses it.
- `planned` gives declarative intent a home (P4).
- Reconciliation becomes a query across modality ([Process, Rules & Activities](../solution/04-process-rules-activities.md)).
- Prior art: [SQL:2011 temporal tables](../references/sql2011-temporal.md); [OpenConfig](../references/openconfig.md) intended vs operational state; [Kubernetes](../references/kubernetes-spec-status.md) spec vs status.

## Consequences

- Easier: drift = `discovered` ≠ `asserted`; intent gap = `planned` ≠ actual; point-in-time audit is a query.
- Harder: every model, API, and query handles three dimensions; storage must support or emulate bitemporality; consumers need a default view so simple queries stay simple.
- Related: who is authoritative per modality — [idea: source of truth dimensions](source-of-truth-dimensions.md).
- Open: precedence when modalities disagree; whether the modality set is closed; whether the Knowledge Platform's history derives from these facts ([Mapping to Core Platforms](../solution/05-core-platforms.md)).

## How We Would Check

The schema registry rejects inventory entity schemas lacking the three dimensions.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Idea: discovery decoupled from inventory](discovery-decoupled-from-inventory.md)
