---
title: "Metrics Catalog for Pilots and Production"
part: "Appendices"
status: review
version: 0.3
last-updated: 2026-07-09
---

Catalog behind Chapter 12's gates and Chapter 13's SLOs. Per task,
charters select a subset and set numbers *before* the pilot starts.

Each entry: definition / how measured, then typical gate use.

**E1 — Operational precision.** Of N flags/outputs, share correct;
cost of the rest in officer time. *Gate:* Stage 2; policy-signed
trade-off with E2.

**E2 — Operational recall.** Of true cases, share caught; misses
stated as risk exposure. *Gate:* paired with E1; the business owner
signs the balance.

**E3 — Consistency (k^n-style).** Same task, n independent trials;
success across all. *Gate:* mandatory for L2+; dependability, not
brilliance.

**E4 — Sequence robustness.** State-dependent multi-step tests;
early-error propagation rate. *Gate:* L3 tasks; mirrors production
reality.

**E5 — Override rate + taxonomy.** Share of outputs corrected,
classified by reason. *Gate:* Stage 2 core; the taxonomy is the
improvement backlog.

**E6 — Calibrated trust.** Seeded known-wrong outputs; reviewer catch
rate. *Gate:* human-factor gate; anti-rubber-stamping.

**E7 — Adoption.** Unprompted use by week N. *Gate:* a passing pilot
with hostile users has failed.

**E8 — Unit cost.** Per-unit all-in (inference + platform + oversight
time) vs the Ch. 5 baseline, at pilot and projected volume. *Gate:*
finance gate; curve position, not point.

**E9 — Trajectory baseline.** Steps / tool calls / tokens per task;
drift bands. *Gate:* production SLO; behavior and cost signal in one.

**E10 — Time-to-resolution.** End-to-end task latency vs baseline.
*Gate:* facilitation-channel value evidence.

**E11 — Injection robustness.** Attack success at 1/10/100 attempts,
document-embedded, production configuration. *Gate:* security gate
(Ch. 10); acceptance criterion.

**E12 — Governance artifacts.** Tier evidence produced, sampled,
readable by a non-builder. *Gate:* gate + standing audit.

**E13 — Incident & demotion.** Count; time-to-demotion when
triggered. *Gate:* "handled well" is itself evidence (Ch. 12).

**E14 — Grounding rate.** Share of answers with a retrievable
citation; "no grounded answer" rate. *Gate:* Rung-2 assistants; the
citation is the verification.

**E15 — Evidence completeness.** Share of agent-prepared cases that
contain every mandatory source, provenance tag and current version
required for the task. *Gate:* case-preparation and L3 pilots; a fast
incomplete file is not facilitation.

**E16 — Recommendation-to-action conversion.** Recommendations accepted
by an officer, then acted on within the service clock, divided by all
recommendations issued. *Gate:* value-capture test (Ch. 5); separates a
useful output from a busy dashboard.

**E17 — Exception leakage.** Cases that leave the intended workflow or
miss their escalation clock, divided by total cases. *Gate:* L2+ service
workflows; exposes bottlenecks moved rather than removed by the agent.

**E18 — Segment parity.** E1, E2, E5 and E10 reported by language,
document type, commodity family, channel and other lawful risk segments.
*Gate:* fairness and operational-safety review; averages do not clear a
rare but consequential segment.

**E19 — Tool-authority utilisation.** Tool calls actually needed for a
completed task versus permissions granted. *Gate:* quarterly least-
agency review; unused write authority is removed, not retained for
convenience.

**E20 — Cost-to-quality frontier.** Pareto view of E1/E2/E10 against E8
at the same task and volume. *Gate:* procurement and scale decision;
compare configurations, not model-brand claims.

**E21 — Time to containment.** Time from anomaly detection to credential
revocation, task freeze and fallback activation. *Gate:* incident
exercise and production SLO; this measures whether demotion is real.

**E22 — Knowledge freshness.** Share of retrieved sources within their
approved validity window, plus superseded-document retrieval rate.
*Gate:* regulation, ruling and procedure assistants; an accurate answer
to an obsolete rule is operationally wrong.

**E23 — Evidence-to-decision latency.** Time from case arrival to a
complete, cited case file available to the accountable officer. *Gate:*
case-preparation value; separates faster text generation from a faster
decision.

**E24 — Fallback service level.** Completion time and quality while the
agent is deliberately unavailable and the human/rules fallback runs.
*Gate:* resilience exercise; a fallback that has never carried real
traffic is only a diagram.

**E25 — Mandate conformance.** Share of trajectories whose inputs,
tools, outputs and escalation route remain inside the active mandate.
*Gate:* weekly L2+ control; any material breach freezes the task pending
review.

**E26 — Reviewer workload.** Median and upper-range minutes of human
review per completed case, plus exceptions arriving per available
supervisor hour. *Gate:* scale decision; protects against a queue that
forces rubber-stamping.

**E27 — Review reversals.** Decisions changed after an internal review,
complaint or appeal, segmented by agent-assisted versus baseline path
where lawful and meaningful. *Gate:* contestability and fairness;
interpret with counsel, not as a standalone model score.

