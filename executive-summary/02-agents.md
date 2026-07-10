---
title: "Agent, Autonomy, and Agency"
---

## The definition that belongs in the RFP

An AI agent is a software system that pursues an assigned goal by planning
multi-step work and using tools—systems, databases, and documents—with a
defined degree of autonomy and under defined human oversight.

Each phrase is a control. The goal bounds purpose. Planning creates the
possibility of adaptive behaviour. Tools define reach. Autonomy allocates
decision rights. Oversight retains human command. Remove any one and the
buyer no longer knows what is being procured.

**The bright-line test:** can one decision-making component choose the next
permitted action; can that choice change because of an intermediate
result; and can it stop, re-plan, or escalate instead of following a fixed
route? A pre-written chain remains a workflow or pipeline even when several
steps use AI. Adaptive selection from bounded actions is agentic. This is
the practical defence against agent washing.

Rules, machine learning, generative AI, and agents are not replacement
generations. A robust customs workflow stacks them: rules enforce hard
boundaries, ML supplies risk signals, GenAI reads and drafts, and an agent
may orchestrate the allowed sequence. A vendor that proposes to replace
hard constraints with a prompt has confused fluent language with control.

## The Autonomy Ladder

![Figure 2.1 — The Autonomy Ladder](/assets/diagrams/fig-ch02-autonomy-ladder.svg){width=100% height=78%}

**L1 Assistant — Operator.** The system drafts, retrieves, extracts, or
summarises. A human checks every output before use. This is the default
entry point for internal knowledge and document work.

**L2 Copilot — Pilot.** The system proposes an action inside the workflow;
the officer confirms each consequential action. HS-code suggestion and
document-completeness recommendations usually belong here.

**L3 Supervised Agent — Supervisor.** The system completes a bounded task
across tools, while a human handles exceptions and retains the
consequential decision. Case-file assembly is a strong candidate when the
write path remains narrow and reversible.

**L4 Autonomous Agent — Governor.** The system decides and acts inside a
machine-checkable mandate; humans audit outcomes and anomalies. It is
defensible only for low-consequence, reversible, tightly bounded work with
complete records and a tested fallback. Penalties and other materially
adverse public-authority decisions do not earn this rung merely because a
model performs well.

Promotion occurs one task and one rung at a time. A platform has no single
autonomy level. On the same architecture, a search assistant may be L1, a
classification suggestion L2, and a case-preparation loop L3.

## Agency is the second dial

Autonomy asks who decides whether an action should occur. **Agency** asks
what the software is technically able to touch: tools, data, permissions,
write actions, communication channels, and transaction limits. The two
must be recorded separately.

A read-only agent may adapt its research autonomously yet create little
direct operational exposure. A copilot may require confirmation but still
hold dangerous broad credentials. The control rule is **least agency**:
grant only the specific capability needed for the task, use a distinct
machine identity, deny everything else, and remove unused reach after
observation.

## The mandate card

Every deployed task needs a short, versioned mandate card:

- task trigger, start, end, and verifiable outcome;
- current autonomy rung and agency profile;
- permitted and prohibited tools, data, writes, and external messages;
- evidence shown to the officer and trajectory retained for audit;
- named accountable owner and human review route;
- quality, cost, safety, security, and queue thresholds;
- material-change and re-authorisation rules;
- demotion, suspension, fallback, and expiry.

No completed card means no authority to operate. Updating a prompt is an
ordinary change only when it does not alter behaviour, evidence, data,
tools, or authority. Otherwise it re-enters the gate.

## Six questions for any “agent”

Task · rung and why not lower · agency and why each permission is needed ·
mandate and signer · reconstructable evidence · oversight and demotion.
An answer that exists only in a vendor deck is not an operating control.

