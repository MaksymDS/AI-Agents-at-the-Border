---
title: "Build, Buy, or Partner — The Vendor Reality"
part: "II — The Business Case"
chapter: 7
status: review
version: 0.3
last-updated: 2026-07-09
---

## The tender that failed on page one

The RFP arrives, as they do, through the portal, and it fails before the
requirements section begins. It asks for "an AI system" — as if AI were
a product category rather than an operating model. It lists modules:
OCR, classification, risk scoring, dashboards, a chatbot, and lately,
inevitably, "agentic AI." What it never defines is **the decision the
system is allowed to influence**.

I have read that RFP many times, from the vendor's chair, and I can
tell you what happens next: the gap is the opening. If the buyer does
not define the decision boundary, a vendor can sell the most impressive
system that fits the words of the tender — not the system the
administration actually needs — and be, on paper, fully compliant.

This chapter is written from the other side of the table. Most of this
book speaks to customs leadership from evidence; this chapter speaks
from delivery — years of reading customs tenders, running the demos,
signing the contracts, and then living with them through production.
The vendor perspective is declared openly because it is the chapter's
value: the advice below is what the people who *respond* to your RFPs
know about which of your clauses protect you and which we could walk
around in our sleep. Vendors reading this will recognize the mirror;
that is intentional.

## 7.1 The RFP that cannot buy the wrong thing

The section missing from the failed tender is not "technical
specifications." It is a **decision-rights and operating-context
section**, and it changes everything downstream. It states: what
decision, recommendation, or workflow the system supports; who remains
accountable; what the system is *not allowed* to do; what evidence must
be shown to the officer; what happens when the model is uncertain; what
data may and may not be used; and what performance is required at each
gate before the system expands.

Readers of Part I will recognize this as the Autonomy Ladder and the
mandate discipline, translated into tender language — which is exactly
the point. If that section exists, a vendor cannot easily sell a
generic AI platform and call it customs modernization. Without it,
almost anything can be presented as compliant. The buyer's first
question is not *"can you build this?"* It is *"what operational
judgment are we delegating, to what level, under what mandate, and with
what evidence trail?"* — and Appendix B builds the tender skeleton
around it.

One drafting rule multiplies the section's force, and it applies to
every governance expectation in the tender: **do not write principles;
write artifacts.** "The vendor shall comply with responsible AI
principles" is satisfied with a paragraph. Write instead the artifacts
you expect to receive and the gates they must pass: an AI impact
assessment, a risk classification, a data-flow map, a model card, an
evaluation report against your samples, a human-oversight design, an
incident process, release governance, audit logs. A principle is an
opinion; an artifact is a deliverable.[^ch07-1]

## 7.2 Build, buy, or partner: own the judgment

The question in this chapter's title is usually asked wrong. In-house
customs AI is not an illusion — but "in-house" does not mean the
administration writes every line of code and replaces the vendor market
with an internal laboratory. That version is expensive, slow, hard to
staff, and fragile when key people leave. The honest version is
different: **the administration owns the problem, the data logic, the
evaluation standard, the operating mandate, the release authority, and
enough technical capability to know whether the system is working.** It
may buy components. It may partner widely. It does not outsource
judgment over the system.

That boundary sorts the portfolio (Figure 7.1). **Build** only where
the capability
is strategic, repeated, sensitive, and deeply dependent on the
administration's own operational knowledge — risk targeting and
selectivity policy, enforcement intelligence, valuation-risk logic,
post-clearance analytics, certain agentic workflows. These are not
software functions; they encode institutional judgment. **Buy** the
commodity layers — OCR engines, translation, ingestion, workflow UI,
infrastructure, identity, monitoring, generic case management: building
those from scratch is rarely sovereignty; it is usually a slower
procurement mistake. **Partner** in the middle, and for most
administrations partnership is the right answer: where the problem is
strategic but the technical frontier moves too fast to carry alone, buy
the engineering acceleration and keep the operating brain inside.

![Figure 7.1 — The Judgment Boundary](/assets/diagrams/fig-ch07-judgment-boundary.svg){width=100%}

