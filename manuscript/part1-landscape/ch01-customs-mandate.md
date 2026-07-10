---
title: "The Customs Mandate in the Age of AI"
part: "I — The Landscape"
chapter: 1
status: review
version: 0.3
last-updated: 2026-07-09
---

## Two hundred parcels a minute

The Director General's morning briefing contains, as it has for years, a
graph that only goes up. E-commerce consignments through the main air hub
have multiplied again — Korea, to take the best-documented example, watched
e-commerce import shipments grow 2.85-fold in five years, from 64 to 181
million[^ch01-1];
each parcel is legally a consignment, each consignment implies a
declaration, and the headcount plan is flat (Figure 1.1). The afternoon contains a
ministerial letter about revenue targets, a media query about seizure
statistics, and a World Bank mission slide showing the country's ranking
on clearance times against two neighbors it competes with for
transshipment traffic.

![Figure 1.1 — The Arithmetic](/assets/diagrams/fig-ch01-arithmetic.svg){width=100%}

Nothing about this day is unusual, and that is the point. The customs
mandate — collect the revenue, protect the border, facilitate the trade —
has not changed. What has changed is the arithmetic around it: transaction
volumes growing far faster than any conceivable workforce, fraud
industrializing at digital speed, traders benchmarking clearance times
across jurisdictions in real time, and finance ministries treating customs
modernization as a revenue program with a technology line item.

Artificial intelligence enters this book not as an innovation agenda but
as the only credible answer to that arithmetic. This chapter establishes
why customs — perhaps more than any other government function — is
structurally suited to AI; why the current technology generation is
categorically different from the analytics wave of the 2010s; and why the
gap between leading and median administrations is now a leadership
variable rather than a budget one. Customs is this book's vantage point
and the source of its verified evidence, but the arithmetic is not
customs' alone: border-management agencies, trade-facilitation and
single-window authorities, and revenue administrations face the same
collision of rising volume, industrializing fraud, and flat headcount,
and the frameworks that follow are built to travel across all of them.

## 1.1 Why customs, specifically

Generic "AI in government" arguments understate the customs case. Four
structural features make the fit unusually tight.

**Customs is a data business that happens to have a uniform.** Every
transaction arrives as data — declarations, manifests, invoices,
certificates — and has for decades, thanks to two generations of
digitization (ASYCUDA-class systems, Single Windows, e-manifests). Few
public institutions possess longitudinal, labeled, outcome-linked data of
this density: a declaration is filed, examined or not, adjusted or not,
and the outcome is recorded. That is, almost literally, a training set.
The Korea Customs Service was reported to accumulate tens of gigabytes of
structured and unstructured data *daily* as far back as 2018[^ch01-2]; volumes
today are a multiple of that, in every administration.

**The work is document-heavy, repetitive, and judgment-topped.** The
bulk of customs labor is reading, checking, reconciling, and drafting —
exactly the work the current AI generation does well — while the
consequential decisions (assess, seize, penalize, accredit) sit on top as
a thin, human, legally accountable layer. This shape is why the Autonomy
Ladder (Chapter 2) maps so cleanly onto customs: the technology can climb
the routine work while decision authority stays precisely where law and
politics require it.

**The dual mandate creates permanent, quantifiable tension.** Facilitation
pulls toward speed; control pulls toward scrutiny; and every administration
lives on the trade-off curve between them. AI's core promise in customs is
not "efficiency" in the abstract — it is *moving the curve itself*:
inspecting less while detecting more, because selection is smarter and
document checks are continuous rather than sampled. That is a promise
finance ministries and trade ministries can agree on, which matters for
budgets.

**Errors are measurable, which makes trust buildable.** Unlike policy
domains where AI quality is contested philosophy, customs outcomes are
countable: hit rates, revenue adjustments, clearance times, override
rates. An administration can *know* whether its AI works. Chapter 12
turns this property into the pilot discipline; here it supports a simpler
claim — customs is one of the few government domains where an evidence-based
autonomy program is actually possible.

## 1.2 What changed: from the analytics wave to this one

Most administrations have lived through one AI wave already: the risk-
scoring and analytics investments of roughly 2012–2022. Some of those
programs delivered; many plateaued as models aged and data teams rotated
out. Leaders who remember that plateau are right to ask why this wave
differs. Three answers, previewed here and developed in Chapter 2:

**The unstructured barrier fell.** The analytics wave could only see
structured fields; the invoices, certificates, images, and correspondence
— where the fraud signals and the officer-hours actually live — were dark.
Generative AI reads them. For a document institution, this is not an
incremental capability; it is access to the majority of its own
information for the first time.

