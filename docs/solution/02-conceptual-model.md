# Conceptual Model

This document describes the current working shape of the solution: the kinds of things we hold data about, the information we keep with every fact, and the main boundaries between components. It is a sketch. Most of it is still at the idea stage, and it will change as we learn which questions the data must answer.

One rule applies throughout (principle P11): every element of the model must be needed by at least one [competency question](../data/use-cases.yaml). If no question needs it, it does not belong here yet.

## Entities

Not yet defined. The core entity types and their relationships are the subject of initiative A, *Define Data We Need* ([roadmap](../ways-of-working/01-roadmap.md)), scoped in [Models, Policy and Governance](03-models-policy-governance.md). The competency questions already name provisional entity types, such as device, link, site, and business function. They are the starting point.

## Fact Dimensions

Our working assumption is that every fact carries the information below. The linked ideas explain the reasoning and the open questions.

| Dimension | Meaning | Recorded as | Idea |
|---|---|---|---|
| **Valid time** | When the fact is, was, or will be true in the network | A time interval | [Bitemporal, modal inventory](../ideas/bitemporal-modal-inventory.md) |
| **Record time** | When the fact was held in our records | A time interval | Same |
| **Modality** | How we know it: observed by discovery, stated by a person or system of record, or planned | `discovered`, `asserted`, or `planned` | Same |
| **Oracle authority** | Who decides the true value | Declared per attribute; may differ by modality | [Source of truth dimensions](../ideas/source-of-truth-dimensions.md) |
| **Source authority** | Which system is authoritative for holding and serving the fact | Declared per attribute | Same |
| **Provenance** | Where this particular value came from, and how | Recorded per fact | Same |

Some needs belong to answers rather than to facts: for example, following dependencies, or a limit on how old the data may be (freshness). Competency questions record these separately, as *answer requirements*.

## Components

| Concern | Current thinking | Idea |
|---|---|---|
| Discovery and inventory | Separate components that share the canonical model | [Discovery decoupled from inventory](../ideas/discovery-decoupled-from-inventory.md) |
| Core processing and AI agents | Core processing is deterministic; agents work at the edge, through the same APIs as people (principle P10) | [Multi-agent coordination](../ideas/multi-agent-coordination.md) |

## Identity

Open. How does one real-world thing get a single identity across many sources? The cross-reference index sketched in [Core Platforms](05-core-platforms.md) is a starting point.

## Policy Attachment

Open. How do policies attach to entities, attributes, and individual facts? This is part of initiative D1, *Policy Model* (principle P6).
