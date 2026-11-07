# Idea: Multi-Agent Coordination at the Edge

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

AI plays three roles: helping to build, design, and use the system ([Stakeholders and Use Cases](../problem/02-stakeholders-use-cases.md)). Analysis, decisions, and automation benefit from agents. Core processing needs speed and reliability, not agents ([principle P10](../solution/01-principles.md)).

## Proposal

Design the edge around multi-agent coordination:

| Layer | Who | Properties |
|---|---|---|
| **Core** | Deterministic services | Ingestion, storage, reconciliation execution, policy evaluation. Fast, repeatable, testable. |
| **Interface** | APIs, with an MCP adapter ([principle P9](../solution/01-principles.md)) | One contract for people and agents |
| **Edge** | Coordinated agents | Analysis, recommendations, change proposals, automation |

Agents propose; the core executes and enforces policy. Every agent action is attributed and audited, just like a person's.

## Trade-offs

- Gains: agents can be added or replaced without touching the core; policy cannot be bypassed by an agent.
- Costs: a coordination protocol and agent identities must be designed; agent outputs vary from run to run, so they need review steps.

## Open Questions

- Which coordination pattern: a central orchestrator, a shared blackboard, or peer-to-peer? [Erlang/OTP](../references/erlang-otp.md) supervision, where a supervisor restarts a failed process, is useful prior art for agents and producers that must fail without taking others down.
- Should agent identity and authorization follow the same model as service accounts?
- Which automation may act without human approval, and under which policy?
