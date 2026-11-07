# Conceptual Model

The shape of the system (P8). Ideas settle here once agreed; decisions behind them become ADRs. Every element cites the competency questions that need it (P11).

## Entities

Core entity types and relationships: initiative A, scoped in [Models, Policy & Governance](03-models-policy-governance.md). TBD.

## Fact Dimensions

Every fact carries:

| Dimension | Values | Source |
|---|---|---|
| Valid time | interval | [Idea: bitemporal, modal inventory](../ideas/bitemporal-modal-inventory.md) |
| Record time | interval | same |
| Modality | discovered, asserted, planned | same |
| Oracle authority | per attribute, per modality | [Idea: source of truth dimensions](../ideas/source-of-truth-dimensions.md) |
| Source authority | per attribute | same |
| Provenance | per fact | same |

Dependencies and freshness are requirements on answers, not dimensions of facts; competency questions record them separately ([use cases](../problem/02-stakeholders-use-cases.md)).

## Components

| Concern | Boundary | Source |
|---|---|---|
| Discovery vs inventory | Separate; shared canonical model | [Idea: discovery decoupled from inventory](../ideas/discovery-decoupled-from-inventory.md) |
| Deterministic core vs agents | Core deterministic; agents at the edge, via the same APIs | [P10](01-principles.md), [Idea: multi-agent coordination](../ideas/multi-agent-coordination.md) |

## Identity

How one real-world thing gets one identity across sources: cross-reference index in [Core Platforms](05-core-platforms.md). TBD.

## Policy Attachment

How policy attaches to entities, attributes, and facts (D1, [P6](01-principles.md)). TBD.
