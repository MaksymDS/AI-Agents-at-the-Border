---
title: "From Rules to Models to Agents — A Leader's Primer"
part: "I — The Landscape"
chapter: 2
status: review
version: 0.3
last-updated: 2026-07-09
---

## The meeting you have already been in

The vendor's slide says *"Agentic AI for Next-Generation Customs."* The
presenter is fluent and the demonstration is impressive: a system reads a
declaration, checks it against the tariff, flags a valuation anomaly, and
drafts a query to the importer — apparently on its own.

Around the table, three of your directors are having three different
meetings. The head of risk management believes she is looking at a better
scoring engine, like the one procured in 2019. The head of IT believes he is
looking at a chatbot with system access, and is quietly calculating what it
could break. The head of legal is wondering who signs the query to the
importer.

None of them is wrong, and none of them is right — because the room has no
shared language for what this system actually is, what it may decide, and
what it may merely suggest. That gap in language becomes a gap in the
contract, then a gap in oversight, and eventually a headline.

This chapter exists to close that gap. It gives you, in plain terms, the
four generations of technology that vendors compress into the word "AI," a
working definition of an *AI agent* that you can put into an RFP, and the
framework this book uses everywhere: the **Autonomy Ladder**. Nothing here
requires a technical background. All of it is meant to be used in meetings
like the one above.

## 2.1 Why terminology is a leadership issue

In most technology procurements, imprecise language is an annoyance. In AI
procurements, it is a risk multiplier, for one reason: **the word "AI" now
spans systems with fundamentally different behavior, failure modes, and
governance needs.**

A rules engine fails predictably; you can enumerate its behavior. A machine
learning model fails statistically; you manage error rates. A generative
model can produce fluent, confident output that is simply wrong; you manage
verification. An agent can *take actions* — query systems, write records,
send messages — so its failures are not just wrong outputs but wrong
*events in the world*; you manage authority.

When a contract, a policy, or a ministerial briefing uses "AI" without
distinguishing these, the administration ends up governing a rules engine
like an agent (paralysis) or an agent like a rules engine (exposure). Both
mistakes are common, and both are leadership failures, not technical ones —
because only leadership can impose a shared vocabulary across risk, IT,
legal, and operations.

The vocabulary below is deliberately small. Four eras, one definition, one
ladder. It is enough to run a modernization program.

## 2.2 Four eras in one page

Customs was an early adopter of every one of these generations. Your
administration almost certainly runs systems from at least two of them
today. Figure 2.2 sets the four side by side — each with its
characteristic strength and its characteristic failure — because a
well-designed program does not choose one; it stacks them.

![Figure 2.2 — Four Eras in One Page](/assets/diagrams/fig-ch02-four-eras.svg){width=100%}

**Era 1 — Rules (1980s → today).** Human experts write explicit logic:
*if country of origin is X and HS chapter is Y and declared value is below
Z, flag for inspection.* Selectivity modules in most customs management
systems are rules engines. Rules are transparent, auditable, and cheap to
run — and they are also brittle, easy for organized fraud to learn and
route around, and expensive to maintain as trade patterns shift. A rules
engine never does anything you did not explicitly write. That is its
strength and its ceiling.

