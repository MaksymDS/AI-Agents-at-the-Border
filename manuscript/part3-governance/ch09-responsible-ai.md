---
title: "Responsible AI for Autonomous Systems"
part: "III — Governance and Trust"
chapter: 9
status: review
version: 0.3
last-updated: 2026-07-09
---

## The audit question

The internal audit of the analytics era had a familiar shape: *why did
the model score this shipment 0.87, and was the score fair?* Difficult
questions, but bounded ones — the model produced a number, a human acted
on it, and responsibility sat visibly with the human.

Now run the audit two years later, one rung up the ladder. A supervised
agent investigating a flagged declaration queried four systems, requested
a document from the importer, re-checked the certificate against the
rulings corpus, and closed the case as compliant. The auditor's question
has changed species: not *why this score* but ***why this sequence of
actions*** — why the agent asked for that document and not another, why
it stopped when it did, whether it was entitled to close the case at all,
and who answers for each step. The score question was about a number.
The action question is about conduct.

Everything the responsible-AI field built for the analytics era — bias
testing, explainability, human review — still applies. This chapter is
about what must be *added* when AI stops producing outputs and starts
taking actions, and about the encouraging fact that the additions are now
well understood: the governance literature, three regulatory regimes, and
this book converge on the same architecture.[^ch09-1]

## 9.1 What actually changes when AI acts

Three shifts define the governance delta between a model and an agent.

**From wrong outputs to events in the world.** A model's failure is
informational until a human acts on it; an agent's failure *is* the act —
the sent request, the written record, the closed case. Failure containment
moves from "review the output" to "bound the possible actions," which is
why the agent's tool list, not its model, is the primary control surface
(Chapter 10 treats it as the security boundary; here it is the
responsibility boundary).

**From single decisions to conduct over time.** An agent's risk lives in
sequences: individually reasonable steps composing into an unreasonable
course of action, or an early error propagating through everything
downstream. Oversight designed for single decisions — approve this
output, yes or no — does not see sequences. Agentic oversight must review
*trajectories*: the full path of steps, tool calls, and intermediate
conclusions (the observability that Chapter 13's AgentOps stack exists to
capture).

**From advisory to delegated.** A score advises; an L3/L4 agent
exercises delegated operational decision-making within its mandate. The
governing analogy is not software but *staff*: a junior officer acting
under standing instructions, with defined authority, supervision
proportionate to experience, and a full record of actions taken. The
analogy fails in exactly one place, and the failure is the book's
refrain: the agent never joins the accountability chain. Its mandate is
signed by a human; its conduct is answered for by humans.

## 9.2 Autonomy and agency: the lever most programs miss

The governance literature's most useful recent contribution is a
distinction this book adopts outright: **autonomy** (how independently
the system operates — a *design choice*) and **agency** (how much it can
do — the capability implied by its tool set) are **two independent
dials** (Figure 9.2).[^ch09-2]

![Figure 9.2 — Autonomy × Agency](/assets/diagrams/fig-ch09-autonomy-agency.svg){width=100%}

The practical force of the decoupling: *you can grant capability while
withholding independence.* An investigation agent can hold broad
read-access agency — every database, the full document store — while
operating at low autonomy, checking in before anything consequential.
Conversely, a green-channel clearance agent at L4 autonomy should hold
almost no agency: a tightly scoped, reversible action set and nothing
else. The two worst configurations are the ones vendors drift toward if
unmanaged: high-agency-high-autonomy (the demo that impresses and the
incident that follows), and low-agency-low-autonomy (the expensive
chatbot).

This gives the Autonomy Ladder its missing second axis. Every use case in
the AI inventory now carries two entries: its autonomy level (L1–L4) and
its tool list (agency). Rule 1 from Chapter 2 — autonomy per task, not
per system — extends naturally: *agency per task too*. The mandate
document (below) fixes both.

## 9.3 Oversight architectures: routing, not vibes

Chapter 2 matched each autonomy level to an oversight pattern. The three
canonical postures behind those patterns — spell them out once per
chapter, per the style guide — are **human-in-the-loop** (HITL: a human
approves each consequential action), **human-on-the-loop** (HOTL: the
agent acts by default; a human monitors and can intervene), and
**human-in-command** (HIC: humans set mandates and audit outcomes;
intervention is retrospective).

