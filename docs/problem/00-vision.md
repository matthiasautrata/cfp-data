# Vision

Answers about CFP Network Data are available when, where, and how they are needed. We know the state and status of our environment, present and past. Anyone can ask a question and get a timely, accurate, and complete answer — through consistent access paths over one consistent data layer, without assembling it across systems, APIs, and databases.

## The Claims

| Claim | Means |
|---|---|
| **Convenient** | An answer to a simple or complex question comes ready-made. It is not assembled in pieces from different systems, APIs, and databases, and then processed afterwards. |
| **Consistent** | Several access paths, one data layer. Every path returns the same facts, with the same identities and semantics. Multiple access points, not a hodge-podge of incompatible ones. |
| **State and status** | All data needed is available: static (systems and infrastructure inventory); operational (configurations, deployments, locations); dynamic (telemetry); historical (how configuration and state changed over time). |
| **Easy means** | Consumers get answers in the form their need requires: request/reply, subscription, single record, batch. Through standard, documented interfaces — SQL/JDBC/ODBC where relational access fits, GraphQL or REST where it does not, MCP for agents ([P9](../solution/01-principles.md)). |
| **Timely, accurate, complete** | Data is collected and served near real time where reasonably possible, not held back for batch. Quality metrics and lineage are available alongside the data. |

## What Follows

Consequences of the vision, not separate goals. Each one constrains the design.

1. **A service, not installable software.** It is not something installed and run independently. It works as a data service inside a governance and operations construct, consumed the way electricity or telephony is — nobody buys a power station to get light. ([P7](../solution/01-principles.md))

2. **Its utility is bounded by governance and metadata.** Data added without documentation and curation turns the service into a data swamp. Metadata and policy are not overhead on the service; they are where its value comes from. ([P6](../solution/01-principles.md), [D1](../ways-of-working/01-roadmap.md))

3. **Trusted aggregator, not a substitute for operational systems.** It interconnects with many systems of record and redistributes their facts with provenance and declared authority. Operational systems stay; they become modules behind contracts. What may be superseded is the aggregation, presentation, and interaction layer built around them: shadow copies, spreadsheets, duplicate tools, bespoke pipelines. ([Source of truth dimensions](../ideas/source-of-truth-dimensions.md))

4. **No single enterprise data model.** It provides interlinked, domain-specific models. Different constituents consume different subsets and aspects, expressed in a model that suits their work. Interlinking is a modelling stance, not an endorsement of a semantic-web stack: RDF or a knowledge graph is adopted only if it passes [P5](../solution/01-principles.md), like any other standard.

5. **Answers, not data dumps.** The measure is whether a consumer got an answer. A store that holds the facts but leaves the assembly to each consumer has not reached this vision.

## How This Sits With the Rest

- [Problem statement](01-problem-statement.md): the current state and why it hurts.
- This document: the target state, in the consumer's terms.
- [Principles](../solution/01-principles.md): the constraints we accept to get there.
