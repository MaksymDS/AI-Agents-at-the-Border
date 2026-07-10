---
title: "RFP Skeleton for AI and Agentic Systems"
part: "Appendices"
status: review
version: 0.3
last-updated: 2026-07-10
notes: "External-review edition: Chapter 7 markers resolved and cross-checked against the decision toolkit."
---

Structure for the AI-specific schedule of a tender (annexed to the
administration's standard contract terms — the MCC-AI pattern). Numbered per RFP convention.

**B.1 Problem statement, not solution specification.** State the task,
its verifiable outcome, current unit cost and volume (Ch. 5 worksheet
baseline). Do not specify model families or architectures. Granularity
rule (Ch. 7): specify the *decision and its operating context* — the
decision supported, who stays accountable, exclusions, evidence shown
to the officer, behavior under uncertainty, data boundaries, gate
performance — and leave the solution space open. An RFP without a
decision-rights section can be answered compliantly and wrongly.

**B.2 Definitions (verbatim from Ch. 2).** Include the book's agent
definition word-for-word; require bidders to classify every proposed
capability on the Autonomy Ladder, per task.

**B.3 The five questions (mandatory response schema, per task):** task ·
proposed rung and why not lower · draft mandate (what it decides, what
is excluded) · tool list with permissions and logging points · matching
oversight pattern + demotion evidence. Non-conforming responses are
returned.

**B.4 Deployment and sovereignty.** "Which models, running where, under
whose jurisdiction, with what data-residency guarantees" — mandatory;
"our platform is cloud-based" is a non-answer. Lawful patterns limited
to the administration's deployment-tree outcome (Ch. 3).

**B.5 Evaluation requirements (Ch. 12).** Reliability as consistency
across repeated trials (k^n-style), not single-shot accuracy;
state-dependent workflow tests; accuracy-versus-cost curve, unit-priced
at the proposed rung; prompt-injection robustness at the 1/10/100
profile on document-embedded attacks (Ch. 10); all validated on the
administration's traffic in the pilot stages, gates pre-committed.

**B.6 Security schedule (the five demands, Ch. 10 §10.5):** channel
separation evidence · agency controls incl. no trust-all-tools in
production · exportable open-format trajectory observability under the
administration's control · incident/patch SLAs + joint runbook ·
supply-chain provenance and update signing.

**B.7 Operations and change.** The four-change rule as a contract term
(no silent model/prompt/corpus/tool updates); canary path; AgentOps
telemetry handover; estate-integration via governed interfaces only.

**B.8 Data, model, and output rights (the audit record's #1 failure
mode).** Buyer owns or holds unrestricted use of: source data; cleaned
and transformed versions; project annotations; officer feedback and
override history; evaluation datasets; performance logs; scores and
explanations generated for its declarations; configuration and
threshold history; documentation sufficient to reproduce, audit, and
migrate. No use of customs data to train systems for other customers
without explicit approval — "anonymized" is not accepted as a magic
word. Vendor retains background IP, generic tools, and reusable
methods, provided the buyer is not trapped inside them. The contract
must separate: background IP · foreground artifacts · customer data ·
derived customer-specific assets · outputs · logs · documentation.
Blurred categories schedule the dispute; they do not avoid it.

**B.9 Lock-in controls.** What works (Ch. 7): data export rights;
documented mappings and interpretation layers (the vendor's
understanding of the buyer's codes and exceptions is a deliverable, not
a notebook); standardized interfaces; WCO Data Model conformance
implemented, not mentioned; in-house capacity transfer (hub-and-spoke
alignment, Ch. 14). Ritual unless enforced: escrow never tested for
third-party deployability; decorative multi-vendor architecture.
Standing contract question, answered in writing annually: "If we
terminate in twelve months, what exactly can we take, who can run it,
and what would be missing?" 

**B.10 Team, references, and verified claims.** All quantified vendor
claims delivered with source + who stated it (the book's attribution
rule, applied to bids). The confidence conversation, asked directly
(Ch. 7): can the vendor handle government data; explain the model;
operate in the required cloud; satisfy cybersecurity review; support
the administration's language mix; and stand in front of leadership if
something goes wrong. Include the twenty-samples demonstration (Ch. 7
toolkit) as a scored tender stage: buyer-selected, representative,
unseen inputs, end-to-end under observation, latency, cost, evidence,
 and failures visible.

**B.11 The 90-day evidence schedule.** The selected bidder shall not
begin with a generic discovery phase. By day 30 it delivers the process
map, baseline, data-flow map and named administration owners. By day 60
it delivers the buyer-selected evaluation set, draft mandate,
tool/identity map, model and corpus inventory, and security threat
model. By day 90 it runs the representative end-to-end test, incident
tabletop and rollback exercise; transfers the evaluation harness; and
produces a gate memo jointly signed by operations, security and the
business owner. Payment is attached to these artifacts as well as to
visible functionality.

**B.12 Acceptance as a right to operate.** Acceptance is not a single
delivery event. For each task, define the authorised rung, the test
population, quality and cost threshold, officer-override ceiling,
security evidence, retention and escalation path, suspension and
rollback rule, and re-validation event. The task is accepted only for
that mandate; any higher autonomy or new write tool is a new gate and a
commercial reset.

**B.13 Commercial transparency.** Require a unit-price schedule for
inference, storage, integration, managed operations, support, change
requests, security testing, data annotation and exit assistance. State
volume assumptions, minimum commitment, price-escalation rule and cost
ceiling per task. A bidder may price uncertainty, but may not hide it in
an undifferentiated platform subscription.

**B.14 Exit rehearsal.** Before final production acceptance, vendor and
administration execute a limited exit rehearsal: export agreed data,
trajectories, configuration, mappings and evaluation artifacts;
demonstrate their readability; revoke vendor credentials; and run one
workflow through the agreed fallback. The goal is not to terminate the
relationship. It is to prove that continuation is a choice.

**B.15 Operational service levels.** Require task-level service levels,
not only platform uptime: response and end-to-end completion time by
priority; evidence/citation availability; maximum exception age;
trajectory-log availability; incident acknowledgement and containment;
knowledge-source update latency; and cost-alert response. State the
service owner on each side, the reporting cadence, the remedy for a
repeated breach and the manual or rules-based fallback that applies. A
99.9% platform is not an adequate service if the agent's evidence layer
is stale or its queue cannot be supervised.

**B.16 Change classification and release evidence.** Bidders shall
propose a change matrix covering model, prompt/policy, corpus,
connector/tool, identity/permission, workflow, region and dependency
changes. For each change class define who may approve it, regression and
adversarial tests, canary/shadow requirement, user communication,
evidence-room update and re-authorisation threshold. Emergency security
patches may be expedited but must still leave a dated record and trigger
post-release validation. "Continuous improvement" never authorises
silent expansion of authority.

**B.17 Transition and knowledge transfer.** The proposal must price and
schedule a transfer plan: joint operation by named administration staff;
administrator and supervisor training; runbook walkthroughs;
configuration and evaluation-harness handover; a tabletop incident;
release participation; and a competency check before reduced vendor
coverage. Score the supplier on evidence that the administration can
perform routine supervision, first-line triage and release acceptance,
not on an assertion that training will be provided.

**B.18 Subcontractors and model providers.** List all material
subprocessors, model providers, hosting providers and critical
open-source dependencies; state their location, data access, purpose,
security responsibility, change-notice path and replacement plan. The
prime supplier remains accountable for the integrated service. No new
entity may receive administration data or gain operational access
without the contractual notice and approval route. This makes the
supply chain visible before an incident rather than during one.

**B.19 Evaluation data protection.** The buyer-selected test set must
be protected as operational evidence. Define access controls, retention,
segregation from vendor training, annotation handling, audit logs and
return/destruction on exit. Where production data cannot be used for an
early test, require a documented representativeness assessment for the
sanitized set and a commitment to re-test on authorised live traffic in
shadow mode. A clean synthetic benchmark cannot be substituted for the
exceptions the workflow will actually face.

**B.20 Bidder clarifications that change risk.** Put a simple rule in
the tender: a clarification that changes data location, tool authority,
subprocessor, model family, evaluation scope, pricing basis, retention,
exit right or proposed rung is a material change and must be re-scored
by the relevant owners. This prevents a bidder from winning with one
architecture and delivering another through a series of innocuous-
sounding implementation decisions.

**B.21 Task mandate schedule.** Attach a blank mandate card for each
initial task and require the bidder to complete it jointly with the
administration. The schedule names the case trigger; objective; current
and proposed rung; required evidence; permitted and prohibited tools;
write actions; human route; affected parties; data classes; service
clock; current owner; demotion triggers; fallback; retention; and gate
evidence. The contract should make clear that an unfilled mandate card
is not authority to operate. It is a discovery artifact awaiting
approval.

**B.22 Architecture decision record.** Require a short, versioned
architecture decision record for every material design choice: why this
deployment pattern; why this model family; why this retrieval and tool
boundary; why this identity pattern; why this data-retention period;
why this fallback. Each record includes options considered, the
decision, risks, named approver and review trigger. This prevents the
system's most important assumptions from disappearing into a slide deck
or a supplier's private ticketing system.

**B.23 Model and component register.** For every production task, the
supplier shall keep a register of model provider and version; hosting
region; weights or API endpoint; system prompts/policies; retrieval
embeddings and index version; orchestration framework; tools/connectors;
identity scopes; critical open-source components; and evaluation version.
The administration needs a readable snapshot before and after every
release. The purpose is not to prescribe a static stack; it is to enable
an investigation when behavior, cost or security posture changes.

**B.24 Agent identity and segregation.** Proposals must show an identity
diagram in which each agent, service and human operator has a distinct
identity; privileges are purpose-bound, time-limited where possible and
reviewable; secrets are not embedded in prompts or documents; and the
agent cannot inherit an administrator's broad session. Require a
demonstration that a prohibited tool call fails, is logged and reaches
the correct response path. A claim that the system is "read only" is
not evidence unless the underlying scopes prove it.

**B.25 Human-interface and explanation design.** The bidder shall show
the exact officer view for a positive recommendation, an uncertainty,
a conflict between sources, a refusal, an escalation and a system
outage. Each view must state the source evidence, confidence or reason
for escalation where meaningful, the action available to the officer,
and the way an override is captured. For trader-facing work, require a
separate design for notices, review requests and accessible language.
The procurement question is not whether the model can explain itself;
it is whether the human can make and record a defensible decision.

**B.26 Evaluation protocol.** Before a bidder sees the full test set,
agree the protocol: representative strata; inclusion of hard and
hostile documents; number of repeated trials; scoring rubric; baseline
path; reviewers; treatment of abstentions; error taxonomy; cost capture;
and how disputed cases are adjudicated. Retain a sealed holdout set for
acceptance and periodic revalidation. Require the supplier to report
failures, not only aggregate success, and prohibit tuning on the final
holdout without declaring it compromised.

**B.27 Safety and security exercises.** Price four exercises as ordinary
delivery work: hostile-document/prompt-injection testing; an excessive-
authority or tool-misuse test; a data-source freshness or conflict test;
and a freeze-preserve-fallback incident tabletop. Each exercise produces
a dated finding, remediation owner, target date and re-test result.
This is more valuable than a generic assurance certificate because it
tests the combined system in the administration's named workflow.

**B.28 Data-quality and corpus stewardship.** Assign a business
custodian for every source corpus and decision-critical feed. The
contract must state who determines source inclusion, validity and
supersession; how corrections are proposed and approved; how stale or
conflicting material is handled; and how an invalid feed constrains
agent authority. Pay for this stewardship explicitly. A retrieval
system with no owner is a short-term demo and a long-term legal risk.

**B.29 Financial-control schedule.** Require a monthly task-level cost
record separating fixed platform cost, inference, retrieval, storage,
tool calls, integration support, human supervision, quality sampling,
security work and exit provision. Set alerts for both spend and unusual
consumption per completed case. The administration should be able to
change a model or routing policy for cost reasons without losing the
ability to compare quality and safety. A lower bill created by removing
logging or human review is not an acceptable optimisation.

**B.30 Incident, liability and cooperation.** Define incident classes
(security, privacy, model/quality, authority breach, service failure),
notification clocks, evidence preservation, communication authority,
investigation roles, remediation, re-testing, data-subject and regulator
support, and the right to suspend the task. Define what the supplier
must provide even when the root cause is an upstream model or cloud
provider. Liability and remedy must be reviewed under local procurement
law, but operational cooperation cannot be deferred until a crisis.

**B.31 Audit and assurance.** Preserve rights for the administration or
its appointed assessor to inspect relevant evidence, observe tests,
request independent assurance and receive remediation status. Scope the
right sensibly so it protects legitimate supplier IP and security; the
minimum is access to facts needed to understand the administration's
data, authority, control performance and contractual compliance. Annual
paper attestation alone is insufficient for a changing agentic service.

**B.32 Termination assistance.** In addition to exit rehearsal, price a
termination-assistance period with named resources, response times and
transfer outputs. Specify how long the supplier will maintain read-only
access to records, support safe cutover, answer audit questions and
delete or return data. Define the conditions under which the
administration may demand immediate credential revocation or a faster
fallback. An exit right without a staffed execution plan is merely a
legal theory.

## Bid-response checklist

Before issuing the RFP, confirm that the administration has supplied or
can supply the following: named workflow and baseline; target rung and
non-negotiable exclusions; lawful deployment constraints; representative
documents and data-access route; existing interfaces; user roles and
languages; evaluation protocol; current security baseline; expected
contract form; procurement timetable; and named evaluators. A buyer that
withholds all operational context does not create competition; it
invites generic promises and later change requests.
