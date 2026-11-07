# Mapping to Core Platforms

## Scope

The concrete platforms that store, serve, and synchronize network data. Three logical categories, potentially multiple physical implementations.

---

## Meta-Data Platform

**Purpose**: Know what data exists, where it lives, what it means.

| Capability | Description |
|---|---|
| **Entity registry** | Canonical list of every named entity type and its attributes. |
| **Location registry** | For each data type: which platform holds the authoritative copy, which platforms hold replicas/caches. |
| **Schema registry** | Versioned schemas for each entity type, with field-level documentation. |
| **Cross-reference index** | Map of identifiers across systems (e.g., device hostname ↔ SNMP sysName ↔ IPAM ID ↔ monitoring ID). |

**Examples**: Data catalog tool, schema registry (e.g., Apicurio, schema registry in Kafka), custom metadata store.

---

## Knowledge Platform

**Purpose**: Store and serve the canonical, relational, curated view of the network.

| Capability | Description |
|---|---|
| **Graph model** | Entities and their relationships (device ↔ interface ↔ circuit ↔ location). |
| **Historical view** | Point-in-time snapshots for audit and what-if analysis. |
| **Policy attachment** | Which policies apply to which entities. |
| **Query interface** | Structured queries (graph, SQL, API) for consumers. |

**Examples**: Network graph database, CMDB replacement, knowledge graph.

---

## Instances Platform — Static Data

**Purpose**: Inventory and configuration data. Candidate shape: bitemporal and modal, with current state as a view ([idea](../ideas/bitemporal-modal-inventory.md)).

| Capability | Description |
|---|---|
| **Device inventory** | Hardware model, serial numbers, firmware, role, location, status. |
| **Interface inventory** | Ports, speeds, media types, administrative state, connected to. |
| **IP address management** | Subnets, allocations, reservations, DNS associations. |
| **Configuration state** | Running and startup configurations, templated vs. actual. |
| **Software/version catalog** | OS versions, features, licenses, end-of-life tracking. |

**Examples**: IPAM tool, config management database, asset management system.

---

## Instances Platform — Time-Series Data

**Purpose**: How the network behaves over time.

| Capability | Description |
|---|---|
| **Telemetry** | Interface counters, CPU/memory, environmental sensors. |
| **Flow data** | NetFlow, IPFIX, sFlow — traffic matrices, conversations. |
| **Event logs** | Syslog, SNMP traps, change events, alarm history. |
| **Performance metrics** | Latency, jitter, packet loss, utilization trends. |

**Examples**: Time-series database (e.g., TimescaleDB, InfluxDB, Prometheus), observability platform.

---

## Key Cross-Cutting Concerns

- **Synchronization**: How do platforms stay consistent? Event-driven? Polling? Periodic reconciliation?
- **Identity**: How does the same device get the same ID across all four categories?
- **Access control**: Who can read/write what, enforced consistently across platforms?
- **Time**: Does Knowledge Platform history derive from bitemporal facts or keep its own snapshots?
