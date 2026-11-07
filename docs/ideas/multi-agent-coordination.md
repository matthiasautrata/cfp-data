# Idea: Multi-Agent Coordination at the Edge

## Status

Idea — under discussion. Promote to an ADR when agreed.

## Context

AI is key in three roles: building, designing, and using the system ([Stakeholders & Use Cases](../problem/02-stakeholders-use-cases.md)). Analysis, decisions, and automation benefit from agents. Core processing needs speed and reliability, not agents ([P10](../solution/01-principles.md)).

## Proposal

Design the edge around multi-agent coordination:

| Layer | Who | Properties |
|---|---|---|
| **Core** | Deterministic services | Ingestion, storage, reconciliation execution, policy evaluation. Fast, repeatable, testable. |
| **Interface** | API + MCP adapter ([P9](../solution/01-principles.md)) | One contract for humans and agents |
| **Edge** | Coordinated agents | Analysis, recommendations, change proposals, automation |

Agents propose; the core executes and enforces policy. Every agent action is attributed and audited like a human action.

## Trade-offs

- Gains: agents can be added or replaced without touching the core; policy cannot be bypassed by an agent.
- Costs: coordination protocol and agent identity to design; non-deterministic outputs need review gates.

## Open Questions

- Coordination pattern: orchestrator, blackboard, or peer-to-peer?
- Agent identity and authorization: same model as service accounts?
- Which automation may act without human approval, and under which policy?