The design question is never "which posture do we believe in" — it is
**which tasks route to which posture, decided by what rule** (Figure
9.1). The state
of the art is a *deterministic* routing function: recent governance
frameworks route each task by four factors — **regulatory impact,
proximity to the affected party, reversibility, and data sensitivity** —
into the appropriate oversight tier, with each tier mandating specific
evidence artifacts for audit.[^ch09-3] The four factors map onto customs
almost embarrassingly well: a seizure is high-impact,
trader-facing, irreversible, and personal-data-heavy — HITL, always; an
internal analytics refresh is none of those — HIC with monitoring; the
long middle (document requests, routing decisions, case-file closures)
is exactly where the routing rule earns its keep, because the middle is
where ad-hoc judgment drifts.

![Figure 9.1 — Oversight Architecture Selector](/assets/diagrams/fig-ch09-oversight-selector.svg){width=100%}

Two implementation rules separate real oversight from its diagram:

**Enforce the routing through identity and permissions, not policy
text.** Each agent runs under its own identity, holding exactly the
permissions its tier allows; a tier upgrade is a permission change with
an approval trail, not a paragraph in a memo. The practitioner phrasing
worth quoting to your CIO: *"if your oversight process only exists in a
diagram, you don't have oversight, you have a manual."*[^ch09-4] Agentic
intervention windows are measured in seconds; only controls that execute
at machine speed count.

**Mandate evidence artifacts per tier.** HITL tasks produce approval
records; HOTL tasks produce intervention logs and sampling reviews; HIC
tasks produce complete decision trajectories and periodic audit reports.
The artifacts are defined *before* deployment — because they are also
precisely what Article-14-class regulation (Chapter 8) and your own
auditor general will ask to see.

One human factor completes the architecture. The public-administration
research on procedural justice in AI-assisted decision-making finds that
the perceived fairness — and therefore the legitimacy — of consequential
decisions depends not only on their outcomes but on *how* they are
reached, and that meaningful human involvement is a load-bearing part of
that "how" when AI enters the process.[^ch09-5] For an institution whose
authority rests on perceived legitimacy, this is not a soft
consideration: it is an argument, from evidence, that the oversight
human is load-bearing even when the agent is right.

## 9.4 Fairness and explainability, one rung up

The analytics-era toolkit transfers, with an upgrade at each piece.

**Bias testing extends from scores to conduct.** The classical question —
does the risk model flag certain origins or traders disproportionately? —
remains mandatory for every scoring component. The agentic addition:
does the *agent's behavior* differ across comparable cases — more
document requests for some trader profiles, faster closures for others,
different escalation patterns? Conduct bias will not appear in model
metrics; it appears in trajectory analytics, which is one more reason the
observability stack is a governance requirement and not an engineering
preference.

**Explainability becomes narration plus record.** For a score, an
explanation is a set of contributing factors. For an agent's case, the
explainable unit is the trajectory: what it did, in what order, on what
grounds, with citations at each step — the same grounding discipline
Chapter 3 made non-negotiable, now applied to actions. Brazil's SISAM
demonstrated the principle a decade early: natural-language explanations
were a deliberate design feature, and officer trust followed.[^ch09-6] The
standard this book recommends: **every consequential agent action must
be explainable to two audiences — the affected trader (in plain terms)
and the auditor (with the full record) — and the explanation is produced
at action time, not reconstructed later.**

**Contestability becomes a design requirement.** Layer-1 law (Chapter 8)
gives affected persons rights against solely-automated decisions; the
agentic implementation is concrete: a trader-facing path to challenge an
agent-touched decision, routing to a human with the trajectory in front
of them, on a clock. If the challenge path leads to a human who cannot
see what the agent did, the right is decorative.

## 9.5 The accountability chain, made of paper

Part I stated the principle — decisions transfer, accountability does not
— and Chapter 2 gave it a test: someone signs the mandate. This section
is the paperwork that makes the principle survive contact with an
incident.

