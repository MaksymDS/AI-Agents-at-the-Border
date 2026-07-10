---
title: "The Pilot Playbook"
part: "IV — Execution"
chapter: 12
status: review
version: 0.3
last-updated: 2026-07-09
---

## The pilot that succeeded at nothing

The closing slide said *94% accuracy*, and the room applauded. Six
months later the pilot is still a pilot. The risk directorate will not
take it into operations ("94% of what, measured how, and who handles the
6%?"). Finance will not fund the scale-up ("what does it save per
declaration?"). Legal has discovered the pilot ran on production trader
data under an authorization written for "a technology evaluation." And
the vendor, reasonably, wants a decision.

Nothing failed, and that is the failure. The pilot was designed to
*demonstrate the technology* when its job was to *produce evidence for a
decision* — a specific decision, named in advance, with the evidence
requirements written down before the first document was processed. This
chapter is the design discipline that separates the two: the charter,
the three stages, the gates, and the metrics that a probabilistic system
actually needs. It is also where the book's central promise gets kept —
"climb one rung at a time, on evidence" (Chapter 2) is operationalized
here, evidence item by evidence item.

## 12.1 A pilot is an evidence factory for a named decision

Write the decision first. Not "pilot an AI classification assistant" but:
*"Decide whether HS-code suggestion moves to L2 operation in the two
main clearance offices, at a unit cost below X, by Q3."* Every design
choice follows from the sentence — the metrics are whatever that
decision needs, the duration is however long the evidence takes, and
"success" and "failure" both become useful outputs, because a pilot that
proves a task is *not* ready at acceptable cost has saved the
administration from a production incident at pilot prices.

Two corollaries discipline the whole exercise. First, **a pilot that
cannot fail is a demo** — if no plausible result would change the
decision, the exercise is theater, and vendors can tell. Second, **pilot
purgatory is a design defect, not a fate**: pilots stall indefinitely
when no one wrote down what evidence would end them. The gate criteria
(12.3) are the exit, in both directions.

Everything in this chapter presupposes the paperwork of Part III: the
task's mandate, its data readiness check (Chapter 11), and a lawful
basis for the data the pilot touches — the legal discovery in the
opening scene is the most preventable failure in this book.

## 12.2 The three stages, and what each one proves

The deployment pattern this book recommends refines the classical
three-step pilot (data preparation → training → monitored deployment)[^ch12-1]
into stages defined by *what is at risk* (Figure 12.1):

![Figure 12.1 — Piloting in Stages](/assets/diagrams/fig-ch12-pilot-stages.svg){width=100%}

**Stage 1 — Shadow mode.** The system runs on live inputs; its outputs
touch nothing and no one. Officers work normally; the system's answers
are recorded alongside theirs. What it proves: raw task performance on
*your* traffic (not the vendor's benchmark), volume handling, and the
first honest measurement of the disagreement rate between system and
officers — which is not yet an error rate, because at this stage nobody
knows which side of a disagreement is right. Shadow mode is cheap,
legally light (no decisions are touched), and skipping it is how vendor
benchmarks become production surprises.

**Stage 2 — Supervised operation.** The system's outputs enter the
workflow at L1/L2: officers see, confirm, correct. What it proves: the
numbers that matter — override rates and *why* (the correction taxonomy
becomes the improvement backlog), officer trust calibration (do they
rubber-stamp, fight, or genuinely verify?), throughput deltas against
the Chapter 5 baseline, and unit cost in reality. This is also where
Chapter 11's feedback capture starts paying: every confirmation is a
label.

**Stage 3 — Gated autonomy expansion.** For tasks whose decision named a
higher rung: autonomy expands *by slice*, not by switch — the
demonstrably safest segment first (the lowest-risk declaration class,
the most routine enquiry type), each slice with its own gate evidence,
the rest remaining supervised. The mandate (Chapter 9) is amended per
slice, with the demotion criteria live from day one: a breached
threshold sends the slice back down automatically, and *that this
happened and was handled well* is itself evidence the program is
governable.

## 12.3 Gates: written before, judged after

A gate is a pre-committed evidence threshold. The catalog to draw from
(Appendix E holds the full version; per-task charters pick a subset and
set the numbers):

- **Task performance** — precision and recall stated *operationally*:
 not "94% accuracy" but "of 100 flags, N are right (officer time cost
 of the rest); of 100 true cases, it catches M (the misses are the
 risk exposure)." The trade-off between the two is a policy choice the
 business owner signs, not a technical default.
- **Reliability, not single-shot accuracy.** A system that answers a
 task correctly once proves little; agentic evaluation now scores
 **consistency across repeated independent trials** of the same task —
 because an officer must know whether the tool is dependable, not
 whether it is occasionally brilliant.[^ch12-2] Require the consistency
 metric in every charter for L2+ tasks.
- **Sequence robustness.** For multi-step tasks, test **state-dependent
 workflows** where an early error propagates — the failure mode that
 single-question benchmarks structurally cannot see and production
 structurally will.[^ch12-2]
- **Cost per unit** — measured, against the Chapter 5 worksheet, at
 pilot volume and projected to production volume. Recall the
 benchmark lesson: more spend does not buy more accuracy, so the gate
 is a curve position, not a budget ceiling.[^ch12-3]
- **Human factors** — override rate trend, correction taxonomy,
 calibrated-trust checks (seeded known-wrong outputs: do reviewers
 catch them?), and adoption (do officers *use* it unprompted by
 week 8?). A technically passing pilot with hostile users has failed;
 it just hasn't admitted it yet.
- **Security evidence** — for any task ingesting external content: the
 Chapter 10 injection tests, run against the pilot's production-like
 configuration, results attached to the gate review.
- **Governance evidence** — the tier's audit artifacts (Chapter 9)
 actually produced, sampled, and readable by someone who didn't build
 the system.

One evaluation caveat belongs in every charter: simulated users and
synthetic benchmarks are design tools, not verdicts — the research
record is explicit that simulated interaction is an unreliable proxy for
real users, and the strongest published metrics in this field include a
synthetic-data result that must not be quoted as an operational
outcome.[^ch12-4] **Gates are judged on your traffic, your officers, your
documents.**

## 12.4 Stakeholders: run the pilot in public

Internally, the pilot's constituencies were named in the opening scene —
operations, finance, legal — and the playbook is to give each a stake in
the charter: operations co-writes the human-factor gates, finance the
unit-cost gate, legal the data authorization and the contestability
check. A gate review with all three in the room converts "the innovation
team's pilot" into "the administration's decision" — which is the
difference between scaling and purgatory.

Externally, say less, later: publicize *outcomes that passed gates*, not
launches. The research record of Chapter 15 is a cautionary museum of
launch-week claims that never grew evidence behind them; an
administration that announces its 90% before the pilot ends has
volunteered for that exhibit.[^ch12-5] The quiet alternative compounds:
Korea's decade of unpublicized data work produced the loudest verified
number in the field.

> **Field note — why the gates are not bureaucracy.** The wider evidence
> on what happens when agentic systems reach production without staged
> gates is now substantial and specific. Gartner projects that more than
> 40% of agentic AI projects will be cancelled by the end of 2027 —
> driven by escalating cost, unclear value, and inadequate risk
> controls, not by model failure (Chapter 1) — and enterprise security
> surveys through 2026 consistently report that a majority of
> organizations running agents experienced a confirmed or suspected
> incident within the year (industry surveys put the figure across a
> roughly 47–88% range, depending on sample and method), against a small
> share of security budget allocated to securing them.[^ch12-6] The pattern behind the numbers is exactly what the
> three-stage gate is built to catch: systems moved from demo to
> consequential action without the shadow-mode measurement, the override
> taxonomy, or the injection testing that would have surfaced the failure
> cheaply. A customs administration reading these figures should draw
> confidence, not caution: the failures cluster in programs that skipped
> the discipline this chapter makes non-optional.

## 12.5 The pilot ledger: measure the decision, not the demo

A pilot should leave behind a ledger that a finance director, an
operations director and an auditor can each read. For every case in the
test population, record the baseline path and the agent-assisted path:
arrival time; documents used; agent recommendation and citations; officer
decision and override reason; tool calls; elapsed time; cost; exception
state; and final operational outcome. Segment the ledger by the features
that hide risk in averages—language, document type, commodity family,
port or channel, complexity and trader profile where lawful.

The design protects both sides. It prevents a vendor from winning with a
clean, unrepresentative sample, and it prevents an administration from
rejecting a useful system because it was judged against a vague memory of
the old process. Pre-register the success metric, the minimum acceptable
quality, the maximum acceptable harm or rework, the cost ceiling and the
demotion trigger. Then do not alter them after seeing the result. The
WCO's AI/ML baseline calls for cost-benefit analysis and pilots; the
agentic extension is to retain the full trajectory that explains how a
result was produced, not merely the final accuracy score.[^ch12-7]

One final rule keeps the pilot businesslike: include the **human time
created by the pilot itself**. Labeling data, maintaining a fallback,
reviewing every case and attending governance meetings can be rational
pilot costs. They are not production savings. Separate them from the
steady-state workflow so leadership knows which costs disappear at scale,
which become permanent supervision, and which were simply the price of
learning.

## 12.6 Pilot economics: price the learning honestly

An agentic pilot has three economic lines that should never be blended.
**Build cost** covers integration, configuration, corpus preparation and
security testing. **Run cost** covers inference, retrieval, tool calls,
monitoring and human supervision for each case. **Learning cost** covers
labeling, parallel processing, sampled audit and the time leaders spend
at gates. The first and third may be high during a pilot and fall later;
the second is the input to a scale decision. Reporting only a single
"pilot cost" makes it impossible to see whether the workflow will
improve with volume or merely move labour into an invisible control
room.

Calculate the unit case before and after assistance. On the old path,
include officer time, rework, queue delay where it creates a measured
business cost, and any external service cost. On the assisted path,
include the human supervisor's time, model and retrieval consumption,
tool charges, quality sampling, incident provision and the share of
platform cost that will persist at scale. Then show a range: base case,
conservative case (lower adoption, higher overrides, more expensive
models) and stress case (fallback active for a defined period). The
decision is robust when the workflow remains worthwhile in the
conservative case, not only in the vendor's best case.

Do not manufacture statistical certainty from a small sample. Segment
the test cases, disclose their composition and report confidence bounds
or simply label the result directional when the sample cannot support a
precise claim. The executive question is practical: *what would we need
to observe in the next stage before committing public funds?* The answer
may be a larger representative sample, a different document class, or
a proof that human-review capacity will not become the new bottleneck.
In each case, the pilot has done its job by narrowing a real decision.

**A simple investment gate:** approve scale only when the conservative
unit-economics case, the quality/safety thresholds and the operational
capacity plan all pass together. A positive ROI with an unaffordable
supervisory queue is not a business case; a safe agent with no path to
recurring value is not a product.

## 12.7 Design the sample for the decision you need to make

The pilot sample is part of the governance design. A clean convenience
sample may show that a model can read documents; it cannot show whether a
workflow will improve a live queue. Define strata before collection:
document type and quality, language, commodity or risk family, channel,
case complexity, source-system variation, time of day or peak period,
and the exceptions that create the most officer work. Include routine
cases to measure capacity and difficult cases to test boundaries. State
which population the pilot will and will not support.

Use parallel processing where possible. Let the normal process decide
the live case while the pilot produces a sealed recommendation and
trajectory. Compare after the decision, with reviewers blinded to vendor
or configuration where practical. Record not only whether the output was
right, but whether its evidence was complete, whether the human could
act on it in time, and what would have happened if the system had been
wrong. This makes the pilot a test of the whole case loop rather than a
test of text quality.

Stop rules should be as clear as pass rules. A material security breach,
authority violation, unsafe segment outcome, unmanageable reviewer queue
or repeated inability to reproduce a result stops progression even if an
average metric looks attractive. The programme can revise the scope,
fix the condition and run another bounded test. What it must not do is
average a known unsafe condition into a positive pilot headline.

## Decision Toolkit — Chapter 12

**The pilot charter** (two pages, signed before start): the named
decision · the task and its mandate reference · lawful basis for pilot
data · stages and their durations · gate criteria with numbers (drawn
from the catalog) · demotion/stop criteria · the gate-review panel
(operations, finance, legal, program) · what happens on pass, on fail,
and on ambiguity (extend once, with a named reason — twice is
purgatory).

**The three questions that kill demo-pilots** (ask at charter review):
What decision does this pilot inform? What result would make us say no?
Who has agreed to act on the answer?

**The evidence file** (the pilot's real deliverable): baseline
measurements · stage results against every gate · correction taxonomy ·
security and governance artifacts · the panel's decision memo. This
file is the "on evidence" in "climb on evidence" — and the template for
every subsequent rung.

**The pilot ledger** (one row per case): baseline and assisted path ·
segment · recommendation and evidence · officer decision and override ·
tool trajectory · elapsed time · cost · final outcome. Pre-register the
success threshold and keep pilot-learning costs separate from steady-state
unit economics.

## Key Takeaways

- A pilot is an evidence factory for a decision named in advance; a
 pilot that cannot fail is a demo, and pilot purgatory is a design
 defect — the gates are the exit, in both directions.
- Three stages by what's at risk: shadow mode (your traffic, zero
 touch), supervised operation (override rates, unit cost, trust
 calibration), gated autonomy expansion (by slice, with live demotion
 criteria).
- Probabilistic systems need probabilistic gates: operational
 precision/recall, consistency across repeated trials, sequence
 robustness, cost-curve position, human factors, and security and
 governance artifacts — judged on your traffic and your officers, not
 simulated ones.
- Give every constituency a gate it co-wrote; hold the review with all
 of them in the room.
- Publicize outcomes that passed gates, not launches — the field's
 verified numbers came from programs that measured for years before
 they spoke.
- Preserve a case-level pilot ledger and pre-register the scorecard. The
  conclusion must survive segmentation, officer overrides and the real
  cost of supervision—not only a polished aggregate accuracy number.

---

## Endnotes

[^ch12-1]: The three-step pilot pattern (data collection and preparation →
 model training → monitored deployment) per the WCO Smart Customs
 report (Mar 2025), Fig. 5; this chapter's stages re-cut the pattern
 by exposure rather than by engineering phase. <!-- bib:
 wco_scp_report2025 -->

[^ch12-2]: Reliability as consistency across n independent trials (the
 k^n metric) per τ-bench (Yao et al., 2024); state-dependent
 sequential workflows where early errors propagate per its
 successors.
 <!-- bib: yao2024_taubench -->

[^ch12-3]: Holistic Agent Leaderboard (arXiv 2510.11977): accuracy reported
 against USD cost on a Pareto frontier; higher spend does not
 guarantee higher accuracy (56.0% at USD 42.11 vs 54.0% at
 USD 180.49 on a 50-task set). <!-- bib: hal2025 -->

[^ch12-4]: LLM-simulated users as unreliable proxies for real humans in
 agentic evaluation ("Lost in Simulation," arXiv 2601.17087); the
 LITE-DATE recall/precision figures are a synthetic-benchmark result,
 not a deployment outcome.
 <!-- bib: lostinsimulation2026, date_kdd2020 -->

[^ch12-5]: Chapter 15's cautionary register: minister-hedged launch-week
 accuracy claims and untraceable secondary figures are contrasted with
 the primary-sourced Korea program (WCO News 108). <!-- bib:
 wconews108_korea, antara2025_tradeai, gulfnews2026_dubai -->

[^ch12-6]: Production-failure evidence: Gartner (25 Jun 2025) on >40% of
 agentic AI projects cancelled by end 2027 (cost, unclear value,
 inadequate risk controls); agent-security incident prevalence from
 2026 industry surveys spanning a ~47–88% range depending on sample
 and method (e.g., CSA/Token survey, N=418, ~65% reporting an incident
 and ~82% shadow agents) — cited as a range, never a single figure as
 fact. Cross-industry data, cited as directional reinforcement of
 staged-gate discipline, not a customs outcome. <!-- bib:
 gartner_agentic_cancel2027, agent_security_survey2026 -->

[^ch12-7]: WCO Smart Customs Project, *Detailed Report on the Adoption of
AI and ML in Customs* (2025), identifies cost-benefit analysis and
piloting as implementation requirements. This chapter's ledger extends
the baseline for agents: retain the action trajectory, officer response
and unit cost needed to explain a result as well as score it.
<!-- bib: wco_scp_report2025 -->
