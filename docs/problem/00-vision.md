# Vision

Anyone who needs to know something about CFP Network Data can get a timely, accurate, and complete answer, in the form they need, without assembling it themselves from several systems. We know the state of our environment now, and how it was in the past.

## What This Means for a Consumer

| Quality | What it means |
|---|---|
| **Ready-made answers** | A simple or complex question gets an answer, not a set of pieces to fetch from different systems and combine afterwards. |
| **Consistent** | There may be several ways in, but all of them draw on one consistent data layer. Every access path returns the same facts, with the same identifiers and the same meaning. |
| **Complete in scope** | The data covers what the questions need: inventory of systems and infrastructure; operational data such as configurations, deployments, and locations; dynamic data such as telemetry; and history, showing how configuration and state changed over time. |
| **Easy to reach** | Consumers get answers in the form their task needs: request and reply, subscription, a single record, or a batch. Access is through standard, documented interfaces: SQL (JDBC, ODBC) where relational access fits, GraphQL or REST where it does not, and MCP for AI agents ([P9](../solution/01-principles.md)). |
| **Timely and trustworthy** | Data is collected and served close to real time wherever that is reasonable, rather than held back for batch processing. Quality measures and lineage are available alongside the data. |

## What Follows from the Vision

These are consequences of the vision, not separate goals. Each one shapes the design.

1. **A service, not a software package.** The result is not something a team installs and runs on its own. It is a data service, run inside a governance and operations framework and consumed the way people consume electricity or telephony. Nobody buys a power station to switch on a light. (Principle [P7](../solution/01-principles.md), *Data Is a Product*.)

2. **Governance and metadata determine its value.** Data added without documentation and curation turns the service into a data swamp. Metadata and policy are not overhead; they are what make the data usable. (Principle [P6](../solution/01-principles.md); initiative [D1](../ways-of-working/01-roadmap.md), *Policy Model*.)

3. **A trusted aggregator, not a replacement for operational systems.** The service connects to many systems of record and passes on their facts, together with where each fact came from and who is authoritative for it. The operational systems stay, and connect as modules through agreed interfaces. What may be replaced is the layer that has grown up around them to collect, present, and work with their data: shadow copies, spreadsheets, duplicate tools, and one-off pipelines. ([Idea: source of truth dimensions](../ideas/source-of-truth-dimensions.md).)

4. **No single enterprise data model.** The service provides domain-specific models that link to each other. Different groups use different parts of the data, each in a model that suits their work. Linking models is a modeling approach, not a commitment to a technology: RDF or a knowledge graph would be adopted only if it passes the same test as any other standard (principle [P5](../solution/01-principles.md)).

5. **Answers, not data dumps.** Success means a consumer got an answer. A store that holds all the facts but leaves each consumer to assemble the answer has not achieved this vision.

## How This Relates to the Other Documents

- The [problem statement](01-problem-statement.md) describes the current state and why it hurts.
- This document describes the target state, in the consumer's terms.
- The [principles](../solution/01-principles.md) describe the constraints we accept to get there.
