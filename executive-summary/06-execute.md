---
title: "Pilot, Production, and People"
---

## Pilot the operating system

A useful pilot tests more than whether a model can produce an answer. It
tests whether the administration can supply lawful evidence, operate the
human gate, observe behaviour, absorb exceptions, control cost, respond to
failure, and decide against its own enthusiasm.

![Figure 6.1 — Piloting in Stages](/assets/diagrams/fig-ch12-pilot-stages.svg){width=100% height=72%}

Use four stages.

**Design and offline evaluation.** Map the current workflow and baseline.
Define the task, mandate, autonomy ceiling, agency profile, affected
people, failure modes, test strata, thresholds, and fallback. Evaluate on
buyer-controlled data with repeated trials and a failure taxonomy.

**Shadow mode.** Run against real or authorised representative traffic
without affecting outcomes. Compare with the current path. Measure
consistency, evidence quality, abstention, overrides, latency, unit cost,
security, and the exception queue.

**Controlled live pilot.** Allow a narrow user group, limited volume, and
reversible actions. Staff the human route as production work. Exercise
freeze, evidence preservation, containment, communication, and fallback.

**Limited production.** Approve only the tested mandate. Canary material
changes, retain a holdout, sample trajectories, and publish a gate memo:
promote, hold/tune, demote, or stop.

## Reliability compounds across steps

Single-shot accuracy disguises workflow risk. If five dependent steps each
succeed 95 percent of the time, the probability of an error-free chain is
about 77 percent before correlations and adversarial conditions. Measure
complete-case success, state transitions, retries, loops, tool errors,
incorrect writes, and escalation—not only the final text.

Repeat identical and equivalent cases. Generative systems are stochastic;
a result that passes once may fail under another run, model release, prompt,
corpus, or tool state. Pre-commit the number of trials and acceptance rule.

## The production control room

Join six views around the task: volume/service · quality/overrides · tools
and trajectories · security/incidents · unit economics · mandate and
owner. The meeting ends in a decision, not a dashboard: continue, tune,
hold, demote, expand, compete, or retire.

Govern four change classes at minimum—model, prompt/policy, corpus, and
tool list—and extend the register to identities, connectors, region,
workflow, and critical dependencies. Every material change carries owner,
test, canary/shadow path, communication, evidence-room update, rollback,
and re-authorisation decision.

The second use case is the platform test. It should reuse identity,
logging, evaluation, security, evidence, deployment, procurement, and
control-room components. If almost nothing transfers, the first project
built an implementation, not an institutional capability.

## The workforce does not disappear

The officer role shifts with the ladder: Operator, Pilot, Supervisor,
Governor. Higher autonomy usually reduces routine touches but increases
exception complexity, calibration, sampling, incident work, and the need
for people able to challenge both system and policy.

Use a hub-and-spoke model: a central AI/data team owns shared engineering,
evaluation, security patterns, and standards; officer-analysts in
operational units own domain meaning, exceptions, feedback, adoption, and
service outcomes. Pair them. A central team without operations builds
generic tools; isolated units duplicate platforms and controls.

![Figure 6.2 — Hub and Spoke](/assets/diagrams/fig-ch14-hub-and-spoke.svg){width=100% height=70%}

Train by role. Users learn evidence limits, uncertainty, secure handling,
and correction. Supervisors learn queue management, sampling, trajectory
review, demotion, and incident escalation. Owners learn mandate and
residual-risk decisions. Procurement/legal learn agent definition, agency,
evaluation, change, audit, and exit. Engineers learn hostile content,
identity, observability, and reproducible release evidence.

## Capacity is a control

Set the authorised task volume against staffed review capacity. A system
that creates exceptions faster than qualified people can resolve them has
exceeded its safe operating envelope even if model metrics remain stable.
Define maximum queue length and exception age, surge arrangements,
prioritisation, and automatic demotion or fallback.

The “silicon workforce” metaphor is useful only operationally: agents need
assignment, permissions, supervision, measurement, change control, and
retirement. It does not make software an employee, legal person, public
authority, or accountable actor.

## Scale gate

Scale only when the local record answers: value captured, not merely time
saved · quality stable across relevant strata · human route staffed ·
security exercises passed · lawful deployment unchanged · unit economics
inside range · evidence export works · fallback rehearsed · owner signs
residual risk. A successful demo is not on this list.

```{=latex}
\clearpage
\begin{ExecutiveToolPage}
```

## Core Tool E: Pilot gate template

Complete before every stage change. Use one task and one proposed rung per
gate.

| Gate field | Decision record |
|---|---|
| **Task, authority, baseline** | Task/owner: ____ · current to proposed rung/agency: ____ · baseline period: ____ · holdout/strata: ____ |
| **Value and quality** | Completed cases/conversion action/unit cost: ____ · complete-case success: ____ · abstention/override/burden: ____ |
| **Human route** | Reviewer: ____ · maximum queue/age: ____ · calibration: ____ · stop authority: ____ |
| **Security and sovereignty** | Hostile-content/tool tests: ____ · approved data path unchanged: yes/no · open finding: ____ |
| **Reliability and change** | Repeats/state transitions: ____ · release/change: ____ · rollback/demotion test: ____ |
| **Evidence and exit** | Trajectory/export: ____ · incident exercise: ____ · fallback: ____ · exit package: ____ |

**Threshold:** pass / conditional / fail · conditions/dates: ____ · residual
risk owner: ____ · evidence-room link: ____.

**Decision:** promote / hold and tune / demote or simplify / stop · authorised
volume/duration: ____ · automatic stop triggers: ____.

**Sign-off:** operations ____ · legal/privacy ____ · security ____ · data/IT
____ · accountable executive ____ · date ____ · next gate date ____.

```{=latex}
\end{ExecutiveToolPage}
```
