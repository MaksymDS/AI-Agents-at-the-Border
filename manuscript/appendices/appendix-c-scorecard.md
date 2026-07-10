---
title: "Vendor Evaluation Scorecard"
part: "Appendices"
status: review
version: 0.3
last-updated: 2026-07-10
notes: "External-review edition: Chapter 7 markers resolved and scorecard checked against the RFP skeleton."
---

The weights below are a considered default, not a fixed rule:
rights/exit and sovereignty carry the heaviest weight because they carry
the failure-mode record. Adjust them to local procurement law before use.

Weights: C1 15% · C2 10% · C3 20% · C4 15% · C5 10% · C6 20% · C7 10%
(Figure C.1 shows these as a single weighted bar — the two 20% domains,
Sovereignty & Security and Rights & Exit, carry the most weight because
they carry the failure-mode record).

::: {.content-visible when-format="epub"}

![Figure C.1 — The Vendor Scorecard](/assets/diagrams/fig-appc-scorecard-weights.svg){width=100%}

:::

```{=latex}
\clearpage
\includepdf[pages=1,pagecommand={\thispagestyle{empty}}]{assets/prebuilt/fig-appc-scorecard-weights.pdf}
```

| Domain | What is scored | Evidence class required |
|---|---|---|
| C1 Problem fit | Response quality to B.1–B.3; rung discipline (did they resist over-autonomy?) | Conforming schema |
| C2 Evidence quality | Verified deployments; attribution of every claim; refs | Primary/secondary grading |
| C3 Sovereignty & security | B.4 + B.6 compliance depth | Architecture + test results |
| C4 Evaluation rigor | B.5 artifacts; willingness to gate | Pre-committed gate plan |
| C5 Operations | B.7 readiness; observability handover | Telemetry demo |
| C6 Rights & exit | B.8–B.9 terms accepted vs red-lined | Marked-up contract |
| C7 Delivery & transfer | Team, in-house capacity building, confidence-conversation signals (B.10) | Named individuals + checks |

### Scoring instructions

Score each domain 0–5 before applying the weight. `0` means no response
or an unacceptable exclusion; `1` means a principle without an artifact;
`3` means a credible artifact and a buyer-verifiable demonstration;
`5` means the artifact is tested on representative buyer inputs, owned
by named people, exportable, and contractually enforceable. A high total
does not override an auto-fail: a bidder cannot compensate for missing
rights, an unsafe agency posture or an untestable claim with a polished
interface.

### The evidence room

Run the final evaluation in a room, not only in a spreadsheet. Ask the
shortlisted bidder to process twenty buyer-selected cases; walk through
one adverse trajectory; show the complete cost record; export a
trajectory; explain a refusal; update a test threshold; and execute the
first step of the exit rehearsal. Score what the administration sees,
not what a slide asserts. Record every deviation as a contract
clarification or a failed criterion.