**The mandate** (one per L3/L4 task): the task and its boundaries; the
autonomy level and the agency (tool list with permissions); the routing
tier and its evidence artifacts; the escalation triggers; the demotion
criteria (what evidence sends the task back down a rung); and the
signature — a name and a title, not a committee. If the mandate cannot
be written in two pages, the task is not understood well enough to
delegate.

**The AI inventory**: every deployed task, its ladder level, its agency,
its mandate owner, its review date. The inventory is the artifact that
turns "we govern our AI" from an assertion into a document — and it is
the first thing a regulator, an auditor, or an incoming Director General
will request.

> **Field note — Singapore, the inventory built as infrastructure.** As
> Singapore prepared to put AI agents in the hands of around 150,000
> public officers, GovTech built the accountability layer alongside the
> capability: a **registry of AI agents that tracks who owns each agent
> and what it does**, sitting inside a suite with "a layer of
> customisable rules, sanctioned AI tools and a registry to provide
> better visibility and security."[^ch09-8] This is precisely the
> inventory-as-graph this chapter argues for — ownership, function, and
> control recorded per agent — implemented not as an afterthought but as
> the platform on which agents are allowed to run at all. It pairs with
> Singapore's Model AI Governance Framework for Agentic AI (Chapter 8):
> the government wrote the taxonomy and then built the registry to
> enforce it.

**The incident path**: agent incidents are operational incidents with an
extra step — freeze the task (demote to L1 or suspend), preserve the
trajectories, review against the mandate, and answer the only question
that assigns responsibility correctly: *did the agent exceed its mandate,
or did the mandate permit the wrong thing?* The first is an engineering
failure; the second belongs to the signer. Both answers improve the
system; neither involves blaming the software.

## 9.6 Anchoring to standards

An administration should not defend its governance architecture as
bespoke. Anchor it: **NIST AI RMF** as the risk-management spine, its
**agentic profile extensions** for autonomy-tier classification and
tool-use risk mapping, **ISO/IEC 42001** as the certifiable management
system your IT organization can be audited against, and an open
evaluation framework (the UK AI Security Institute's Inspect is the
reference) for in-house agent testing.[^ch09-7] This stack is
jurisdiction-portable by construction — it satisfies EU Article-14
expectations, the WCO's HITL baseline, and GCC/ASEAN soft law
simultaneously (Chapter 8's portable baseline — explicitly a design
baseline, not a compliance guarantee — in engineering form) —
and it converts governance from a debate into a certification plan.

## 9.7 The operational assurance record: prove the right to operate

Policies describe intention; an agentic system needs an **operational assurance record**:
a concise, reviewable argument that it is acceptably safe for one
specific task at one specific autonomy level. This is not an imported
aviation metaphor or a new bureaucratic report. It is the binder that
connects the decision the administration wants to delegate to the
evidence that permits delegation.

Here, *operational assurance record* means an **internal governance artifact**: a structured
argument linking the task, evidence, controls, residual risks, owner, and
right to operate. The term does not imply a filing with a regulator,
conformity assessment, certification, or equivalence to the formal safety-
case regimes used in aviation, medical devices, nuclear operations, or
other regulated engineering domains. If local law assigns the phrase a
specific meaning, use the required name and process; preserve the evidence
logic, not the label.

For a customs agent, the claim might read: *this agent may assemble and
recommend a low-risk document-completeness disposition at L2; it may not
release cargo, alter a risk score, send an external request, or close a
case.* The evidence beneath it is concrete: the mandate; a data-flow
map; test results by language, commodity and exception type; injection
and tool-misuse tests; officer override and calibration results;
trajectory samples; training records; incident and rollback exercise;
and the owner’s dated sign-off. The argument also names **residual
risk**. A system that has no documented residual risk has not been
assessed; it has been marketed.

The operational assurance record gives the executive a better governance rhythm. Review
it before pilot, before every autonomy expansion, after any material
change, and after every incident. The board does not need to re-litigate
model theory. It asks four questions: has the task changed; has the
tool authority changed; has the evidence changed; has the residual risk
become unacceptable? A "yes" on any one freezes the existing mandate
until the case is updated. This makes safety legible in business terms:
**the system earns the right to operate, and keeps earning it.**[^ch09-9]

## 9.8 Contestability: design the path before the adverse outcome

