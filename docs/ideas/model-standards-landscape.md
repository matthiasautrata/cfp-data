# Idea: Model and Interface Standards Landscape

## Status

Idea — landscape scan, not a decision. Decisions go to ADRs per boundary.

## Context

"How do we model this" has no single answer. A standard can apply at six different layers, each with its own cost. Adopting a stack instead of per-layer choices is the failure mode P5 exists to prevent. This document records the candidates and a working verdict for each, so ADRs can cite one place. A verdict is a leaning, not a decision.

## 1. Device and configuration models

| Standard | Covers | Verdict |
|---|---|---|
| [YANG 1.1](../references/yang-rfc7950.md) | Modelling language: typed leaves, containers, lists, keys, augments, versioning rules | **Adopt as the modelling language** for device-shaped data |
| IETF base modules — `ietf-interfaces` (RFC 8343), `ietf-ip` (8344), `ietf-hardware` (8348), `ietf-system` | Concrete models for ports, addresses, chassis, inventory | **Adopt** — small, stable, vendor-neutral |
| [OpenConfig](../references/openconfig.md) | Vendor-neutral YANG models; gNMI transport | **Pilot** — good on modern kit, uneven on older estate |
| [NMDA](../references/rfc8342.md) | Standard datastores: `running`, `candidate`, `startup`, `intended`, `operational` | **Adopt the vocabulary** for device configuration — a standardised subset of the modality dimension |

NMDA is the important one. YANG already separates **intended** configuration from **operational** state; OpenConfig does it per leaf with `config`/`state` containers. That is the device-config part of the [modality](bitemporal-modal-inventory.md) split, deployed since OpenConfig (c. 2015) and NMDA (RFC 8342, 2018). Use their vocabulary where it applies; do not invent a parallel one. Modality is broader: NMDA has no `asserted` (a claim by a person or system of record) and no planned assets that do not yet exist.

Costs: YANG module versions drift, and vendors ship deviations rather than conforming. Adoption requires a per-platform conformance record — an input to the cross-reference index, not an afterthought.

## 2. Topology

| Standard | Covers | Verdict |
|---|---|---|
| [RFC 8345](../references/rfc8345.md) network / network-topology | Abstract base: nodes, termination points, links, supporting relationships | **Adopt the shape** |
| RFC 8795 TE topology | Traffic-engineering augment of 8345 | **Reference** — only if capacity/routing matters |
| [GQL](../references/gql-39075.md) (ISO/IEC 39075:2024) | Query language for property graphs | **Reference** — choose with the Knowledge Platform |

RFC 8345 is worth reading even if YANG is never used: nodes, termination points, and links with explicit supporting relationships is a mature answer to modelling containment and dependency without exploding the entity count. Cheapest prior art for R-7.

## 3. Interface contracts

Not data semantics — the wire format at each boundary. OpenAPI 3.1 (REST), AsyncAPI 3 (events), JSON Schema 2020-12 (payload validation), Avro or Protobuf where a schema-registry-mediated bus is chosen. One choice per boundary, recorded in an ADR, versioned in the metadata registry. YANG's encodings (JSON per RFC 7951, XML) cover device-facing interfaces, so no second contract is needed there. Agent access (MCP, [P9](../solution/01-principles.md)) is an adapter generated from these contracts, not a separate one. Data-product contracts (ownership, SLA, quality) are a further layer: ODCS (Open Data Contract Standard) is the candidate to evaluate.

## 4. Telemetry, flows, events

| Domain | Standard | Verdict |
|---|---|---|
| Metrics, logs, traces | [OpenTelemetry](../references/opentelemetry.md) + semantic conventions; OpenMetrics exposition | **Adopt** |
| Flow | IPFIX (RFC 7011), NetFlow v9, sFlow v5 | **Accept as input**, normalise on ingest |
| Events | syslog (RFC 5424), SNMP traps | **Accept as legacy input** |
| Streaming config/state | YANG-push (RFC 8641), gNMI subscribe | **Reference** |

## 5. Time, provenance, metadata

| Concern | Standard | Verdict |
|---|---|---|
| Bitemporality | [SQL:2011](../references/sql2011-temporal.md) application-time + system-versioned tables | **Adopt semantics** |
| Provenance | [W3C PROV](../references/prov.md) entity/activity/agent | **Adopt as a model**, not a serialization |
| Units, time format | UCUM; ISO 8601 | **Adopt** — trivial, prevents silent unit bugs |
| Metadata registry | ISO/IEC 11179 data element concepts | **Reference** — borrow the definitions, not the process ceremony |
| Data quality dimensions | ISO/IEC 25012 | **Reference** — shared vocabulary for the Quality success dimension |
| Lineage events | OpenLineage | **Reference** — only if pipeline lineage becomes a requirement |
| Catalog vocabulary | DCAT | **Defer** — RDF-based; adopt only if the catalog is RDF anyway |

## 6. Policy language

Important, deliberately undecided. The policy *model* is Phase 0 work ([P6](../solution/01-principles.md), D1); the *language* that expresses and evaluates it can be chosen later, provided the model does not foreclose it.