Korea, this book's recurring reference, belongs here with a warning
label. It is not "we hired three data scientists and built a chatbot";
it is a national capability compounded over a decade — digital
foundations, institutional continuity, data access, research
partnerships, and the workforce design of Chapter 14. Korea is not
irrelevant as a benchmark; it is hard to imitate *casually*. The right
ambition for most administrations is not "build like Korea
immediately" but: buy commodity technology; partner for acceleration;
build internal capability around data, evaluation, governance, and
operational ownership; and progressively move the strategic control
points inside.

The rule, compressed: **buy the tools; partner on the build; own the
judgment.** The dangerous option is not buying from vendors — vendors
are necessary. The dangerous option is buying in a way that leaves the
administration unable to challenge, test, replace, or govern the
vendor. "Build versus buy" is the wrong question; the real question is
whether the administration is building dependency or building
capability.

## 7.3 Reading the room — in both directions

Vendors read customers in the first meeting, and the signals travel in
both directions.

The customer a serious vendor wants does not begin with the model; they
begin with the work — the current process, the exceptions, the people
who will live with the system after the demo team leaves. They know
which officers are overburdened, where data quality is weak, which
controls are politically sensitive, and which metric actually matters.
And they ask uncomfortable operational questions early: *What will your
system do when the declaration is incomplete? How do you separate model
confidence from business confidence? What evidence will the officer
see? How do we override it? How do we know the model has degraded? What
do we need to own internally so we are not dependent on you forever?*

**Weak customers ask for features. Strong customers ask for failure
modes.** The other reliable signal is the room itself: a viable project
has operations, risk, legal, data, cybersecurity, and a senior business
owner at the first serious briefing — not only IT, procurement, and the
innovation team. Whoever is absent from that meeting will appear later
as a blocker. And the strongest customers understand that AI delivery
is not a single acceptance event; **it is a controlled expansion of
trust** — pilots, gates, monitoring, retraining rules, exit rights.
That sentence, from the vendor side, is the entire Chapter 12 restated
as a compliment.

The demo deserves its own literacy, because many demos are optimized to
impress rather than to predict delivery. Four patterns account for most
of the gap: **curated input** (real system, unrepresentative sample —
clean documents, known commodities); **hidden human effort**
(pre-processed, pre-labeled, manually corrected behind the scenes);
**latency hiding** (you see the answer, not the time, cost, or retries
behind it); and **integration theater** (the screen looks connected to
a customs environment but runs against a static file or a mock API).
One request collapses all four: *"Can we give you twenty examples you
have not seen, from our real workflow, and watch the system process
them end to end — latency, confidence, evidence, failures, and cost
included?"* Not adversarial samples — representative ones: messy,
multilingual, incomplete, duplicated, ordinary. If the answer becomes
complicated, the buyer has learned something important.

The industry analysts have given this problem a name. Gartner calls the
dominant pattern *agent washing* — vendors rebranding chatbots, robotic
process automation, and assistants as "agentic AI" without the
underlying capability — and estimates that only a small fraction of the
thousands of vendors marketing agentic products offer genuine
autonomous capability.[^ch07-5] For a customs buyer this reframes the
demo from a sales courtesy into a due-diligence instrument: the point of
the twenty-samples test is precisely to separate an agent from a chatbot
with better marketing, on the administration's own data, before the
contract is signed rather than after.

## 7.4 The contract: four clauses that decide the project

The audit record across governments is unambiguous about where AI
procurements fail: rights to data, models, and outputs left undefined
at award.[^ch07-2] The vendor-side view confirms it and adds three more
clauses to the short list.

**Rights — the fair boundary.** The administration should be
uncompromising about its own side: source data; cleaned and transformed
versions; annotations created during the project; officer feedback and
override history; evaluation datasets; performance logs; the scores and
explanations generated for its declarations; configuration and
threshold history; and the documentation needed to reproduce, audit, or
migrate. Customs data must not train systems for other customers
without explicit, legally safe, operationally understood approval —
and **"anonymized" is not a magic word in customs**: trade data is
commercially sensitive even with no personal data in sight. At the same
time, demanding ownership of the vendor's pre-existing platform,
foundation-model weights, or reusable libraries usually raises price
and reduces vendor interest without improving control. The fair
boundary: *the buyer owns its data, its operational knowledge, its
outputs, and the evidence needed to audit and migrate; the vendor keeps
its generic tools and background IP — provided the buyer is not trapped
inside them.* Contracts that blur background IP, foreground artifacts,
customer data, derived assets, outputs, logs, and documentation have
not avoided the dispute; they have scheduled it.

