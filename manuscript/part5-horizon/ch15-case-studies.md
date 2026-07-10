---
title: "Case Studies: Business Value from the Field"
part: "V — The Horizon"
chapter: 15
status: review
version: 0.3
last-updated: 2026-07-09
---

## The conference slide and the field

Every customs technology conference has the slide: a flag, a percentage,
a rising arrow. This chapter exists because that slide is where most
administrations' case-study knowledge begins and ends — and because the
research behind this book found, systematically, that the slides divide
into three very different populations: verified AI outcomes,
digitalization gains wearing an AI costume, and launch-week claims that
never grew evidence. The cases below are drawn exclusively from the
first population, read through this book's frameworks, and presented
with the discipline the whole book has practiced: every figure carries
who stated it, and every lesson is one the source actually supports.

## 15.1 The reading protocol

Each case is examined in six fixed passes: **context** (the problem and
its arithmetic) · **solution, with the technology precisely
identified** (rules, ML, computer vision, GenAI, agentic — never just
"AI") · **deployment model** · **measured value, with attribution**
(who stated the figure; primary or secondary) · **stated lessons** (the
administration's own, not ours) · and a closing pass this book adds:
**what the frameworks would have flagged** — the case re-read through
the Autonomy Ladder, the Maturity Ladder, and Part III's governance
lens, to extract what the source itself could not say.

Figure 15.1 sets all seven administrations side by side on the
dimensions that matter for transfer — technology precisely identified,
deployment model, measured value, and evidence grade — so the shape of
the whole record is visible before the individual cases are read. Read
the evidence-grade tags first: verified customs outcomes (Korea, China),
peer-reviewed (Brazil), qualitative primary sources without a headline
metric (India, Netherlands, Uruguay), and a single anecdote shown for
governance transparency and expressly not as a metric (US CBP).

![Figure 15.1 — Case Studies at a Glance](/assets/diagrams/fig-ch15-case-comparison.svg){width=100%}

## 15.2 Korea Customs Service — the compounding decade

**Context.** KCS entered the 2020s facing the arithmetic of Chapter 1
in its purest form: e-commerce import shipments grew 2.85-fold in five
years — from 64 to 181 million — against a flat workforce, on top of
data volumes (roughly 45 GB structured and 30 GB unstructured daily as
far back as 2018) that made outsourced analytics implausible.[^ch15-1]

**Solution, precisely identified.** Not one system but a compounding
portfolio: a 2017 big-data roadmap and an organization-wide platform;
eleven AI models in production spanning risk selectivity, X-ray image
analysis, early warning, HS-code prediction, and passenger targeting;
an ML/deep-learning fusion that presents X-ray imagery and manifest
data to the analyst in a single display at postal and express hubs;
and — arriving last, in the mid-2020s — a generative layer ("AI
Innovation in Customs") that lets any officer query import data in
natural language.[^ch15-2]

**Deployment model.** Administration-run and national, built on a
deliberately in-house capability: the hub-and-spoke workforce design of
Chapter 14 (a central analytics team; officer-analysts paired with
domain experts in the units; a six-month training pipeline aimed at 300
experts, roughly 7% of the workforce), with private-sector IT refining
tools rather than owning them.[^ch15-3]

**Measured value, with attribution.** High-risk cargo analysis time
fell from roughly one hour to under one minute — a ~98% reduction —
while the 2.85× volume surge was absorbed without matching headcount;
the administration estimates annual savings of KRW 125.7 billion
(~USD 92 million, 2025). Figures are administration-stated via WCO News
and APEC; primary confidence, technology precisely
identified.[^ch15-2]

**Stated lessons.** KCS's own, compressed: data access is a basic
requirement, but "data is a means, not an end"; analytics teams must
understand operational staff; ICT–customs teamwork runs on standing
feedback loops; top-management backing is essential.[^ch15-2]

**What the frameworks would have flagged.** Read against this book,
Korea is less a success story than a *sequencing proof*. The Maturity
Ladder was climbed in order — a decade of Rung-1/Rung-2 data and
platform work before the generative layer, which is precisely why the
top rung held (Chapter 3's argument, executed before it was written).
The workforce model anticipated Chapter 14's blueprint. And the
program's public record consists of outcomes, not launches — the
communications discipline of Chapter 12, sustained for years. The one
question the sources leave open is the Chapter 9 question: the
governance apparatus behind the auto-clearance of low-risk declarations
(mandates, demotion criteria, audit artifacts) is not publicly
documented — which is an observation about publication, not a criticism
of the program, and a gap this book's Part III fills generically.

**Transfer boundary.** What cannot be copied quickly matters as much as
what can. Korea's public record reflects a decade of cumulative
investment, national-scale access to operational data, a stable specialist
cadre, research partnerships, and institutional continuity. An
administration can copy the sequencing, bounded progression, and insistence
on internal capability; it cannot copy the elapsed time or assume the same
outcome. The transfer sheet in §15.13 is mandatory before any Korea number
enters a local business case.

## 15.3 China GACC — detection at national scale

**Context.** The problem was volume against a fixed ceiling: a national
NII estate producing image streams no analyst corps could watch, and a
false-alarm rate that made naive automation counterproductive.

**Solution, precisely identified.** An AI Image Analysis System across
hundreds of NII devices — deep-neural-network image classification
organized into Prohibition and Recognition algorithm classes, with an
"autonomous selection of algorithms" step choosing the model per
stream — inside a broader stack (knowledge graph, intelligent control
model, document examination) fed by a 261-billion-record data lake
spanning 678 customs houses.[^ch15-4]

**Deployment model.** Administration-run, national, and deliberately
mounted on the *existing* NII estate rather than replacing it.

**Measured value, with attribution.** More than 20,000 smuggling
attempts detected via AI-generated alarms since 2022 — the
administration's phrasing matters: *without increasing human
resources* — at deployed recognition accuracy above 95%; an unmanned
terminal analyzes an image in roughly five seconds.[^ch15-4]
Administration-stated (WCO), primary confidence.

**Stated lessons.** Mature algorithms plus autonomous algorithm
selection cut false-alarm rates; scale on the estate you have.

**What the frameworks would have flagged.** Two things. First, the
attribution discipline the sources themselves require: China's famous
scanner-throughput gains (a vehicle inspected in one minute instead of
thirty) are *hardware*, and the case is only honest when the AI figures
above are kept separate from them — this book's Chapter 5 rule,
enforced at the source. Second, the realism anchor already deployed in
Chapter 6: the same administration reports 62 smart models with 2 in
full production — national scale and a narrow production funnel are
not a contradiction; they are what the frontier actually looks like.

## 15.4 Brazil SISAM — explainability before it was fashionable

**Context.** The oldest problem in the book — which declarations to
inspect — at national scale, around the clock, since the mid-2010s.

**Solution, precisely identified.** SISAM: Bayesian networks
(supervised and unsupervised) estimating some thirty distinct error
types and producing a **natural-language explanation for every flag**
— explainable by design, in production since August 2014 — flanked by
a rules/expert-knowledge integrator and a real-time alert layer, with
a stated plan to add deep learning and LLMs for product
descriptions.[^ch15-5]

**Deployment model.** Administration-run, national.

**Measured value, with attribution.** Inspecting SISAM-flagged items is
"20 times more effective than random selections," and more than 30% of
officer selections nationwide follow the system's suggestions — both
figures peer-reviewed, the strongest evidence class in this
book.[^ch15-5]

**Stated lessons.** Explainability matters for officer trust; combine
ML selection with a rules layer and real-time alerting.

**What the frameworks would have flagged.** SISAM is Chapter 9's
explainability standard running a decade before Chapter 9 — the
explanation produced at action time, for the officer, as a deliberate
trust mechanism — and Chapter 2's "eras stack" thesis in production:
rules, ML, and (soon) language models composed, not substituted. It is
also a cautionary exhibit about fame: a 2026 secondary outlet credits
SISAM with figures no primary evaluation supports; the program's real,
peer-reviewed numbers need no decoration, and Box 15.A explains why the
decorated version circulates anyway.

## 15.5 Indian Customs — the data-foundation route

**Context.** Two problems that look unrelated and are not: analyzing
X-ray imagery at scale, and the fact that supplier names arrive as
free text — unusable for the cross-importer comparison that
undervaluation detection needs.

**Solution, precisely identified.** AI/ML X-ray analytics for
contraband, concealment, and misdeclaration; and — the quieter half —
**unsupervised ML codifying free-text supplier entities** into
structured identities, unlocking cross-importer undervaluation
comparison and network analytics, all inside the Integrated Risk
Management System run by the National Customs Targeting
Centre.[^ch15-6]

**Deployment model.** Administration-run, national.

**Measured value, with attribution.** KPIs report enhanced detection
accuracy, a higher hit rate, and reduced dwell time —
administration-stated, qualitative, with **no single headline
percentage published**. This book treats that as a feature of the
case, not a defect: the administration declined to manufacture a
number, which is more than several louder programs can say.[^ch15-6]

**Stated lessons.** The administration's own formulation deserves
quoting into every data strategy: *codified machine-readable data is
the foundation of automated targeting* — free text must be structured
first.

**What the frameworks would have flagged.** This is Chapter 11 §11.1
embodied at national scale — the document work enabled the targeting
value — and the cleanest public illustration of the Maturity Ladder's
dependency logic: the unglamorous Rung-1 codification is what made the
analytics rung possible.

## 15.6 Netherlands — computer vision and the cooperative route

**Context.** Pills concealed in envelopes and parcels, at e-commerce
volume, visible only in X-ray imagery.

**Solution, precisely identified.** A deliberately **two-model**
computer-vision design: a detection model that draws the bounding box
on the analyst's screen, and a separate classification model that
feeds a probability score to the risk engine — developed within the
EU's PROFILE shared risk platform (with Belgium, Sweden, Norway, and
Estonia contributing to cross-administration image annotation), plus a
vendor-built web-crawler cross-checking e-commerce declarations
against online information.[^ch15-7]

**Deployment model.** Administration-run; EU-funded R&D; vendor
collaboration on the crawler.

**Measured value, with attribution.** The primary sources publish **no
headline percentage** — the documented value is technology maturity
feeding a human-reviewed risk engine. A secondary academic source
attached a "~95% of declarations without human involvement" figure to
this program; it is not traceable to any primary evaluation and this
book declines it.[^ch15-7]

**Stated lessons.** Separate detection from classification; annotate
images cooperatively across administrations; keep humans reviewing
model outputs.

**What the frameworks would have flagged.** The two-model separation is
a design lesson with governance teeth — the component that *shows* the
analyst and the component that *scores* the risk are different objects
with different oversight needs. And the cooperative annotation is a
small preview of Chapter 16's ecosystem argument: administrations that
pool the expensive substrate (labeled imagery) climb faster than
administrations that guard it.

## 15.7 Uruguay LUCIA — the small-administration playbook

**Context.** A small administration with the universal problem —
pointing scarce NII capacity at the right cargo — and no national-scale
data machine to throw at it.

**Solution, precisely identified.** The LUCIA customs management
system's risk model selects cargo for NII control; the scanner
software carries AI tools supporting the analysts reading radioscopic
images; and the design's real signature is the **closed loop** —
selection flows to inspection, inspection results flow back into the
risk model.[^ch15-8]

**Deployment model.** Administration-run, vendor-developed — and then
**donated**: the risk module was given to Colombia's DIAN and to
Uruguay's own single window in 2023.

**Measured value, with attribution.** No headline percentage; the
documented value is a re-engineered NII selection process aligned to
WCO procurement guidance, with the feedback loop closed —
primary-sourced via the WCO.[^ch15-8]

**Stated lessons.** Close the loop between risk selection and
inspection results; reuse modules across agencies.

**What the frameworks would have flagged.** Uruguay is Chapter 11's
"the loop is the asset" implemented by an administration a fraction of
Korea's size — evidence for a claim this book needs to be true: **the
entry ticket is discipline, not scale.** The donation model adds an
economics footnote Chapter 5 would endorse: a module built once and
reused across agencies is the second-agent test, passed at
international level.

## 15.8 United States CBP — a compact case, for two reasons

Presented compactly, and for two specific angles rather than its
numbers. CBP runs ML risk scoring inside the Automated Targeting
System, machine-vision object identification over streaming imagery,
and computer-assisted detection — technology precisely identified —
and shares ATS globally with partner administrations, an early
production instance of the cross-border risk plumbing Chapter 16
anticipates. Just as instructive: DHS *itself* documents the system's
risks — false positives and negatives, and algorithmic bias from
training on historical seizures — a governance transparency posture
this book would like to see become the norm. The widely quoted number
(a pattern flagged in 1.4 seconds; ~75 kg of narcotics found) is a
single testimony anecdote, presented here as an illustration of
capability and expressly **not** as a program metric.[^ch15-9]

## 15.9 What the adjacent domains have already proven

Customs is not the first institution asked to find rare wrongdoing in a
vast, hostile stream of transactions under regulatory scrutiny. Banking
compliance, trade finance, and logistics have run that problem at
enormous scale for a decade, and their evidence — read with the same
attribution discipline applied to the customs cases, and labeled as
adjacent throughout — is directly transferable, because the underlying
task is the same shape: anomaly detection in a transaction flow, where
the cost of a false positive is wasted skilled labor and the cost of a
false negative is a missed threat.

**Financial-crime detection is customs targeting under a different
name.** The anti-money-laundering problem maps onto risk selectivity
almost feature for feature: enormous transaction volumes, adversaries
who actively study and evade the rules, a legacy of brittle
rules-and-thresholds systems, and a punishing false-positive burden.
McKinsey's work in the sector reports that rule-based transaction
monitoring can generate false-positive rates as high as 90% — the AML
equivalent of Chapter 12's "a passing pilot that floods officers with
noise has failed" — and that replacing those rules with machine
learning, particularly network analytics that detect linked entities
and laundering typologies rather than isolated transactions, can improve
the identification of genuinely suspicious activity by up to
40%.[^ch15-12] The pattern that customs should read most closely is the
network-analytics one: the highest-value fraud in trade, as in finance,
hides in relationships between entities — the cross-importer
undervaluation ring, the circular supply chain — exactly what India's
supplier-codification work (§15.5) was built to expose, and exactly what
isolated per-declaration rules miss. The sector has also learned
Chapter 9's lesson the hard way: explainability is not optional where a
determination has legal consequence and a regulator will ask how the
model decided.[^ch15-12]

> **ADJACENT EVIDENCE — HYPOTHESIS, NOT FORECAST.** These figures describe
> financial crime, not customs. Borrow the network method and the false-
> positive failure mode; replace every percentage with a local baseline
> and representative customs pilot.

**IT service operations have already run the Operator-to-Supervisor
shift — under governed autonomy.** The workforce transition this book
describes in the abstract (Chapter 2's ladder, Chapter 14's staffing) is
running in production in enterprise service desks. In McKinsey's 2026
analysis of agentic AI infrastructure, service-desk agents operating
under "governed autonomy" with "clear accountability" delivered on the
order of 25–45% cost savings — and the framing is the load-bearing
detail: the autonomy is *governed*, and accountability is explicitly
retained rather than diffused into the software.[^ch15-13] That is the
exact sentence this book has been making in customs terms: the human
moves from doing the work to supervising the exceptions, and
accountability stays with the human by design. The adjacent operational
evidence more broadly — distribution and supply-chain deployments report
material cost and productivity gains, consistently gated by data quality
and workflow redesign rather than model capability — tells the customs
leader the same thing the enterprise surveys did in Chapter 1: the value
is real, it is function-level first, and it is unlocked by organization
rather than by algorithm.[^ch15-13]

The caution travels with the evidence. These are not customs numbers,
and a bank's transaction is not a declaration; the domains differ in
data, in law, and in the shape of the adversary. But the transferable
asset is not the percentage — it is the *method* and the *failure
mode*, both of which customs inherits wholesale: build for networks not
isolated transactions, insist on explanations where decisions carry
legal weight, expect the false-positive burden to be the real
operational cost, and redesign the human's role around exceptions. The
adjacent domains paid for those lessons already. Customs can read the
receipt.

## 15.10 Practice-reported evidence: useful, but not interchangeable

The public record also contains a third kind of evidence: practical
case reporting by consultancies and delivery firms. It is neither a
government publication nor an independent evaluation. Dismissing it
would leave leaders blind to how regulated organizations are actually
redesigning work; treating it as independently verified would violate
this book's own rule. The right category is **practice-reported**:
named source, transparent author, figures attributed to that author,
and no transfer of the number across domains without a local pilot.

**A customs precedent, openly reported but client-anonymized.** McKinsey
describes a G-20 customs administration that rebuilt post-clearance-audit
targeting with supervised and unsupervised models. The consultancy reports
that detected violations moved from 30% to 60% and workforce productivity
rose by 75%.[^ch15-14] This is a useful operating pattern — a weak
baseline, a clearly defined audit outcome, and two complementary models
— but it is not a country case study. The administration is unnamed and
the figures are consultant-reported, so the case belongs in the planning
conversation, not in a ministry forecast.

> **PRACTICE-REPORTED.** The source is public and the workflow is useful;
> the client is unnamed and the outcome is consultant-reported. It is not
> independently verified customs evidence and must not be converted into a
> forecast without a local baseline and pilot.

**A named regulated-compliance analogue.** Blackstone's Legal &
Compliance function offers a closer analogue to agentic document work
than a generic chatbot success story. McKinsey reports an AI-enabled
first-pass review of roughly 25,000 investor-facing documents a year,
with relevant precedent surfaced for reviewers, 30%+ productivity
improvement, and an expected USD 5 million annual run-rate saving by
2027.[^ch15-15] The transferable lesson is not the dollar figure. It is
the operating design: map the decision lifecycle first, decide where
expert review is indispensable, then use AI to prepare and route routine
work. That is an L1/L2 customs pattern, not evidence for autonomous
enforcement.

The wider public-sector practitioner record points in the same
direction. BCG's 2026 government-assurance work argues for reusable
artifacts, risk triage, named accountability, and controls embedded in
delivery — precisely the shift from policy to operating discipline that
Parts III and IV of this book make concrete.[^ch15-16] It adds no
customs number, and should not be quoted as one. It strengthens the
claim that the artifacts in this book are how serious public programs
are increasingly being run.

---

> ### Box 15.A — The cautionary museum
>
> The research behind this book maintains a register of claims that
> could not be verified — kept not to embarrass anyone, but because the
> patterns repeat and a leader should recognize the exhibit labels:
>
> - **The minister-hedged number.** A fraud-detection accuracy of "90%"
> announced at launch — by a speaker who added, in the same breath,
> is not an outcome; a hedge is not a measurement.
> - **The vague-technology seizure total.** Hundreds of kilograms
> seized "using AI and big data" — real seizures, unverifiable
> attribution: the technology is never precisely identified, and
> seizures have many parents.
> - **The untraceable percentage.** "AI reduces processing time up to
> 70%" circulating through secondary sources with no primary
> evaluation behind it — a figure that improves with each retelling
> because nothing anchors it.
> - **The borrowed miracle.** Clearance-time transformations (80% under
> 48 hours; release times halved) that are real, primary-sourced —
> and attributable to single windows and process re-engineering, not
> to AI. The gain is genuine; the attribution is laundering.
> - **The pilot that never scaled.** A polished proof of concept passes on
> curated cases, then waits indefinitely for a production data route,
> accountable owner, security approval, operating budget, or staffed
> exception queue. Technical success without a conversion path is not a
> delayed deployment; it is evidence that the programme tested the model
> before it tested the institution.
>
> The exhibit-label test, applicable to any conference slide: *Who
> stated the figure? Is the technology precisely identified? Is there a
> primary evaluation? Would the number survive the attribution rule of
> Chapter 5?* Four questions, thirty seconds, most slides.[^ch15-10]

> ### Box 15.B — Adjacent evidence, honestly borrowed
>
> Where customs-specific revenue figures are scarce, revenue-agency
> neighbors offer anchors — usable if, and only if, they travel with
> their labels. Austria's tax administration attributes EUR 185 million
> (2023) of incremental revenue to AI-assisted detection
> (OECD-sourced). Belgium's VAT analytics narrow ~15,000 monthly
> high-risk returns to ~100 confirmed fraud cases through an ML
> pipeline (peer-reviewed). Both are tax, not customs; both are
> disciplined precedents for what detection-driven revenue value looks
> like when it is actually measured. Borrow the method, label the
> domain.[^ch15-11]

> **Grey-literature rule.** Consultant or vendor case reporting may be
> used when the source is public, named, and specific about the workflow
> and metric. It is labelled **practice-reported**, never upgraded to
> independently verified, and never used as a customs forecast without a
> local baseline and pilot.

## 15.11 What the cases say about agents—and what they do not

The honest reading is uncomfortable and useful: the strongest customs
cases are not yet autonomous agents. They are mature ML, computer vision,
risk models, data platforms and—in Korea's case—a natural-language layer
on top of a decade of operational AI. This is not an evidence failure.
It is the evidence base a prudent agentic programme should want. The
cases prove that customs value is real when technology is embedded in a
measured workflow, that data and operating continuity compound over
years, and that claims can be distinguished from launches.

They do **not** prove that a border should delegate consequential
decisions to an L4 agent. For that, the book requires a different proof:
a bounded task, an operational assurance record, a pilot ledger, trajectory observability,
a named mandate and a right to demote. The absence of a headline
"autonomous customs agent" case is therefore not a reason to fill the
gap with vendor narrative. It is the reason the Autonomy Ladder is
conservative by design.

For executives this turns the case-study chapter into a portfolio tool.
Borrow Korea's compounding-capability lesson, Brazil's explainability,
India's data-foundation sequence, Uruguay's focused-loop discipline and
the grey-literature workflow patterns—but borrow none of their numbers
without their labels. Build the first agent on the same evidence
discipline that made the ML cases credible, then publish your own
outcome only after it has survived the gates.[^ch15-17]

## 15.12 A practical evidence ladder for the next case

The question for a Director General is not which country to copy. It is
which evidence is strong enough to change a local decision. Use the
following ladder when a new case reaches the programme office.

| Evidence level | What it can support | What it cannot support | Executive response |
|---|---|---|---|
| **Primary, operating metric** | A hypothesis about a comparable workflow, subject to local baseline | A guaranteed local ROI or autonomy level | Ask for the operating definition, period, denominator and independent owner of the number. |
| **Primary, qualitative** | A capability or implementation lesson | A quantified benefit | Borrow the sequence, then set a local measurement plan. |
| **Peer-reviewed / official synthesis** | A pattern across cases and a control baseline | Proof that a named implementation will work | Use it to set policy or evaluation questions. |
| **Practice-reported grey literature** | A workflow pattern, commercial lesson or directional benchmark | A public-sector forecast or fact about customs performance | Label it, request the underlying conditions and test locally. |
| **Launch claim or anecdote** | A market lead worth investigating | A business-case number | Do not put it in the investment case. |

The same case can move up or down the ladder as evidence changes. A
vendor's named public customer with a reproducible metric is stronger
than an anonymous benchmark, but it still may have different volume,
law, data and workforce conditions. Conversely, a local shadow-mode
pilot with a modest sample may be more decision-useful than a large
foreign case because it tests the actual mandate. The purpose of the
ladder is not scepticism for its own sake. It protects scarce attention
from being spent on claims that cannot affect a decision.

For agentic AI, add one final test: does the evidence describe a system
that merely generated or predicted, or one that used tools and changed a
workflow under a stated authority boundary? Most current customs cases
belong to the first category. That is valuable evidence for the
substrate, but not a shortcut around the safety, security and operating
tests required for the second. The distinction keeps the book ambitious
about value and honest about the frontier.

## 15.13 Turn an external case into a local hypothesis

Do not ask a visiting vendor or foreign administration, "can we copy
this?" Ask for a transfer sheet. Record the source workflow, its stated
volume and baseline, operating owner, data dependencies, technology
boundary, autonomy and tool authority, human-review design, published
outcome, evidence grade and the conditions the source itself identifies
as critical. Then place the local equivalents beside them: our queue,
documents, legal basis, downstream capacity, skills, hosting constraint
and service goal.

The gaps become the local hypothesis. A Korea-style document and risk
workflow may suggest that a target queue merits a baseline and Rung-1
extraction test; it does not establish that the same value will appear
in a smaller administration with a different inspection capacity. A
practice-reported procurement agent may suggest a closed-loop design;
it does not prove that a customs agent should send external requests.
The transfer sheet protects the useful part of borrowing—the question it
teaches—while discarding the false part—the imported result.

Give the hypothesis an expiry. Within a defined pilot window, either
produce local evidence that narrows the decision, alter the scope based
on a discovered constraint, or stop. This makes international learning
fast rather than deferential. It also improves the sector evidence base:
when administrations publish their own results with task, baseline,
control design and limitations, the next reader can make a better
comparison than the previous one.

## Decision Toolkit — Chapter 15

**The case-reading checklist** (for any case, including these): the
four exhibit-label questions (Box 15.A) · the six-pass protocol (15.1)
· evidence grade (primary / peer-reviewed / qualitative / anecdote /
practice-reported)
· one addition for internal use — *what would our readiness profile
(Appendix A) have to look like before this case is transferable to
us?* A case is a direction, never a template; the transfer question is
where its real value lives.

## Key Takeaways

- Verified customs AI value exists and is substantial — but it lives in
 a small set of programs that measured for years before they spoke;
 the loudest number in the field (Korea's ~USD 92M) sits on a decade
 of sequenced foundation work.
- The strongest cases are sequencing proofs: Maturity Ladder in order,
 workforce built deliberately, outcomes published instead of launches.
- Three claim populations circulate at every conference: verified AI
 outcomes, digitalization wearing an AI costume, and launch-week
 numbers. The exhibit-label test separates them in thirty seconds.
- Adjacent (tax/VAT) evidence is usable with its labels on; borrowed
 miracles without attribution are laundering.
- Consultancy cases are operational evidence, not independent
 evaluations: cite the source and limitation with every metric.
- Adjacent domains prove the method, not customs percentages: design
 for networks, explain legal decisions, budget false positives and
 redesign the human role around exceptions.
- A case is direction, not template: transfer it through your own
 readiness profile.

---

## Endnotes

[^ch15-1]: Volume and data context: WCO News 108 (Issue 3, 2025) —
 e-commerce imports 64M → 181M over five years; WCO News 86 (Jun
 2018) — ~45 GB structured + ~30 GB unstructured daily. <!-- bib: wconews108_korea,
 wconews86_kcs2018 -->

[^ch15-2]: Solution, figures, and stated lessons: WCO News 108 (2025);
 APEC SCCP (2025); WCO News 96 (2020). Analysis time ~1 h → <1 min;
 estimated savings KRW 125.7 bn (~USD 92 M, 2025);
 administration-stated, primary confidence, technology precisely
 identified. <!-- bib:
 wconews108_korea, apec_sccp2025_korea, wconews96_kcs_bigdata -->

[^ch15-3]: Workforce model: WCO News 86 (2018) — six-month program, 300
 experts (~7% of workforce); WCO News 96 (2020) — hub-and-spoke
 pairing, vendor role limited to tool refinement. <!-- bib:
 wconews86_kcs2018, wconews96_kcs_bigdata -->

[^ch15-4]: China GACC: WCO News 104
 (Issue 2, 2024); WCO AI/ML Case Study — China (2025); World Customs
 Journal 2024 (Cao & Xia). Attribution guard applied: H986 scanner
 throughput gains are hardware, not AI. <!-- bib: wconews104_china,
 wco_china_aicasestudy2025, caoxia2024_wcj -->

[^ch15-5]: Brazil: Jambeiro Filho
 (RFB), peer-reviewed (2015/2019); WCO News 105 (2024). The
 untraceable secondary figures (riotimesonline, 2026) are declined
 per the sourcing rule. <!-- bib: jambeiro2019_sisam,
 wconews105_brazil2024 -->

[^ch15-6]: India: WCO News 109 (Issue
 1, 2026); WCO News 108 (2025). Administration-stated qualitative
 KPIs; no headline percentage published. <!-- bib:
 wconews109_india2026, wconews108_korea -->

[^ch15-7]: Netherlands: WCO
 News 99 (Issue 3, 2022); World Customs Journal 14(2) 2020
 (Giordani et al., PROFILE). The secondary "~95%" figure is
 secondary/weak and declined. <!-- bib: wconews99_netherlands2022,
 giordani2020_profile -->

[^ch15-8]: Uruguay: WCO News 107
 (Issue 2, 2025); VUCE Uruguay; Concepto SAS. <!-- bib:
 wconews107_uruguay2025 -->

[^ch15-9]: US CBP per:
 DHS AI Use Case Inventory; DHS "Using AI to Secure the Homeland";
 the 1.4-second/75-kg figure is a single 2023 House-testimony
 anecdote (secondary), presented as illustrative only. <!-- bib:
 dhs_cbp_aiinventory, potomac_cbp2023 -->

[^ch15-10]: The register: Indonesia's minister-hedged "90%" (secondary,
 ANTARA/VOI, Dec 2025); Dubai 2026 seizure totals with vague
 technology attribution (Gulf News); the untraceable "70%/85%"
 aggregate (secondary, 2026); ZATCA and Egypt NAFEZA gains
 attributed to single windows and process re-engineering (WCO News
 103; Egypt TRS 2024). <!-- bib: antara2025_tradeai,
 gulfnews2026_dubai, wconews103_zatca, egypt_trs2024 -->

[^ch15-11]: Austria: OECD-sourced EUR 185 M (2023), tax domain. Belgium:
 peer-reviewed VAT ML pipeline (arXiv 2106.14005). <!-- bib:
 oecd_austria_fieldfisher2025, belgium_vat_arxiv2021 -->

[^ch15-12]: Financial-crime detection as adjacent evidence: McKinsey &
 Company, *The Fight Against Money Laundering: Machine Learning Is a
 Game Changer* (2022) and related risk-and-resilience analyses —
 rule-based transaction monitoring false-positive rates up to ~90%;
 machine learning with network analytics improving identification of
 suspicious activity by up to ~40%; explainability required where
 determinations carry legal consequence. Cross-domain (banking
 AML), cited as method-and-failure-mode precedent, not a customs
 outcome. <!-- bib: mckinsey_aml_ml2022 -->

[^ch15-13]: IT service operations as adjacent evidence: McKinsey &
 Company, *Reimagining Tech Infrastructure for Agentic AI* (Apr
 2026) — enterprise service-desk agents under "governed autonomy"
 with "clear accountability" delivering ~25–45% cost savings.
 Broader distribution/supply-chain AI value (material cost and
 productivity gains gated by data quality and workflow redesign) per
 McKinsey operations research, 2024–2026. Cross-domain (IT service
 operations), cited as an operational precedent for the
 Operator-to-Supervisor transition under retained accountability,
 not a customs outcome. <!-- bib: mckinsey_agentic_infra2026 -->

[^ch15-14]: McKinsey public customs case, client anonymized: a G-20
 administration's post-clearance-audit models reportedly moved detected
 violations from 30% to 60% and raised workforce productivity by 75%.
 Consultant-reported; used as practice-reported evidence, not an
 independently audited country result. <!-- bib:
 mckinsey_customs_analytics2022 -->

[^ch15-15]: Blackstone Legal & Compliance case: ~25,000 annual documents,
 30%+ reviewer-productivity improvement, and expected USD 5 million
 annual run-rate savings by 2027. Client/consultant-reported; adjacent
 regulated-compliance evidence, not a customs metric. <!-- bib:
 mckinsey_blackstone_compliance2026 -->

[^ch15-16]: BCG, *Trust Imperative 5.0* (2026): practical public-sector
 assurance guidance on risk triage, accountability, reusable artifacts,
 and delivery-embedded controls for agentic systems. Grey literature;
 cited for the operating pattern, not for a quantified customs result.
 <!-- bib: bcg_trust_imperative2026 -->

[^ch15-17]: The case portfolio is deliberately graded: Korea, China,
Brazil and the other customs cases document ML/CV/data-platform value;
the agentic governance and operating patterns are supported separately
by WCO's implementation baseline and practice-reported cross-sector
evidence. No source in this chapter is treated as proof for autonomous
customs adjudication. <!-- bib: wco_scp_report2025,
mckinsey_agentic_advantage2025, bcg_trust_imperative2026 -->
