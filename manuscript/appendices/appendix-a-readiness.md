---
title: "The Customs AI Readiness Assessment"
part: "Appendices"
status: review
version: 0.3
last-updated: 2026-07-09
---

The instrument behind Chapter 6. Protocol: six dimensions; **every
answer is an artifact** (a named document, measurement, or decision —
never an opinion); each dimension scores as a **rung ceiling** on the
Maturity Ladder (R1 Document Intelligence · R2 GenAI Assistants · R3 AI
Agents); the output is a **routing table**, not a score. Dimension 3 is
assessed per candidate use case. Dimension 5 carries double weight in
routing. Re-run at a fixed cadence; a dimension unmoved for a year is a
leadership finding.

## Dimension 1 — Leadership and ownership

**1.1 Who is the named executive owner of AI adoption?** *Artifact:* Name + role + appointment record. *Ceiling:* No living owner → ceiling R1 overall.

**1.2 What AI decision did the owner take last quarter?** *Artifact:* Minute / memo of the decision. *Ceiling:* No decision in 2 quarters → owner is nominal.

**1.3 Who signs mandates for L3+ tasks?** *Artifact:* Signed mandate or draft with named signer. *Ceiling:* No willing signer → no task above L2.

**1.4 Has the ministry conversation (Ch. 5) been survivably held?** *Artifact:* Business-case document as presented. *Ceiling:* Absent → R2 ceiling until held.


## Dimension 2 — Legal and sovereignty environment

**2.1 Has the Ch. 8 applicability checklist been run with counsel?** *Artifact:* Counsel's written opinion (not verbal). *Ceiling:* Unrun → R2 ceiling; personal-data use cases R1.

**2.2 Is there a lawful deployment pattern in this jurisdiction?** *Artifact:* Deployment-tree decision record (Ch. 3). *Ceiling:* No lawful terminating node → stop; escalate.

**2.3 Automated-decision provisions identified and designed for?** *Artifact:* Legal note mapping ADM rights to oversight tiers. *Ceiling:* Unmapped → no natural-person-facing task above L2.

**2.4 Data-sharing agreements inventoried for AI clauses?** *Artifact:* Inventory with per-agreement AI-consumption status. *Ceiling:* Unknown → non-native data excluded from corpora.


## Dimension 3 — Data estate *(per candidate use case)*

**3.1 Machine-readable share of the documents this task reads?** *Artifact:* Measured % from last full month. *Ceiling:* <50% → R1 is the work, not the prerequisite.

**3.2 Does the reasoning corpus exist (inventoried, current, cited, owned)?** *Artifact:* Corpus charter (Ch. 11). *Ceiling:* No charter → R2 blocked for this task.

**3.3 Are required system interfaces governed and listed?** *Artifact:* Interface list w/ owners + auth model. *Ceiling:* Screen-scraping anywhere → R3 blocked.

**3.4 Is feedback capture designed?** *Artifact:* Feedback-loop design doc. *Ceiling:* Absent → evidence for rung climbing cannot accrue.


## Dimension 4 — Technology and operations

**4.1 Per-agent identity and permission fabric feasible?** *Artifact:* IAM assessment note. *Ceiling:* Shared credentials only → R3 blocked.

**4.2 Can logging hold and retain a trajectory?** *Artifact:* Logging architecture note + retention rule. *Ceiling:* No → R3 blocked; R2 needs output logging min..

**4.3 Change control able to absorb the four-change rule (Ch. 13)?** *Artifact:* CAB scope statement incl. model/prompt/corpus/tools. *Ceiling:* No → production blocked at any rung.

**4.4 Integration surfaces of the estate documented?** *Artifact:* Interface catalog for CMS / Single Window. *Ceiling:* Undocumented → pilot-only posture.


## Dimension 5 — People and skills *(double weight)*

**5.1 Literacy floor status for the general workforce?** *Artifact:* Training completion data / plan with budget line. *Ceiling:* None → R2 deployments limited to volunteer units.

**5.2 Are mandate signers fluent (can they read gate evidence)?** *Artifact:* Executive session record. *Ceiling:* No → mandates cannot responsibly be signed → L2 cap.