Red-flags checklist (auto-fail candidates): "fully autonomous" without
exception path · accuracy without unit cost · silent-update rights ·
trajectory data only in vendor cloud · trust-all-tools anywhere ·
claims that fail attribution · a complicated answer to the
twenty-samples request · no answer to the twelve-month termination
question · acceptance offered as a single event rather than staged ·
acceptance criteria that sound strict but are untestable ("100%
accurate," "free from hallucination").

### Scoring record and decision rule

Keep a one-page record for every score: criterion; raw score; weight;
evidence observed; evaluator; open clarification; and whether a
non-negotiable condition has been met. Evaluate independently before the
consensus meeting so the most confident technical voice does not set the
score for operations, legal or finance. At consensus, resolve the
evidence—not the average. A score of `4` because the buyer observed a
test is different from a score of `4` because a supplier promised a test
after award.

Use two decision rules alongside the weighted total. First, any
auto-fail or unresolved material risk stops the bidder regardless of
score. Second, set minimum domain thresholds for C3 Sovereignty &
security and C6 Rights & exit; they are conditions of public control,
not features that a superior interface can compensate for. Record any
approved deviation, its rationale, expiry and compensating control in
the evidence room. A verbal risk acceptance is not procurement
governance.

### References and proof of delivery

Ask each shortlisted supplier for two reference conversations of the
buyer’s choosing: one operational owner and one security, data or
governance counterpart. Use a common script: what task and rung were
actually deployed; what changed after award; what evidence could the
customer export; how did an incident or rollback work; which costs were
not obvious at tender; would they buy the same service again? A refused
reference is not automatically disqualifying, but it lowers the evidence
grade until a credible alternative is provided.

The final recommendation should state both the winning score and the
conditions precedent to award: named deployment region, accepted data-
rights schedule, successful representative test, evidence-room access,
price baseline, model/tool inventory and initial mandate. This preserves
competitive fairness while preventing the common handoff in which a
careful evaluation is replaced by an ungoverned implementation.

### Domain-level scoring anchors

Use the anchors below to force a discussion about evidence rather than
product language. They are not a substitute for local procurement law
or for the auto-fail conditions.

| Domain | 1 — insufficient | 3 — credible | 5 — decision-grade |
|---|---|---|---|
| C1 Problem fit | Generic assistant; task, exclusions and rung unclear | Task map and draft mandate fit the requested workflow | Buyer-observed workflow handles representative cases, respects exclusions and identifies when to abstain |
| C2 Evidence quality | Anonymous benchmarks, unqualified accuracy claims | Named references and source-labelled claims | Verifiable operating evidence, candid limits and reference conversations confirm delivery conditions |
| C3 Sovereignty & security | Vague cloud answer; shared identity or untestable safeguards | Region, data flow, controls and security artefacts supplied | Buyer observes hostile-input and least-privilege tests; components, logs and change path are exportable and contractually bound |
| C4 Evaluation rigor | Demo or benchmark only; success undefined | Representative plan, baseline and pre-set gates | Sealed holdout, repeated trials, failure taxonomy, cost curve and re-validation plan jointly accepted |
| C5 Operations | Project team only; no release or incident route | Named operating roles, telemetry and runbooks | Joint control-room design, tested canary/rollback, service levels and administration-owned evidence room |
| C6 Rights & exit | Opaque data rights, proprietary records, vague termination | Marked-up rights and export clauses mostly accepted | Exit rehearsal, readable export, documented mappings, termination assistance and no unacceptable training/data use rights |
| C7 Delivery & transfer | CVs and generic training plan | Named team, 90-day plan and reference checks | Administration counterparts trained through joint operation and can perform supervision, release acceptance and first-line triage |

### Evaluation agenda: from paper to decision

Run the evaluation in four short stages. **Conformance:** exclude bids
that do not answer the task/rung/authority questions or reject
non-negotiable terms. **Paper evidence:** score the written artifacts
independently. **Observed evidence:** run the twenty-case session,
reference conversations and security/exit demonstrations. **Decision
review:** reconcile the scorecard, red lines, commercial schedule and
conditions precedent into a written recommendation.

Do not collapse all stages into one supplier presentation. The supplier
will naturally optimise a presentation for polish; the administration's
job is to observe operating behaviour. Provide the same test conditions
to each shortlisted bidder, record configuration differences, and allow
written clarification only where it does not alter the basis of
evaluation. If a bidder needs a materially different architecture or
assumption to pass, record the change and re-score it.

### Commercial-normalisation worksheet

Compare proposed prices on the same operational unit. For each bidder,
normalise: expected monthly case volume; document pages; input/output
tokens or model calls; retrieval and storage; tool/connector calls;
human support; annotation; security testing; implementation; managed
operations; change; and exit. State any assumptions that cannot be
normalised, then run a conservative volume and exception scenario.

::: {.worksheet-table}

| Cost item | Bidder A | Bidder B | Bidder C | Buyer assumption / source |
|---|:---:|:---:|:---:|---|
| One-time mobilisation | ................ | ................ | ................ | 90-day evidence schedule |
| Steady-state platform | ................ | ................ | ................ | Named users / environments |
| Inference and retrieval per case | ................ | ................ | ................ | Representative case mix |
| Human supervision and managed operations | ................ | ................ | ................ | Target service clock and exception rate |
| Security, evaluation and release work | ................ | ................ | ................ | Required annual exercises |
| Change and integration allowance | ................ | ................ | ................ | Planned interfaces and release cadence |
| Exit / termination assistance | ................ | ................ | ................ | Contract scenario |
| **Conservative all-in unit cost** | ................ | ................ | ................ | Volume, quality and fallback assumptions retained |

:::

The table prevents the cheapest visible subscription from becoming the
most expensive operating service. It also gives finance a clear way to
ask which costs disappear after mobilisation, which increase with volume
and which are unavoidable controls.
