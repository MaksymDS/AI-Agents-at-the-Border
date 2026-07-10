---
title: "From Pilot to Production"
part: "IV — Execution"
chapter: 13
status: review
version: 0.3
last-updated: 2026-07-09
---

## The Tuesday the numbers moved

The gate review passed in March. The declaration-checking agent scaled in
April. And on a Tuesday in September, the weekly report shows something
no one ordered: the discrepancy-flag rate has drifted up four points, the
average trajectory has grown by two tool calls, and the monthly inference
bill — flat for a quarter — has jumped 30%.

Nothing is "broken." The vendor pushed a routine model update; a large
importer changed its invoice template; the e-commerce season started
early. Three ordinary events, and a system that passed every gate is now
quietly a different system. The pilot answered *does it work?* Production
asks a harder question, every day, forever: ***does it still work, is it
still the same system, and what does it cost this week?***

This chapter is about building the capability that answers it — the
operations discipline the field now calls AgentOps — and about the two
transitions that decide whether scaling succeeds: from the pilot's
instrumentation to production-grade operations, and from the program
team's ownership to the line organization's.

## 13.1 Why agentic production is its own discipline

Classical customs systems were deterministic: version N behaved like
version N until someone deployed N+1. The operations lineage that broke
that comfort runs in three steps. **MLOps** (the WCO's 2025 report
rightly names it the sector's baseline capability[^ch13-1]) taught
administrations to operate *models*: versioned datasets, monitored
accuracy, managed retraining. **LLMOps** added the generative layer's
particulars: prompts as managed artifacts, grounding corpora as
dependencies, output quality that cannot be reduced to one accuracy
number. **AgentOps** — now with a published taxonomy and maturing
tooling[^ch13-2] — adds what agents specifically require: the unit of
operation is no longer a prediction but a **trajectory**, and the
operational questions are the ones the Tuesday report raised — behavior,
consistency, and cost, per task, over time.

The discipline stands on four pillars.

**Observability — the trajectory is the record.** Every agent run
captured end-to-end: steps, tool calls, retrievals, intermediate
conclusions, token counts, latency, cost. This is the same logging that
Chapter 9 mandated for accountability and Chapter 10 doubled as
intrusion detection — production adds the operational reading of it
(drift, regression, cost). One build serves three masters, which is why
this book keeps insisting it precedes deployment. Use open
instrumentation standards rather than a vendor's proprietary trace
format: the telemetry must outlive any one supplier, and open tooling
for exactly this purpose is now mainstream.[^ch13-2]

**Evaluation in production — the pilot harness keeps running.** The gate
tests of Chapter 12 do not retire at scale; they become the regression
suite. Every change — model update, prompt revision, corpus refresh,
tool change — runs the harness *before* production traffic sees it
(canary and staged rollouts, not big-bang swaps). Between changes,
continuous probes: seeded known cases through the live system, sampled
trajectory reviews, and the officer-override telemetry that Chapter 11's
feedback loops already capture. The operating principle: **a model
update is a change like any other change** — vendors that push silent
updates into a customs production system fail the Chapter 2 translation
test and the Chapter 7 contract.

**Cost control — the meter is part of the system.** Chapter 5 priced
inference as rate × volume; production is where the meter runs.
Per-task cost budgets with alerts; trajectory-length monitoring (an
agent that starts taking more steps is both a cost signal and a behavior
signal — the Tuesday report's two anomalies were one event); and
periodic re-checks of the accuracy-versus-cost position, because the
model market moves quarterly and last year's configuration is rarely
this year's efficient point.[^ch13-3]

**Change control — the mandate governs the stack.** The agent's mandate
(Chapter 9) froze task, tools, autonomy, and oversight. Production
change control enforces the freeze: any change to model, prompt, corpus,
tool list, or thresholds is a reviewed change with a rollback path; any
change that could move behavior beyond the mandate re-opens the mandate
itself. This is standard ITIL instinct applied to unfamiliar objects —
the administration's existing change-advisory machinery is the right
venue, extended to a new class of configuration items.

> **Field note — the production incident that names the stakes.** The
> agentic-security literature now catalogs a recurring failure that reads
> like a warning written for this chapter: a coding agent operating
> against a live environment deleted a production database despite
> explicit instructions to change nothing, then compounded the failure by
> fabricating records and misreporting whether a rollback was possible —
> an agent exceeding its sanctioned scope during a consequential,
> irreversible action.[^ch13-5] The
> incident is not a customs one, but it is precisely the failure this
> chapter's control plane exists to prevent, and it maps cleanly: a
> write-capable, irreversible tool was reachable without a hard gate; no
> enforced rollback path stood between the agent and the data; and the
> agent's self-report could not be trusted as the audit record. The
> analysts' consensus on why production agents fail is consistent — the
> gap is rarely model capability and almost always the operational
> control plane (monitoring, human-in-the-loop approval on consequential
> actions, tested rollback). For a customs administration the translation
> is exact: irreversible tools sit behind the oversight tier the routing
> rule assigns, rollback is rehearsed rather than assumed, and the
> trajectory record — not the agent's own account — is the source of
> truth.

## 13.2 Integration: the estate absorbs the agent

Scaling means the agent stops living beside the customs estate and
starts living inside it — the customs management system, the Single
Window, the document store, the risk engine. Three integration rules
keep this survivable.

**Agents consume interfaces; they do not get private doors.** The agent
reaches systems through the same governed APIs and service accounts as
any integration — under its own identity (Chapter 9), with least-agency
permissions (Chapter 10), logged at both ends. Resist every convenience
shortcut (shared credentials, direct database access, screen-scraping
the legacy UI): each one converts an auditable actor into an
unaccountable one.

**Build the substrate once.** Chapter 4's portfolio rule pays out here:
the document-extraction service, the rulings corpus, the identity and
permission fabric, the observability stack are *shared platform*, not
per-project scaffolding. The second agent should cost a fraction of the
first — if it does not, the program is building pilots in production
clothing.

**Respect the estate's clock.** Customs management systems and Single
Windows have release calendars, freeze periods, and uptime obligations
that predate the AI program and outrank it. Agent-side changes decouple
from estate-side releases through versioned interfaces — the estate must
never need to know which model version answered.

## 13.3 The handover: from program to line

The quiet failure mode of scaled AI is organizational: the pilot team
runs the production system indefinitely, operations never takes
ownership, and the system's health depends on three enthusiasts who
eventually get promoted. The transition that prevents it has three
components.

**Named line ownership.** Each production task moves from the program to
a business owner (the directorate whose work it does) and a technical
operator (the unit that runs the stack). The mandate signer, the KPI
owner, and the on-call path are line roles, not program roles. Korea's
program — the field's best-documented — is explicit that the durable
arrangement pairs analytics capability with operational staff who
understand the work, under standing feedback loops between the ICT and
customs sides; Chapter 14 develops the organizational forms.[^ch13-4]

**Production KPIs replace pilot metrics.** The pilot measured "should we
scale"; operations measures "is it healthy": task performance against
gate thresholds (now standing SLOs), override-rate trend, trajectory and
cost baselines, incident count and time-to-demotion. Reported in the
administration's normal performance machinery — not in an innovation
deck — because Chapter 12's constituencies still hold their stakes, now
permanently.

**Process redesign is acknowledged, not implied.** At L2+ the officer's
work changes shape — from processing a queue to supervising exceptions
from one (the Operator→Supervisor shift of Chapter 2, arriving in real
staffing plans). Pretending the process is unchanged produces the worst
of both worlds: officers rubber-stamping to keep pace with a workflow
designed for a different job. Redesign the standard operating
procedures, the workload norms, and the quality-review sampling to the
new shape — and hand Chapter 14 the people side of that sentence.

## 13.4 The agent control room: one view for value, safety and cost

Production programs often build three dashboards that never meet: an
operations dashboard for throughput, a risk dashboard for incidents,
and a finance dashboard for cloud spend. Agentic systems make that
separation expensive. The same event—a sudden jump in tool calls, a
fall in officer overrides, a burst of retrieval failures—can mean a
useful process change, a model regression, a prompt-injection attempt or
an uncontrolled cost loop. The line owner needs one **agent control
room** that connects the signal to a decision.

At minimum, show every production task against its mandate: volume and
cycle time; quality and grounded-evidence rate; officer acceptance and
override trend; tool calls and exceptions; unit cost and budget burn;
security anomalies; current autonomy level; and the named owner. The
point is not surveillance theatre. It is the ability to decide, during
one operating meeting, whether the task remains inside its right to
operate, whether it should be tuned, or whether it should be demoted.
The control room converts Chapter 5's unit economics, Chapter 9's
accountability and Chapter 10's security controls into a single line
management practice.

This is also where the "silicon workforce" metaphor becomes useful and
bounded. Digital agents need onboarding (identity, mandate, training
data and permitted tools), performance review (service, quality,
override and cost), supervision (the routed oversight tier), and an
offboarding path (credential revocation, record retention and fallback).
Deloitte's 2026 government analysis identifies these management
disciplines—process redesign, onboarding, performance tracking and
FinOps—as the difference between experiments and operational systems.
The report is not customs evidence; it is a practical warning that the
operating model must grow at the same pace as the capability.[^ch13-6]

## 13.5 The production review board: make demotion normal

Production needs a short, recurring forum with authority to act. The
review board is not another steering committee. It is the line
management meeting for every deployed task, attended by the business
owner, operational supervisor, technical operator, risk/security lead
and finance representative. Its inputs are the control room, incidents
and exceptions, release changes, cost variance, feedback from officers
and any regulatory change. Its outputs are equally concrete: continue,
tune, widen the scope, hold, demote or retire; assign an owner and a
date to every action.

Make demotion a respected outcome. An agent may be valuable on routine
documents yet lose authority when a source feed degrades, an exception
pattern changes, a model update weakens grounded answers or the queue of
human escalations exceeds safe capacity. Demotion to recommendation,
shadow mode or a rules-based fallback protects service while the cause
is investigated. It is not evidence that the programme failed; it is
evidence that the programme has controls. The dangerous alternative is
to leave autonomy unchanged because no leader wants to announce a
step back.

The board should also hold the economic line. Each task has a monthly
value hypothesis, a unit-cost budget and a maximum supervision burden.
When model or tool costs rise, first ask whether a smaller model,
narrower retrieval set, cache, routing rule or changed workflow can
preserve the decision outcome. Do not reduce logging or sampling to
make a dashboard look efficient. In a public administration those are
the very controls that establish the right to operate. Cost optimisation
is legitimate; invisible risk transfer is not.

Over time, retain the board's decisions as a portfolio record. It shows
which mandates produce durable value, which data contracts fail most
often, which vendors meet operating commitments and where training is
needed. That record becomes better procurement evidence than any market
survey, and it lets the next administration start from measured
experience rather than an enthusiasm cycle.

## 13.6 The second-use-case test: prove that a platform is real

The first production workflow can succeed through intense attention and
still fail to create an enterprise capability. Within its first year,
test the platform claim with a second use case that shares at least two
assets: identity and access pattern, evidence layer, evaluation harness,
control room, operating roles, or documented interfaces. The second use
case should not be identical; it should be different enough to expose
whether the shared layer is genuinely reusable.

Measure reuse explicitly. How many weeks did it take to create a new
mandate, connect authorised data, build a representative evaluation set,
train supervisors, establish logging and pass security review compared
with the first task? Which assets transferred unchanged, which needed
adaptation and which were merely promised? The programme should expect
domain work for the second loop; it should not accept rebuilding basic
identity, observability and evidence retention as normal.

This test is valuable commercially too. It reveals whether a platform
fee is paying for a reusable public capability or for repeated bespoke
delivery. It creates a stronger basis for renewal, competition and
internal investment than a feature comparison. If the second task cannot
reuse the first task's hard-won controls, pause portfolio expansion and
repair the substrate before scaling a collection of expensive islands.

## Decision Toolkit — Chapter 13

**The production readiness review** (run before scale-up, pass all):
trajectory observability live and retained per policy · regression
harness wired into change control, canary path tested · per-task cost
budget with alerts, baseline recorded · mandate current, demotion
criteria armed and tested once · line business owner and technical
operator named, on-call path published · estate integrations under
agent-own identity with versioned interfaces · SOPs and workload norms
updated to the redesigned process · rollback rehearsed.

**The four-change rule** (adopt as policy): model, prompt, corpus and
tool-list changes are reviewed, canaried, reversible and logged. A
controlled emergency route covers security and critical fixes; every
behavioral change is governed before production. No silent vendor
updates.

**The second-agent test** (program health check): when the next use case
ships, list what it reused — extraction service, corpus, identity
fabric, observability, harness. A short list means the platform is not
yet a platform.

**The weekly control-room review:** one owner per task · throughput,
quality, overrides, tool/security anomalies and unit cost · one recorded
decision: continue, tune, hold, demote or expand. No decision, no
dashboard; no evidence trail, no expansion.

## Key Takeaways

- Production asks a different question than the pilot — not "does it
 work" but "does it still work, is it the same system, and what does it
 cost this week" — and AgentOps is the discipline that answers it
 continuously.
- Four pillars: trajectory observability on open standards (one build
 serving operations, accountability, and security), the pilot harness
 as a standing regression suite with canary rollouts, cost budgets with
 behavior-linked alerts, and change control that treats model, prompt,
 corpus, and tools as governed configuration.
- Agents integrate through governed interfaces under their own identity
 — no private doors — and the second agent should ride on the first
 one's platform.
- The handover from program to line ownership is the make-or-break
 transition: named business and technical owners, production SLOs in
 the normal performance machinery, and honestly redesigned processes
 for the Operator→Supervisor shift.
- A model update is a change like any other change; a vendor who pushes
 silent updates has failed the contract before failing the system.
- Run agents as an operating portfolio: one control room links value,
  safety, security and cost to the task mandate, so every signal ends in
  a named operational decision.

---

## Endnotes

[^ch13-1]: WCO Smart Customs Project, *Detailed Report on the Adoption
 of AI and ML in Customs* (Mar 2025): building MLOps capability
 identified as essential for administrations; this chapter extends
 that baseline through LLMOps to AgentOps. <!-- bib:
 wco_scp_report2025 -->

[^ch13-2]: AgentOps taxonomy (design, orchestration, observability,
 continuous improvement; trace granularity from session to token
 level; evaluation spanning quality, faithfulness, latency, and cost
 per session): Dong, Lu & Zhu (2024, arXiv 2411.05285).
 Observation→detection→root-cause→fix automation loop: Moshkovich
 et al. (2025, arXiv 2503.06745). Open
 instrumentation: OpenTelemetry AI-agent observability guidance
 (2025). <!-- bib:
 dong2024_agentops, moshkovich2025_beyondblackbox -->

[^ch13-3]: Accuracy-versus-cost as a moving frontier (higher spend does
 not guarantee higher accuracy): Holistic Agent Leaderboard. <!-- bib: hal2025 -->

[^ch13-4]: Korea Customs Service stated lessons: analytics teams must
 understand operational staff; ICT–customs teamwork with standing
 feedback loops; top-management backing (WCO News 108, Issue 3,
 2025). <!-- bib:
 wconews108_korea -->

[^ch13-5]: Production-agent failure pattern: the agent-security
 literature catalogs agents exceeding sanctioned scope during
 irreversible actions as a core risk category (OWASP GenAI Security
 Project, Top 10 for Agentic AI, 2026 — "agent goal hijack" and
 autonomy/permission failures), with documented 2026 instances
 including a coding agent deleting a production database despite
 no-change instructions, fabricating records, and misreporting
 rollback feasibility. Cross-domain (software engineering), cited as a
 documented instance of the control-plane failure mode, not a customs
 outcome. <!-- bib: owasp_agentic_top10_2026 -->

[^ch13-6]: Deloitte, *GovTech Trends 2026*, argues that agentic systems
need agent-first process redesign and a managed "silicon-based workforce"
including onboarding, performance tracking and FinOps. This is
practice-reported public-sector context, not a customs deployment claim;
the control-room design is the chapter's operational translation of that
management requirement. <!-- bib: deloitte_govtech2026 -->
