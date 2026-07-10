---
title: "Glossary"
part: "Appendices"
status: review
version: 0.4
last-updated: 2026-07-10
---

Terms as fixed by the book's terminology conventions and the
chapters cited.

- **AI agent** — a software system that pursues an assigned goal by
 planning multi-step work and using tools, with a defined degree of
 autonomy and under defined human oversight (Ch. 2; RFP-verbatim).
- **Autonomy Ladder** — L1 Assistant · L2 Copilot · L3 Supervised
 Agent · L4 Autonomous Agent; human roles Operator · Pilot ·
 Supervisor · Governor (Ch. 2).
- **Agency (vs autonomy)** — the capability implied by an agent's tool
 set, granted independently of its autonomy (Ch. 9).
- **Autonomy ceiling** — the highest rung a task may justify in
 principle; an entry discipline, not a verdict (Ch. 4).
- **Accountability strip** — the design principle that operational
 decisions may transfer to an agent within mandate; accountability
 never transfers (Chs. 2, 9; Fig. 2.1).
- **Mandate** — the signed two-page delegation for an L3/L4 task:
 boundaries, tools, oversight tier, escalation, demotion criteria,
 named signer (Ch. 9).
- **Maturity Ladder** — Document Intelligence → GenAI Assistants → AI
 Agents; a dependency chain, not a menu (Ch. 3).
- **Document intelligence** — OCR + extraction + classification +
 search over customs documents; Rung 1 (Ch. 3).
- **Grounding** — answers carry the retrievable source passage; no
 source, no answer (Ch. 3).
- **Sovereign deployment** — on-premises or accredited
 government/enterprise cloud under national jurisdiction (Ch. 3).
- **Excluded territory** — consumer subscriptions and unvetted
 third-party APIs for customs data (Ch. 3).
- **HITL / HOTL / HIC** — human-in-the-loop (approves each
 consequential action) / human-on-the-loop (monitors, can intervene) /
 human-in-command (sets mandates, audits outcomes) (Ch. 9).
- **Oversight routing (OCM-style)** — deterministic assignment of tasks
 to oversight tiers by regulatory impact, affected-party proximity,
 reversibility, data sensitivity (Ch. 9).
- **Trajectory** — the full recorded path of an agent's steps, tool
 calls, and intermediate conclusions; the unit of oversight, audit,
 security detection, and operations (Chs. 9, 10, 13).
- **Hostile paper** — trader-supplied documents treated as adversarial
 input by design; indirect prompt injection's normal channel in
 customs (Ch. 10).
- **Four-change rule** — model, prompt, corpus, and tool-list changes
 are governed production changes; no silent updates (Ch. 13).
- **Second-agent test** — the next use case should ride on the first
 one's platform; a short reuse list means no platform (Ch. 13).
- **Hub-and-spoke** — central analytics team + officer-analysts paired
 with domain experts in units; augment, never replace (Ch. 14).
- **Rung ceiling (readiness)** — per-dimension highest supportable
 Maturity-Ladder rung; the readiness output format (Ch. 6, App. A).
- **Marketing-claim discipline** — every figure recorded with who
 stated it and whether the technology is precisely identified; AI
 never credited with digitalization or hardware gains (research
 protocol; Chs. 1, 5, 15).
- **Legal cut-off** — the dated regulatory baseline used for publication;
 re-verify post-cut-off items against the calendar, not the page (Ch. 8).
- **Agent control room** — the operating view that joins task volume,
  quality, overrides, tool use, security anomalies, unit cost, current
  mandate and named owner; it ends in a decision to continue, tune,
  hold, demote or expand (Ch. 13).
- **AgentOps** — the production discipline for designing, observing,
  evaluating, changing and governing agentic workflows; the extension
  of MLOps and LLMOps when tools and actions enter the system (Ch. 13).
- **Bounded case loop** — a small, observable workflow in which an agent
  gathers authorised evidence, prepares a recommendation, passes a
  human gate and makes only a reversible approved write-back (Ch. 3).
- **Decision-grade evidence** — data accompanied by source, provenance,
  validity, permissible use and relationship to the task, so an officer
  can justify a decision rather than merely retrieve a record (Ch. 11).
- **Demotion** — reducing a task's authorised autonomy or suspending it
  when a threshold, incident, control failure or evidence gap is met;
  the opposite of silent tolerance for degradation (Chs. 9, 12, 13).
- **Evidence room** — the buyer-led final evaluation in which a vendor
  processes representative unseen cases, exports records, explains an
  adverse trajectory and demonstrates the first step of exit (App. C).