**Era 2 — Machine learning (2000s → today).** Instead of writing the
logic, you show the system historical outcomes — declarations that turned
out to be fraudulent, valuations that were later adjusted — and it learns
statistical patterns that predict them. This is the technology behind
modern risk scoring, valuation anomaly detection, and image-based cargo
inspection. ML finds patterns no human wrote and adapts as data changes.
The price: its reasoning is statistical rather than explicit, it is only
as good as the historical data (including that data's biases), and it
produces *scores*, not explanations — a property that Chapter 9 treats as
a governance problem with known mitigations, not a mystery.

**Era 3 — Generative AI (2022 → today).** Large language models trained on
vast text corpora can read, summarize, translate, draft, and answer
questions in natural language — including the dense, multilingual,
semi-structured language of trade: invoices, certificates of origin,
rulings, regulations. Two properties changed the game for customs. First,
GenAI handles *unstructured* documents, which is where most customs
information actually lives. Second, it is general-purpose: the same model
that summarizes a case file can draft a reply to a trader. Its
characteristic failure is fluent error — output that reads confidently and
is wrong — which is why Chapter 3 pairs every GenAI use case with a
verification design.

**Era 4 — AI agents (2024 → today).** Give a generative model three
additions — a goal, access to tools, and memory of what it has done so far
— and it stops being a text generator and becomes an actor. It can decompose
a task into steps, call systems, read the results, adjust its plan, and
carry work to completion. That is the technical substance behind the word
"agentic." Everything else is packaging.

The eras do not replace each other; they stack. A well-designed agentic
workflow in customs will typically contain rules (hard constraints that
must never be crossed), ML models (scoring within the workflow), and GenAI
(reading and writing documents) — orchestrated by an agent. Vendors who
present agents as making the earlier eras obsolete are selling architecture
they have not thought through.

## 2.3 What an AI agent actually is — and is not

Here is the definition this book uses, and the one we recommend you put,
verbatim, into policy documents and RFPs:

> **An AI agent is a software system that pursues an assigned goal by
> planning multi-step work and using tools — systems, databases, documents —
> with a defined degree of autonomy and under defined human oversight.**

Every phrase is load-bearing.

- **Assigned goal.** The administration sets the objective ("resolve this
  classification query," "compile the case file for this flagged
  declaration"). An agent without an explicit, bounded goal is not
  deployable in government.
- **Planning multi-step work.** This is what separates an agent from a
  chatbot. A chatbot answers; an agent decomposes, sequences, and executes.
- **Using tools.** The agent's reach is exactly the set of systems it may
  touch — the declaration processing system, the tariff database, the
  document store, email. Tool access is a *permission decision*, and
  Chapter 10 treats the tool list as a security boundary.
- **Defined degree of autonomy.** Not a marketing adjective — a design
  parameter you choose per task. The Autonomy Ladder below is the scale.
- **Defined human oversight.** The counterpart of autonomy. Every level of
  autonomy has a matching oversight pattern; an agent proposal that
  specifies the former without the latter is incomplete by definition.

Just as important is what an agent is **not**:

- **Not a person in law.** It holds no authority of its own; it exercises
  delegated operational decision-making *within a mandate*, the way a
  junior officer exercises delegated authority under standing instructions
  — with the crucial difference that the accountability chain runs entirely
  to humans.
- **Not a single product.** "Agent" names a behavior pattern, not a box.
  The same vendor platform may run L1 assistants and L3 agents side by
  side; each deployment is classified separately.
- **Not self-improving in production.** A properly governed agent does not
  silently rewrite its own instructions or expand its own tool access.
  Changes go through change management like any other system change.

## 2.4 The Autonomy Ladder

The single most consequential design decision for any AI deployment in
customs is not which model to use. It is **how much autonomy to grant, for
which task**. The Autonomy Ladder (Figure 2.1) makes that decision explicit
and gives the whole administration one scale to discuss it on.

![Figure 2.1 — The Autonomy Ladder](/assets/diagrams/fig-ch02-autonomy-ladder.svg){width=100%}

Autonomy rises from left to right: operational decisions pass from the
officer to the agent — **accountability does not**.

**Level 1 — Assistant.** The AI drafts and suggests; the human does the
work. The officer is an **Operator**. *Customs example: the system drafts a
reply to a trader enquiry for the officer to review and send.* Oversight:
every output is checked before use. Failure exposure: near zero beyond
wasted time — which is why L1 is where administrations should build their
first muscle.

**Level 2 — Copilot.** The AI assists live inside the workflow; the
officer stays in control and confirms each action. The officer is a
**Pilot**. *Customs example: the system proposes an HS code; the officer
confirms each one before it is applied.* Oversight: human confirms each
action. This is the highest level most administrations should contemplate
for anything touching a trader's legal position — until the evidence
justifies more.

**Level 3 — Supervised Agent.** The agent works end-to-end on a task and
decides within its mandate; the human sets goals and handles exceptions.
The officer is a **Supervisor**. *Customs example: the agent investigates
flagged declarations — pulls data across systems, compiles a case file; the
officer takes the decision.* Oversight: review by exception and sampling.
Note what moved: the agent now *acts* across systems, but the consequential
decision — what to do about the declaration — remains human.

**Level 4 — Autonomous Agent.** The agent decides and acts within its
mandate; the human sets the mandate and audits outcomes. The officer — in
practice, the administration — is a **Governor**. *Customs example: the
agent clears low-risk declarations end-to-end and escalates anomalies to
staff.* Oversight: post-hoc audit plus anomaly alerts. L4 is legitimate
only where three conditions hold simultaneously: the decision is
low-stakes and reversible, the mandate is narrow and machine-checkable,
and the audit trail is complete. Green-channel clearance of demonstrably
low-risk declarations can meet that bar. Penalty decisions never will.

Three rules govern the use of the ladder in practice:

**Rule 1 — Autonomy is assigned per task, not per system.** "We bought an
agentic platform" is not a governance statement. The unit of classification
is the task: *HS code suggestion* may run at L2 while *case-file
compilation* runs at L3 on the same platform. Your AI inventory (Chapter 9)
lists tasks and their levels, not products.

**Rule 2 — Climb one rung at a time, on evidence.** The ladder is also a
deployment path. A task earns promotion from L2 to L3 by accumulating a
measured track record — override rates, error rates, audit findings — at
the current level. Chapter 12 turns this into pilot gate criteria. Vendors
proposing to enter at L4 are asking you to skip the evidence.

**Rule 3 — Decisions transfer; accountability does not.** At every level,
legal and political accountability remains with the administration. The
practical consequence: before any task moves to L3 or L4, someone with a
name and a title signs the mandate — the written boundaries of what the
agent may decide. If no one will sign it, the task stays at L2. This single
test resolves more governance debates than any framework in this book.

## 2.5 Translating vendor language

You will encounter the ladder wearing costumes. A translation guide:

| When the vendor says… | Ask… |
|---|---|
| "Agentic AI" | Which tasks, at which autonomy level? Show me the mandate per task. |
| "Fully autonomous" | What is the exception path to a human, and what triggers it? If none: not deployable. |
| "Human-in-the-loop by design" | At L2 (confirms each action) or L3 (exceptions only)? These are different systems. |
| "The system learns continuously" | Does anything change in production without change control? If yes: stop. |
| "Guardrails" | Hard constraints (rules the agent cannot cross) or soft instructions (text the model is asked to follow)? Only the former counts as a control. |
| "Our agent integrates with your systems" | Exactly which tools, with which permissions, logged where? The tool list is the security boundary. |

None of these questions requires technical knowledge. All of them change
procurement outcomes.

## 2.6 The autonomy budget

Autonomy is not a feature to switch on; it is a **budget of delegated
discretion**. Every increase buys a business benefit—shorter cycle time,
elastic capacity, fewer handoffs, earlier intervention—but spends some
combination of reversibility, explainability, human attention and public
confidence. Treat the budget like credit: grant a small, bounded amount
to a task that has collateral in the form of data, controls and a
fallback; increase it only after repayment in evidence.

This gives senior leaders a simple way to prevent the two common errors.
The first is the universal cap: "all AI must remain advisory," which
preserves every low-value handoff forever. The second is the blanket
mandate: "the agent may handle customs cases," which disguises many
different decisions behind one label. The operational unit is always the
task: retrieve a ruling; reconcile fields; propose a missing document;
prioritize a queue; draft a response; request evidence; release cargo.
Each has a different business upside and a different autonomy budget.

The management routine is correspondingly short. For every task, record
the starting rung, the benefit expected from one higher rung, the
evidence needed to earn it, and the demotion trigger. A leader can then
ask a portfolio question rather than a technology question: *where are
we buying real cycle-time or capacity benefit by spending autonomy, and
where are we spending it merely to make a demo look advanced?*

## 2.7 The mandate card: one task, one accountable boundary

The Autonomy Ladder becomes governable when every deployed task has a
short **mandate card**. It states the task in plain language; the start
and end of the workflow; current rung; permitted inputs, tools and
outputs; explicit exclusions; the evidence shown to the officer; the
named accountable owner; the human review route; performance and safety
thresholds; and the demotion action. It is a practical object: an
officer, auditor or vendor engineer should reach the same answer from
the card without reading a model specification.

The card stops scope drift. A team may begin with "summarise an
inspection case" and gradually add lookups, recommendations, trader
messages and queue changes. Each addition may be useful, but it changes
the authority being exercised. Updating the mandate card forces a fresh
question: has the task crossed a rung, acquired a new data purpose, or
gained a tool whose failure is consequential? If so, the change goes
through the appropriate gate rather than arriving disguised as a prompt
improvement.

Keep the card visible in the control room and link it to the release
record. At scale it becomes the administration's agent inventory and
the simplest response to the question, "what do our agents actually do?"
An inventory of model names cannot answer that; a portfolio of mandate
cards can.

## Decision Toolkit — Chapter 2

**The five questions to ask whenever anyone proposes an "AI agent":**

1. **Task:** What is the specific task, stated in one sentence, with a
   verifiable outcome?
2. **Level:** Which rung of the Autonomy Ladder — and why not one lower?
3. **Mandate:** What exactly may it decide within that task, and what is
   explicitly excluded? Who signs this?
4. **Tools:** Which systems may it touch, with which permissions, and
   where is every action logged?
5. **Oversight:** What is the matching oversight pattern (per the ladder),
   and what evidence would trigger demotion to a lower level?

A proposal that cannot answer all five in writing is a demonstration, not
a deployment.

## Key Takeaways

- "AI" spans four generations — rules, ML, GenAI, agents — with different
  failure modes and governance needs. Well-designed systems stack them; the
  agent orchestrates, it does not replace.
- An AI agent = assigned goal + multi-step planning + tools + defined
  autonomy + defined oversight. Put the definition in your RFPs verbatim.
- The Autonomy Ladder (Assistant → Copilot → Supervised Agent → Autonomous
  Agent) is the book's core framework: autonomy is assigned **per task**,
  climbed **one rung at a time**, on **evidence**.
- Operational decisions can transfer to an agent within a signed mandate;
  **accountability never transfers**. If no one will sign the mandate, the
  task is not ready for L3/L4.
- The officer's role shifts up the ladder — Operator, Pilot, Supervisor,
  Governor — which is a workforce transformation story (Chapter 14), not a
  replacement story.
