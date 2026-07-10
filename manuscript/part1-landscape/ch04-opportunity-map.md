---
title: "The Agentic Opportunity Map for Customs"
part: "I — The Landscape"
chapter: 4
status: review
version: 0.3
last-updated: 2026-07-09
---

## The prioritization workshop

It is the second hour of the modernization workshop and the whiteboard has
become a hostage situation. The head of risk targeting wants AI on
selectivity first — "that is where the revenue is." The head of the call
center wants the trader helpdesk automated — "that is where the complaints
are." The classification directorate wants HS support — "that is where the
disputes are." Legal wants none of it near penalties, and the CFO wants to
know why the list has eleven items and the budget has room for two.

Everyone in the room is right about their own function and blind to the
portfolio. What is missing is not enthusiasm but a **map**: a single view
of the customs value chain that shows, for every function, what kind of AI
fits, how much autonomy it can bear, what value it produces, and what can
go wrong. This chapter is that map. It will not tell you what to deploy —
that depends on your readiness (Chapter 6) and your business case
(Chapter 5). It will make the argument in the workshop three hours shorter.

## 4.1 Three axes, one discipline

Every cell of the map is scored on three axes.

**Value driver.** Customs AI creates value through four channels, and it
pays to name which one a use case serves: **revenue** (better detection of
undervaluation, misclassification, evasion), **efficiency** (officer-hours
returned, throughput per lane), **facilitation** (clearance time, trader
experience, predictability), and **control** (detection of prohibited and
restricted goods, sanctions compliance, security). A use case that cannot
name its channel is a demonstration in search of a budget line.

**Risk class.** What happens when the system is wrong? The map uses three
classes. **Low**: the error is caught in review or costs minutes (a bad
draft, a poor summary). **Medium**: the error affects operations or a
trader's time but is reversible (a wrong routing, an unnecessary document
request). **High**: the error touches a trader's legal position, revenue
determination, or enforcement (an assessment, a penalty, a seizure, an
AEO status decision). Risk class is about the *decision the output feeds*,
not about the model.

**Autonomy ceiling.** The highest rung of the Autonomy Ladder (Chapter 2)
a task can justify even in principle, given its risk class and
reversibility. Ceilings are conservative by design: a ceiling of L2 means
"do not accept vendor proposals above L2 for this task, whatever the
accuracy claims." Programs then climb *toward* the ceiling on evidence —
they do not start there.

The discipline the axes impose is simple: **high-value functions are often
high-risk functions, and the resolution is not to avoid them but to enter
them at low autonomy.** Valuation is the canonical example: enormous
revenue value, high risk class — so the map places AI there early, but as
an L1/L2 analyst's tool, with the autonomy ceiling rising only for
narrow, reversible slices of the task.

## 4.2 The map, function by function

Table 4.1 is the master view. The paragraphs that follow give the
reasoning a leader needs when the table is challenged — and it will be.

**Table 4.1 — The Agentic Opportunity Map** *(content specification for
Figure 4.1)*

![Figure 4.1 — The Agentic Opportunity Map](/assets/diagrams/fig-ch04-opportunity-map.svg){width=100%}

::: {.opportunity-table}

| Function | Agent role | Value | Risk / autonomy ceiling | Minimum data |
|---|---|---|---|---|
| Declaration processing & validation | Document checker: reconciles declaration and documents; flags discrepancies | Efficiency; facilitation | Medium · L3; L4 only for low-risk green-lane release | Readable documents; declaration history |
| HS classification support | Classification analyst: proposes code, sources and rationale | Revenue; efficiency | High · L2 at determination; L3 internal pre-screen only | Rulings; tariff; product description |
| Customs valuation | Valuation analyst: comparables, anomalies, case file | Revenue | High · L2; L3 compiles case file, never assessment | Transactions; reference prices; exchange data |
| Risk targeting & selectivity | Targeting co-analyst: enriches signals, drafts and explains profiles | Revenue; control | High · L3; officer approves profiles; scoring ML remains governed | Outcomes; seizures; manifest data |
| Post-clearance audit (PCA) | Audit associate: selects candidates, compiles dossiers, drafts findings | Revenue | Medium–High · L3 for selection/dossier; findings human | Readable declarations; audit history |
| AEO / trusted trader management | Compliance monitor: obligations, renewal dossiers, early warnings | Facilitation; control | Medium · L3 monitoring; status decision human | AEO records; compliance events |
| Passenger processing | Risk assistant: advance-information triage for officers | Control | High / rights-sensitive · L2; most regulated cell | API/PNR under legal basis |
| Trader helpdesk & rulings support | Service agent: grounded information; drafts rulings for review | Facilitation; efficiency | Low–Medium · L3 information with citations; binding answer L2 | Cited Rung-1/2 corpus |
| Internal operations | Back-office assistant | Efficiency | Low · L3 | Internal document stores |