- **Exit rehearsal** — a controlled proof that data, trajectories,
  configuration, mappings and evaluation evidence can be exported and
  the workflow can fall back without vendor credentials (App. B).
- **Grey literature** — public reporting by consultancies, vendors or
  industry bodies. It may provide useful workflow patterns and named
  context but is labelled practice-reported and never upgraded to
  independent customs evidence (Ch. 15).
- **Safety case** — the evidence-backed argument that a specified task
  may operate at a specified autonomy level with stated residual risk,
  named owner, controls, rollback and review cycle (Ch. 9).
- **Value capture** — the conversion of a system output into an action
  that changes capacity, facilitation, revenue protection or control;
  an agent recommendation without a named conversion point has no
  established business value (Ch. 5).
- **Agent inventory** — the administration's current register of agentic
  tasks, their mandate cards, owner, current rung, tools, deployment,
  evidence location and review date; a list of models alone is not an
  inventory (Chs. 2, 13).
- **Authority boundary** — the hard line separating actions an agent is
  permitted to take from actions reserved to a human or rules engine;
  expressed in the mandate, identity scopes and workflow routing (Chs.
  2, 9, 10).
- **Canary release** — introduction of a governed change to a limited,
  monitored share of real work before wider deployment, with pre-set
  rollback thresholds (Chs. 10, 13).
- **Case loop** — the end-to-end movement from a signal or case arrival,
  through evidence and judgment, to action, record and feedback. It is
  the unit of operational redesign, not a model prompt (Chs. 1, 3, 4).
- **Contestability** — the practical ability to request a meaningful
  human review, understand the applicable procedure and have a wrong or
  incomplete outcome corrected (Ch. 9).
- **Corpus charter** — a one-page operating specification for a
  knowledge base: contents/exclusions, provenance, status metadata,
  retrieval granularity, update SLA, named custodian and review cadence
  (Ch. 11).
- **Data contract** — the agreed operating specification for a data feed:
  owner, permitted purpose, fields, freshness, quality, change notice,
  retention and escalation when the feed is unreliable (Ch. 11).
- **Demotion trigger** — a measurable threshold or event that reduces an
  agent's authorised scope or rung; examples include broken data
  contracts, injection success, unsafe queue length, material regression
  or a missing mandate (Chs. 9, 12, 13, 14).
- **Evidence grade** — the label attached to a claim: primary operating
  metric, primary qualitative evidence, peer-reviewed/official synthesis,
  practice-reported grey literature, or launch claim/anecdote (Ch. 15).
- **Evidence-to-decision latency** — the time from a case arriving to a
  complete, cited file being available to the accountable decision maker;
  unlike generation latency, it reflects usable operational value
  (App. E).
- **Fallback** — the pre-tested human or rules-based path that preserves
  service when an agent is held, demoted, unavailable or unsafe. A
  fallback is a production control, not a post-incident improvisation
  (Chs. 10, 12, 13).
- **Human review capacity** — the staffed ability to absorb agent
  exceptions at required quality and service level; it sets a real
  autonomy ceiling under peak conditions (Ch. 14).
- **Least agency** — granting an agent only the minimum set of tools and
  permissions needed for its named task, then removing unused authority
  after observation (Chs. 9, 10; App. E).
- **Material change** — a change to model, prompt/policy, corpus, tool,
  identity, connector, workflow, deployment region or critical
  dependency that can alter behaviour, authority, data or risk and must
  enter change control (Ch. 10; App. B).
- **Operational baseline** — the measured current volume, time, quality,
  cost, exception pattern and capacity for a named workflow before
  intervention; the denominator for later value claims (Chs. 1, 5, 12).
- **Practice-reported** — a disclosure label for public grey literature
  (for example, a consulting case) whose workflow or metric may be
  useful but is not independently verified evidence (Ch. 15).
- **Re-authorisation** — a formal review of a mandate and safety case
  after material change, incident, autonomy expansion or scheduled
  interval; it confirms that the task has retained its right to operate
  (Chs. 8, 9, 13).
- **Residual risk** — the risk that remains after controls and is
  knowingly accepted by a named accountable owner, with a rationale,
  expiry and monitoring plan. It is never a blank field (Ch. 9).
- **Shadow mode** — running a system against real or representative
  cases without allowing it to affect the operational outcome, in order
  to collect decision-grade evidence (Ch. 12).
- **Value bridge** — a transparent chain from baseline to gross benefit,
  permanent costs, human supervision, risk provision and the named
  operational action that captures value (Ch. 5).
