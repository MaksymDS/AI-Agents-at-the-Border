---
title: "Regulatory Reference Tables"
part: "Appendices"
status: review
version: 0.4
last-updated: 2026-07-10
notes: "Legal cut-off verified against primary regulator and legislation sources."
---

Compact reference as of 2026-07-10; Chapter 8 carries the analysis.

## D.1 Binding instruments reaching customs AI

Stacked profiles; fields — *Instrument · Key dates · Customs-relevant
core*.

**EU** — AI Act (Reg. 2024/1689) + Digital Omnibus (adopted 29 Jun
2026). Key dates: prohibitions 2 Feb 2025 · GPAI 2 Aug 2025 · Art. 50
transparency solutions **2 Dec 2026** · national AI regulatory sandboxes
**2 Dec 2027** · **standalone Annex III high-risk 2 Dec 2027** · embedded
(Annex I) 2 Aug 2028. Customs-relevant core: border management =
Annex III high-risk; Arts. 9/10/14 (risk management, data governance,
human oversight); Art. 4 AI-literacy duty; extraterritorial reach.

**China** — PIPL/DSL/CSL stack · GenAI Interim Measures (2023) ·
Labeling Rules (1 Sep 2025) · **Intelligent Agents Opinions** (May
2026, policy framework). Customs-relevant core: agent definition,
permission management, lifecycle security, standards work, and nineteen
application scenarios; determine the binding service rules per use case
under the PIPL/DSL/CSL stack. The anthropomorphic-interaction measures
were scheduled to take effect on 15 Jul 2026 and were not in force at
the legal cut-off.

**Korea** — AI Basic Act and Enforcement Decree (in force 22 Jan 2026)
and PIPA. Key dates: administrative fines carry at least a one-year grace
period. Customs-relevant core: high-impact duties — disclosure + impact
assessment.

## D.2 Data-protection-operative jurisdictions (priority regions)

Stacked profiles; fields — *Binding layer · Automated-decision (ADM)
provision · Soft law shaping tenders · Legal cut-off record*.

**UAE** — Binding: PDPL 45/2021; DIFC Reg 10 (enforced 2026). ADM:
via the DIFC/ADGM regimes. Tender-shaping soft law: AI Charter; AI
Procurement Guidelines; Dubai Ethical AI Toolkit; TDRA validation
lab. **Cut-off record:** no federal PDPL Executive Regulations were
identified on the UAE Legislation portal by 10 Jul 2026.

**Saudi Arabia** — Binding: PDPL (enforceable Sep 2024; active
enforcement). ADM: **explicit objection right to solely-automated
decisions.** Tender-shaping soft law: SDAIA Adoption Framework + GenAI
Guidelines (Procurement Review Boards); ISO/IEC 42001 as the de facto
supplier bar. **Cut-off record:** the PDPL and its implementing and
transfer regulations remain the binding baseline; no horizontal AI
statute is treated as enacted here.

**Egypt** — Binding: PDPL 151/2020 + Executive Regulations (Decree
816/2025, effective 2 Nov 2025). ADM: lawful-basis regime. Soft law:
National AI Strategy (2nd ed.). **Cut-off record:** the PDPC identifies
these as the operating framework; calculate licences, DPO and transition
obligations for the deploying entity and activity.

**Kuwait** — Binding: CITRA regulation (2021). ADM: none. Soft law:
National AI Strategy 2025–2028 (draft). **Cut-off record:** CAIT's
published document remains marked *Draft*; do not treat it as binding.

**Malaysia** — Binding: PDPA as amended 2024 (phased to Jun 2025).
ADM: **no general statutory right in the Act.** Soft law: AIGE; National
AI Office; the Commissioner’s ADMP guideline (Apr 2026). Use the latter
with DPIA guidance; it is not a new primary-law right.

**Singapore** — Binding: PDPA. ADM: via PDPC advisories, including its
2024 AI recommendation-and-decision guidance. Soft law: model
frameworks incl. the **agentic AI framework (2026, updated May)**;
GovTech playbooks; AI Verify. No horizontal AI statute.

## D.3 Multilateral layer

