# Requirements

The trace matrix: [use case](03-stakeholders-use-cases.md) → requirement → [principle](../solution/01-principles.md). Links are recorded here only. Reverse views (which requirements a principle serves) are derived from this table, not maintained separately.

All requirements are candidates until their use cases are validated.

## Functional

| ID | Requirement | From | Principles |
|---|---|---|---|
| R-1 | Every entity type has one canonical, versioned definition. | UC-3, UC-9 | P7, P8 |
| R-2 | Facts are queryable as of any valid time and any record time. | UC-1, UC-2, UC-6 | P8 |
| R-3 | Facts carry modality: discovered, asserted, or planned. | UC-5, UC-6, UC-7 | P4 |
| R-4 | Every attribute declares oracle and source authority; every fact carries provenance. | UC-1, UC-6 | P6, P7 |
| R-5 | Policy attaches to every entity type and data element and can be evaluated. | UC-1, UC-7 | P6 |
| R-6 | Anyone can find what data exists, where it lives, and what it means. | UC-3 | P7 |
| R-7 | Dependencies between entities are queryable for impact analysis. | UC-2, UC-4 | — |
| R-8 | Every meaningful function is available via API and MCP. | UC-8, UC-9 | P2, P9 |
| R-9 | New sources and consumers connect via contract, without core code. | UC-9 | P2 |
| R-10 | Agent actions use the same APIs, policies, and audit trail as human actions. | UC-8 | P6, P10 |

## Quality

| ID | Requirement | From | Principles |
|---|---|---|---|
| Q-1 | Resilience: the data plane serves critical queries during control-plane failures. | UC-2 | P1 |
| Q-2 | Core processing is deterministic; latency and availability meet `[T]`. | UC-2, UC-6 | P10 |
| Q-3 | Any component can be replaced without rebuilding its consumers. | UC-9 | P2, P3 |
| Q-4 | Migration does not degrade operational capability. | UC-2 | — ([Migration](../delivery/02-migration.md) principles) |

## Gaps

- R-7 and Q-4 trace to no architecture principle. Either a principle is missing or none is needed; open.
- Weak traces after the P-numbering change: R-2 → P8, R-6 → P7, Q-1 → P1. None of the three states the concern the requirement actually serves. Open issue I-9.
- P3 and P5 are decision rules: they govern how every requirement is met, so they trace weakly by design. P8 is a sequencing rule, not a system property. The principles table mixes two kinds; the trace matrix treats them uniformly. See I-9.
- Nine use-case actors, three named stakeholders. No UC actor maps to a stakeholder role. Open issue I-10.
