# Idea: Three Layers of Metadata at the Core of the Data Architecture

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

Several earlier ideas each needed a way to describe something about the data rather than the data itself: the fact protocol needs schemas and streams; source authority and provenance need to know producers and paths; the time-series subsystem needs to be described in the registry. Taken together, they point to the core of the data architecture: metadata that describes how data management itself is structured.

## Proposal

Facts sit at the bottom. Above them are three layers of metadata, with policy alongside all of them.

| Layer | Describes | Examples |
|---|---|---|
| **1. Structure** | How data is shaped | Entity types, attributes, relationships; event and stream types and how they relate; fact dimensions; identity |
| **2. Flow and provenance** | How data moves, and where each value came from | Producers, consumers, streams, subscriptions, contracts; rich provenance, including which source events were correlated into an aggregated event |
| **3. Rules and processes** | What is done to data | Transformations and derivations, correlation and aggregation rules, reconciliation, processes and workflows |
| **Policy** (across all layers) | What must or may happen | Policies are independent, versioned objects with their own lifecycle, attached to facts, structure, flows, and transformations |

The metadata is itself data (principle P13). It is versioned in time, governed by policy, queryable through the same access paths as the data, and covered by competency questions. Metadata changes, such as a new schema version, a re-pointed subscription, or a revised rule, have a valid time and a record time like any other fact. That is what answers questions such as "which rule produced this value last March?"

Rich provenance spans layers 2 and 3. A statement such as "this alarm was correlated from events A and B by rule R, version 4" links a flow to a rule.

## An Extensible Meta-Model

The meta-model must be extensible. Stability is highest at the center, and flexibility grows toward the leaves:

| Tier | Stability | Content |
|---|---|---|
| **Core** | Fixed | The few concepts every layer uses: entity, relationship, fact, stream, rule, policy, and the fact dimensions |
| **Information models** | Stable, versioned | Domain models: devices, topology, services, and so on |
| **Taxonomies** | Managed, evolving | Classifications and controlled vocabularies |
| **Leaves** | Flexible | Domain-specific attributes and details |

## Layer 1 Is Unlikely to Be One Model

Our preference for layer 1 is to adopt existing models (principle P5; see the [standards landscape](model-standards-landscape.md)). But no single model is likely to cover everything. Layer 1 will more likely be several adopted and local models, linked to one another: layers of a hypergraph.

A hypergraph fits because many relationships here involve more than two things: an aggregated event and the many events behind it; a provenance step with several inputs; a link with several termination points; a relationship that is itself described by further relationships. This is a statement about structure, not a choice of technology. How it is represented, whether as a property graph, as relational tables, or otherwise, is open.

## Prior Art

- [OpenLineage](../references/openlineage.md) (jobs, runs, datasets, lineage events) and [W3C PROV](../references/prov.md) (derivation, aggregation): inspiration for layer 2, to be adapted rather than adopted.
- Open-source metadata platforms such as DataHub, OpenMetadata, and Egeria have their own type systems. They are worth inspecting for layers 1 and 2.
- Considered and set aside: OMG CWM (Common Warehouse Metamodel) and MOF (Meta-Object Facility). Their layering resembles this proposal, but they are heavy and dated.

## Trade-offs

- Gains: one place to answer "what is this, where did it come from, and what was done to it"; agents can discover the meaning of data from the metadata itself; extension happens at the leaves without disturbing the core.
- Costs: the meta-model becomes critical shared infrastructure; versioning metadata in time adds complexity; linking several models requires careful identity and mapping work.

## Open Questions

- What exactly belongs in the fixed core?
- How are layer-1 models linked, and how is the hypergraph represented (issue I-15)?
- How does policy attach: to types, to instances, or to both?
- Where does layer 3 end and policy begin, for rules that both transform and constrain?

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Idea: extensible fact protocol](extensible-fact-protocol.md), [Idea: source of truth dimensions](source-of-truth-dimensions.md), [Idea: record time and modality](bitemporal-modal-inventory.md)
