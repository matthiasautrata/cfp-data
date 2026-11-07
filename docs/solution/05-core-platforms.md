# Core Platforms

A first sketch of the logical platforms. Names, boundaries, and examples are illustrative; they are not a design.

## Scope

The platforms that store, serve, and synchronize network data. The sketch has four logical categories: metadata, knowledge, and two kinds of instance data (static and time-series). Each may have several physical implementations.

---

## Metadata Platform

**Purpose**: Know what data exists, where it lives, what it means.

| Capability | Description |
|---|---|
| **Entity registry** | Canonical list of every named entity type and its attributes. |
| **Location registry** | For each data type: which platform holds the authoritative copy, which platforms hold replicas/caches. |
| **Schema registry** | Versioned schemas for each entity type, with field-level documentation. |
| **Cross-reference index** | Map of identifiers across systems (e.g., device hostname ↔ SNMP sysName ↔ IPAM ID ↔ monitoring ID). |

**Examples**: a data catalog tool, a schema registry (such as Apicurio or a Kafka schema registry), or a custom metadata store.

---

## Knowledge Platform

**Purpose**: Store and serve the canonical, relational, curated view of the network.

| Capability | Description |
|---|---|
| **Graph model** | Entities and their relationships (device ↔ interface ↔ circuit ↔ location). |
| **Historical view** | Point-in-time views for audit and what-if analysis. Whether these come from snapshots or from time-stamped facts is open (issue I-8). |
| **Policy attachment** | Which policies apply to which entities. |
| **Query interface** | Structured queries (graph, SQL, API) for consumers. |

**Examples**: a network graph database, a CMDB replacement, or a knowledge graph.

---

## Instances Platform — Static Data

**Purpose**: Inventory and configuration data. One candidate shape keeps every fact with its time and modality, and derives the current state as a view ([idea](../ideas/bitemporal-modal-inventory.md)).

| Capability | Description |
|---|---|
| **Device inventory** | Hardware model, serial numbers, firmware, role, location, status. |
| **Interface inventory** | Ports, speeds, media types, administrative state, connected to. |
| **IP address management** | Subnets, allocations, reservations, DNS associations. |
| **Configuration state** | Running and startup configurations, templated vs. actual. |
| **Software/version catalog** | OS versions, features, licenses, end-of-life tracking. |

**Examples**: an IPAM tool, a configuration management database, or an asset management system.

---

## Instances Platform — Time-Series Data

**Purpose**: How the network behaves over time. High-volume time-series data is a subsystem that we source, describe, and use rather than build ([Producers, Consumers, and Extension Points](06-producers-consumers.md)).

| Capability | Description |
|---|---|
| **Telemetry** | Interface counters, CPU/memory, environmental sensors. |
| **Flow data** | NetFlow, IPFIX, sFlow — traffic matrices, conversations. |
| **Event logs** | Syslog, SNMP traps, change events, alarm history. |
| **Performance metrics** | Latency, jitter, packet loss, utilization trends. |

**Examples**: a time-series database (such as TimescaleDB, InfluxDB, or Prometheus), or an observability platform.

---

## Open Questions Across Platforms

- **Synchronization**: How do the platforms stay consistent: through events, polling, or periodic reconciliation?
- **Identity**: How does the same device get the same identifier across all four categories?
- **Access control**: Who may read and write what, and how is that enforced consistently across platforms?
- **Time**: Is the Knowledge Platform's history derived from time-stamped facts, or does it keep its own snapshots?
