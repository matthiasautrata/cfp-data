# Current State and Constraints

This document collects facts about today's systems, their owners, and the constraints we must work within. Most of it is still empty: it will be filled in during the first pass over the estate (issues I-3 and I-4).

## Domains

Candidate domains, taken from [Core Platforms](../solution/05-core-platforms.md).

| Domain | Current systems | Owner | Notes |
|---|---|---|---|
| Device inventory | TBD | TBD | |
| Interfaces | TBD | TBD | |
| IP address management | TBD | TBD | |
| Circuits | TBD | TBD | |
| Topology | TBD | TBD | |
| Configuration | TBD | TBD | |
| Software / versions | TBD | TBD | |
| Telemetry | TBD | TBD | |
| Flow data | TBD | TBD | |
| Events / logs | TBD | TBD | |

## Estate

The decision for each data source (keep, migrate, retire) will be recorded in [`estate-disposition.csv`](../data/estate-disposition.csv), as part of initiative B.

## Constraints

| Category | Constraint |
|---|---|
| Firm-wide standards | TBD |
| Approved platforms | TBD |
| Languages and tooling | TBD |
| Regulatory | TBD |
| Security | TBD |

## Non-Goals

- Not a monolith ([P1](../solution/01-principles.md)).
- Not a reorganization: we change how data is modeled, governed, and shared, not who does what.
- Not a set of operational tools: we do not build discovery, monitoring, or event-management systems; we enable them ([P12](../solution/01-principles.md)).
- Further non-goals: to be agreed.