| Candidate | Character |
|---|---|
| ODRL | Rights and obligations vocabulary; W3C; JSON-LD serialisation |
| Rego (OPA) | General-purpose policy-as-code; Datalog-derived |
| Cedar | Authorization language; analysable, fast evaluation |
| XACML | Attribute-based access control; mature, verbose |

Criteria when deciding: expressiveness (permissions, prohibitions, obligations, duties) against evaluation speed and determinism in the core ([P10](../solution/01-principles.md)).

## 7. What not to adopt now

- **TMF SID / Open APIs** (TMF639 resource inventory, TMF638 service inventory). Complete and heavy: a telecom-wide information model of hundreds of entities. The rational case to adopt is an existing OSS/BSS integration, not model quality. Cost far exceeds return at this stage.
- **RDF / OWL / SHACL as the substrate.** The rational case is cross-domain inference not expressible relationally; that requirement does not exist yet. If it appears, SHACL for validation is the cheap entry point; OWL reasoning is not.
- **Vendor "digital twin" schemas.** Proprietary and a lock-in vector (P2, P3).

## LinkML — does it have a role?

[LinkML](../references/linkml.md) is a schema authoring language (YAML) that compiles one schema to many artifacts: JSON Schema, SQL DDL, JSON-LD, OWL, SHACL, GraphQL, Python dataclasses, documentation.

**Yes, a narrow one — as a compiler, not as a standard.**

What it buys:

- One canonical definition, many physical realisations. That is R-1 (`one canonical, versioned definition`) with a concrete mechanism, and it collapses the "which artefact is the truth" question.
- Documentation and validation generated from the same source, so the registry cannot drift from the model.
- **A deferred RDF decision with the door left open.** The same schema can emit JSON-LD, OWL, and SHACL later. That satisfies P5: no semantic-web commitment now, no foreclosure either. This is the RDF bridge argument, and it is sound precisely because the bridge is generated, not maintained.
- Low lock-in: the outputs are standards. LinkML can be dropped and the artefacts kept. It is a build-time dependency, not a runtime one — which is what P2 and P3 ask for.

What it costs, honestly:

- It is **not a standard**. It is a community project (`linkml` org), strong in life sciences, thin in networking and telecom. No IETF, ISO, or TM Forum status. Choosing it is a tooling decision, not a standards adoption, and should be recorded as such.
- A second metamodel on top of YANG, with **no mechanical round-trip**. YANG has list keys, augments, and NMDA datastores; LinkML has classes and slots and no config/state concept. Authoring the same entity in both is exactly the "two models of one thing" failure already rejected in [discovery decoupled from inventory](discovery-decoupled-from-inventory.md), option 3.
- It does not solve bitemporality. Valid time and record time are slots you add; SQL:2011 semantics still carry the query model.
- Small, Python-centric tooling base. A Scala implementation is reported (verify), but the bus factor is not that of YANG.

Working position, not yet a decision:

| Layer | Authoring source |
|---|---|
| Device-shaped data (interfaces, hardware, addresses, config/state) | **YANG** — the devices already speak it, and IETF/OpenConfig modules exist |
| Estate-shaped data (identity, service, location, policy, provenance, cross-references) | **LinkML** — multiple output targets are the point |

The seam between them is a generated crosswalk, not hand-maintained duplication. If a third model is ever needed, that is a signal the boundary is wrong.

Alternatives if LinkML is rejected: JSON Schema plus generated Markdown (simplest, no SQL or RDF target), SQL DDL as the source (drifts from documentation), or SHACL-first (commits to RDF now). LinkML's differentiator is multi-target generation from one source; if that is not wanted, none of these is clearly better than plain JSON Schema.

## Consequences

- Adopting YANG for device data and LinkML for estate data creates two model sources. Only worth it if the crosswalk is generated and reviewed; otherwise pick YANG and accept weak estate semantics, or LinkML and accept weak device fidelity.
- Every adopted standard above adds a per-platform conformance burden. Budget it in the migration cycle, not after.

## Open Questions

- Does OpenConfig coverage on the actual estate justify the pilot, or are vendor-native YANG modules the real source? (Needs estate facts.)
- Is the Knowledge Platform a property graph (GQL) or relational (SQL:2011)? Decides the query standard and whether LinkML's SQL or RDF targets matter more.
- Does LinkML earn its place given a YANG-first device model, or is plain JSON Schema enough for estate entities?

## How We Would Check

Each adopted layer has one ADR naming the standard, the boundary it governs, and the conformance check. Two authoring sources, one generated crosswalk, no hand-maintained duplicate model.

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [RFC 8342](../references/rfc8342.md), [RFC 8345](../references/rfc8345.md), [YANG](../references/yang-rfc7950.md), [LinkML](../references/linkml.md), [OpenConfig](../references/openconfig.md), [GQL](../references/gql-39075.md), [OpenTelemetry](../references/opentelemetry.md)
- **Prior art, not standards**: NetBox and Nautobot data models — the most widely deployed opinion on what network inventory entities actually look like. Cheap to read, useful to disagree with.
