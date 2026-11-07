# Supporting Features

## Scope

Features that sit above the core platforms and make the data ecosystem useful, usable, and adopted.

## Sub-Areas

### Discovery

- Automated discovery of devices, links, and services (LLDP/CDP, SNMP, API polling, cloud APIs).
- Import adapters for existing data sources (spreadsheets, legacy tools, vendor databases).
- Change detection: what changed since the last discovery cycle.
- Decoupled from inventory; shares the canonical model ([idea](../ideas/discovery-decoupled-from-inventory.md)).

### Analysis & What-If

- Impact analysis: "what breaks if this link goes down / this device is decommissioned?"
- What-if scenarios: "can we absorb this traffic shift / failure?"
- Dependency mapping: which services depend on which infrastructure.
- Capacity planning: trend analysis, utilization forecasting.

### AI Enablement

- AI in three roles (build, design, use): [Stakeholders & Use Cases](../problem/02-stakeholders-use-cases.md). Access via API + MCP (P9); agents at the edge, not in the core (P10).

- Structured, queryable data that AI/ML tools can consume without bespoke extraction pipelines.
- Labeled, versioned datasets for training models (anomaly detection, predictive maintenance, traffic forecasting).
- Explanation-ready interfaces: models should be able to cite the data and policy that drove their recommendation.

### Telemetry & Observability

- Health of the data ecosystem itself: platform uptime, sync latency, data quality metrics, pipeline failures.
- Data lineage: end-to-end traceability from source to consumer.
- Usage analytics: what data is being queried, by whom, how often.

### API & Integration Layer

- Consistent API gateway for all data platforms.
- Webhook/event bus for real-time notifications.
- Bulk export for offline analysis and reporting.

## Key Questions

- What is the minimum set of discovery mechanisms needed to bootstrap the data ecosystem?
- How do we handle devices that cannot be discovered (air-gapped, legacy, third-party managed)?
- What is the threshold for "good enough" data quality before we expose data to AI/ML consumers?