**Acceptance — staged, or scheduled for conflict.** No serious vendor
should sign "100% accurate," "fully automated," or "free from
hallucination" — clauses that sound strict and are operationally
untestable — and no serious buyer should want a vendor who would. What
a serious vendor *can* sign is a controlled evaluation design: a
defined test population and locked evaluation set; a baseline; a metric
basket rather than one number, **with performance by class and risk
segment, because average accuracy is often the wrong metric — a system
can be accurate on common cases and dangerous on rare, high-impact
ones**; false-positive and false-negative tolerances; latency and
cost limits (the accuracy-versus-cost curve of Chapter 5, now a
contract exhibit); explainability and evidence requirements; the
override path; monitoring; rollback; a post-go-live review window. And
above all, staged: each gate answering a different question — does it
work technically; does it help the officer; does it improve the
decision process; can it be governed in production; can it be
maintained without hidden dependency.

If I could rewrite one clause across the contracts I have lived with,
it would be acceptance and change control, together. Conventional
contracts treat acceptance as a finish line: deliver, test, accept,
support begins. For AI, acceptance should mean something else: **the
system has earned the right to operate within a defined mandate, under
these controls, with this monitoring** — and the clause defines not
only initial acceptance but the conditions for expansion, retraining,
model change, threshold change, suspension, rollback, and
revalidation. Do not accept the system once; **accept its right to
operate at a specific level of autonomy.** That one change makes the
vendor more honest — no hiding behind a successful demo — and makes the
buyer unable to pretend governance is someone else's problem. Both
sides are forced to manage AI as a living operational capability, which
is the central procurement lesson of this book: **buy the operating
discipline, not only the technology.**

**Change governance — ban invisibility, not maintenance.** Chapter 13's
rule against silent updates is right and easy to write badly. "No
change without a full formal change request" freezes security patches
and bug fixes — protecting the buyer one way while creating risk
another. The workable clause classifies: security patches, critical
fixes, and infrastructure maintenance flow through a controlled
emergency and maintenance path; anything that may affect
recommendations, scores, explanations, routing, thresholds, officer
workload, legal defensibility, or user-facing outputs is governed
before production — versioned models and prompts, release notes, change
classification, pre-production testing, canary or shadow deployment for
material changes, rollback, post-release monitoring, and an audit log
of what changed, when, why, and on whose approval. **The key is not "no
updates." The key is no invisible change to operational behavior.**

**Pricing — matched to the Maturity Ladder.** The worst model is fixed
price for an undefined research problem: it forces the vendor to
overprice risk, underdeliver, or fight change requests — and rewards
theater. Uncapped time-and-materials has the mirror flaw. Outcome-based
pricing sounds attractive and rarely survives customs reality: detection
and clearance outcomes are shaped by policy, staffing, data access, and
trader behavior — a vendor should be accountable for the system, not
for every variable in the administration. Per-transaction pricing works
only for mature, high-volume services, and even then with care: if
every model call costs money, officers stop using the system. The
recommendation follows the ladder: Document Intelligence — fixed price
with volume bands, once document types, languages, targets, and
exceptions are defined; GenAI Assistants — capped T&M for discovery and
pilot, then subscription or managed service with usage bands and
service levels; AI Agents — **never the whole future in one fixed-price
contract**: staged gates (design, sandbox, controlled pilot, limited
production, scale-out), each with acceptance criteria, a stop/go
decision, and a **commercial reset**. For high-risk operational
systems, the best structure is not the cheapest-looking one; it is the
one that keeps incentives honest.

## 7.5 Lock-in: convenience, not conspiracy

Vendor lock-in rarely begins as a plot. **It begins as convenience**,
and it accumulates at four points. First, *data interpretation*: the
vendor learns how the administration's codes, exceptions, documents,
and informal practices actually work — and if that knowledge lives in
the vendor's notebooks, scripts, prompts, and undocumented mapping
layers, the customer is already losing the ability to move. Second,
*integration*: once the vendor's system is the bridge between legacy
systems, case management, and document stores, the dependency is no
longer on the model but on the vendor's private understanding of the
environment. Third, *performance history*: if only the vendor knows how
the model was evaluated, which samples were excluded, which thresholds
were tuned and why, no alternative can ever be fairly compared. Fourth,
*urgency*: after go-live, operational pressure makes replacement look
risky; "we will document this later" — and later rarely comes.

