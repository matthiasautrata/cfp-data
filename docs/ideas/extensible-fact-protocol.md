# Idea: One Extensible Fact Protocol for All Producers

## Status

Idea, under discussion. It becomes an ADR once the team agrees.

## Context

We do not build discovery, monitoring, or event-management tools; we enable them (principle P12). That moves the design effort from features to the protocol through which those tools deliver data. If each producer delivers data in its own way, we recreate today's fragmentation inside the new platform.

Discovery agents, monitoring systems, systems of record, and planning tools all produce facts about the same entities. They differ mainly in how they know what they report: observed, stated, or planned. That is the modality dimension we already keep with every fact ([idea: record time and modality](bitemporal-modal-inventory.md)).

## Proposal

All producers publish facts through one extensible protocol, as streams on an event bus. Each message carries:

| Field | Content |
|---|---|
| **Entity** | The identifier of the entity the fact is about, and its type |
| **Attributes** | The values reported, in the versioned schema for that entity type |
| **Valid time** | When the reported values are true in the network |
| **Modality** | `discovered`, `asserted`, or `planned` |
| **Provenance** | Which producer, from which source, and when it was collected |
| **Schema version** | The version of the entity-type schema used |

Record time is not sent by the producer: it is the time the data layer accepted the message.

The data layer keeps the stream. Inventory, current state, and history are views built from it. This is close to the *event sourcing* pattern: the stream of facts is what is stored, and everything else is derived.

Extending the protocol means adding entity types and attributes to the registry, not changing the protocol itself.

## Trade-offs

- Gains: a new producer is a new publisher, not a project; one path in for every modality; history and record time come naturally; producers can be replaced without touching consumers (principle P2).
- Costs: the protocol and its schemas become critical shared infrastructure that must be versioned with care; views must be rebuilt when their logic changes; producers that only deliver batch files need adapters.

## Prior Art

- [CloudEvents](../references/cloudevents.md): a standard event envelope; the obvious candidate for wrapping each message.
- [AsyncAPI](../references/asyncapi.md): for describing the streams and their messages.
- [OpenTelemetry](../references/opentelemetry.md): its collector and protocol are a working example of many pluggable producers feeding one pipeline.
- [RFC 9232](../references/rfc9232.md), the IETF network telemetry framework, and streaming with gNMI and YANG-push: the same idea, from the network side.
- [Event sourcing](../references/event-sourcing.md): the pattern for deriving views from a stream of facts.
- [Erlang/OTP](../references/erlang-otp.md), loosely: components that connect only by messages, fail in isolation under supervision, and can be replaced while the system runs. Telecom management planes and some messaging back ends are built this way.

## Open Questions

- Ordering and duplicates: what guarantees do producers give, and what must the data layer tolerate?
- Facts that arrive late, or are corrected later.
- How does a producer say that something is no longer observed?
- Does high-volume time-series data use this protocol, or only its metadata? (See the time-series subsystem in [Producers, Consumers, and Extension Points](../solution/06-producers-consumers.md), and issue I-14.)
- What happens when producers send faster than the data layer can accept?

## Notes

- **Date**: 2026-11-07
- **Author**: Matthias Autrata
- **Reviewed by**: —
- **References**: [Idea: discovery decoupled from inventory](discovery-decoupled-from-inventory.md), [Idea: record time and modality](bitemporal-modal-inventory.md)
