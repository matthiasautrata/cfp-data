# 7. Glossary

| Term | Definition |
|---|---|
| **Canonical model** | The authoritative, agreed-upon definition of an entity type and its attributes. There is exactly one canonical model per entity type. |
| **Data platform** | A system that stores, serves, and manages a category of network data. Part of the target architecture. |
| **Entity** | A thing we model: device, interface, circuit, location, service, customer, policy, etc. |
| **Estate** | The complete set of data sources, stores, and pipelines that exist today (legacy + target). |
| **Knowledge platform** | The system that holds the curated, relational, historical view of the network. The "what we know" layer. |
| **Metadata registry** | The system that tells you what data exists, where it lives, and what it means. The "map" of the data ecosystem. |
| **Platform** | See *Data platform*. |
| **Reconciliation** | The process of comparing data across sources to detect and resolve conflicts. |
| **Source of truth** | The authoritative system for a given data element. Every element has exactly one. |
| **Strangler fig pattern** | A migration pattern where new capabilities are built alongside existing systems; traffic gradually shifts to the new system; the old system is retired when empty. |
| **Target architecture** | The desired future state of the data ecosystem, as defined by this program. |
| **Telemetry (data ecosystem)** | Observability of the data platforms themselves: uptime, sync latency, quality metrics, pipeline health. |