Against this, some measures work and some are rituals. **Working:**
data export rights; documented mappings; standardized interfaces; a
real data model (specifying WCO Data Model conformance in the tender is
an anti-lock-in lever, not a formality); and — best of all — internal
capability: people who understand the data, the workflow, the model
behavior, and the contract (Chapter 14's hub, wearing its procurement
hat). **Ritual unless enforced:** escrow that no one has ever tested
for deployability by a third party; multi-vendor architecture whose
interfaces and responsibilities are decorative; a standard data model
"mentioned in a slide" rather than implemented conformantly. The audit
record shows where the ritual path ends: two decades of incumbency and
nine-figure spending outside competition in a revenue
administration.[^ch07-3]

The practical test fits in one sentence, and belongs in every
governance review: *"If we terminate this contract in twelve months,
what exactly can we take, who can run it, and what would be missing?"*
If the answer is vague, lock-in already exists.

> **Field note — GAO on the mistake that repeats.** The US Government
> Accountability Office's April 2026 audit of federal AI acquisitions
> (GAO-26-107859) found something more useful than a list of failures: it
> found the *meta*-failure. Across the four agencies it examined — Defense,
> Homeland Security, GSA, and Veterans Affairs — none had processes to
> systematically collect and reuse the lessons learned from earlier AI
> procurements, which, the GAO warned, leaves agencies "missing
> opportunities to learn from more established acquisitions and increasing
> the risk that future AI procurement efforts will repeat avoidable, and
> potentially costly, mistakes."[^ch07-6] Read it as the institutional form
> of this chapter's argument: the individual defenses — decision-rights
> clauses, the twenty-samples test, export rights, WCO Data Model
> conformance — only compound into protection if the administration keeps
> and reuses what each procurement taught it. All four agencies concurred
> with the recommendation to build that memory. An administration that
> writes its acquisition lessons down, and reads them before the next
> tender, is already ahead of four large federal departments.

## 7.6 Where soft law buys hard things

Chapter 8 established that across the GCC and much of Asia, AI
procurement is disciplined by frameworks rather than statutes —
SDAIA's adoption framework and review boards, the UAE's procurement
guidelines and charter, ISO/IEC 42001 as a de facto supplier
bar.[^ch07-4] The vendor-side confirmation comes with a sharpening:
**soft law is not soft in the commercial sense.** If a framework is not
legally binding but the committee scores vendors against it, it is a
procurement gate. If a certification is not mandatory but the buyer
treats it as evidence of maturity, it is part of the sales process. If
responsible-AI guidelines are "principles" but the project board
requests a self-assessment, they are delivery obligations.

What the research cannot see is the informal sequencing. In practice,
the governing question inside the buying institution is rarely "what
does the AI law require?" — it is "**will this pass the internal
governance route?**": responsible-AI expectations, data protection,
cybersecurity review, hosting and sovereignty posture, auditability,
and alignment with the national digital agenda. A vendor can pass the
technical conversation and fail the confidence conversation — *can they
handle government data; can they explain the model; can they operate in
our cloud; can they support Arabic and English; can they stand in front
of leadership if something goes wrong?* In these tenders, **trust
architecture matters**: the winning proposal is the model *plus*
hosting posture, governance posture, local delivery capability,
documentation, and the ability to reduce perceived institutional risk.
For the customs buyer, the consequence loops back to section 7.1: turn
the soft-law expectations into the hard artifact list, and let the
tender do the enforcing.

## 7.7 Buy an operating model, not an implementation team

The most consequential vendor question is asked after the demonstration
and before award: **who will operate the system when the delivery team
has gone?** A proposal should identify, by role, the accountable product
owner, customs-domain lead, solution architect, security lead, model or
prompt operator, integration owner, incident commander, and local
support path. If these are merely names in CVs, the buyer has purchased
a project. If they are named roles with handover criteria, access rights,
runbooks, service objectives and an administration counterpart, the
buyer has begun to purchase an operating model.

Make the operating model demonstrable in procurement. Require a 90-day
mobilisation plan that produces a process map and baseline; a data-flow
and identity map; a minimum viable evaluation harness built on
administration-selected examples; a model and tool inventory; an
incident tabletop; and the first transfer of knowledge to the internal
team. Score the proposal for this evidence, not only for architecture.
By day 90 the administration should be able to answer four questions
without the vendor presenting slides: what task is being changed, who
owns it, how will failure be detected, and what will be retained if the
project stops.