**The technology now does work, not just scores.** A risk engine hands an
officer a number; the officer still does everything else. The agentic
generation compiles the case file, drafts the query, reconciles the
documents — it removes work rather than annotating it. That changes the
economics from "decision support" to "capacity," which is the difference
between a tool budget and a transformation budget.

**The deployment problem became solvable — and political.** In the
analytics wave, the frontier lived in commercial clouds few customs
administrations could lawfully use. Today, capable open-weight models run
on-premises, and sovereign cloud regions are spreading through exactly
the regions this book prioritizes. Deployment is now a genuine choice
(Chapter 3) — which also means "we could not deploy it lawfully" has
expired as a reason to wait.

## 1.3 The divide, honestly stated

International surveys — including the WCO's 2025 report on AI/ML adoption
— show a frontier of impressive deployments and a long tail of
administrations still assembling basics: data quality, connectivity,
skills.[^ch01-3] The divide is
real, but this book rejects the fatalism that usually accompanies it, for
a reason visible across the author's own delivery work: **the current
technology generation lowers the entry rung.** Document intelligence and
grounded assistants (Chapter 3) require modest infrastructure, tolerate
imperfect legacy data far better than the analytics wave did, and produce
value in months.

The record, though, deserves honest reading — this book's evidence
standard begins here. The verifiable, quantified AI frontier today runs
through East Asia and the Americas: Korea's analysis-time collapse, China's
image-analysis detections at national scale, Brazil's SISAM steering
inspections since 2014.[^ch01-4] The headline modernization numbers from this
book's home region are real and primary-sourced — Saudi Arabia clearing
80% of declarations in under 48 hours, Egypt halving cargo release times —
but they were earned by single windows and process re-engineering, **not
by AI**, and Chapter 15 refuses to launder one into the other.[^ch01-5] Read
correctly, this is not a deflating finding; it is the opportunity stated
plainly. The region has already proven it can execute national-scale
digital modernization — precisely the delivery discipline AI adoption
requires — while its verified AI value record remains to be written. The
administrations this book is written for are the ones positioned to write
it.

What actually separates administrations today is not budget but four
leadership variables: a named executive owner; a sequenced portfolio
(Chapter 4) instead of scattered pilots; a sovereignty posture decided
early (Chapter 3); and a governance apparatus proportionate to autonomy
(Part III). Every one of those is free. All of them are rare.

The wider enterprise data confirms that the constraint is
organizational, not technological, and that customs is not behind some
imagined curve. In McKinsey's 2025 global survey of nearly 2,000
organizations, the overwhelming majority reported using AI — yet fewer
than one in five had scaled AI agents in even a single business
function, and only about a third had begun scaling AI across the
enterprise at all; the analysts' own phrase for the majority state is
the transition "from pilots to scaled impact" still unfinished.[^ch01-6]
The pattern that separated the high performers was not superior models
but exactly the leadership variables above: senior-leader ownership,
redesigned workflows, and — tellingly for Part III of this book — far
more mature human oversight, with high performers roughly three times as
likely to have defined human-in-the-loop validation. Gartner, from the
other direction, projects that more than 40% of agentic AI projects will
be cancelled by the end of 2027 — citing not model failure but
escalating cost, unclear value, and inadequate risk controls — and notes
that of the thousands of vendors marketing "agentic" products, only a
small fraction offer genuine capability, a practice it labels *agent
washing*.[^ch01-7] An administration that reads these numbers correctly
draws the opposite of discouragement from them: the failure modes are
known, they are governable, and they are precisely what the rest of this
book is about. Figure 1.2 sets the pattern out as a single funnel — the
gap between what is deployed, what is piloted, and what reaches
production is the reality this book routes against, and it recurs from
the sector's own numbers (Chapters 3 and 6) to the enterprise surveys
above.

![Figure 1.2 — The Adoption Funnel](/assets/diagrams/fig-ch01-adoption-funnel.svg){width=100%}

## 1.4 The stance of this book

Three commitments run through every chapter that follows, and they are
worth stating before the first framework appears.

![The Stance](/assets/diagrams/fig-three-pillars.svg){width=100%}

**Ambitious on value.** The opportunity is not 10% efficiency; it is
restructuring the cost of control — continuous document verification,
audit coverage limited by risk rather than headcount, service levels that
attract transshipment traffic. Leaders should size the ambition
accordingly, and Chapter 5 gives the arithmetic.

**Conservative on autonomy.** Decisions transfer one rung at a time, on
evidence, within signed mandates — and accountability never transfers at
all. This conservatism is not a brake on the ambition; it is what makes
the ambition survivable in a government institution.