WCO: AI/ML Adoption Report (Mar 2025; HITL + MLOps baseline) ·
Readiness Self-Assessment Tool (Jan 2025, Members' area) · Data Model
(interoperability/anti-lock-in) · BACUDA/CLiKC!. Soft law: OECD AI
Principles; UNESCO Recommendation; G7 Hiroshima.

## D.4 The applicability record

Do not treat this appendix as legal advice or as a compliance checklist
that can be completed once. For every proposed task, create a one-page
**applicability record** with six fields: jurisdiction and deploying
entity; affected people and data classes; task, autonomy and agency;
binding instruments and contractual obligations; required controls and
evidence; named counsel and next review date. The record is the bridge
between Chapter 8's landscape and Chapter 9's mandate.

The practical test is simple: an executive should be able to ask why a
task is limited to L2, why it is hosted in a particular environment, or
why a trader-facing challenge path exists, and receive an answer that
links to one legal or policy record. If the answer is "because legal
approved AI," the administration has approved a technology category,
not a deployment.

## D.5 The standing watch list

Maintain the regulatory watch list as a management object, not a note in
a research folder. Each row carries: source link; publication date;
jurisdiction; whether it is law, regulator guidance, procurement
standard or commentary; impacted tasks; owner; next verification date;
and the required action (none / update control / update contract / pause
deployment). Review it quarterly in the AI portfolio meeting and before
every material autonomy expansion.

Add a 12–24 month planning view to the live register. The entries are
management judgments, not statements that a proposal will become law.

| Field | Record |
|---|---|
| Probability | Low / medium / high, with one-sentence rationale |
| Earliest plausible effect | Date range, dependency, and official source |
| No-regret preparation | Control, evidence, contract right, or capability useful even if the change does not occur |
| Avoided commitment | Irreversible architecture, purchase, or authority expansion that should wait |
| Readiness | Not started / designed / tested / operating; named owner and next review |

| Trigger | Immediate question | Typical action |
|---|---|---|
| New binding AI rule or implementation date | Which live task is in scope? | Update applicability records and safety cases. |
| New privacy or transfer guidance | Did the lawful hosting decision change? | Re-run deployment-tree decision. |
| Regulator enforcement or public incident | Does the failure mode exist in our estate? | Run targeted assurance test and report result. |
| New model/provider term | Does it alter data, training, logging or exit rights? | Route through change control and contract review. |

The legal cut-off is not a promise that the law will stand still. Retain
the named post-cut-off review with a source, owner and next verification
date; never substitute a stale table for an applicability record.

## D.6 Requirement-to-control crosswalk

This crosswalk is a management aid, not legal advice. It translates the
portable baseline into the operating evidence that a customs programme
can ask for. Local counsel must confirm applicability and any
jurisdiction-specific control.

| Requirement theme | Typical source family | Operating control | Evidence in the record | Re-test trigger |
|---|---|---|---|---|
| Lawful purpose and data minimisation | Privacy laws; sharing agreements | Task-specific purpose, data inventory and access scope | Applicability record; data-flow map; data contract | New data class, source or user group |
| Automated-decision / human oversight | Privacy/AI law; public-law duties | Rung ceiling, human route, override and escalation | Mandate card; trajectory; supervisor training | Authority, outcome or affected-party change |
| Risk management and safety | AI law; NIST/ISO; procurement policy | Safety case, evaluation gates, residual-risk register | Test reports; sign-off; incident drill | Material release, incident or autonomy increase |
| Transparency and contestability | AI/privacy law; administrative procedure | Notices, explanation boundary, human review and correction route | User journey; review log; template communications | New channel, policy or adverse-use case |
| Security and resilience | Cyber law; government security baseline | Least-privilege identity, hostile-input separation, fallback | Threat model; access test; containment exercise | Tool, connector, model or supplier change |
| Records and auditability | Records law; audit policy; AI law | Retained trajectory, version record and evidence room | Retention schedule; export test; release record | Retention change, audit finding or contract renewal |
| Residency and international transfers | Privacy/data sovereignty rules | Approved region, subprocessor control, encryption and transfer assessment | Hosting decision; contract schedule; processor list | Location/provider/subprocessor change |
| Supplier accountability | Procurement law; contract policy | Acceptance gates, audit rights, incident and exit obligations | Signed schedules; service reports; exit rehearsal | Award, renewal, material change or incident |

## D.7 Applicability-record template

Complete one record per task, not one per platform. A platform may host
ten tasks with different authority, data and affected people.

| Field | Record the answer | Evidence / owner |
|---|---|---|
| Task and purpose | What operational task is supported; what outcome is excluded | Mandate owner |
| Entity and jurisdictions | Deploying administration, users, data origin, processing and hosting locations | Legal lead |
| People and data | Traders, travellers, employees; personal/sensitive/confidential data classes | Privacy lead |
| Autonomy and agency | Ladder rung, tools, write actions, human route and reversibility | Operations + security |
| Applicable instruments | Binding laws, policies, contracts and procurement standards; applicability rationale | Counsel |
| Controls | Oversight, transparency, security, records, transfer and supplier controls | Control owners |
| Residual risks / exceptions | What remains unresolved; temporary cap; compensating measure and expiry | Executive signer |
| Evidence and review | Links to safety case, testing, contract clauses; next review and change triggers | Programme office |

An applicability record should fit on two pages. If it cannot, the task
may be too broad to approve or the programme may be attempting to solve
several legal questions with one generic "AI" label.

## D.8 Regulatory-change response protocol

When a relevant rule, guidance, enforcement action or supplier term
changes, use the following response rather than a general legal review:

1. Classify the source: binding law, regulator interpretation,
   procurement condition, court decision, provider term or commentary.
2. Identify the specific live and planned mandate cards affected; do not
   infer impact only from the model brand.
3. Assess whether the change touches purpose, data transfer, authority,
   disclosure, records, security, supplier obligation or workforce
   competence.
4. Decide the interim posture: no action, update documentation, add a
   control, limit scope, pause a task, or invoke a contract right.
5. Update the applicability record, safety case, RFP/contract schedule
   where needed, and the watch-list row with source and next review.
6. Report material changes to the portfolio board, including whether
   there is a budget or service impact.

The protocol prevents a new regulation from becoming either an excuse to
freeze all progress or an item delegated indefinitely to a legal inbox.
