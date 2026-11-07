# Supporting Features

This document outlines a work area. It lists topics and open questions, not decisions.

## Scope

Features that sit above the core platforms and make the data useful, easy to use, and widely adopted.

## Sub-Areas

### Discovery

- Automated discovery of devices, links, and services (LLDP/CDP, SNMP, API polling, cloud APIs).
- Import adapters for existing data sources (spreadsheets, legacy tools, vendor databases).
- Change detection: what changed since the last discovery cycle.
- Current thinking: discovery is kept separate from inventory, and both share the canonical model ([idea](../ideas/discovery-decoupled-from-inventory.md)).

### Analysis & What-If

- Impact analysis: what breaks if this link goes down, or this device is decommissioned?
- What-if scenarios: can we absorb this traffic shift, or this failure?
- Dependency mapping: which services depend on which infrastructure.
- Capacity planning: trend analysis, utilization forecasting.

### AI Enablement

- AI plays three roles here: helping to build, design, and use the system ([Stakeholders and Use Cases](../problem/02-stakeholders-use-cases.md)). Agents reach the data through APIs and MCP (principle P9), and work at the edge rather than in the core (principle P10).
- Structured, queryable data that AI/ML tools can consume without bespoke extraction pipelines.
- Labeled, versioned datasets for training models (anomaly detection, predictive maintenance, traffic forecasting).
- Explainable answers: a model should be able to cite the data and policy behind its recommendation.

### Telemetry & Observability

- Health of the data platforms themselves: uptime, synchronization delay, data quality measures, and pipeline failures.
- Data lineage: end-to-end traceability from source to consumer.
- Usage analytics: what data is being queried, by whom, how often.

### API & Integration Layer

- One consistent API gateway for all data platforms.
- Webhooks or an event bus for real-time notifications.
- Bulk export for offline analysis and reporting.

## Key Questions

- Which discovery mechanisms do we need first, to get started?
- How do we handle devices that cannot be discovered (air-gapped, legacy, third-party managed)?
- How good must data quality be before we expose the data to AI and machine-learning consumers?
