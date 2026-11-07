# Producers, Consumers, and Extension Points

This program builds the data layer: the models, the protocols, and the storage and serving of data. Operational capabilities such as discovery, monitoring, event management, and analysis are modules that connect to it. We enable them; we do not build them (principle P12, *Enable, Don't Build*).

This document outlines how modules connect. It lists topics and open questions, not decisions.

## What the Data Layer Offers

| Offer | Purpose |
|---|---|
| **A fact protocol** | Lets any producer publish facts as a stream, with their modality, time, and provenance ([idea: extensible fact protocol](../ideas/extensible-fact-protocol.md)) |
| **Contracts** | Let a producer or consumer connect without changes to core code (principle P2) |
| **Streams and subscriptions** | Serve consumers that need changes as they happen |
| **Query and batch access** | Serve consumers through SQL, GraphQL, REST, and MCP, all returning the same facts (requirement R-11) |
| **Metadata** | Tells everyone what data exists, where it is held, and what it means |

## Producers

Every producer publishes through the same protocol. What differs is the modality of the facts it publishes.

| Producer | Publishes | Modality | Examples |
|---|---|---|---|
| **Discovery agents** | Observations of devices, links, and services | Discovered | LLDP and CDP, SNMP, device and cloud APIs |
| **Monitoring and event management** | Events, alarms, and state changes | Discovered | Syslog, SNMP traps, alarm systems |
| **Systems of record** | The records they own | Asserted | IP address management, asset management |
| **Change management** | Change records and approvals | Asserted | Change tickets |
| **Planning and intent tools** | Intended and future state | Planned | Network design and provisioning tools |
| **Import adapters** | Data from spreadsheets and legacy tools, during migration | Asserted | One-off loaders |

Current thinking keeps discovery separate from inventory, with both sharing the canonical model ([idea](../ideas/discovery-decoupled-from-inventory.md)). A new discovery tool then becomes a new publisher, not a new project.

## Consumers

| Consumer | Needs from the data layer |
|---|---|
| **Operational tools** (incident, change, capacity) | Queries and subscriptions; dependencies for impact analysis |
| **Analysis and what-if tools** | History, dependencies, and planned state |
| **AI agents** | APIs and MCP (principle P9), working at the edge rather than in the core (principle P10); answers that cite their data and policy; labeled, versioned datasets for training |
| **Reporting and audit** | Queries as of a past date, and what our records said then |

## Time-Series Data: A Subsystem

High-volume time-series data, such as interface counters, flow records, and performance metrics, is treated as a subsystem. We source it, describe it in the metadata registry, and use it. We build it only if, later, nothing suitable exists.

One possible path, not a commitment:

| Horizon | Candidate | Role |
|---|---|---|
| Recent data (around the first 24 hours) | [Cortex](../references/cortex.md) | Fast store for recent metrics, compatible with Prometheus |
| History | [Apache Iceberg](../references/iceberg.md) | Long-term storage in an open table format |
| Later, if needed | [Apache Doris](../references/doris.md) or similar | Fast analytical queries across recent and historical data |

The data layer would hold the subsystem's metadata and the identifiers that link its series to entities. Whether it also holds summaries is open (issue I-14).

## Observing the Data Layer

The data layer's own health is ours to observe:

- Platform uptime, synchronization delay, data quality measures, and pipeline failures.
- Data lineage: traceability from source to consumer.
- Usage: what data is queried, by whom, and how often.

## Open Questions

- Which producers do we need first, to get started?
- How do devices that cannot be discovered (air-gapped, legacy, or managed by third parties) get into the data? Probably as asserted facts, through systems of record or import adapters.
- How good must data quality be before we expose the data to AI and machine-learning consumers?
- Where exactly is the boundary between the data layer and the time-series subsystem (issue I-14)?