:::

Four rows deserve commentary because they carry the most workshop
conflict.

**HS classification** is where administrations most want autonomy and
should accept it last. The task looks mechanical and is actually legal
interpretation: a code determines duty, and a systematically wrong code is
systematic revenue error with trader-litigation attached. The ceiling —
L2 at the point of determination — is not timidity; it reflects that
classification disputes are *adversarial*, and an agent's reasoning will
be examined by the other side. What changes the economics anyway: an L2
copilot that turns a 20-minute lookup into a 2-minute confirmation, and an
L3 pre-screener that checks *incoming declarations'* self-classified codes
at scale and routes only anomalies to humans. Same technology, different
autonomy per task — Rule 1 from Chapter 2 doing real work.

The public record supports the ceiling. Deployments exist — Dubai Customs'
Al Munasiq suggests HS codes from a photo or description, and HS-code
prediction is one of the Korea Customs Service's eleven production AI
models[^ch04-1] — yet no administration has published an accuracy figure for
HS classification support, anywhere. Read that absence as information: the
administrations furthest ahead treat classification AI as officer support
whose performance is managed internally, not as an autonomous capability
to advertise. When a vendor quotes an HS accuracy number no customs
administration will publicly stand behind, the ceiling has already told
you what to do with it.

> **Field note — HS classification, where the private market confirms the
> ceiling.** The trade-compliance software market — where vendors *do*
> publish accuracy — corroborates the caution rather than undermining it.
> Commercial classifiers report reasoning traced step-by-step through the
> General Rules of Interpretation, confidence scores on every code, and
> automatic citation of binding rulings — an agentic pattern that looks
> impressive precisely because it is built for defensibility. But the
> published accuracy is exactly where the ceiling lives: reported figures
> range widely and are entirely scope-dependent — a top-3 suggestion at
> the six-digit level is a different claim from a single top-1 code at
> full national granularity — and even a 95%-class result means roughly
> one in twenty shipments misclassified. The peer-reviewed customs
> literature bears this out rather than the marketing sheets; and Canada's
> Auditor General once estimated that a fifth of goods entering the
> country were misclassified *by humans*.[^ch04-4]
> The lesson is not that the tools fail; it is that classification is hard
> enough that error is the normal case, which is why the honest deployments
> keep an officer at the point of determination and route confidence scores,
> not verdicts. The market's own numbers argue for the book's L2 ceiling.

**Risk targeting** already runs on ML in most modern administrations; the
agentic addition is not "a smarter score" but the work *around* the score:
enriching a hit with context pulled across systems, drafting the target
profile a human approves, explaining in writing why a shipment tripped.
Keep the scoring model and the agent conceptually separate — they are
governed differently (Chapter 9), and vendors blur them.

**Passenger processing** gets the map's brightest warning color, not
because the technology differs but because the legal environment does:
natural persons, fundamental-rights exposure, and — in AI-regulation
regimes taking effect now — probable high-risk classification with
attendant obligations.[^ch04-2] Enter last, at L2, with counsel in the room
from day one.

**The trader helpdesk** is the map's honest quick win — Low risk class,
immediate facilitation value, and a built-in verification pattern
(grounded answers with citations, per Chapter 3). It is also the cell
where the line between Low and High risk is one sentence wide: the moment
an answer *binds* the administration, the risk class jumps. The design
consequence: informational answers carry an explicit non-binding notice
and citations; anything approaching a ruling routes to the L2 drafting
flow. Get that boundary into the system prompt, the interface, *and* the
policy.

## 4.3 Reading the map as a portfolio

Plotted on value-versus-risk (Figure 4.1), the functions fall into three
zones that correspond to program phases rather than verdicts.

**The entry zone** (meaningful value, Low–Medium risk): helpdesk with
citations, declaration-support document processing, internal operations,
PCA dossier compilation. This is where Chapter 3's quick wins live and
where the first 12–18 months should concentrate. The zone's job is not
just value — it is manufacturing the *evidence and operational muscle*
that the next zone requires.

