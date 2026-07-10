---
title: "Value and Economics of AI in Customs"
part: "II — The Business Case"
chapter: 5
status: review
version: 0.3
last-updated: 2026-07-09
---

## The ministry meeting

The modernization program has survived the internal workshops, and now it
faces its real examiner: the ministry of finance. The deputy minister has
three questions and a calendar slot of twenty minutes. *What will it
return? What will it cost — all of it, not the license line? And why
should I believe either number?*

Most AI business cases die on the third question, because they were built
backwards: a vendor's benefit claim, multiplied by enthusiasm, minus a
license fee. This chapter builds the case the other way — from verified
public evidence, honest attribution, and a cost model that reflects how
this technology generation actually bills. The examiner's skepticism is
not an obstacle; properly used, it is the business case's quality control.

## 5.1 The four value channels, with the evidence that exists

Chapter 4 named the channels — revenue, efficiency, facilitation, control.
Here is what the verified public record supports in each, and the
discipline for using it. Figure 5.1 collects the headline numbers as a
value board, each tagged with its evidence grade (verified customs
outcome versus adjacent revenue-agency precedent) so the ministry sees
the strength of each claim, not just its size.

![Figure 5.1 — The Verified Value Board](/assets/diagrams/fig-ch05-value-board.svg){width=100%}

**Efficiency has the strongest verified anchor in customs.** Korea's
program collapsed high-risk cargo analysis from roughly an hour to under
a minute while absorbing a near-tripling of e-commerce volume, with the
administration estimating annual savings around USD 92 million (2025).[^ch05-1]
The structure of that number matters more than its size: the savings came
from *capacity absorbed without headcount* — volume growth met with the
same staff — which is precisely the arithmetic from Chapter 1, and the
form in which efficiency value is most credible to a finance ministry
(avoided cost, not hypothetical layoffs).

**Control has quantified detection evidence.** China's image-analysis
deployment reports more than 20,000 smuggling detections since 2022
"without increasing human resources," at recognition accuracy above
95%.[^ch05-2] Brazil's SISAM — in production since 2014 — makes flagged
inspections roughly twenty times more effective than random selection.[^ch05-3]
The 20× figure is the single most useful number in this book for a
ministry audience, because it translates directly: the same inspection
workforce, pointed twenty times better.

**Revenue is where honesty pays.** Customs-specific, AI-attributable
revenue figures are scarce in the public record; the nearest strong anchor
is adjacent — Austria's tax administration attributes EUR 185 million
(2023) of incremental revenue to AI-assisted detection, and Belgium's VAT
analytics narrow ~15,000 monthly high-risk returns to ~100 confirmed fraud
cases.[^ch05-4] Use these as *revenue-agency* precedents, labeled as such. A
business case that borrows tax numbers and calls them customs numbers will
be caught doing it — by exactly the examiner who matters.

**Facilitation is real value that is easiest to mis-attribute.** The
region's famous clearance-time gains — Saudi Arabia's 80% under 48 hours,
Egypt's halved release times — were delivered by single windows and
process re-engineering, not AI (Chapter 1). The honest facilitation case
for AI is prospective and specific: continuous document verification
replacing sampling, grounded helpdesks compressing enquiry cycles,
pre-arrival document checks shortening the critical path. Model it; do
not borrow it.

The discipline across all four channels is one rule: **every figure in
the business case carries its attribution** — who reported it, whether
the technology is precisely identified, and whether it is customs or
adjacent. Chapter 15's case studies are built to this standard; your
business case should quote nothing weaker.

