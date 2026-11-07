# Glossary

| Term | Definition |
|---|---|
| **Asserted** | Modality: a fact stated by a person or system of record. See [idea](ideas/bitemporal-modal-inventory.md). |
| **Bitemporal** | A fact carries both valid time and record time. |
| **Canonical model** | The authoritative, agreed-upon definition of an entity type and its attributes. There is exactly one canonical model per entity type. |
| **CFP Network Data** | The data describing the network estate owned by Core Foundational Platforms (CFP). The subject of this program. |
| **Data platform** | A system that stores, serves, and manages a category of network data. Part of the target architecture. |
| **Discovered** | Modality: a fact observed by a discovery mechanism. |
| **Discovery** | Observing the network to produce facts. Proposed as separate from inventory ([idea](ideas/discovery-decoupled-from-inventory.md)). |
| **Effort size** | T-shirt estimate (S, M, L, XL) for a phase or initiative. Not a duration. |
| **Entity** | A thing we model: device, interface, circuit, location, service, customer, policy, etc. |
| **Estate** | The complete set of data sources, stores, and pipelines that exist today (legacy + target). |
| **Idea** | Early, non-binding thinking in `ideas/`. Promoted to an ADR when agreed. |
| **Inventory** | Curated record of what exists, existed, or is planned. |
| **Knowledge platform** | The system that holds the curated, relational, historical view of the network. The "what we know" layer. |
| **Metadata registry** | The system that tells you what data exists, where it lives, and what it means. The "map" of the data ecosystem. |
| **Modality** | The basis on which a fact is held: discovered, asserted, or planned. |
| **Oracle authority** | Who decides what is true for an attribute (device, control plane, person, planning system). |
| **Planned** | Modality: a fact stating intent — a desired or future state (P4). |
| **Platform** | See *Data platform*. |
| **Points** | Team-relative effort for a backlog item. Converts to time only via measured velocity. |
| **Provenance** | The recorded path by which a specific fact arrived: collector, origin system, time. |
| **Reconciliation** | The process of comparing data across sources to detect and resolve conflicts. |
| **Record time** | When we held a fact. Also called transaction or system time. |
| **Source authority** | The system authoritative for holding and serving an attribute (e.g. the inventory system). |
| **Source of truth** | Not one thing. Splits into oracle authority, source authority, and provenance ([idea](ideas/source-of-truth-dimensions.md)). |
| **Strangler fig pattern** | A migration pattern where new capabilities are built alongside existing systems; traffic gradually shifts to the new system; the old system is retired when empty. |
| **Target architecture** | The desired future state of the data ecosystem, as defined by this program. |
| **Telemetry (data ecosystem)** | Observability of the data platforms themselves: uptime, sync latency, quality metrics, pipeline health. |
| **Threshold** | The value a KPI must meet. Required for every success dimension; set from a measured baseline. |
| **Valid time** | When a fact is true in the network. Also called application or business time. |