**Uncompromising on sovereignty and trust.** Trade data stays under
national jurisdiction; consumer subscriptions and unvetted APIs are
excluded territory; every system answers to the administration's own
oversight before anyone else's. These are entry conditions, not
aspirations.

An administration that holds all three simultaneously will find the rest
of this book to be engineering. An administration that drops any one of
them will find the rest of this book to be a description of its future
incident report.

## 1.6 The operating question behind the technology question

For a Director General, the practical question is not whether AI will
become capable enough. It already is capable enough to change the
economics of selected information-heavy tasks. The question is whether
the administration can convert that capability into a more resilient
operating model without delegating public authority by accident.

That means treating the border as a portfolio of queues, decisions and
exceptions rather than a catalogue of systems. Which queues grow faster
than staffing? Which decisions are delayed because evidence is scattered
across documents and agencies? Which exceptions consume senior judgment
but could arrive as a grounded, complete case file? Which controls need
more attention, not less, when throughput rises? These are business
questions. The model, hosting pattern and vendor are answers chosen
afterward.

The WCO's 2025 report describes the common ML-era pressure points—risk
management, trade facilitation, real-time processing, intelligence,
capacity and data quality. Agentic systems change the unit of redesign:
not just a prediction, but the handoff between a signal, a case,
evidence, a human decision and a recorded action.[^ch01-8] This book is
therefore not an argument to automate customs. It is an argument to
redesign selected operating loops so that scarce officers spend more
time on judgment and less time assembling the evidence needed to use it.

## 1.7 The executive baseline: make the pressure visible

Every programme should begin with a one-page baseline that makes the
pressure legible without claiming a technology solution. Show five
trends for the last three to five years: transaction and parcel volumes;
average and upper-percentile clearance time; exception and rework rate;
inspection or post-clearance capacity; and funded operational headcount.
Then add the demand signal that matters locally—e-commerce, new trade
lanes, sanctions exposure, trusted-trader growth, or a policy commitment
to faster release. The resulting picture tells leadership where the
system is bending before it breaks.

This baseline is more than a strategy chart. It is the denominator for
every later claim. If a document-to-case workflow says it saved time,
compare it with the appropriate baseline queue and service clock. If a
risk workflow says it found more, compare it with inspection capacity
and confirmed outcome, not a count of alerts. If a vendor promises
elastic capacity, ask which peak period it will absorb and what human
fallback remains when the service is unavailable. Numbers prevent the
programme from substituting a generic productivity story for an
administration's actual operating constraint.

The baseline also establishes a political discipline: service
facilitation, revenue protection, safety and fairness need not compete
for a single headline metric. State the trade-off in advance. A faster
low-risk lane is a success only if it does not hide a rising error or
equity problem; a more productive targeting queue is a success only if
the downstream inspection resource can act. This is the business context
in which an autonomy decision becomes meaningful.

## 1.8 The portfolio charter: decide before the vendor arrives

The executive owner should issue a short portfolio charter before
market engagement. It names the public outcomes that matter over the
next planning cycle; the two or three operating queues eligible for
investment; the excluded territory; the deployment and sovereignty
principles; the current autonomy ceiling; the evidence standard for
claims; and the governance route by which a task can earn more scope.
It also names the first decision to be made—select a bounded pilot,
fund a foundation, issue an RFP, or pause a high-risk idea.

This document is not a technology strategy. Its purpose is to prevent
the technology market from setting the programme's agenda by default.
Without a charter, every compelling demonstration becomes an apparent
priority, benefits are counted in incompatible ways, and vendors are
asked to solve an undefined administrative problem. With one, a vendor
can be invited to propose an operating model for a named task and
evaluated against evidence rather than presentation skill.

Review the charter annually and after a material service shock, legal
change or portfolio incident. Keep it short enough that a port director,
privacy lead and finance director can all recognise their role in it.
The strongest signal it can send is also the simplest: the administration
will move decisively on value, but it will decide the boundary of public
authority before it decides the model.

## Decision Toolkit — Chapter 1

**The positioning snapshot.** Before any strategy work, answer five
questions in writing, one page total:

1. **Volume arithmetic:** transactions per year now vs. five years ago
 vs. headcount trend — what is the gap AI must close?
2. **Data estate:** what share of our documents is machine-readable
 today? (Most leaders discover they do not know; that discovery is the
 deliverable.)
3. **Last wave audit:** what did the analytics-era investments deliver,
 and what plateaued — and why?
4. **Sovereignty options:** does an accredited in-country cloud region
 exist for us? What does data protection law permit?