**The strategic zone** (high value, High risk): classification, valuation,
targeting, PCA findings. Enter early but low — L1/L2 analyst tools — and
climb on evidence. The strategic zone is where the revenue case for the
whole program is ultimately made, which is precisely why it must not be
entered at high autonomy: a public failure here does not kill one use
case, it kills the program.

**The regulated frontier** (passenger and any rights-sensitive
processing): sequence last, design with legal from the start, and expect
external obligations regardless of internal comfort.

Two portfolio rules complete the picture. **Balance the channels**: a
portfolio of pure efficiency plays will bore the ministry of finance; a
portfolio of pure revenue plays concentrates risk in the strategic zone.
Pair them. **One function's agent is another function's tool**: the
document checker built for declaration processing becomes a tool called by
the PCA agent later — which is an argument for building shared substrate
(Chapter 3's Rungs 1–2) rather than nine disconnected pilots.

## 4.4 Five enterprise patterns worth funding

The map becomes practical when it produces patterns rather than a list
of fashionable use cases. For a large administration, five patterns
repeat across ports, airports, parcels and post-clearance work.

**Document-to-case:** ingest a declaration, invoice, certificate or
image; extract and reconcile facts; cite the source; route exceptions
to an officer. Value: lower handling time and fewer avoidable loops.
**Case-to-decision:** assemble a complete, grounded case file from
authorized systems; recommend the next procedural step; keep the human
decision. Value: faster, more consistent officer preparation.
**Signal-to-queue:** monitor an approved risk or service signal; explain
why it matters; create or reprioritize a review task within a policy
ceiling. Value: attention shifts to the queue where it can change an
outcome.
**Exception-to-resolution:** coordinate the collection of missing
documents, standard replies and status checks; escalate on a defined
clock. Value: shorter exception cycles without delegating enforcement.
**Control-to-evidence:** watch agent and process behaviour; preserve
the record; flag deviations for the owner. Value: production scale with
auditability rather than a larger compliance burden.

The first four are business workflows; the fifth is the shared control
layer that makes the others safe to scale. The portfolio rule follows:
fund one or two workflows in a single operational chain and fund the
control layer once. Do not procure five disconnected assistants because
they each have a plausible demo. The WCO's report already identifies the
common enabling requirements—data, interoperability, pilot discipline,
security and skills; agentic AI increases the return on building them as
shared infrastructure.[^ch04-5]

## 4.5 Design the portfolio around a constrained case loop

The most useful first portfolio is not a collection of departmental
ideas. It is a **constrained case loop** in which the output of one
capability becomes governed input to the next. For example: document
intelligence extracts and reconciles an invoice; a grounded assistant
assembles the relevant ruling and policy evidence; an officer decides
the exception; the outcome and correction improve the corpus and rules.
The loop has a measurable beginning, a clear human decision and a
learning signal. It creates value in its own right while building assets
that later workflows can reuse.

This design avoids a common false economy. A standalone chat assistant
may be cheap to launch but creates little reusable evidence; a large
end-to-end autonomous ambition may be impossible to approve. The loop
is a middle path: enough integration to change work, enough boundary to
measure it, and enough human control to be credible. Choose a queue
where documents are repetitive but exceptions are meaningful, where a
line owner wants a result, and where a rules-based fallback can keep
trade moving.

At portfolio review, test each candidate against three questions. Does
it share a corpus, data contract, identity pattern or evaluation set
with another candidate? Can it reuse a correction made by an officer?
Does it strengthen a decision chain rather than merely generate text?
Prioritise the candidates that answer yes. This is how a modest first
investment becomes an enterprise capability rather than a row of
expiring pilots.

## 4.6 Allocate portfolio capital by evidence stage

Do not fund every candidate as if it were ready for scale. Divide the
portfolio into three capital buckets. **Discover** funds process mapping,
baseline measurement, corpus and data checks, and a small evaluation;
its output is a decision to proceed or stop. **Prove** funds a bounded
case loop, safety and security tests, supervision design and a
representative pilot; its output is evidence of unit value and the right
to operate. **Scale** funds shared integration, operating capacity,
service continuity and the next reusable workflow; its output is a
durable operating service rather than a one-off success.

Set a maximum number of simultaneous work items in each bucket. An
administration that funds ten discovery projects but no shared control
layer creates a queue of presentations. An administration that scales a
single vendor's tool before proving the workflow creates a costly
dependency. The portfolio board should be able to see, at a glance,
which tasks are earning their next investment and which are consuming
attention without changing a decision.

Release money by artifact, not by optimism. A Discover task earns a
pilot only when its owner, baseline, lawful data path, preliminary
mandate and representative evaluation population exist. A Prove task
earns scale only when its conservative economics, safety case and
supervisory capacity pass. This is not slow governance. It is how a
large institution keeps its scarce delivery capacity on the problems
that can actually become services.

## Decision Toolkit — Chapter 4

**Prioritization scoring.** Score each candidate use case 1–5 on: (a)
value magnitude in its named channel, (b) risk class inverted (Low = 5),
(c) data readiness today, (d) evidence availability (can success be
measured within two quarters?), (e) reuse (does it build substrate other
use cases consume?). Weight (b) and (e) double for the first program
phase. Rank; take the top three into Chapter 5's business-case template.

**The ceiling check.** For every shortlisted use case, write one line:
*"Autonomy ceiling: L_, because the decision it feeds is ___ and a wrong
output would ___."* If the room cannot fill in the blanks, the use case
returns to analysis.

**The workshop script.** Run the map exercise in this order: (1) place
every proposed use case on the value/risk grid *before* discussing
vendors or models; (2) assign ceilings; (3) apply the scoring; (4) only
then discuss solutions. Sequencing the conversation this way is the
chapter's entire practical payload.

## Key Takeaways

- The opportunity map scores every customs function on three axes — value
 driver (revenue / efficiency / facilitation / control), risk class, and
 autonomy ceiling. Ceilings are entry disciplines, not verdicts.
- High value and high risk usually coincide. The resolution is low-autonomy
 entry into high-value functions, not avoidance — valuation and
 classification are analyst-tool plays first.
- The entry zone (helpdesk, document processing, internal ops, PCA
 dossiers) exists to produce evidence and operational muscle, not only
 value. The strategic zone is entered early but low. The regulated
 frontier (passenger) is sequenced last, with counsel.
- Autonomy is per task, not per function: L2 at the point of legal
 determination can coexist with L3 pre-screening in the same directorate.
- Build shared substrate, not nine disconnected pilots — today's agent is
 tomorrow's tool for another agent.
- Fund enterprise patterns—document-to-case, case-to-decision,
  signal-to-queue, exception-to-resolution—together with the shared
  control-to-evidence layer; do not buy disconnected assistants.

---

## Endnotes

[^ch04-1]: Dubai Customs' Al Munasiq application (HS-code suggestion from photo
 or description) per WCO News 102 (Issue 3, 2023) — primary confidence
 for the capability; no accuracy figures published. Korea Customs
 Service's HS-code prediction model is one of eleven AI models in
 production per WCO News 108 (Issue 3, 2025). See
 <!-- bib: wconews102_dubai2023,
 wconews108_korea -->