**5.3 Specialist cadre: existing, planned, or absent?** *Artifact:* Hub-and-spoke design / hiring-training plan (Ch. 14). *Ceiling:* Absent w/o plan → vendor dependency finding; R3 caution.

**5.4 Training ≥ ~10% of technology line?** *Artifact:* Budget extract. *Ceiling:* Below → routing flags proportion before procurement.


## Dimension 6 — Governance apparatus

**6.1 Does an AI inventory exist (even empty)?** *Artifact:* The inventory document. *Ceiling:* Existence is the artifact; absence = first action item.

**6.2 Draft oversight routing rule (Ch. 9 four factors)?** *Artifact:* Routing table draft. *Ceiling:* Absent → L3 blocked.

**6.3 Incident path with a named freezer?** *Artifact:* Incident procedure naming role with demotion authority. *Ceiling:* Absent → L3 blocked.

**6.4 Standards anchoring underway (NIST RMF / ISO 42001)?** *Artifact:* Gap assessment or certification plan. *Ceiling:* Informational; strengthens vendor + regulator posture.


## Scoring and routing

Per dimension record: **ceiling (R1/R2/R3)** + the failing artifacts.
Then produce the routing table:

| Output | Content |
|---|---|
| Start-now use cases | Candidates (from Ch. 4 scoring) whose per-case D3 and the global ceilings permit their target rung |
| Binding constraints | The two lowest dimensions + the specific failing artifacts, each with an owner and a date |
| Deliberate caps | Any artificial ceilings imposed (e.g., high-tech/low-governance → cap R2) with removal criteria |
| Next review | Date + expected artifact deltas |

**Profile patterns** (Ch. 6 §6.4): high-D4/low-D6 → cap R2 by design;
low-everything → start R1 anyway (D3.1 *is* the first project); patchy →
match use cases to patches, invest in the two lowest dimensions.

**Calibration line:** the sector's scale frontier reports 62 models →
22 pilots → 2 in production. Route accordingly; do not grade against
imagination.

## The 30-day executive readiness packet

Do not wait for a perfect enterprise assessment before making the first
decision. Within thirty days, the executive owner should receive one
short packet assembled from this instrument:

1. **One start-now workflow** — its current queue, baseline unit cost,
   target rung, named business owner and human gate.
2. **Two binding constraints** — not generic "data" or "skills," but
   the failing artifact, owner, budget action and completion date.
3. **One deliberate cap** — a task that will remain at L1/L2 even if
   capability exists, with the reason recorded.
4. **One procurement decision** — build, buy or partner boundary; the
   first evidence artifact required from a bidder.
5. **One governance decision** — initial mandate signer, inventory
   owner, incident freezer and date of the first gate review.

The packet is deliberately asymmetric: it should contain enough evidence
to start a bounded programme and enough honesty to prevent an
unbounded one. A readiness assessment that only describes deficiencies
has not done its job; it must route money, ownership and authority.

## Reassessment cadence

Re-run the full assessment annually and the task-level constraints before
each material autonomy expansion. A change in model quality does not by
itself raise a ceiling. The record must show which evidence changed:
data coverage, interfaces, security controls, workforce capability,
legal posture, pilot outcome or safety case. This keeps the Maturity
Ladder evidence-led and prevents a procurement renewal from becoming an
automatic autonomy upgrade.

## Assessment workshop guide

Run the first assessment as a working session, not as a survey sent by
email. Invite the executive owner, the line manager for the proposed
workflow, an experienced officer, data/architecture, security, legal or
privacy, procurement and workforce lead. Give the group the candidate
case loop, the last month of queue data and a blank evidence register.
The facilitator's job is to replace each claim with an artifact, an
owner or an explicit unknown.

Use this sequence:

1. **Name the decision and service clock.** What case moves, what
   action does the officer retain, and what counts as an unacceptable
   delay or error?
2. **Walk the actual evidence path.** Which documents, source systems,
   rules and people contribute to the decision? Mark unknown sources and
   off-system workarounds; those are design inputs, not embarrassment.
3. **Apply the six dimensions.** Score only on visible artifacts. If an
   artifact exists but is not current, owned or usable by the workflow,
   record it as a gap.
