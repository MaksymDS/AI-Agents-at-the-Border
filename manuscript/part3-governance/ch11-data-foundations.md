---
title: "Data Foundations and Governance"
part: "III — Governance and Trust"
chapter: 11
status: review
version: 0.3
last-updated: 2026-07-09
---

## The question that finds the fourteen folders

The pilot planning session is going well until someone asks the agent's
first question for it: *"When it checks a classification dispute, where
does it read the precedents?"*

The tariff database, everyone agrees, is fine — structured, maintained,
queryable. The precedents are another matter. Binding rulings live in a
document management system, except the ones before 2016, which live in a
shared drive, except the appeals decisions, which the legal directorate
keeps in its own folders — fourteen of them, one per year, organized by a
scheme that changed twice. Three of the most important rulings exist as
scans of signed paper. One officer knows where everything is; he retires
in March.

No modern administration is surprised by this scene, and no vendor slide
survives contact with it. Classical data management — quality,
governance, integration, the discipline the WCO's 2025 report documents
thoroughly[^ch11-1] — remains the foundation, and this chapter will not
repeat it. What it adds is the layer that reports written for the
scoring era did not need: **what agents specifically require from data**,
and how the governance apparatus of this Part extends to the corpora,
feeds, and feedback loops that agents live on.

## 11.1 The four things agents need that models did not

A risk-scoring model needed one thing from the data estate: a clean
training table. An agent needs four, and each is a build.

**A machine-readable substrate.** Chapter 3's Rung 1, restated as a
dependency: every document class the agent must read — declarations,
invoices, certificates, prior correspondence — extracted, structured,
and indexed at ingestion, not on demand. The test is operational: if a
human investigator needs three systems and a folder hunt to assemble a
case file, an agent needs the same integrations *plus* the guarantee
that each one is machine-consumable. India's codification of free-text
supplier names into structured entities is the canonical example of this
unglamorous, value-unlocking work.[^ch11-2]

> **Field note — the knowledge graph, where structured entities become
> a risk instrument.** India's supplier-codification (§15.5) is the first
> step of a pattern the adjacent financial-crime domain has already
> industrialized: once entities are resolved, the relationships *between*
> them become the highest-value signal, and a knowledge graph is the
> structure that holds them. The banking evidence is quantified. The EDM
> Council's Open Knowledge Graph prototype reported KYC/AML cost
> reductions of 30–40% with fewer false positives; entity-resolution on
> open corporate-registry data has mapped ownership networks to flag risk
> hubs — single addresses linked to thousands of companies, the signature
> of shell-company formation — and the same technique helped a government
> detect fraud in pandemic loan schemes.[^ch11-4] The customs translation
> is immediate: the cross-importer undervaluation ring and the circular
> supply chain (Chapter 15) are graph structures, invisible to
> per-declaration rules and visible the moment entities are linked.
> Figure 11.1 shows the shift — the same three shipments read first as
> isolated declarations, then as one linked network. These are banking
> numbers, not customs outcomes, but the method transfers because the task
> is identical: find the rare bad actor hiding in the relationships (see
> endnote 3).

> **ADJACENT EVIDENCE — HYPOTHESIS, NOT FORECAST.** The financial-crime
> example supports the network method: linked entities can reveal a pattern
> that isolated records conceal. It does not establish a customs detection
> uplift. The local hypothesis must name the entities, labels, review cost,
> lawful data links, and pilot threshold before a benefit is claimed.

![Figure 11.1 — From Filings to a Network](/assets/diagrams/fig-ch11-entity-network.svg){width=100%}

**Retrieval-ready knowledge.** The regulations, rulings, procedures, and
circulars the agent reasons *from* — assembled into a corpus with three
properties the fourteen folders lack: **completeness** (a defined
inventory of what is in and what is not — an agent that silently lacks
the appeals decisions gives confidently incomplete answers),
**currency** (a maintenance process with an owner, because a corpus that
was right in January is a liability by June), and **citability** (every
retrievable passage carries its source identity, so the grounding
discipline of Chapter 3 has something to ground *to*).

