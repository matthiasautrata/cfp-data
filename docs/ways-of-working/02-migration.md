# Migration Strategy

A draft. It describes how we expect to migrate, and will be refined with the first domain.

## Scope

How we move from today's fragmented state to the target architecture without breaking the network, losing data, or losing the team.

---

## Principles of Migration

1. **Keep the network running.** The migration must not degrade operational capabilities at any point. If a legacy system is the only source for a critical function, it stays until the replacement is proven.
2. **Operational systems stay; the layers around them may go.** Systems of record remain the authority for their own data, and connect as modules through contracts ([P2](../solution/01-principles.md)). What we replace is the layer that has grown up around them to collect, present, and work with their data: shadow copies, spreadsheets, duplicate tools, and one-off pipelines. Each new capability should retire at least one such layer, so that we do not add to the sprawl.
3. **Strangler fig pattern.** New capabilities are built alongside existing systems, use shifts across gradually, and the old layer is retired once nothing depends on it.
4. **Faithful migration first.** Migration is not cleanup. We move data as it is, and clean it up in the target system after validation.
5. **Prove value early.** Each migration phase must deliver visible value (reduced toil, faster queries, eliminated manual steps) before the next phase begins.

---

## Migration Cycle (per domain)

Each domain goes through the same cycle: the first domain in Phase 1, the others in Phase 2. The phases themselves are in the [roadmap](01-roadmap.md).

| Step | Activity | Exit |
|---|---|---|
| **1. Inventory** | List the domain's sources, stores, pipelines, and consumers. Rate each for criticality, quality, replaceability, and number of consumers. | Decision recorded in the estate register |
| **2. Map** | Map the domain's data to the canonical and policy models. Fix gaps in the model quickly. | Mapping reviewed; gaps fixed or recorded as ideas |
| **3. Build or acquire** | Provide the target platform for the domain. | Accepted against the model and policy |
| **4. Parallel run** | Load data faithfully from the old layer; consumers move across. | Differences within an agreed threshold `[T]`; every consumer has signed off |
| **5. Cut over** | The target becomes the authoritative place to get the domain's data. The operational systems still decide what is true ([source of truth dimensions](../ideas/source-of-truth-dimensions.md)). | Old layer is read-only |
| **6. Retire** | Decommission the old layer. | No consumers remain; at least two people understand any remaining data flows |

Work across the whole estate, such as the first-pass inventory and integration across domains, is planned in the [roadmap](01-roadmap.md).

---

## What Could Be Replaced

Illustrative examples, not commitments.

| Superseded | Replaced by | Trigger |
|---|---|---|
| Spreadsheet-based IPAM | IPAM module in Instances Platform | All subnets migrated and verified |
| Vendor-specific inventory tool | Instances Platform + API adapter | Vendor contract renewal |
| Homegrown CMDB with one owner | Knowledge Platform | Owner leaves / system fails |
| Duplicate monitoring tools | One time-series platform | Data quality audit |

---

## Key Risks

- **Phase 0 paralysis**: spending too long listing systems without delivering value. Limit the time for the first pass, and refine domain by domain.
- **Premature decommissioning**: retiring something before all its consumers have moved. Require sign-off from every consumer.
- **Model mismatch**: the canonical model does not fit a domain's real data. Fix the model rather than bending the migration, and do it quickly.
- **Loss of undocumented knowledge**: data flows that only one person understands. Document them as part of each migration.