4. **Set the target and ceiling separately.** The target may be a
   Rung-2 case-preparation service while the long-term opportunity is an
   Rung-3 bounded agent. Do not score the future as if it existed now.
5. **Choose two constraints.** Select the gaps that actually bind this
   case, not every enterprise weakness. Assign an accountable owner,
   budget implication, test and date.
6. **Write the executive packet.** Confirm the start-now task, cap,
   procurement choice, governance decision and next review before the
   meeting ends.

The workshop should produce disagreement. A security lead may see an
identity gap where an operations lead sees a workflow opportunity; an
officer may reveal that the stated process is not the working process.
Record the disagreement and the test that would resolve it. False
consensus creates a polished readiness score and a fragile pilot.

## Artifact register template

Use a short card per answer rather than forcing every fact into a wide
table. The card is deliberately simple enough to export to a board pack
or an evidence room.

**Example card — 1.3 mandate signer.** *Artifact:* draft mandate and
delegation record. *Current state:* draft only. *Decision:* name signer
and exclusions. *Owner:* executive owner. *Test/date:* signed review
within 30 days. *Rung effect:* L3 blocked until signed.

**Example card — 2.2 deployment pattern.** *Artifact:* data-flow map
and legal note. *Current state:* incomplete. *Decision:* confirm
residency and processor chain. *Owner:* legal and architecture leads.
*Test/date:* counsel sign-off within 45 days. *Rung effect:* pilot cap
at R2.

**Example card — 3.2 corpus.** *Artifact:* corpus charter and source
inventory. *Current state:* 70% inventoried. *Decision:* add current
rulings and name custodian. *Owner:* policy owner. *Test/date:* retrieval
sampling within 30 days. *Rung effect:* R2 conditional.

**Example card — 4.1 identity.** *Artifact:* IAM design. *Current
state:* shared service account. *Decision:* create agent identity and
tool scopes. *Owner:* security lead. *Test/date:* access test within 60
days. *Rung effect:* R3 blocked.

**Example card — 5.2 signer literacy.** *Artifact:* executive-session
record. *Current state:* not scheduled. *Decision:* run an evidence-
reading session. *Owner:* programme lead. *Test/date:* exercise within
21 days. *Rung effect:* L2 cap until signer can read a gate pack.

**Example card — 6.3 incident freezer.** *Artifact:* incident runbook.
*Current state:* role named but untested. *Decision:* rehearse demotion
and fallback. *Owner:* operations lead. *Test/date:* tabletop within 45
days. *Rung effect:* L3 blocked.

Replace the illustrative cards with local evidence; do not mark a card
complete because a policy exists elsewhere in the administration. The
test must show that the policy works for the named task.

## Readiness-to-action patterns

**Evidence rich, controls thin.** Good documents and owners; weak
logging, mandates or incident path. **Start:** R1 extraction and offline
evaluation. **Fund next:** identity, trajectory logging and oversight
routing. **Do not yet:** give a tool-using agent external authority.

**Controls rich, evidence thin.** Strong government cloud and
governance; fragmented corpus and data. **Start:** corpus curation and
document intelligence. **Fund next:** data contracts, source ownership
and feedback capture. **Do not yet:** deploy a grounded-answer service
that appears authoritative without an owned current corpus.

**Operational urgency, uneven estate.** Queue pressure is high but only
one document class is workable. **Start:** a bounded document-to-case
loop with a human gate. **Fund next:** baseline measurement, supervisor
capacity and governed integration. **Do not yet:** buy an enterprise
platform framed as the solution to an undefined queue.

**Vendor pressure, no owner.** Demos are available but no executive has
signed a business decision. **Start:** independent assessment and a
mandate workshop. **Fund next:** executive ownership and a value
baseline. **Do not yet:** issue a tender or award a pilot.

**Mature first loop.** Measured use, capable supervisors and working
controls exist. **Start:** reuse the substrate for a second case loop.
**Fund next:** control room, data product and portfolio governance.
**Do not yet:** treat the first success as an automatic L3/L4 approval.

The patterns are routes, not labels. An administration can be mature in
one port or process and constrained in another; the task-level evidence
always overrules the enterprise average.
