# Glossary

Terms that are new, specific to this program, or easily misread.

| Term | Definition |
|---|---|
| **Activity** | An operational practice that uses CFP Network Data, such as incident management or capacity planning (`AC-n`). Most are named after ITIL 4 practices. |
| **ADR** | Architecture decision record: a short document that records one decision the team has agreed. Kept in `adr/`. |
| **Answer requirement** | A need that applies to an answer rather than to a stored fact, such as following dependencies, or a limit on how old the data may be (freshness). |
| **Asserted** | A modality: the fact was stated by a person or by a system of record. See the [idea](ideas/bitemporal-modal-inventory.md). |
| **Bitemporal** | Recording two times for each fact: when it is true in the network (valid time), and when we held it in our records (record time). |
| **Canonical model** | The agreed definition of an entity type and its attributes. There is one per entity type; each domain works with a view of it that suits its needs. |
| **CFP Network Data** | The data that describes the network estate run by Core Foundational Platforms (CFP). The subject of this program. |
| **Competency question** | A concrete question the data must be able to answer (`CQ-n`). Use cases are described by them, and each one doubles as an acceptance test. All are kept in [`use-cases.yaml`](data/use-cases.yaml). |
| **Consumer** | A tool, person, or agent that uses data from the data layer, through queries, subscriptions, or batch access. |
| **Contract** | The published, versioned interface through which a source or consumer connects. It covers the schema, the meaning of the data, and the service terms (principle P2). |
| **Data platform** | A system that stores, serves, and manages one category of network data, as part of the target architecture. |
| **Discovered** | A modality: the fact was observed by a discovery mechanism. |
| **Discovery** | Observing the network to produce facts. Current thinking keeps it separate from inventory ([idea](ideas/discovery-decoupled-from-inventory.md)). |
| **Effort size** | A T-shirt estimate (S, M, L, XL) for a phase or initiative. It is not a duration. |
| **Entity** | A kind of thing we hold data about, such as a device, interface, circuit, location, service, or policy. |
| **Estate** | All the data sources, stores, and pipelines that exist today, old and new. |
| **Event sourcing** | Storing every change as an event, and deriving current state and history from the stream of events. |
| **Fact protocol** | The single, extensible protocol through which all producers publish facts, with their modality, time, and provenance ([idea](ideas/extensible-fact-protocol.md)). |
| **Freshness** | The maximum age of a fact when it is served, measured against a threshold `[T]` (R-14). An answer requirement, not a fact dimension. |
| **Hypergraph** | A graph whose relationships can connect more than two things, such as an aggregated event and all the events behind it. A statement about structure, not a technology. |
| **Idea** | Thinking in progress, kept in `ideas/`. Not binding. An idea becomes an ADR once the team agrees. |
| **Inventory** | The curated record of what exists, what has existed, and what is planned. |
| **Knowledge platform** | The platform that holds the curated, connected, historical view of the network: "what we know". |
| **KPI** | Key performance indicator: a measure with a threshold, used to track a success dimension. |
| **Lifecycle dates** | Asset attributes such as the support expiration date (R-12). They are ordinary attributes, not fact dimensions. |
| **Metadata layers** | Structure (layer 1), flow and provenance (layer 2), and rules and processes (layer 3), with policy across all three ([idea](ideas/metadata-layers.md)). |
| **Metadata registry** | The system that records what data exists, where it is held, and what it means: the map of the data. |
| **Meta-model** | The model that defines how data, flows, rules, and policies are described. It has a small, fixed core and grows toward the leaves ([idea](ideas/metadata-layers.md)). |
| **Modality** | How we know a fact: it was discovered, asserted, or planned. |
| **Oracle authority** | Whoever decides the true value of an attribute: for example a device, a control plane, a person, or a planning system. |
| **Planned** | A modality: the fact describes an intended or future state (principle P4). |
| **Platform** | See *Data platform*. |
| **Points** | A team-relative effort estimate for a backlog item. Points convert to time only through measured velocity. |
| **Producer** | A module that publishes facts into the data layer, such as a discovery agent, a system of record, or a planning tool. |
| **Provenance** | The recorded path by which a particular fact arrived: which collector, from which system, and when. |
| **Reconciliation** | Comparing data across sources to find and resolve conflicts. |
| **Record time** | When we held a fact in our records. Also called transaction time or system time. |
| **Source authority** | The system that is authoritative for holding and serving an attribute, such as the inventory system. |
| **Source of truth** | Not a single concept here. It splits into oracle authority, source authority, and provenance ([idea](ideas/source-of-truth-dimensions.md)). |
| **Strangler fig pattern** | A migration pattern: new capabilities are built alongside existing systems, use shifts gradually to the new system, and the old system is retired once nothing depends on it. |
| **Subsystem** | A capability we source, describe, and use rather than build, such as high-volume time-series storage (principle P12). |
| **Target architecture** | The future state of the data landscape that this program aims for. |
| **Taxonomy** | A managed classification or controlled vocabulary within the meta-model. |
| **Telemetry (data platforms)** | Monitoring of the data platforms themselves: uptime, synchronization delay, quality measures, and pipeline health. |
| **Threshold** | The value a KPI must reach. Every success dimension needs one; each is set from a measured baseline. |
| **Use case** | A need of a specific actor in a specific activity (`UC-n`), described by one or more competency questions. |
| **Valid time** | When a fact is true in the network. Also called application time or business time. |
