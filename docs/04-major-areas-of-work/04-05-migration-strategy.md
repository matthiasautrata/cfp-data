# 4.5 Migration Strategy

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

## Migration Phases

### Phase 0: Inventory & Classification
- Catalog every current data source, store, and pipeline.
- Classify each by: criticality, data quality, replaceability, consumer count.
- Identify quick wins: systems that are expensive to maintain, have few consumers, and have a clear replacement.

### Phase 1: Core Model + Meta-Data Registry
- Define and publish the canonical models for the top 10 entity types.
- Stand up the metadata registry with pointers to existing systems.
- No data moves yet — this is a map of what exists.

### Phase 2: Target Platform for One Domain
- Pick one domain (e.g., IPAM or device inventory) with a clear replacement candidate.
- Build/acquire the target platform, populate it from the legacy source.
- Run in parallel until all consumers have migrated; then cut over and decommission the legacy system.

### Phase 3: Expand
- Repeat Phase 2 for each domain, in order of value and independence.
- Each cycle validates the model and the migration pattern.

### Phase 4: Integrate & Optimize
- Cross-domain integrations: topology ↔ inventory, telemetry ↔ capacity planning.
- Policy-driven automation: rules that span domains.
- Retire the remaining legacy systems.

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

- **Phase 0 paralysis**: spending too long cataloging without delivering value. Set a 2-week timebox.
- **Premature decommissioning**: retiring a legacy system before all consumers are migrated. Require a consumer sign-off checklist.
- **Model mismatch**: the canonical model does not fit a domain's actual data. Fix the model, not the migration — but do it fast.
- **Loss of tribal knowledge**: undocumented data flows that only one person understands. Pair documentation with migration.
