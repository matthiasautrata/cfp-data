# Idea: Model and Interface Standards Landscape

## Status

Idea: a survey of candidate standards, not a decision. Decisions will be recorded as ADRs, one per boundary.

## Context

"How do we model this?" has no single answer. Standards apply at several different layers, each with its own costs. Adopting a whole technology stack instead of choosing layer by layer is exactly what principle P5 is meant to prevent. This document records the candidates and our current leaning on each, so that future ADRs can refer to one place. A leaning is not a decision.

We prefer to adopt, but do not expect one model to cover everything: the structural layer will more likely be several models linked as layers of a hypergraph ([idea: three layers of metadata](metadata-layers.md)).

## 1. Device and configuration models

| Standard | Covers | Current leaning |
|---|---|---|
| [YANG 1.1](../references/yang-rfc7950.md) | Modeling language: typed leaves, containers, lists, keys, augments, versioning rules | **Adopt as the modeling language** for device-shaped data |
| IETF base modules — `ietf-interfaces` (RFC 8343), `ietf-ip` (8344), `ietf-hardware` (8348), `ietf-system` | Concrete models for ports, addresses, chassis, inventory | **Adopt** — small, stable, vendor-neutral |
| [OpenConfig](../references/openconfig.md) | Vendor-neutral YANG models; gNMI transport | **Pilot** — good on modern kit, uneven on older estate |
| [NMDA](../references/rfc8342.md) | Standard datastores: `running`, `candidate`, `startup`, `intended`, `operational` | **Adopt the vocabulary** for device configuration — a standardized subset of the modality dimension |

NMDA matters most here. YANG already separates **intended** configuration from **operational** state; OpenConfig does it per leaf with `config`/`state` containers. That is the device-config part of the [modality](bitemporal-modal-inventory.md) split, deployed since OpenConfig (c. 2015) and NMDA (RFC 8342, 2018). Use their vocabulary where it applies; do not invent a parallel one. Modality is broader: NMDA has no `asserted` (a claim by a person or system of record) and no planned assets that do not yet exist.

Costs: YANG module versions drift, and vendors often publish deviations instead of conforming. Adopting YANG means keeping a conformance record per platform, which also feeds the cross-reference index.

## 2. Topology

| Standard | Covers | Current leaning |
|---|---|---|
| [RFC 8345](../references/rfc8345.md) network / network-topology | Abstract base: nodes, termination points, links, supporting relationships | **Adopt the shape** |
| RFC 8795 TE topology | Traffic-engineering augment of 8345 | **Reference** — only if capacity or routing becomes relevant |
| [GQL](../references/gql-39075.md) (ISO/IEC 39075:2024) | Query language for property graphs | **Reference** — choose with the Knowledge Platform |

RFC 8345 is worth reading even if we never use YANG. Its nodes, termination points, and links, with explicit supporting relationships, are a mature way to model containment and dependency without a large number of entity types. It is the cheapest prior art for requirement R-7.

## 3. Interface contracts

This layer is about the format at each boundary, not the meaning of the data. OpenAPI 3.1 (REST), AsyncAPI 3 (events), JSON Schema 2020-12 (payload validation), Avro or Protobuf where a schema-registry-mediated bus is chosen. One choice per boundary, recorded in an ADR, versioned in the metadata registry. YANG's encodings (JSON per RFC 7951, XML) cover device-facing interfaces, so no second contract is needed there. Agent access (MCP, [P9](../solution/01-principles.md)) is an adapter generated from these contracts, not a separate one. Data-product contracts (ownership, SLA, quality) are a further layer: [ODCS](../references/odcs.md) (Open Data Contract Standard) is the candidate to evaluate.

## 4. Telemetry, flows, events

High-volume time-series data is treated as a subsystem that we source rather than build ([Producers, Consumers, and Extension Points](../solution/06-producers-consumers.md)). Event envelopes and streams: [idea: extensible fact protocol](extensible-fact-protocol.md).

| Domain | Standard | Current leaning |
|---|---|---|
| Metrics, logs, traces | [OpenTelemetry](../references/opentelemetry.md) + semantic conventions; OpenMetrics exposition | **Adopt** |
| Flow | IPFIX (RFC 7011), NetFlow v9, sFlow v5 | **Accept as input**, normalize on ingest |
| Events | syslog (RFC 5424), SNMP traps | **Accept as legacy input** |
| Streaming config/state | YANG-push (RFC 8641), gNMI subscribe | **Reference** |

## 5. Time, provenance, metadata

| Concern | Standard | Current leaning |
|---|---|---|
| Bitemporality | [SQL:2011](../references/sql2011-temporal.md) application-time + system-versioned tables | **Adopt semantics** |
| Provenance | [W3C PROV](../references/prov.md) entity/activity/agent | **Adopt as a model**, not a serialization |
| Units, time format | UCUM; ISO 8601 | **Adopt** — trivial, prevents silent unit bugs |
| Metadata registry | ISO/IEC 11179 data element concepts | **Reference** — borrow the definitions, not the process ceremony |
| Data quality dimensions | [ISO/IEC 25012](../references/iso-25012.md) | **Reference** — shared vocabulary for the Quality success dimension |
| Lineage events | [OpenLineage](../references/openlineage.md) | **Reference** — only if pipeline lineage becomes a requirement |
| Catalog vocabulary | DCAT | **Defer** — RDF-based; adopt only if the catalog is RDF anyway |

