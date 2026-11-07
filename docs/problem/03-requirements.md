# Requirements

The trace matrix: [use case](02-stakeholders-use-cases.md) → requirement → [principle](../solution/01-principles.md). Model elements trace to [competency questions](../data/use-cases.yaml) (P11). Links are recorded here only. Reverse views (which requirements a principle serves) are derived from this table, not maintained separately.

All requirements are candidates until their use cases are validated.

## Functional

| ID | Requirement | From | Principles |
|---|---|---|---|
| R-1 | Every entity type has one canonical, versioned definition. | UC-3, UC-9 | P7, P8, P11 |
| R-2 | Facts are queryable as of any valid time and any record time. | UC-1, UC-2, UC-6, UC-11, UC-16 | P8 |
| R-3 | Facts carry modality: discovered, asserted, or planned. | UC-5, UC-6, UC-7, UC-10, UC-14 | P4 |
| R-4 | Every attribute declares oracle and source authority; every fact carries provenance. | UC-1, UC-6 | P6, P7 |
| R-5 | Policy attaches to every entity type and data element and can be evaluated. | UC-1, UC-7 | P6 |
| R-6 | Anyone can find what data exists, where it lives, and what it means. | UC-3 | P7 |
| R-7 | Dependencies between entities are queryable for impact analysis. | UC-2, UC-4, UC-11, UC-12, UC-15 | — |
| R-8 | Every meaningful function is available via API and MCP. | UC-8, UC-9 | P2, P9 |
| R-9 | New sources and consumers connect via contract, without core code. | UC-9 | P2 |
| R-10 | Agent actions use the same APIs, policies, and audit trail as human actions. | UC-8 | P6, P10 |
| R-11 | Every access path (SQL, GraphQL, REST, MCP, subscription, batch) returns the same facts with the same identities and semantics. | UC-3, UC-8 | P2, P9 |
| R-12 | Every asset records owner, location, classification, support expiration date, and recovery objectives ([NYDFS 500.13](../references/nydfs-500-13.md)). | UC-13 | P7 |
| R-13 | Assets map to the business functions they support, with criticality, reviewed on every major change ([DORA Art. 8](../references/dora-art8.md)). | UC-12 | P6 |
| R-14 | Current operational state is available within freshness `[T]`. | UC-2, UC-10 | P10 |

## Quality

| ID | Requirement | From | Principles |
|---|---|---|---|
| Q-1 | Resilience: the data plane serves critical queries during control-plane failures. | UC-2 | P1 |
| Q-2 | Core processing is deterministic; latency and availability meet `[T]`. | UC-2, UC-6 | P10 |
| Q-3 | Any component can be replaced without rebuilding its consumers. | UC-9 | P2, P3 |
| Q-4 | Migration does not degrade operational capability. | UC-2 | — ([Migration](../ways-of-working/02-migration.md) principles) |

## Gaps

- R-7 and Q-4 trace to no architecture principle (I-5). R-7 now has a regulatory driver via R-13.
- Weak traces (R-2 → P8, R-6 → P7, Q-1 → P1) and mixed principle kinds: I-9.
- Use-case actors not mapped to stakeholders: I-10.
- Vision claims (access modes, freshness, quality and lineage alongside data, answer assembly) not yet covered by requirements: I-13.