> **Field note — the adoption curve on the trade side.** The private
> trade-compliance market is a useful leading indicator of where customs
> value is heading, because it prices the same underlying tasks —
> classification, screening, document preparation — under competitive
> pressure. Industry reporting put the share of organizations using
> generative AI for trade compliance at around 40% in early 2026, up from
> roughly 22% a year earlier — a near-doubling in twelve months, driven
> by exactly the workloads (HS classification, sanctions screening,
> document extraction, audit-trail generation) that sit at Rungs 1–2 of
> this book's ladder.[^ch05-7] Two cautions keep the figure honest: it is
> an *adoption* rate, not a *value* rate — using a tool is not the same
> as realizing measured benefit (Chapter 1's EBIT gap) — and it is the
> trader side of the border, not the administration. But the direction is
> the signal: the counterparties an administration processes are
> automating their side of the paperwork, which raises both the volume
> and the sophistication of what arrives at the border, and strengthens
> the facilitation case for meeting it with capability rather than
> headcount.

## 5.2 The cost side: how this generation actually bills

Leaders who priced the analytics wave will misprice this one unless three
structural differences are absorbed.

**Inference is an operating cost that scales with use.** Classical
software licensed per seat or per server; a deployed model bills per unit
of work — per document read, per query answered, per agent step. This is
genuinely good news for entry (small pilots are cheap; no capital cliff)
and a genuine trap at scale (a successful workload's costs *grow with its
success*). The budget consequence: present AI running costs as a
per-unit rate multiplied by projected volume, never as a flat line —
and expect the rate itself to fall over time as models improve, an
assumption you should state explicitly and revisit quarterly.

**More spend does not buy more accuracy.** Public agent benchmarking now
prices accuracy against cost, and the frontier is not a straight line: in
one published comparison, a well-engineered configuration scored *higher*
at USD 42 per task-set than a larger model at USD 180.[^ch05-5] The
procurement consequence (Chapter 7 operationalizes it): demand
accuracy-versus-cost curves from vendors, not accuracy points. A vendor
who quotes accuracy without unit cost is quoting half a number.

**Sovereignty is a cost parameter, decided early.** The deployment
patterns of Chapter 3 carry different cost shapes: on-premises trades a
hardware and skills investment for a low marginal cost per unit;
sovereign cloud trades a higher unit rate for zero capital and managed
operations; hybrid pays some of both. None of these is "the cheap
option" universally — the point is that the sovereignty decision *is* a
TCO decision, and making it late (after a vendor's architecture is
entrenched) is the most expensive way to make it.

Beyond these three, the TCO lines that programs most often omit: data
preparation (Chapter 3's Rung 1 — routinely the largest single line in
year one), evaluation and monitoring infrastructure (the AgentOps stack
of Chapter 13), model updates and re-validation, and the human oversight
itself — supervisor time is a real cost of L3 autonomy and belongs in the
model, not in the footnotes.

## 5.3 Unit economics: the worksheet that survives scrutiny

The business-case format that withstands a finance ministry is neither a
benefits narrative nor a five-year NPV built on soft assumptions. It is a
**unit-cost comparison**: what does one unit of work cost today, all-in,
and what will it cost with the system — at current volumes and at
projected volumes?

The worksheet (Appendix E provides the full template) has five lines per
workload:

1. **Unit defined** — one declaration validated; one enquiry resolved; one
 audit dossier compiled. If the unit cannot be defined, the workload is
 not ready for a business case.
2. **Baseline unit cost** — loaded officer time per unit today, from a
 simple time study (not from anyone's memory).
3. **Projected unit cost with the system** — officer time remaining
 (review, exceptions, oversight) plus the per-unit inference and
 platform cost, at the autonomy level actually planned, not the level
 aspired to.
4. **Volume line** — units per year, today and projected; this is where
 the e-commerce curve does the arguing.
5. **Quality delta** — the channel-specific gain (detection rate,
 clearance time, error rate), stated with its evidence grade:
 *verified elsewhere / piloted here / modeled*.

Three honest features make this format credible. It prices oversight
instead of hiding it. It separates efficiency (lines 2–4, hard) from
quality gains (line 5, graded). And it produces the number the deputy
minister actually asked for: cost per declaration, before and after — a
number that survives being checked.

## 5.4 The cost of not adopting

The counterfactual belongs in the case, stated without melodrama. It has
three components, each computable from the administration's own data:
the **capacity gap** (projected volume growth priced at today's unit
cost — the staffing budget that would otherwise be requested); the
**detection gap** (what a 20×-class targeting improvement implies about
what current selection is missing — bounded, conservatively, using the
administration's own post-clearance audit recovery rates); and the
**competitive gap** (traffic elasticity to clearance times where the
administration competes for transshipment — the one component that is
partly strategic rather than arithmetic, and should be labeled so).

The counterfactual is also where timing enters honestly: waiting has a
price, but so does haste — a failed high-autonomy deployment sets a
program back years (Chapter 4's strategic-zone logic). The recommendation
this book stands behind: the cost of *not starting Rungs 1–2* is nearly
pure loss; the cost of *not yet attempting L4* is nearly zero.

Two external reference points help calibrate the ministry conversation,
carefully labeled — both are cross-industry enterprise figures, not
customs, and belong in the case as directional benchmarks rather than
promises. First, the value that does materialize tends to be
function-level before it is enterprise-level: McKinsey's 2025 survey
found respondents reporting roughly 10–20% cost reductions in functions
such as software engineering and IT and revenue uplift in others, even
as only about 39% reported measurable enterprise-level EBIT impact — the
gap between the two being, in the analysts' reading, a matter of
operating model and workflow redesign rather than model quality.[^ch05-6]
The lesson for a customs business case is to promise at the function
level (declaration processing, document handling, targeting) where the
evidence lives, and to treat enterprise-wide financial transformation as
a trajectory, not a launch claim. Second, the same discipline that
protects the downside is what converts pilots to value: the enterprise
failure rate is high (Chapter 1's Gartner figure), and the programs that
avoid it are the ones that scoped narrowly and measured honestly — which
is the entire argument of Chapters 4, 6, and 12, now with a price tag on
getting it wrong.

## 5.5 Value capture: the benefit is not the output

An agent can produce an excellent recommendation and still create no
value. The missing step is **value capture**: a named operational change
that turns the recommendation into a different queue, action, or
allocation of scarce officer time. If a classification agent drafts a
better code but the declaration still waits in the same queue, the
benefit is editorial. If a document agent detects a discrepancy but no
one owns the exception queue, the benefit is a dashboard. If an agent
identifies a high-risk network but targeting policy and post-clearance
capacity do not change, the benefit is an interesting lead.

For every business case, name the conversion point: *this output changes
this operating decision, owned by this role, within this service clock.*
Then measure the conversion rate alongside model quality: recommendations
accepted; accepted recommendations acted on; actions completed; value
realized. This is especially important for L3 workflows, where the
headline efficiency can be misleading. An agent that prepares ten times
as many cases may merely move a bottleneck to the officer who approves
them. The correct number is not "cases generated"; it is **net resolved
case capacity at the required quality and cost**.

Adjacent procurement evidence makes the business pattern tangible but
does not license customs promises. McKinsey reports agentic workflows
that automate tender preparation, supplier qualification, bid analysis,
clarification routing, and invoice-to-contract checks; the stated gains
come from the entire closed loop, not from a language model alone.[^ch05-8]
For customs, substitute a declaration or post-clearance case for the
tender: the value arrives only when the agent is connected to the
authorized workflow, exceptions and all. This is why Chapters 7, 12 and
13 are economic chapters as much as technology chapters.

## 5.6 Value certainty: separate observed, modelled and aspirational value

Public programmes lose credibility when a pilot's observed time saving,
a vendor's scenario model and a strategic aspiration are added into one
large number. Keep three value labels separate. **Observed value** comes
from a representative operating comparison and is traceable to cases.
**Modelled value** applies measured unit changes to an explicit volume,
adoption and cost assumption. **Aspirational value** describes a future
operating outcome that depends on policy, process or capacity changes
not yet made. All three may be useful; only the first should be reported
as realised.

Present the business case as a value bridge. Start with the baseline
cost or service measure. Show the gross benefit from the changed task,
then subtract permanent human supervision, platform and inference,
integration support, quality assurance, security and the cost of
fallback. Finally state which authority must act to capture the
remaining benefit: a queue manager, inspection director, finance lead
or policy owner. The bridge turns a model output into an accountable
management plan.

This discipline is especially important when value is societal rather
than a direct budget reduction. Faster predictable release can reduce
trader friction, but an administration should not invent a fiscal saving
unless it can measure it. Better case preparation may improve fairness
and audit quality, but it should be supported by correction and appeal
evidence. A rigorous business case makes these benefits visible without
pretending they all become cash in the same budget year.

## 5.7 Sensitivity is a management tool, not a finance appendix

The best business case identifies the assumptions that can reverse the
decision. For an agentic workflow these are usually volume, adoption,
exception rate, supervisor minutes, model and tool consumption, source-
quality remediation, downstream capacity and the duration of fallback.
Vary each in a conservative range and show the point at which the
workflow no longer creates net value or violates a service/safety limit.
The result is not a prediction; it is a map of what management must
watch.

For example, a case-preparation service may look attractive at high
volume but become uneconomic if the exception rate doubles and every
case needs senior review. That does not invalidate the idea. It may
suggest a narrower document class, a different review route, a smaller
model, better source stewardship or a phased scale plan. The sensitivity
analysis turns a debate about "AI ROI" into a set of operational levers
that named owners can change.

Report the downside honestly. Include a stress case in which the agent
is held or demoted for a defined period and the fallback absorbs the
work. If the service cannot survive that period, resilience investment is
part of the business case. A programme that prices only the expected
path is not efficient; it has simply left its risk cost off the page.

## Decision Toolkit — Chapter 5

**The business-case skeleton** (one page per workload): unit defined →
baseline unit cost (time study) → projected unit cost (with oversight
priced) → volume curve → quality delta with evidence grade → sovereignty
cost shape → counterfactual line. Appendix E holds the full template.

**Three rules for the ministry meeting:**
1. Quote no benefit without attribution (who reported it, what technology,
 customs or adjacent).
2. Present running costs as rate × volume with the rate's trajectory
 stated — never as a flat line.
3. Ask for a phased envelope tied to gate evidence (Chapter 12), not a
 monolithic multi-year budget. It is easier to grant, and it makes the
 program's honesty structural.

**The vendor cost question:** require an accuracy-versus-cost curve per
workload, unit-priced, at the autonomy level proposed. Half-numbers
(accuracy without unit cost, or cost without volume assumptions) are
returned for completion.

## Key Takeaways

- Build the case from verified anchors with attribution: Korea's ~USD 92M
 efficiency estimate, China's >20,000 detections, Brazil's 20× targeting
 effectiveness — and label adjacent (tax/VAT) evidence as adjacent.
- This generation bills per unit of work: costs scale with success.
 Present rate × volume, price the oversight, and expect — but state —
 falling unit rates.
- More spend does not buy more accuracy; demand accuracy-versus-cost
 curves from vendors, not accuracy points.
- The sovereignty decision is a TCO decision; make it before a vendor's
 architecture makes it for you.
- The unit-cost worksheet — cost per declaration before and after, with
 oversight priced and quality deltas evidence-graded — is the format
 that survives a finance ministry. The strongest counterfactual is the
 administration's own volume curve.
- Value is captured at a named operational conversion point, not when an
  agent produces a recommendation. Track the full chain from output to
  action to realized capacity or revenue.

---

## Endnotes

[^ch05-1]: Korea Customs Service: analysis time ~1 hour → under 1 minute
 against a 2.85× e-commerce volume surge (64M → 181M shipments over
 five years); estimated annual savings KRW 125.7 bn (~USD 92 M, 2025).
 Administration-stated (WCO News 108, Issue 3, 2025; APEC SCCP 2025).
 <!-- bib: wconews108_korea -->

[^ch05-2]: China GACC AI Image Analysis System: >20,000 smuggling attempts
 detected via AI alarms since 2022 without increased human resources;
 deployed algorithm recognition accuracy >95%. Administration-stated
 (WCO News 104, Issue 2, 2024; WCO AI/ML Case Study — China, 2025).
 <!-- bib: wconews104_china -->

[^ch05-3]: Brazil Receita Federal, SISAM: flagged inspections ~20× more
 effective than random selection; >30% of officer selections
 system-driven. Peer-reviewed (Jambeiro Filho / RFB). Primary.
 <!-- bib: jambeiro2019_sisam -->

[^ch05-4]: Austria Predictive Analytics Competence Centre: EUR 185 M (2023)
 incremental revenue attributed to AI-assisted detection (OECD-sourced)
 — tax, not customs; label as adjacent. Belgium VAT: ML pipeline
 narrowing ~15,000 monthly high-risk returns → ~100 confirmed fraud
 (peer-reviewed, arXiv 2106.14005) — VAT, adjacent. <!-- bib: oecd_austria_fieldfisher2025,
 belgium_vat_arxiv2021 -->

[^ch05-5]: Holistic Agent Leaderboard (HAL, arXiv 2510.11977): on a 50-task
 agent benchmark, one configuration scored 56.0% at USD 42.11 versus
 54.0% at USD 180.49 for a larger model — accuracy reported against
 cost on a Pareto frontier. <!-- bib: hal2025 -->

[^ch05-6]: McKinsey & Company, *The State of AI in 2025* (Nov 2025):
 function-level cost reductions reported in the ~10–20% range for
 software engineering and IT with revenue uplift in other functions,
 against ~39% reporting enterprise-level EBIT impact — the gap
 attributed to operating-model and workflow factors rather than model
 capability. Cross-industry enterprise data, cited here as a
 directional benchmark, not a customs-specific outcome. <!-- bib:
 mckinsey_stateofai2025 -->

[^ch05-7]: Trade-compliance GenAI adoption reported at ~40% of
 organizations in early 2026, up from ~22% a year earlier (Thomson
 Reuters trade-compliance reporting). Private-sector trader-side
 adoption data, cited as a leading indicator of task-level demand,
 not a customs-administration outcome or a value (as distinct from
 adoption) measure. <!-- bib: thomsonreuters_trade_ai2026 -->

[^ch05-8]: McKinsey, *Redefining Procurement Performance in the Era of
Agentic AI* (2026), describes linked procurement-agent workflows across
tender preparation, supplier qualification, bid analysis, clarification
routing and invoice-to-contract compliance. The examples and performance
figures are consultant-reported and adjacent to customs; this chapter
uses the closed-loop value-capture pattern, not the reported percentages,
as the transferable evidence. <!-- bib: mckinsey_procurement_agentic2026 -->
