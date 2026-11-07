# Requirements

This document lists what CFP Network Data must do (functional requirements, `R`) and how well it must do it (quality requirements, `Q`). Each requirement names the [use cases](02-stakeholders-use-cases.md) it comes from and the [principles](../solution/01-principles.md) it relies on. This table is the only place those links are recorded; any reverse view, such as which requirements a principle serves, is derived from it.

Elements of the data model are justified differently: each must be needed by at least one competency question (principle P11).

All requirements are candidates. They will change as the use cases are reviewed and as new questions come in.

## Functional Requirements

| ID | Requirement | Use cases | Principles |
|---|---|---|---|
| R-1 | Each entity type has one agreed, versioned definition. | UC-3, UC-9 | P7, P8, P11 |
| R-2 | We can ask what was true in the network at any point in time (valid time), and what our records said at any point in time (record time). | UC-1, UC-2, UC-6, UC-11, UC-16 | P8 |
| R-3 | Each fact records how we know it: discovered, asserted, or planned (its modality). | UC-5, UC-6, UC-7, UC-10, UC-14 | P4 |
| R-4 | For each attribute, we know who decides its true value (oracle authority) and which system is authoritative for serving it (source authority). Each fact records where it came from (provenance). | UC-1, UC-6 | P6, P7 |
| R-5 | Policies can be attached to every entity type and data element, and evaluated. | UC-1, UC-7 | P6 |
| R-6 | Anyone can find what data exists, where it is held, and what it means. | UC-3 | P7 |
| R-7 | Dependencies between entities can be queried, for example for impact analysis. | UC-2, UC-4, UC-11, UC-12, UC-15 | — |
| R-8 | Every meaningful function is available through an API, and through MCP for AI agents. | UC-8, UC-9 | P2, P9 |
| R-9 | New sources and consumers connect through a published contract, without changes to core code. | UC-9 | P2 |
| R-10 | AI agents act through the same APIs, policies, and audit trail as people. | UC-8 | P6, P10 |
| R-11 | Every access path (SQL, GraphQL, REST, MCP, subscription, batch) returns the same facts, with the same identifiers and meaning. | UC-3, UC-8 | P2, P9 |
| R-12 | Each asset records its owner, location, classification, support expiration date, and recovery objectives, as [NYDFS 500.13](../references/nydfs-500-13.md) requires. | UC-13 | P7 |
| R-13 | Each asset is mapped to the business functions it supports, with their criticality, and the mapping is reviewed after every major change, as [DORA Article 8](../references/dora-art8.md) requires. | UC-12 | P6 |
| R-14 | The current operational state is available within an agreed freshness limit `[T]`. | UC-2, UC-10 | P10 |

## Quality Requirements

| ID | Requirement | Use cases | Principles |
|---|---|---|---|
| Q-1 | Critical queries are still answered when supporting control components, such as the metadata registry, fail. | UC-2 | P1 |
| Q-2 | Core processing gives repeatable results and meets agreed latency and availability targets `[T]`. | UC-2, UC-6 | P10 |
| Q-3 | Any component can be replaced without rebuilding the systems that consume it. | UC-9 | P2, P3 |
| Q-4 | Migration does not reduce operational capability at any point. | UC-2 | — (see the [migration principles](../ways-of-working/02-migration.md)) |

## Known Gaps

- R-7 and Q-4 do not trace to any architecture principle (issue I-5). R-7 does have a regulatory driver, through R-13.
- Some traces are weak, because the principles mix two kinds: properties of the system, and rules for how we make decisions (issue I-9).
- Use-case actors are not yet mapped to named stakeholders (issue I-10).
- Two parts of the vision have no requirement yet: quality measures and lineage served alongside the data, and assembling answers for consumers (issue I-13).