Fairness and explanation are incomplete if the affected party and the
officer lack a practical route to challenge an outcome. For every
workflow that influences a trader, traveller or employee, document the
contestability path: what is communicated; what evidence can be seen;
who may request review; who conducts it; how the case is corrected; how
quickly the decision is reconsidered; and how the correction becomes a
system-learning signal. The path must work when the agent is wrong,
uncertain, unavailable or simply applied the wrong current rule.

This is not a promise to expose sensitive targeting methods or every
internal model parameter. It is a disciplined distinction between
protected risk information and a person's right to meaningful process.
An officer needs the sources and reasons necessary to exercise judgment;
an external party needs the applicable procedure and a route to human
review where law or policy requires it. Counsel should specify the
boundary per workflow, then test it with real case scenarios instead of
assuming that a generic privacy notice solves the problem.

Measure the path. Track requests for review, time to resolution,
reversals, recurring explanation failures and the segments in which they
cluster. A rising review rate can reveal a model issue, but it may also
show ambiguous policy, poor communication or a newly excluded document
type. Treat it as operational intelligence. The administration's claim
to responsible autonomy is strongest when a person can see the route to
challenge and the programme can show that the route changes practice.

## 9.9 Ethics becomes concrete at the boundary cases

Ethical principles become operational when a case sits at a boundary:
the document is incomplete but the trader's service clock is running; a
risk signal is strong but its basis cannot be disclosed; an officer
disagrees with an apparently well-grounded recommendation; a language
or accessibility condition makes the standard interface unreliable.
Build a small boundary-case library from real, de-identified patterns
and use it in evaluation, training and governance review. The library
should include the expected human route, not merely the desired model
answer.

This is where fairness is more than a statistical test. Ask whether the
workflow creates extra burden for a group or document type, whether the
officer can identify a harmful recommendation in time, whether the
fallback is equally available, and whether the correction reaches the
source of the error. Where the answer is uncertain, cap the authority or
design a more visible review—not because technology has failed, but
because the public process is not yet defensible.

Review the library after incidents, appeals, recurring overrides and
policy changes. It becomes a shared memory of the hard judgments the
system is not allowed to make silently. This is a practical form of
ethical governance: not a universal promise of perfect outcomes, but a
recorded commitment to recognise, route and learn from the cases where
automation is least trustworthy.

## Decision Toolkit — Chapter 9

**The oversight router** (adopt as policy): route every AI task by four
questions — regulatory impact? affected-party proximity? reversibility?
personal-data sensitivity? Any "high" on irreversibility or enforcement
impact → HITL. Trader-facing but reversible → HOTL with sampling.
Internal and reversible → HIC with full trajectory logging. Publish the
routing table; enforce it through per-agent identity and permissions.

**The mandate template** (two pages, per L3/L4 task): boundaries ·
autonomy level · tool list and permissions · routing tier and evidence
artifacts · escalation triggers · demotion criteria · named signer ·
review date.

**The two-audience explainability test**: for each consequential action
type, confirm the system produces, at action time, (a) a plain-language
account adequate for the affected trader and (b) a full grounded
trajectory adequate for the auditor. Fail either → the task's ceiling
drops to L2 until fixed.

**The inventory check** (quarterly): tasks without a current mandate,
mandates without a living signer, tiers without their evidence artifacts,
challenge paths without a human who can see trajectories. Any finding is
a demotion trigger, not a memo.

**The safety-case review** (before L3/L4 and after material change): one
claim per task · bounded authority · evidence by risk segment · residual
risk stated · named signer · exercised rollback. If the argument cannot
be read in one meeting, the task is too broad to delegate.

## Key Takeaways

- Agents change the governance question from *why this output* to *why
 this conduct*: failures are events, risk lives in sequences, and
 oversight must review trajectories, not outputs.
- Autonomy and agency are independent dials — grant capability while
 withholding independence, and fix both per task in a signed two-page
 mandate.
- Route oversight deterministically by regulatory impact, affected-party
 proximity, reversibility, and data sensitivity — and enforce the
 routing through per-agent identity and permissions, or you have a
 manual, not oversight.
- Fairness and explainability extend from scores to conduct: trajectory
 bias analytics, action-time explanations for two audiences, and a
 contestability path that ends at a human who can see the record.