## 6. Policy language

Important, deliberately undecided. The policy *model* is Phase 0 work ([P6](../solution/01-principles.md), D1); the *language* that expresses and evaluates it can be chosen later, provided the model does not foreclose it.

| Candidate | Character |
|---|---|
| ODRL | Rights and obligations vocabulary; W3C; JSON-LD serialization |
| Rego (OPA) | General-purpose policy-as-code; Datalog-derived |
| Cedar | Authorization language; analyzable, fast evaluation |
| XACML | Attribute-based access control; mature, verbose |

Criteria when deciding: expressiveness (permissions, prohibitions, obligations, duties) against evaluation speed and determinism in the core ([P10](../solution/01-principles.md)).

## 7. What not to adopt now

- **TM Forum SID and Open APIs** (TMF639 resource inventory, TMF638 service inventory). Complete but heavy: an information model for the whole telecom business, with hundreds of entities. The case for adopting it would be an existing integration with operator support systems, not the quality of the model. At this stage the cost far exceeds the benefit.
- **RDF, OWL, or SHACL as the foundation.** The case for them would be inference across domains that relational models cannot express. We have no such requirement yet. If one appears, SHACL for validation is the cheap entry point; OWL reasoning is not.
- **Vendor "digital twin" schemas.** Proprietary, and a route to lock-in (principles P2 and P3).

## LinkML — does it have a role?

[LinkML](../references/linkml.md) is a schema authoring language (YAML) that compiles one schema to many artifacts: JSON Schema, SQL DDL, JSON-LD, OWL, SHACL, GraphQL, Python dataclasses, documentation.

**Possibly a narrow one: as a compiler, not as a standard.**

What it offers:

- One canonical definition, many physical forms. That gives requirement R-1 (one agreed, versioned definition) a concrete mechanism, and settles the question of which artifact is the real definition.
- Documentation and validation generated from the same source, so the registry cannot drift from the model.
- **The RDF decision can wait, with the door left open.** The same schema can produce JSON-LD, OWL, and SHACL later. That fits principle P5: no commitment to semantic-web technology now, but nothing ruled out either. The argument holds because the RDF output would be generated, not maintained by hand.
- Little lock-in: the outputs are standard formats. LinkML could be dropped and the generated artifacts kept. It is needed only when building, not when running, which is what principles P2 and P3 ask for.

What it costs:

- It is **not a standard**. It is a community project, strong in the life sciences and little used in networking or telecom, with no IETF, ISO, or TM Forum status. Choosing it would be a tooling decision, not the adoption of a standard, and should be recorded as such.
- It would be a second way of defining models alongside YANG, with **no automatic conversion between them**. YANG has list keys, augments, and NMDA datastores; LinkML has classes and slots, and no notion of intended versus operational state. Defining the same entity in both would repeat the "two models of one thing" problem already rejected in [discovery decoupled from inventory](discovery-decoupled-from-inventory.md), option 3.
- It does not handle time for us. Valid time and record time are fields we would add; the query semantics would still come from SQL:2011.
- The tooling is small and mostly Python, and its community is far smaller than YANG's.

Current leaning, not a decision:

| Layer | Authoring source |
|---|---|
| Device data (interfaces, hardware, addresses, configuration and state) | **YANG**: the devices already use it, and IETF and OpenConfig modules exist |
| Estate data (identity, service, location, policy, provenance, cross-references) | **LinkML**: here, generating several output formats is the point |

The two would be joined by a generated mapping, not by duplicated definitions maintained by hand. If a third model were ever needed, that would be a sign that the boundary is in the wrong place.

Alternatives, if LinkML is rejected: JSON Schema plus generated documentation (simplest, but no SQL or RDF output); SQL table definitions as the source (they drift from the documentation); or SHACL first (which commits us to RDF now). What sets LinkML apart is generating many outputs from one source. If we do not need that, none of these alternatives is clearly better than plain JSON Schema.

## Consequences

- Using YANG for device data and LinkML for estate data means two sources of model definitions. That is only worth it if the mapping between them is generated and reviewed. Otherwise, choose YANG and accept a weaker estate model, or LinkML and accept a less faithful device model.
- Every standard adopted adds conformance work for each platform. Plan for it in the migration cycle, not afterwards.

## Open Questions

- Does OpenConfig coverage on the actual estate justify the pilot, or are vendor-native YANG modules the real source? (Needs estate facts.)
- Is the Knowledge Platform a property graph (GQL) or relational (SQL:2011)? Decides the query standard and whether LinkML's SQL or RDF targets matter more.
- Does LinkML earn its place given a YANG-first device model, or is plain JSON Schema enough for estate entities?

## How We Would Check

Each adopted layer has one ADR, naming the standard, the boundary it governs, and how conformance is checked. There are at most two sources of model definitions, joined by one generated mapping, and no duplicated model maintained by hand.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [RFC 8342](../references/rfc8342.md), [RFC 8345](../references/rfc8345.md), [YANG](../references/yang-rfc7950.md), [LinkML](../references/linkml.md), [OpenConfig](../references/openconfig.md), [GQL](../references/gql-39075.md), [OpenTelemetry](../references/opentelemetry.md)
- **Prior art, not standards**: the NetBox and Nautobot data models, the most widely used view of what network inventory entities look like in practice. Cheap to read, and useful to disagree with.
