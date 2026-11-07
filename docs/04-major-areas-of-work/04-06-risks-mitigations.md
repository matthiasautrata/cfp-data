# 4.6 Risks & Mitigations (Program-Level)

## Scope

Risks inherent to the program itself — not the risks of *not* doing it (those are in `02-risks-and-importance.md`).

---

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Scope creep** — the program tries to solve every data problem at once. | High | High | Clear scope definition per phase. "No" is an acceptable answer. Each phase has a bounded delivery window. |
| **Analysis paralysis** — the team spends months on models and principles without shipping anything. | Medium | High | Timeboxed sprints. First deliverable must be a working thing (even if small), not a document. |
| **Stakeholder fatigue** — too many meetings, too many documents, not enough progress. | Medium | Medium | Visible, frequent deliverables. Status updates emphasize what shipped, not what was discussed. |
| **Legacy system owners resist retirement** — teams are attached to their tools and processes. | High | Medium | Show, don't tell. Prove the replacement works before asking anyone to give up their tool. Include the legacy owner in the replacement design. |
| **Underestimating data quality** — migration reveals that the source data is much worse than expected. | Medium | High | Budget 20% of each migration phase for data cleanup. Do not stop migration — fix data in the target system. |
| **Key person dependency** — one person holds the knowledge for a critical data flow. | Medium | High | Pair every migration with documentation and knowledge transfer. No legacy system is retired until at least two people understand the data flow. |
| **Technology pivot** — a vendor or standard we depend on changes direction mid-program. | Low | Medium | Prefer open standards and decoupled interfaces. No single dependency should be able to block the program. |
| **Adoption failure** — the target platforms are built but no one uses them. | Medium | High | Design for the consumer experience first. Every platform must be demonstrably better than what it replaces on day one. |
