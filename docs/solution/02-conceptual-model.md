# Conceptual Model

This document describes the current working shape of the solution. It is a sketch. Most of it is still at the idea stage, and it will change as we learn which questions the data must answer.

One rule applies throughout (principle P11): every element of the model must be needed by at least one [competency question](../data/use-cases.yaml). If no question needs it, it does not belong here yet.

## Facts and Three Layers of Metadata

Our working assumption is that the core of the data architecture is metadata that describes how data management is structured, in three layers above the facts, with policy alongside all of them ([idea: three layers of metadata](../ideas/metadata-layers.md)).

| Layer | Describes |
|---|---|
| **Facts** | What is, was, or will be true about the network |
| **1. Structure** | How data is shaped: entity types, attributes, relationships, event and stream types, fact dimensions, identity |
| **2. Flow and provenance** | How data moves and where each value came from: producers, consumers, streams, subscriptions, contracts, rich provenance |
| **3. Rules and processes** | What is done to data: transformations, correlation, reconciliation, processes |
| **Policy** | What must or may happen: independent, versioned objects attached to facts, structure, flows, and transformations |

The metadata is itself data (principle P13): versioned in time, governed, and queryable like everything else.

The meta-model is extensible. A small, fixed core is surrounded by information models, then taxonomies, with flexibility growing toward the leaves.

## Layer 1: Structure

### Entities

Not yet defined. The core entity types and their relationships are the subject of initiative A, *Define Data We Need* ([roadmap](../ways-of-working/01-roadmap.md)), scoped in [Models, Policy and Governance](03-models-policy-governance.md). The competency questions already name provisional entity types, such as device, link, site, and business function.

We prefer to adopt existing models, but expect no single model to cover everything. Layer 1 will more likely be several models linked to one another, as layers of a hypergraph (issue I-15).

### Fact Dimensions

Every fact carries the information below. The linked ideas explain the reasoning and the open questions.

| Dimension | Meaning | Recorded as | Idea |
|---|---|---|---|
| **Valid time** | When the fact is, was, or will be true in the network | A time interval | [Record time and modality](../ideas/bitemporal-modal-inventory.md) |
| **Record time** | When the fact was held in our records | A time interval | Same |
| **Modality** | How we know it: observed by discovery, stated by a person or system of record, or planned | `discovered`, `asserted`, or `planned` | Same |
| **Oracle authority** | Who decides the true value | Declared per attribute; may differ by modality | [Source of truth dimensions](../ideas/source-of-truth-dimensions.md) |
| **Source authority** | Which system is authoritative for holding and serving the fact | Declared per attribute | Same |
| **Provenance** | Where this particular value came from, and how | Recorded per fact | Same |

Some needs belong to answers rather than to facts: for example, following dependencies, or a limit on how old the data may be (freshness). Competency questions record these separately, as *answer requirements*.

### Identity

Open. How does one real-world thing get a single identity across many sources? The cross-reference index sketched in [Core Platforms](05-core-platforms.md) is a starting point.

## Layer 2: Flow and Provenance

All producers publish facts through one extensible protocol, as streams ([idea: extensible fact protocol](../ideas/extensible-fact-protocol.md)). Layer 2 records who produces and consumes what, through which streams, subscriptions, and contracts ([Producers, Consumers, and Extension Points](06-producers-consumers.md)). Provenance reaches into layer 3 when facts are correlated or derived: which inputs, combined by which rule, in which version.

## Layer 3: Rules and Processes

Transformations, correlation and aggregation, reconciliation, and the processes that run them. Scoped in [Process, Rules and Activities](04-process-rules-activities.md).

## Policy

Policies are independent objects with their own lifecycle, and are attached to facts, structure, flows, and transformations (principle P6; initiative D1, *Policy Model*). How they attach, to types, to instances, or to both, is open.

## Components

| Concern | Current thinking | Idea |
|---|---|---|
| Core and modules | A thin core (protocols, meta-model, identity, fact store, access paths); everything else is a module (principle P14) | [Build versus buy](../ideas/market-landscape-build-vs-buy.md) |
| Discovery and inventory | Separate components that share the canonical model | [Discovery decoupled from inventory](../ideas/discovery-decoupled-from-inventory.md) |
| Core processing and AI agents | Core processing is deterministic; agents work at the edge, through the same APIs as people (principle P10) | [Multi-agent coordination](../ideas/multi-agent-coordination.md) |
