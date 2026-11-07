# The Problem Statement

## The One-Liner

**Our network data is fragmented, inconsistent, and untrusted. Every team that needs data builds their own copy, their own model, their own pipeline — and none of them agree.**

## The Details

We operate a network of significant scale and complexity. To run it, we need data: what devices exist, how they connect, what they run, how they behave, what policies apply. Today, that data is scattered across:

- **Multiple source-of-truth systems** that disagree with each other.
- **Spreadsheets and local databases** maintained by individuals.
- **Vendor-specific tools** that expose data in proprietary formats and cannot talk to each other.
- **Custom integrations** that break silently when upstream systems change.

The result is a system that is:

| Symptom | Effect |
|---|---|
| **Fragile** | One team's pipeline breaks another team's workflow. No one knows until something burns. |
| **Expensive** | Every new use case requires building bespoke data pipelines. We pay for the same integration N times. |
| **Error-prone** | Decisions are made on stale or contradictory data. "Which IPAM is correct?" is a recurring question. |
| **Slow** | Adding a new device type, vendor, or location takes weeks of manual work across teams. |

## What We Are Not Saying

- This is not about "bad people." The current state is the rational outcome of years of point solutions solving immediate problems.
- This is not about building a monolith. We are not replacing fragmentation with a single database that rules them all.
- This is not a reorg. We are changing how data is modelled, governed, and shared — not necessarily who does what.

## The Core Tension

> *The network exists to serve the business. The data about the network exists to serve the network teams. If the data is not trusted, the teams cannot move fast — and neither can the business.*

We solve this by building a coherent data architecture: clear models, agreed conventions, governed policies, and platforms that make data discoverable and trustworthy by default.