This changes commercial incentives. Pay for artifacts that reduce
asymmetry—tested interfaces, documented mappings, evaluation datasets,
release records, runbooks and trained internal owners—at the same time
as you pay for visible functionality. Hold back a modest but meaningful
share of each gate until the administration can reproduce the agreed
test, export the relevant evidence, and run a rollback exercise. It is
not punitive: a capable vendor should prefer a buyer with clear
acceptance and a route to scale over a buyer who keeps rediscovering the
requirements. The public-sector evidence is consistent on this point:
agentic systems fail to scale when legacy processes, integration,
governance, performance management and operating costs are treated as
post-award details.[^ch07-7]

Finally, distinguish the **platform fee** from the **judgment fee**. A
model gateway, document extractor or workflow engine may be priced as a
repeatable service. Customs-domain design, evaluation and operating
accountability are not generic consumption. They need named effort,
named outputs and a transfer plan. Hiding both under one opaque
"AI-platform subscription" prevents the buyer from comparing bids and
prevents the vendor from being honest about where the work lives.

## 7.8 The evidence room: keep the buyer in a position to decide

Create an **evidence room** as a contractual deliverable from the first
month. It is a controlled administration-owned repository containing
the mandate cards, architecture and data-flow maps, model and component
inventory, test sets and results, release records, trajectories or their
retention pointers, security findings, incident records, training
materials, interface specifications and runbooks. It should be usable
without the vendor's project portal and exportable in normal formats.

The evidence room solves a practical problem often mistaken for lock-in:
the buyer cannot evaluate a change because the facts are dispersed among
vendor systems and individual consultants. With the record in hand, the
administration can accept or reject a release, compare suppliers,
investigate an incident and carry a service through an orderly exit. It
also changes weekly governance: instead of asking whether delivery is
"on track," the programme asks whether the artifacts needed to operate
and audit the next gate are complete.

Price it accordingly. Make upkeep part of the recurring service, set a
service-level expectation for updates after a change or incident, and
test export before final acceptance. A vendor may protect legitimate
intellectual property; that is different from withholding the evidence
of how the administration's own data, authority and workflows were
used. The former can be handled through access controls. The latter is
incompatible with public accountability.

## 7.9 Red-team the buying decision before award

Before contract award, convene a short red-team review led by people who
did not design the tender. Give them the preferred proposal, scorecard,
cost normalisation, draft mandate and evidence-room contents. Ask them
to try to invalidate the purchase: Where does authority expand without a
new approval? Which promised data feed is not actually available? What
is the first non-exportable artifact? Which price assumption fails at
peak volume? Can the human queue absorb the vendor's claimed automation
rate? What happens if the model or hosting provider changes terms?

The purpose is not to reopen a fair competition or reward cynicism. It
is to identify the assumptions that the evaluation team has become too
close to see. Every finding receives one of four dispositions: correct
the tender/contract; add an acceptance condition; accept a named,
time-bound residual risk; or reject the proposal. Record the result in
the recommendation. A decision that survives this challenge will move
faster after award because its dependencies are already owned.

Use the same exercise at major renewal. Procurement is not a one-time
defence against lock-in; it is a recurring capability to compare the
service being received with the service originally promised and with the
administration's current authority, evidence and exit position.

## Decision Toolkit — Chapter 7

**The five instruments** (full versions in Appendices B and C):
1. **The decision-rights section** — no tender without it: decision
 supported · accountability · exclusions · evidence to the officer ·
 uncertainty behavior · data boundaries · gate performance.
2. **The artifact rule** — replace every "shall comply with
 principles" with the named deliverables and their gates.
3. **The twenty-samples test** — buyer-selected, representative,
 unseen, end-to-end under observation, with latency, cost, evidence,
 and failures visible.
4. **The staged operational acceptance clause** — acceptance = the
 earned right to operate at a specific autonomy level; expansion,
 change, suspension, rollback, and revalidation defined in the same
 clause; a commercial reset at each gate.
5. **The twelve-month termination test** — what can we take, who can
 run it, what would be missing; asked annually, answered in writing.

