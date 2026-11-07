# 6. Success Dimensions

How we measure whether the target state is better than the current state.

---

| Dimension | What Good Looks Like | How We Measure |
|---|---|---|
| **Definition & Policy** | Every entity type has a canonical definition. Every data element has a policy owner. | % of entity types with published, versioned definitions. % of data elements with assigned policy. |
| **Estate Decisions** | Every data source is classified (keep/migrate/retire). No orphan data sources. | Estate disposition matrix is complete and reviewed quarterly. Zero "unclassified" entries after 6 months. |
| **Discoverability** | Anyone can find what data exists, where it lives, and what it means — in under 5 minutes. | Time-to-answer for a new team member: "find the authoritative device count." Survey: "I can find the data I need" > 80% positive. |
| **Quality** | Data is accurate, complete, timely, and consistent across platforms. | Automated quality score per entity type. Reconciliation pass rate > 99.5%. Manual data cleanup tickets trend to zero. |
| **Telemetry** | The health of the data ecosystem is observable. Pipeline failures are detected before consumers complain. | Data pipeline uptime > 99.9%. Mean time to detect a data quality issue < 15 minutes. |
| **AI Readiness** | AI/ML tools can consume network data through standard interfaces without bespoke pipelines. | Number of AI/ML use cases that required no custom data extraction. Time from "we have a model" to "model runs on live data" measured in days, not months. |
| **Resilience** | The data plane survives failures in the control plane. Operators can always access critical data. | Data availability during platform outages. % of queries served from degraded-but-functional paths. |
| **Adoption** | Teams choose the target platforms over their spreadsheets and point solutions. | % of data consumers using target platforms. Legacy system query volume trend (should decrease). Spreadsheets replaced by automated feeds. |
| **Reconciliation / Source of Truth** | Every data element has exactly one authoritative source. Conflicts are detected and resolved automatically or through a defined process. | Number of cross-system conflicts per entity type (trending to zero). Time to resolve a detected conflict. |
| **Remediations** | Data quality issues are found and fixed proactively, not reactively. | Remediation rate: % of known issues fixed within SLA. Proactive vs. reactive remediation ratio (target: > 80% proactive). |
| **Risk Reduction** | The risks in `02-risks-and-importance.md` are materially lower. | Annual risk assessment shows reduction in each category. Audit findings related to data quality trend to zero. |
