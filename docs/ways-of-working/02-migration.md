# Migration Strategy

## Scope

How we move from the current fragmented state to the target architecture — without breaking the network, losing data, or losing the team.

---

## Principles of Migration

1. **Keep the network running.** The migration must not degrade operational capabilities at any point. If a legacy system is the only source of truth for a critical function, it stays until the replacement is proven.
2. **Cannibalize, don't supplement.** Every new platform should enable the retirement of at least one legacy platform. We are not adding to the sprawl.
3. **Strangler fig pattern.** New capabilities are built alongside existing systems. Traffic shifts gradually. Legacy systems are retired when no consumers remain.
4. **Data fidelity first.** Migration is not cleanup. We migrate data faithfully; we clean up in the target system after validation.
5. **Prove value early.** Each migration phase must deliver visible value (reduced toil, faster queries, eliminated manual steps) before the next phase begins.

---

## Migration Cycle (per domain)

Phasing lives in [Initiatives & Roadmap](01-roadmap.md). This is the cycle each domain runs: the first domain in Phase 1, the rest in Phase 2.

| Step | Activity | Exit |
|---|---|---|
| **1. Inventory** | Catalog the domain's sources, stores, pipelines, consumers. Classify by criticality, quality, replaceability, consumer count. | Disposition recorded in the estate matrix |
| **2. Map** | Map domain data to the canonical and policy models. Fix model gaps fast. | Mapping reviewed; gaps resolved or captured as ideas |
| **3. Build / acquire** | Target platform for the domain. | Accepted against model and policy |
| **4. Parallel run** | Populate faithfully from legacy; consumers migrate. | Reconciliation within agreed threshold; consumer sign-off checklist complete |
| **5. Cut over** | Target becomes source of truth. | Legacy read-only |
| **6. Retire** | Decommission legacy. | No remaining consumers; at least two people understand any residual flows |

Estate-wide work (first-pass inventory, cross-domain integration) is phased in [Initiatives & Roadmap](01-roadmap.md).

---

## What "Cannibalize" Looks Like

| Legacy System | Target Replacement | Migration Trigger |
|---|---|---|
| Spreadsheet-based IPAM | IPAM module in Instances Platform | All subnets migrated and verified |
| Vendor-specific inventory tool | Instances Platform + API adapter | Vendor contract renewal |
| Homegrown CMDB with one owner | Knowledge Platform | Owner leaves / system fails |
| Duplicate monitoring tools | Consolidate to one time-series platform | Data quality audit |

---

## Key Risks

- **Phase 0 paralysis**: spending too long cataloging without delivering value. Timebox the first pass; refine per domain.
- **Premature decommissioning**: retiring a legacy system before all consumers are migrated. Require a consumer sign-off checklist.
- **Model mismatch**: the canonical model does not fit a domain's actual data. Fix the model, not the migration — but do it fast.
- **Loss of tribal knowledge**: undocumented data flows that only one person understands. Pair documentation with migration.