**The boundary rule:** buy the tools; partner on the build; own the
judgment — and audit yourself yearly on which side of
dependency-versus-capability the program is moving.

## Key Takeaways

- The RFP that cannot buy the wrong thing has a decision-rights and
 operating-context section; without a defined decision boundary,
 "compliant" and "right" part ways on page one.
- Build only what encodes institutional judgment; buy the commodity
 layers; partner where the frontier moves too fast to carry alone —
 buy the tools, partner on the build, own the judgment.
- Strong customers ask for failure modes, staff the first meeting with
 every future blocker, and treat delivery as a controlled expansion of
 trust; the twenty-samples test collapses demo theater in one request.
- Four clauses decide the project: rights (the fair boundary —
 "anonymized" is not a magic word), staged operational acceptance
 (accept the right to operate, not the system), change governance (ban
 invisible behavioral change, not maintenance), and ladder-matched
 pricing with commercial resets at gates.
- Lock-in begins as convenience and accumulates at four points; export
 rights, documented mappings, data-model conformance, and internal
 capability work — untested escrow and decorative multi-vendor
 architectures are rituals. Ask the twelve-month question yearly.
- Soft law is commercially binding when it becomes named tender
 artifacts. The real gate is the confidence conversation, not the
 technical one.

---

## Endnotes

[^ch07-1]: The artifact-based tender pattern aligns with the EU Model
 Contractual Clauses for AI (MCC-AI, v1 Sep 2023; updated with
 Commentary Mar 2025) — a modular AI-specific schedule annexed to
 the base contract, covering risk management, data governance,
 transparency, human oversight, and audit rights; usable outside the
 EU as a best-practice checklist, and best treated as a floor
 rather than a complete risk allocation. <!-- bib:
 eu_mccai_2025 -->

[^ch07-2]: US GAO, *AI Acquisitions* (Apr 2026): data, model, and
 output-rights uncertainty at award as the recurring documented
 failure mode across reviewed federal AI contracts. <!-- bib:
 gao_ai_acquisitions2026 -->

[^ch07-3]: UK National Audit Office on government technology suppliers
 (Jan 2025): GBP 3.8 bn of tech-supplier contracts over five years
 at HMRC, GBP 591 m of it excluding competition, with suppliers
 engaged 20+ years — the audit record's illustration of incumbent
 lock-in in a revenue administration. <!-- bib:
 uknao_tech_suppliers2025 -->

[^ch07-4]: GCC procurement mechanism ("soft-law-as-procurement-filter"
 + ISO/IEC 42001 as de facto supplier bar): SDAIA AI Adoption
 Framework (Sep 2024) and Generative AI Guidelines for Government
 (Jan 2024, Procurement Review Boards); UAE AI Procurement
 Guidelines, AI Charter, and the TDRA AI Test and Validation Lab
 under the new Federal Authority for AI and Data (Jun 2026). <!-- bib: sdaia_regs,
 ailawguide_uae2026 -->

[^ch07-5]: Gartner, *Over 40% of Agentic AI Projects Will Be Canceled by
 End of 2027* (25 Jun 2025): "agent washing" defined as rebranding
 assistants, RPA, and chatbots as agentic AI without substantial
 capability; Gartner's estimate that only ~130 of thousands of
 self-described agentic vendors offer genuine capability. <!-- bib:
 gartner_agentic_cancel2027 -->

[^ch07-6]: US GAO, *Artificial Intelligence Acquisitions: Agencies
 Should Collect and Apply Lessons Learned to Improve Future
 Procurements* (GAO-26-107859, 13 Apr 2026): across Defense, Homeland
 Security, GSA, and Veterans Affairs, no processes to systematically
 collect and reuse AI-procurement lessons learned; all four concurred
 with the recommendation to establish them. Cited as an adjacent
 government audit finding on procurement discipline. <!-- bib:
 gao_ai_acquisitions2026 -->

[^ch07-7]: Deloitte, *GovTech Trends 2026*, frames production agentic
systems as a managed digital workforce requiring process redesign,
integration, onboarding, performance tracking and FinOps; McKinsey's
2026 procurement analysis describes the operational workflow rather
than a standalone assistant as the source of value. Both are
practice-reported adjacent evidence, used here for the operating-model
pattern rather than as a customs performance claim. <!-- bib:
deloitte_govtech2026, mckinsey_procurement_agentic2026 -->