**Governed system access.** The agent's tools are data interfaces, and
the data governance question is now a permissions question: which
systems, which fields, read or write, under whose identity. This is
Chapter 9's agency dial expressed in data terms — and it is where
purpose limitation (Chapter 8's Layer 1) becomes engineering: an agent
compiling valuation case files has no lawful reason to read passenger
records, and the permission set, not a policy memo, is what enforces
that.

**Feedback capture.** Every officer confirmation, correction, and
override of an AI output is a labeled data point — the administration's
own, unpurchasable, most valuable dataset. Capturing it is a design
requirement from day one of Rung 1: it is simultaneously the evidence
for the ladder's "climb on evidence" rule (Chapter 12 consumes it), the
retraining signal, and the drift alarm. Korea's stated lesson from a
decade of this work compresses the section into a sentence: data access
is a basic requirement, but *"data is a means, not an end"* — the asset
is the loop, not the lake.[^ch11-3]

## 11.2 The knowledge base is infrastructure — build it like some

The retrieval corpus deserves its own discipline, because Chapter 3 made
it the highest-leverage build and Chapter 10 made it an attack surface.
The build sequence that works:

1. **Inventory before ingestion.** List the corpus's intended contents —
 instruments, rulings, procedures, date ranges, languages — and,
 equally, its exclusions. The inventory is a governance document: it
 is the answer to "what does the assistant know," and its gaps are
 disclosed, not discovered.
2. **Digitize with provenance.** Every item enters with source, date,
 authority, and status (in force / superseded / under appeal). A
 ruling without status metadata is a wrong answer waiting for its
 moment.
3. **Structure for retrieval, not for archiving.** The unit of retrieval
 is the passage a question needs, not the 400-page PDF that contains
 it — which means investment in segmentation and cross-references
 (the ruling that cites the regulation that implements the code).
4. **Version and sign.** Chapter 10's rule made operational: corpus
 changes go through controlled, signed updates with an audit trail —
 the knowledge base is protected like the codebase because it now
 *functions* like one.
5. **Assign the owner.** A named custodian per corpus, with a currency
 SLA (new rulings ingested within N days) and a quarterly completeness
 review. The retiring officer's knowledge becomes an institutional
 process or it becomes a loss.

An honest note on effort: this is routinely the largest single line in a
program's first year (Chapter 5 said so in the TCO discussion), and it
is the least demonstrable — no minister was ever photographed next to a
well-provenance corpus. Build it anyway; every assistant and agent the
administration ever deploys will stand on it.

## 11.3 Governance extensions, not governance repetition

Three classical governance topics acquire an agentic clause each.

**Classification drives two decisions now.** Data sensitivity
classification always drove storage and access; it now also drives
**deployment pattern** (Chapter 3's decision tree routes workloads by
the sensitivity of the data they touch) and **agency** (the more
sensitive the data a task requires, the lower the oversight tier that
task can route to — Chapter 9's four factors, one of which is data
sensitivity, doing double duty). The practical artifact: the data
classification scheme and the AI inventory reference each other, task
by task.

**Sharing agreements gain an AI clause.** Inter-agency and international
data exchange — Single Window partners, other border agencies, WCO-
framework exchanges — was negotiated for human and system-to-system
consumption. When an agent becomes the consumer, two questions need
explicit answers in the agreement: may shared data enter model training
or retrieval corpora, and may agent-produced outputs derived from shared
data flow onward? Assuming yes has ended partnerships; asking early is
free.

**Retention meets trajectories.** Chapter 9 mandated trajectory logging;
those logs *contain* the data the agent touched — trade data, personal
data — and inherit its protection obligations and retention rules. The
audit trail is itself a data governance object: retained long enough for
accountability (and Article-14-class regulation), minimized and
protected like the sensitive data it embeds.

## 11.4 Quality: the honest sequencing answer

Every administration asks the same question in the same words: *"Is our
data good enough?"* The scoring-era answer was a multi-year cleansing
program before value. The agentic-era answer is more useful: **match the
workload to the data you have while building the data you need.**
Document intelligence (Rung 1) *tolerates* messy inputs — reading
imperfect scans is its job — and, run at scale, it becomes the
administration's most effective data quality instrument: extraction
reconciliation surfaces the inconsistencies no audit ever found, at the
source, transaction by transaction. Grounded assistants (Rung 2) need
corpus quality, which section 11.2 builds deliberately. Agents (Rung 3)
need transactional data quality high enough to act on — and by the time
a task has climbed the ladder on evidence, the feedback loops of 11.1
have been improving exactly that data for months.

The sequencing is the answer: data readiness is not a gate in front of
the program; it is a product of running the program in the right order.

## 11.5 From data lake to decision-grade evidence

The tempting architecture answer is a data lake: collect everything,
standardize later, and let models find patterns. For an agentic customs
workflow that is insufficient. The agent needs to know not only that a
record exists, but **what it means, who supplied it, when it was valid,
which version governed the case, and whether it is permitted evidence
for this decision**. A lake stores; a decision-grade evidence layer
explains and constrains.

Build that layer around a small number of high-value entities—consignment,
declaration, trader, document, ruling, commodity, conveyance, inspection,
case and outcome—and make the relationships explicit. Use the WCO Data
Model where it fits, preserve source-system identifiers, attach
provenance and validity, and expose the result through governed APIs.
The first target is not an enterprise ontology program. It is the
minimum semantic spine needed for one case loop to cite its evidence and
for an officer to correct it.

This changes the business conversation around data quality. A generic
"clean the data" initiative is costly and endless. A decision-grade
initiative asks: which fields, links and documents are necessary to make
this specific action defensible; which missing values force escalation;
which conflicting sources have priority; which corrections become
feedback for the next case? The scope becomes fundable, testable and
reusable. Every added agent then consumes a stronger evidence layer
instead of inventing its own private context.[^ch11-5]

## 11.6 The data contract: make the evidence layer operable

The semantic spine becomes durable only when its contributors and
consumers have a **data contract**. For each high-value feed, specify
the business owner, permitted purpose, fields and classifications,
source-system identifier, freshness expectation, allowed values,
quality thresholds, retention rule, change notice, and the response
when the feed is late or contradictory. The contract belongs to the
operating workflow, not to an abstract enterprise architecture library.

This changes integration from an optimistic project milestone into a
managed service. If a declaration status feed is delayed, the agent
must know whether to wait, escalate or proceed on an older version. If
a tariff ruling is superseded, retrieval must prevent the older ruling
from silently governing a new case. If a trader identifier changes, the
case record must preserve the link without creating a false match. Such
questions sound technical until they decide whether an officer can rely
on a recommendation. The contract supplies the answer before the busy
day arrives.

Start with the two or three feeds that decide the first workflow, not
with a cross-government data perfection programme. Publish a simple
scorecard each month: availability, freshness, completeness for the
decision-critical fields, conflict rate, and time to correct. Pair it
with an escalation rule: when a feed falls below threshold, the agent
loses the authority that depended on it and routes the case to human
review. That is not a data-team failure; it is a designed safety
behaviour. It makes data quality visible to the operational owner who
benefits from fixing it.

The result is compounding value. The first agent pays for an evidence
contract that is reusable by valuation, classification, risk and trader
service workflows. Conversely, every ungoverned private retrieval index
creates another migration and audit problem. Fund the shared evidence
layer as a product with a roadmap, service levels and a named product
owner; judge it by decisions made more defensible and faster, not by
terabytes accumulated.

## 11.7 Evidence quality is a frontline management responsibility

Data governance often appears to officers as a request from a central
team to improve fields they do not own. Reverse the relationship. Show
the frontline which missing field, stale ruling or contradictory document
caused an avoidable escalation; let the officer classify the correction;
then route that correction to the source owner with a measurable service
clock. The evidence layer becomes useful when it shortens the next real
case, not when it produces a larger data-quality report.

Create an exception taxonomy that separates extraction error, source
absence, source conflict, policy ambiguity, data-entry defect, identity
mismatch and workflow gap. Each category has a different remedy. A
model team can improve extraction; a policy owner must clarify a rule;
a source-system owner must correct a feed; operations may need to change
the case route. Without this taxonomy, all corrections become generic
"AI feedback" and none of the underlying causes gets fixed.

Publish only a few measures: mandatory-evidence completeness, source
freshness, conflict rate, time to correction and the number of cases
that lost authority because a feed did not meet its contract. These are
not technical vanity metrics. They tell leadership whether the evidence
needed for a lawful, timely decision is becoming more reliable. The
feedback loop is also the investment case for steward capacity: it turns
ordinary case work into a compounding asset rather than a private
workaround.

## Decision Toolkit — Chapter 11

**The per-use-case data readiness check** (run before any pilot
charter): Which document classes must this task read, and what share is
machine-readable today? Which corpus does it reason from — inventoried,
current, cited, owned? Which systems must it touch — integrated,
permissioned to purpose, under whose identity? What feedback will it
capture, and where does that land? Which sharing agreements cover any
non-native data — and do they contemplate AI consumption?

**The corpus charter** (one page per knowledge base): contents and
exclusions · provenance and status metadata standard · retrieval
granularity · update SLA and signing process · named custodian · review
cadence.

**The two-registry rule:** the data classification scheme and the AI
inventory (Chapter 9) cross-reference each other — every AI task lists
its data classes; every sensitive data class lists the AI tasks touching
it. Any orphan on either side is a finding.

## Key Takeaways

- Agents need four things models did not: a machine-readable substrate,
 retrieval-ready knowledge, governed system access, and feedback
 capture — each a build with an owner, not an assumption.
- The knowledge base is infrastructure and attack surface at once:
 inventoried, provenance-tagged, retrieval-structured, version-signed,
 and owned — protected like the codebase because it functions like one.
- Classical governance extends rather than repeats: classification now
 drives deployment and agency; sharing agreements need an explicit AI
 clause; trajectory logs inherit the obligations of the data they
 embed.
- "Is our data good enough?" is a sequencing question: Rung 1 tolerates
 mess and repairs it at the source; the ladder's own feedback loops
 build the quality that higher rungs require.
- The loop is the asset, not the lake — every officer correction is the
 administration's own labeled data, and capturing it is a day-one
 design requirement.

---

## Endnotes {#ch11-endnotes .ch11-endnotes}

[^ch11-1]: WCO Smart Customs Project, *Detailed Report on the Adoption of AI
 and ML in Customs* (Mar 2025) — data management, quality, and
 governance foundations: structured, semi-structured and unstructured
 data; cleansing, normalization, structuring, labeling and validation.
 This chapter extends, rather than restates, that baseline.
 <!-- bib: wco_scp_report2025 -->

[^ch11-2]: Indian Customs (NCTC): unsupervised ML codification of free-text
 supplier entities enabling cross-importer comparison and network
 analytics (WCO News 109, Issue 1, 2026). <!-- bib: wconews109_india2026 -->

[^ch11-3]: Korea Customs Service stated lessons (WCO News 108, Issue 3,
 2025): data access as a basic requirement; "data is a means, not an
 end"; analytics teams must understand operational staff; feedback
 loops between ICT and customs teams. <!-- bib: wconews108_korea -->

[^ch11-4]: Knowledge-graph evidence (adjacent, financial-crime domain):
 EDM Council Open Knowledge Graph prototype reporting KYC/AML cost
 reductions of ~30–40% with reduced false positives; entity-resolution
 on open corporate-registry data (e.g., Quantexa with OpenCorporates
 bulk data) mapping ownership networks to flag risk hubs — addresses
 linked to thousands of companies — and supporting UK Cabinet Office
 detection of Covid-19 loan fraud; Gartner tracking graph technology
 from ~10% (2021) toward a large majority of data-and-analytics
 innovations by 2025. Cross-domain evidence, cited as method-transfer
 precedent for entity-network risk detection, not a customs outcome.
 <!-- bib: edmcouncil_okg2025, opencorporates_leg2025, gartner_graph2025 -->

[^ch11-5]: WCO's detailed report identifies data management, quality,
governance and integration with Customs Management Systems and Single
Windows as implementation foundations. The decision-grade evidence layer
is the agentic extension: provenance, validity and permissible use are
retained with the data so an action can be justified later.
<!-- bib: wco_scp_report2025 -->
