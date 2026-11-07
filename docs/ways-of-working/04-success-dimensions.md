# Success Dimensions

How we will measure whether the target state is better than the current state.

Every dimension needs a threshold: without measurable targets we can neither plan reliably nor show results. We do not have the thresholds yet. `[T]` marks each one. They will be set from a baseline measured in Phase 1, and refined as the program matures.

---

| Dimension | What Good Looks Like | How We Measure |
|---|---|---|
| **Definition & Policy** | Every entity type has a canonical definition. Every data element has a policy owner. | % of entity types with published, versioned definitions ≥ `[T]`. % of data elements with assigned policy ≥ `[T]`. |
| **Estate Decisions** | Every data source is classified (keep/migrate/retire). No orphan data sources. | Estate disposition matrix is complete and reviewed quarterly. Unclassified entries ≤ `[T]` by a date set at phase planning. |
| **Discoverability** | Anyone can find what data exists, where it lives, and what it means — quickly. | Time-to-answer for a new team member: "find the authoritative device count" ≤ `[T]`. Survey: "I can find the data I need" ≥ `[T]` positive. |
| **Quality** | Data is accurate, complete, timely, and consistent across platforms. | Automated quality score per entity type. Reconciliation pass rate ≥ `[T]`. Manual data cleanup tickets trend to zero. |
| **Telemetry** | The health of the data ecosystem is observable. Pipeline failures are detected before consumers complain. | Data pipeline uptime ≥ `[T]`. Mean time to detect a data quality issue ≤ `[T]`. |
| **AI Readiness** | AI/ML tools can consume network data through standard interfaces without bespoke pipelines. | Number of AI/ML use cases that required no custom data extraction. Time from "we have a model" to "model runs on live data" ≤ `[T]`. |
| **Resilience** | The data plane survives failures in the control plane. Operators can always access critical data. | Data availability during platform outages ≥ `[T]`. % of queries served from degraded-but-functional paths ≥ `[T]`. |
| **Adoption** | Teams choose the target platforms over their spreadsheets and point solutions. | % of data consumers using target platforms ≥ `[T]`. Legacy query volume trend ≤ `[T]`. Spreadsheets replaced by automated feeds: count ≤ `[T]`. |
| **Reconciliation / Source of Truth** | Every attribute declares its oracle and source authority; every fact carries provenance ([idea](../ideas/source-of-truth-dimensions.md)). Conflicts are detected and resolved automatically or through a defined process. | Cross-system conflicts per entity type ≤ `[T]`. Time to resolve a detected conflict ≤ `[T]`. |
| **Remediations** | Data quality issues are found and fixed proactively, not reactively. | Remediation rate: % of known issues fixed within SLA. Proactive vs. reactive remediation ratio (≥ `[T]` proactive). |
| **Risk Reduction** | The [consequences](../problem/01-problem-statement.md#consequences) of the current state are materially lower. | Annual risk assessment shows reduction in each category ≥ `[T]`. Audit findings related to data quality ≤ `[T]`. Consequential cost (rework, redundancy, reconciliation, redundant licenses and infrastructure) ≤ `[T]` of baseline. |
