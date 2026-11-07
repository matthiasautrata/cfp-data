# The Problem Statement

This document describes the current state: what is wrong, why it matters, and what it costs. The target state is described in the [vision](00-vision.md).

## The One-Liner

**CFP Network Data is fragmented, inconsistent, and untrusted. Every team that needs data builds their own copy, their own model, their own pipeline — and none of them agree.**

## The Details

We operate a network of significant scale and complexity. To run it, we need data: what devices exist, how they connect, what they run, how they behave, what policies apply. Today, that data is scattered across:

- **Multiple systems claiming authority** that disagree with each other.
- **Spreadsheets and local databases** maintained by individuals.
- **Vendor-specific tools** that expose data in proprietary formats and cannot talk to each other.
- **Custom integrations** that break silently when upstream systems change.

The result is a landscape that is:

| Symptom | Effect | Leads to |
|---|---|---|
| **Fragile** | One team's pipeline breaks another team's workflow, and nobody notices until something fails. | [Operational](#operational-risk) |
| **Expensive** | Every new use case requires bespoke data pipelines. We pay for the same integration N times. | [Consequential cost](#consequential-cost) |
| **Error-prone** | Decisions are made on stale or contradictory data. "Which IP address management (IPAM) system is correct?" is a recurring question. | [Untrusted decisions](#untrusted-decisions), [Compliance](#compliance--audit-risk) |
| **Slow** | Adding a new device type, vendor, or location takes weeks of manual work across teams. | [Reputation](#reputation-risk), [Consequential cost](#consequential-cost) |

## Consequences

If we do not fix CFP Network Data, these consequences compound. Each is happening now; none is hypothetical.

### Untrusted Decisions

If the data is wrong, no conclusion drawn from it can be trusted. Resources are invested needlessly, in the wrong places, or too late.

| Risk | Example |
|---|---|
| **Needless investment** | Buying hardware we already have, because the inventory tool says we don't. |
| **Misplaced investment** | Designing for capacity in one place while the shortfall is in another we cannot see. |
| **Late investment** | Capacity gaps found when they cause incidents, not when they can still be planned and procured. |
| **Missed opportunity** | A consolidation goes unseen because no one has a complete picture. |

### Operational Risk

| Risk | Example |
|---|---|
| **Outage duration** | Outages last longer (higher mean time to repair, MTTR) because the correct topology or configuration data cannot be found during an incident. |
| **Change-induced failures** | An unrelated change breaks a data pipeline and silently corrupts the systems that depend on it. |
| **Manual drift** | Engineers bypass broken tooling and keep their own spreadsheets, which become the de facto authority, known to one person. |

### Compliance & Audit Risk

| Risk | Example |
|---|---|
| **Inaccurate reporting** | Audit asks "which devices hold customer data" and we cannot answer definitively. |
| **Undetected policy violations** | Security policies exist but cannot be enforced, because the data needed to check compliance does not exist in a usable form. |
| **Regulatory inventory gaps** | [DORA Art. 8](../references/dora-art8.md) and [NYDFS 500.13](../references/nydfs-500-13.md) require a maintained inventory of assets, their dependencies, and lifecycle dates. With fragmented data, we cannot attest to that inventory with confidence. |
| **Retention failures** | We cannot prove data is retained or destroyed according to policy, because we cannot see what data exists. |

### Security Risk

| Risk | Example |
|---|---|
| **Blind spots** | Devices unknown to any inventory system cannot be patched or monitored. |
| **Inconsistent segmentation** | Policy intent (VLAN A is isolated from VLAN B) is not reflected in the data, so violations go unnoticed. |
| **Slow incident response** | During a security event, the data needed to trace impact (what talks to what, what runs where) is scattered across N tools. |

### Reputation Risk

| Risk | Example |
|---|---|
| **Credibility with the business** | Every new initiative starts with "first we need to clean up our data", and the business stops believing we can deliver. |
| **Talent retention** | Engineers burn out fighting data quality instead of solving interesting problems. |

### Consequential Cost

Nobody knows for certain what the data means or where it is held, so each team finds it again, extracts it again, and reconciles it again.

| Cost | Example |
|---|---|
| **Rework** | Analyses and reports redone when a second source contradicts the first. |
| **Redundancy** | The same data copied, stored, and maintained in several places. |
| **Duplicated effort** | Several teams build and run overlapping pipelines and tools for the same data. |
| **Reconciliation** | Recurring manual effort to make sources agree, for every consumer that needs them to. |
| **Software and infrastructure** | Licenses, storage, and compute for redundant tools and copies. |
| **Vendor lock-in** | Point solutions embed data in proprietary formats, making change prohibitively expensive. |
| **Opportunity cost** | Engineering time spent stitching data together is time not spent improving the network. |

We do not yet know the size of these costs. The first pass over the estate will give a first estimate, which becomes the baseline for the *Risk Reduction* [success dimension](../ways-of-working/04-success-dimensions.md).

## Why Now

The current state will not become cheaper, faster, or more reliable on its own. Every new tool, integration, and team adds to the disorder. The cost of doing nothing is rising faster than the cost of acting.

## What We Are Not Saying

- This is not about blaming anyone. The current state is the rational result of years of point solutions to immediate problems.
- This is not about building a monolith. We are not replacing fragmentation with a single database that rules them all.
- This is not a reorg. We are changing how data is modeled, governed, and shared — not necessarily who does what.

## The Core Tension

> *The network exists to serve the business. The data about the network exists to serve the network teams. If the data is not trusted, the teams cannot move fast — and neither can the business.*

We solve this by building a coherent data architecture: clear models, agreed conventions, governed policies, and platforms that make data discoverable and trustworthy by default.