[^ch04-2]: EU AI Act (Regulation (EU) 2024/1689), Annex III, covers AI in law
 enforcement and in migration, asylum and border management — customs
 risk-targeting of natural persons operated in a border-management
 context can fall within high-risk classification (risk management,
 data governance, human oversight per Art. 14, conformity assessment).
 Timing note: the Digital Omnibus (final adoption June 2026) set
 standalone Annex III high-risk compliance at 2 Dec 2027; Article 50
 transparency obligations apply from 2 Aug 2026. Full analysis in
 Chapter 8 and <!-- bib: ec_navigating_aiact, consilium_aiact_omnibus2026 -->

[^ch04-4]: HS-classification accuracy: reported figures are
 scope-dependent (top-3 vs top-1, six-digit vs full national
 granularity, class count), spanning roughly 71–95% across studies —
 a bare "X% accuracy" is not meaningful without its scope. Customs-
 specific peer-reviewed treatment: Vijayakumar (2025), *World Customs
 Journal* 19(1):38–63 (BERT-based classification with explainability).
 The Auditor General of Canada estimated ~20% of goods entering Canada
 in 2015–16 were misclassified (human baseline). Cited as
 corroboration of the L2 ceiling. <!-- bib: wcj_riskmgmt2025 -->

[^ch04-5]: WCO Smart Customs Project, *Detailed Report on the Adoption of
AI and ML in Customs* (2025), identifies data management,
interoperability, cybersecurity, pilots and capacity building as shared
implementation requirements. This chapter extends the pattern to
agentic workflows: reuse the control and integration substrate rather
than funding a separate stack per use case. <!-- bib: wco_scp_report2025 -->