- Accountability is made of paper: the mandate, the inventory, the
 incident path — anchored to NIST AI RMF, ISO/IEC 42001, and open
 evaluation tooling so the architecture is certifiable, portable, and
 defensible.
- A policy is not an operational assurance record. Every consequential task should carry an
  short, evidence-backed argument for its right to operate and a stated
  residual risk, re-approved when authority or evidence changes.

---

## Endnotes

[^ch09-1]: The governance architecture described here is a synthesis of
 the NIST AI RMF, the Cloud Security Alliance Agentic Profile, the EU
 AI Act's high-risk obligations, and Singapore's agentic governance
 framework. The sources differ in legal force, but converge on bounded
 authority, auditable controls, and human accountability. <!-- bib:
 nist_airmf2023, csa_agentic_nistprofile2026, ec_navigating_aiact,
 lw_singapore2026 -->

[^ch09-2]: Autonomy vs. agency as independent axes: Feng et al. (2025);
 NIST's definition of full autonomy ("within a defined scope, without
 human intervention"); and Mitchell et al. (2025) on the risk-benefit
 profile of semi-autonomous configurations. <!-- bib:
 feng2025_autonomyagency, mitchell2025autonomy -->

[^ch09-3]: Deterministic oversight routing by regulatory impact, customer
 proximity, reversibility, and data sensitivity, with tier-specific
 evidence artifacts: GAIE / Oversight Classification Model (2026),
 mapped to NIST AI RMF, ISO/IEC 42001, and the EU AI Act; agentic
 supplementation of NIST RMF per the Cloud Security Alliance Agentic
 Profile (2026).
 <!-- bib: gaie2026, csa_agentic_nistprofile2026 -->

[^ch09-4]: Practitioner formulation on identity-enforced, machine-speed
 oversight (intervention windows "shrink to seconds"): Strata (2026),. <!-- bib:
 strata_hitl2026 -->

[^ch09-5]: Procedural justice in public AI decision-making: de Fine
 Licht (2025), "Resolving Value Conflicts in Public AI Governance: A
 Procedural Justice Framework," *Government Information Quarterly*
 42(2); de Fine Licht & Folland (2025), "AI in Public
 Decision-Making," *Public Administration* (doi:10.1111/padm.70029).
 These replace an earlier reference ("Diebel et al., 2025") that
 could not be verified against public sources — see the provenance
 note in `research/sources.bib`. <!-- bib:
 definelicht2025_procedural, definelicht_folland2025_padm -->

[^ch09-6]: Brazil RFB SISAM: explainable Bayesian networks with
 natural-language explanations as a deliberate trust mechanism
 (peer-reviewed, Jambeiro Filho). <!-- bib: jambeiro2019_sisam -->

[^ch09-7]: NIST AI RMF 1.0 (2023) + Generative AI Profile (NIST AI 600-1,
 2024); CSA "NIST AI RMF: Agentic Profile" (2026) with the AI
 Controls Matrix; ISO/IEC 42001; UK AI Security Institute Inspect
 (2024) and Inspect Sandboxing Toolkit (2025). <!-- bib: nist_airmf2023,
 csa_agentic_nistprofile2026, isoiec42001, aisi_yearinreview2025 -->

[^ch09-8]: Singapore GovTech AI-agent deployment: a registry tracking
 agent ownership and function, within the AI Assistant Desk suite,
 ahead of a broader 2026 rollout to ~150,000 public officers; CE Goh
 Wei Boon on the "layer of customisable rules, sanctioned AI tools
 and a registry." *The Straits Times* / GovInsider reporting, 2026.
 Cited as an adjacent government exemplar of the AI inventory built
 as enforcement infrastructure. <!-- bib: singapore_govtech_registry2026 -->

[^ch09-9]: The safety-case formulation operationalizes the NIST AI RMF
and Cloud Security Alliance Agentic Profile: map the task, measure and
manage the risk, bind authority to controls, retain evidence and revisit
the risk after change. It is a governance pattern, not a claim that a
standard certifies a system safe. <!-- bib: nist_airmf2023,
csa_agentic_nistprofile2026, bcg_trust_imperative2026 -->
