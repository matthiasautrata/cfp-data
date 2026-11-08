# Idea: Market Landscape and Build Versus Buy

## Status

Idea, early days. This is a first scan, made while the design is still very fluid. Products, positions, and conclusions here will change; nothing in this document is a sourcing decision.

## The Main Point

**Keep the core thin** (principle P14). Define the protocols and the capabilities that modules must provide. Then use those protocols and capabilities, together with the competency questions, to measure how well any candidate fits, and to decide what to build and how.

## Context

We are not the first to see this problem. Standards bodies and vendors have worked on network inventory, intent, discovery, and digital twins for years. This document records who is already here, where we overlap, where we differ, and what that means for building versus buying.

## Who Is Already Here

| Category | Examples | What they do |
|---|---|---|
| **Network source of truth** | [NetBox](../references/netbox.md), [Nautobot](../references/nautobot.md) | Intended state, inventory, and IP address management; increasingly also discovery and drift detection |
| **Network digital twin and assurance** | [Forward Networks](../references/forward-networks.md), [IP Fabric](../references/ip-fabric.md) | Discovered state, history kept as snapshots, a query language, and AI assistants on top |
| **Federated inventory** (telecom operations) | [Blue Planet Inventory](../references/blue-planet-inventory.md) | An overlay that unifies many legacy inventories and reconciles them |
| **CMDB and service management** | [ServiceNow](../references/servicenow-cmdb.md) | Governed ingestion of third-party data into one service-centered CMDB |
| **Metadata catalogs** | [DataHub](../references/datahub.md), [OpenMetadata](../references/openmetadata.md) | General-purpose metadata and lineage |
| **Standards bodies** | IETF, TM Forum, OpenConfig | Models and concepts, not products ([standards landscape](model-standards-landscape.md)) |

## Where We Overlap

Almost every capability exists somewhere: intended versus discovered state and drift (network sources of truth); a queryable model with history (digital twin and assurance tools); a unified view over existing systems (federated inventory); governed ingestion (CMDB connectors); and lineage (metadata catalogs). Some vendors already combine products in a producer pattern similar to ours, with discovery and assurance tools feeding a network source of truth.

## Where We Differ

1. **No single kind of truth at the center.** Each product category centers on one modality: a network source of truth on intent (planned), assurance tools on observation (discovered), a CMDB on records (asserted). We treat all three as equals, and keep time, authority, and provenance with every fact. Products typically keep history as snapshots or change logs.
2. **Network meaning joined with data-management metadata.** Network products model the network but not flows, rules, and policy; metadata catalogs describe flows and lineage but know nothing about networks. The three layers of metadata join the two ([idea](metadata-layers.md)).
3. **Products as interchangeable producers.** In our design, discovery, assurance, and inventory products publish into the data layer through an open protocol. In their designs, the product is the center.

None of the individual techniques is new. What is new is the combination and the stance: equal modalities, a self-describing data layer, question-driven modeling, and an open protocol. The honest claim is a distinctive architecture, not new technology. Integration is where the cost and the risk lie.

## Too Much or Not Enough?

- **Possibly too much:** the full meta-model, hypergraph linking, and time-versioned metadata across every domain is a platform-sized ambition. Phase 1 should prove a thin slice: one domain, the fact protocol, time and modality on facts, the first two metadata layers, and policy attached at the level of entity types.
- **Not enough yet:** how we source and evaluate products; which enterprise systems already exist (issue I-3); security and access control (issue I-16); and who runs the service once it exists (issue I-17).

## Build Versus Buy

| Option | Fit | Risk |
|---|---|---|
| **1. Compose: thin core, bought modules** (current leaning) | Matches principles P12 and P14 and the vision. Modules such as a network source of truth, assurance, time-series storage, and a catalog are sourced; the core is built | The core must stay thin |
| **2. Adopt a network source of truth as the core, and extend it** | Fastest to show value; extensible through plugins | The product's model becomes the canonical model, against vision point 4; intent becomes the center; history is limited |
| **3. Buy a federated inventory product** | Closest to the aggregator idea | Designed for telecom operators; heavy; lock-in |
| **4. Build everything** | — | Against principles P3 and P12 |

### The Thin Core

Current thinking on what the core holds:

| In the core (built) | Outside the core (modules, sourced) |
|---|---|
| The fact protocol and contracts | Discovery and assurance |
| The meta-model: structure, flow, rules, policy | Monitoring and event management |
| Identity and cross-referencing | Time-series storage |
| The store of facts with their time, modality, and provenance | Network source of truth for intended and asserted data, if one fits |
| Consistent access paths (SQL, GraphQL, REST, MCP) | Analysis, what-if, and AI agents |

Anything proposed for the core must be justified by a competency question that no module can answer.

## Measuring Fit

We evaluate candidates on three things, not on feature lists:

| Measure | Question |
|---|---|
| **Protocols** | Can the candidate publish or consume through our fact protocol and contracts, or be adapted to? |
| **Capabilities** | Which of the capabilities we need does it provide, and how well? |
| **Competency questions** | Which of the questions (CQ-1 onward) can it answer, how well, and from which kinds of truth? |

Running the competency questions against each candidate in a proof of concept makes the comparison concrete, and shows what remains to be built.

## Open Questions

- Which capabilities do we need to define first, and at what level of detail?
- Which existing enterprise systems are candidates to become modules?
- Is any product close enough to be the store of facts, or is that always built on standard technology?

## Notes

- **Date**: 2026-11-08
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Idea: three layers of metadata](metadata-layers.md), [Idea: extensible fact protocol](extensible-fact-protocol.md), [Producers, Consumers, and Extension Points](../solution/06-producers-consumers.md)
