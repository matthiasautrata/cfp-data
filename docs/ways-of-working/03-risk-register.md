# Risk Register (Program-Level)

## Scope

Risks that come from running the program itself. The risks of *not* running it are in the [problem statement](../problem/01-problem-statement.md#consequences). Likelihood and impact are first estimates.

---

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Scope creep** — the program tries to solve every data problem at once. | High | High | Clear scope definition per phase. "No" is an acceptable answer. Each phase has a bounded delivery window. |
| **Analysis paralysis** — the team spends months on models and principles without shipping anything. | Medium | High | Time-limited sprints. The first deliverable must be something that works, however small, not a document. |
| **Stakeholder fatigue** — too many meetings, too many documents, not enough progress. | Medium | Medium | Visible, frequent deliverables. Status updates emphasize what shipped, not what was discussed. |
| **Legacy system owners resist retirement** — teams are attached to their tools and processes. | High | Medium | Show, don't tell. Prove the replacement works before asking anyone to give up their tool. Include the legacy owner in the replacement design. |
| **Underestimating data quality** — migration reveals that the source data is much worse than expected. | Medium | High | Reserve a share of each migration phase (`[T]`) for data cleanup. Do not stop migration — fix data in the target system. |
| **Key person dependency** — one person holds the knowledge for a critical data flow. | Medium | High | Pair every migration with documentation and knowledge transfer. No legacy system is retired until at least two people understand the data flow. |
| **Technology pivot** — a vendor or standard we depend on changes direction mid-program. | Low | Medium | Prefer open standards and decoupled interfaces. No single dependency should be able to block the program. |
| **Adoption failure** — the target platforms are built but no one uses them. | Medium | High | Design for the consumer experience first. Every platform must be demonstrably better than what it replaces on day one. |