**E28 — Data-contract health.** Availability, freshness, critical-field
completeness and conflict rate for each feed used by the task. *Gate:*
authority control; a failing feed removes the permissions that depended
on it.

**E29 — Release regression rate.** Material quality, safety, cost or
mandate-control regressions discovered in canary or after release,
divided by releases. *Gate:* change-control maturity; trending down is
useful only if testing coverage is not being reduced.

**E30 — Benefit-realisation lag.** Time between a valid recommendation
and the operational action that captures its value. *Gate:* portfolio
management; reveals whether value is delayed in a downstream queue.

### Cadence and ownership

Report E1–E8 at every pilot gate; E9–E14 weekly in production; E15–E22
monthly to the task owner and quarterly to the AI portfolio board.
Every metric has a named owner, threshold, action and evidence location.
A metric without an action is telemetry, not governance; a threshold
without a named decision-maker is a decorative dashboard.

Rules: metrics are judged on the administration's traffic, officers,
and documents — simulated results are design tools, not verdicts;
synthetic-benchmark numbers are never quoted as operational outcomes.

### Metric-card template

Do not place a metric on a dashboard until its task owner can complete
this card. The aim is to make a number actionable rather than merely
available.

| Field | Required entry |
|---|---|
| Metric and decision | Which E-number; what decision it informs (continue, tune, demote, scale, fund)? |
| Task and population | Mandate card, case strata, inclusion/exclusion and period |
| Formula | Numerator, denominator, treatment of abstentions, missing data and duplicate cases |
| Baseline and target | Baseline period; pre-committed threshold; expected range; why it is appropriate |
| Owner and audience | Named data owner; accountable decision maker; operational, weekly or board audience |
| Evidence location | Query, trajectory sample, source system and retention location |
| Action rule | What happens on amber, red, missing data or a material segment difference |
| Review and change | Cadence; change-control route; when the metric is retired or recalibrated |

### Gate packs by autonomy level

Select fewer metrics and use them well. A long dashboard without an
action path is a reporting burden. The following packs are starting
points; local law and task risk may require more.

| Task posture | Minimum gate pack | Scale questions |
|---|---|---|
| R1 document intelligence | E1, E5, E8, E10, E15; document-type segments | Is extracted evidence complete enough to reduce rework, and does correction time fall? |
| R2 grounded assistant | E3, E5, E6, E7, E8, E14, E18, E22, E23 | Are officers adopting it with calibrated trust, and are sources current and retrievable? |
| R3 supervised agent | E3, E4, E5, E8, E9, E11–E13, E15–E21, E24–E29 | Does the task remain inside mandate, supervision capacity and cost/safety thresholds under real variation? |
| Trader-facing or rights-sensitive | Above relevant pack + E18, E27, explanation/review service level | Can affected parties obtain meaningful review and do outcomes differ across lawful segments? |

### Interpreting patterns, not isolated numbers

Some metric combinations carry more meaning than individual results.
High precision with falling recall may mean an agent is avoiding hard
cases; high adoption with weak E6 reviewer catch rate may signal
over-trust; falling unit cost with rising E17 exception leakage may mean
the bottleneck moved downstream. A low override rate can indicate a good
system, passive reviewers or an interface that makes correction hard.
Always pair E5 with correction reasons and a sampled review of accepted
cases.

For cost, chart E8 beside E1/E2/E10/E26, not alone. A configuration that
is slightly more expensive but reduces supervisor minutes and preserves
quality may be the right operating choice. For security, chart E11,
E19, E21 and E25 together: an agent with fewer attacks observed may
have been exposed to fewer hostile documents, or logging may have become
weaker. The control room must see the context before it changes a rung
or declares savings.

### Threshold-setting rules

Set thresholds from baseline, task harm and supervisory capacity—not by
copying a benchmark. For a new workflow, begin with a conservative
pilot band, collect enough representative cases to understand variance,
then ask the accountable owner to sign the production band. Define three
states: **green** (continue), **amber** (investigate or narrow), **red**
(hold or demote). A red threshold must name the immediate action and the
role authorised to take it.

Never average away a critical segment. A task can be green overall and
red for a language, commodity family, document type or queue condition
that matters operationally. Likewise, do not set a threshold that no
one can measure on the service clock. If a metric requires a quarterly
manual study, it cannot be the only trigger for a same-day safety
decision; pair it with a leading signal from trajectories or queue
telemetry.

### A monthly task review page

For each live task, prepare a one-page review that includes: current
mandate/rung and change since last month; volume and service result;
quality and grounding; override and feedback pattern; human workload;
unit cost versus budget; data-contract health; security and incident
signals; open findings; and a proposed decision. The accountable owner
signs one of six outcomes: continue, tune, narrow, expand to a defined
new population, hold, or demote. Preserve the page in the evidence room.
This discipline is how a portfolio board sees value, safety and cost
together. It avoids the two failure modes of AI reporting: the technical
dashboard that omits public accountability, and the executive dashboard
that omits the evidence needed to believe it.