5. **Ownership:** who is the named executive owner of AI adoption — a
 person, not a committee?

The snapshot feeds the readiness assessment (Chapter 6) and keeps the
first strategy discussion anchored in the administration's actual
arithmetic rather than the vendor's slides.

## Key Takeaways

- The customs mandate is unchanged; the arithmetic around it — volumes,
 fraud industrialization, competitive clearance benchmarking — is not.
 AI is the only credible response to that arithmetic, which makes
 adoption a leadership question, not an innovation hobby.
- Customs is structurally suited to AI: dense outcome-linked data,
 document-heavy repetitive work topped by a thin layer of accountable
 human decisions, and measurable errors that make trust buildable.
- This wave differs from the 2010s analytics wave in three ways:
 unstructured documents became readable, the technology removes work
 rather than annotating it, and sovereign deployment became genuinely
 possible.
- The digital divide is real but the entry rung has dropped; the
 differentiators now are ownership, sequencing, sovereignty posture, and
 governance — all leadership variables, all free, all rare.
- The book's stance: ambitious on value, conservative on autonomy,
 uncompromising on sovereignty and trust. Hold all three or expect the
 incident report.

---

## Endnotes

[^ch01-1]: Korea Customs Service, reported in WCO News 108 (Issue 3, 2025):
 e-commerce import shipments grew from 64 million to 181 million over
 five years. Administration-stated; technology and figures. <!-- bib: wconews108_korea -->

[^ch01-2]: WCO News 86 (June 2018), on KCS clearance analytics for express
 cargo and postal items: ~45 GB structured + ~30 GB unstructured data
 accumulated daily. <!-- bib: wconews86_kcs2018 -->

[^ch01-3]: WCO Smart Customs Project, *Detailed Report on the Adoption of
 Artificial Intelligence and Machine Learning in Customs* (March 2025)
 — digital-divide framing per the report's executive summary.
 <!-- bib: wco_scp_report2025 -->

[^ch01-4]: Korea: high-risk cargo analysis time reduced from ~1 hour to under
 1 minute (≈98%), estimated annual savings KRW 125.7 bn (~USD 92 M,
 2025), administration-stated (WCO News 108). China GACC: >20,000
 smuggling attempts detected via AI image-analysis alarms since 2022,
 recognition accuracy >95%, administration-stated (WCO News 104).
 Brazil RFB: SISAM-flagged inspections ~20× more effective than random
 selection; >30% of officer selections system-driven (peer-reviewed,
 Jambeiro Filho). All primary-. <!-- bib: wconews108_korea,
 wconews104_china, jambeiro2019_sisam -->

[^ch01-5]: Saudi ZATCA: 80% of declarations cleared <48 h, supporting documents
 reduced 12→2 (WCO News 103) — attributable to the FASAH single window
 and process re-engineering, not AI/ML. Egypt: cargo release time 16→8
 days per Time Release Studies 2021→2024 — attributable to the NAFEZA
 single window and Advance Cargo Information, ML not confirmed.
 <!-- bib: wconews103_zatca, egypt_trs2024 -->

[^ch01-6]: McKinsey & Company, *The State of AI in 2025: Agents,
 Innovation, and Transformation* (Nov 2025), QuantumBlack — global
 survey of 1,993 respondents across ~105 countries: near-universal
 AI use but ~23% scaling agentic AI in at least one function, and
 roughly two-thirds not yet scaling AI enterprise-wide; high
 performers markedly more likely to show senior-leader ownership,
 workflow redesign, and defined human-in-the-loop validation
 (65% vs 23%, ≈2.8×; distinct from the separate transformational-
 change figure). <!-- bib: mckinsey_stateofai2025 -->

[^ch01-7]: Gartner press release, *Over 40% of Agentic AI Projects Will
 Be Canceled by End of 2027* (25 Jun 2025) — cancellation drivers:
 escalating costs, unclear business value, inadequate risk controls;
 "agent washing" and the estimate that only ~130 of thousands of
 self-described agentic vendors offer genuine capability; and the
 forecast that ~15% of day-to-day work decisions will be made
 autonomously by 2028 (from ~0% in 2024). <!-- bib:
 gartner_agentic_cancel2027 -->

[^ch01-8]: WCO Smart Customs Project, *Detailed Report on the Adoption of
AI and ML in Customs* (2025), identifies operational efficiency, trade
facilitation, risk management, intelligence, real-time processing,
capacity building and data management as the main adoption domains. The
workflow-loop framing is this book's agentic extension of that baseline.
<!-- bib: wco_scp_report2025 -->
