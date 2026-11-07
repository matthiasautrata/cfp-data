# Idea: Record Time and Modality with Every Inventory Fact

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

Inventory changes over time. We need to be able to answer:

- What was true in the network at time *t*? (incident review, what-if analysis)
- What did our records say at time *t*? (audit; see [Compliance and Audit Risk](../problem/01-problem-statement.md#compliance--audit-risk))
- What is planned?

Facts also differ in how we know them: observed by discovery, stated by a person or system of record, or planned.

Options:

| # | Option | Problem |
|---|---|---|
| 1 | Current state plus a change log | History has to be reconstructed; it cannot simply be queried |
| 2 | Periodic snapshots | Coarse and costly, and misses changes between snapshots |
| 3 | One time (valid time) plus modality | Cannot answer "what did our records say then?" |
| 4 | Two times (valid time and record time) plus modality | — |

## Proposal

Option 4. Every inventory fact carries three pieces of information:

| Dimension | Values | Answers |
|---|---|---|
| **Valid time** | A time interval | When is, was, or will this be true in the network? |
| **Record time** | A time interval | When did our records hold this fact? |
| **Modality** | `discovered`, `asserted`, or `planned` | How do we know it? |

The current state is a view derived from these facts, not what is stored.

## Rationale

- Audit needs record time, which option 3 does not keep.
- `planned` gives intended state a natural home (principle P4).
- Reconciliation becomes a query that compares modalities ([Process, Rules and Activities](../solution/04-process-rules-activities.md)).
- Prior art: [SQL:2011 temporal tables](../references/sql2011-temporal.md); the split between intended and operational state in [OpenConfig](../references/openconfig.md); desired state (spec) and observed state (status) in [Kubernetes](../references/kubernetes-spec-status.md).

## Consequences

- Easier: drift shows up as a difference between discovered and asserted values; the gap between plan and reality shows up as a difference between planned and actual values; a point-in-time audit is a query.
- Harder: every model, API, and query must handle all three; storage must support two times per fact, or emulate it; consumers need a default view so that simple queries stay simple.
- Related: who is authoritative for each modality ([idea: source of truth dimensions](source-of-truth-dimensions.md)).
- Open: which modality wins when they disagree; whether three modalities are enough; whether the Knowledge Platform's history is derived from these facts ([Core Platforms](../solution/05-core-platforms.md)).

## How We Would Check

The schema registry rejects any inventory entity definition that lacks the three.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Idea: discovery decoupled from inventory](discovery-decoupled-from-inventory.md)
