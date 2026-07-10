---
title: "The Regulatory Landscape"
part: "III — Governance and Trust"
chapter: 8
status: review
version: 0.4
last-updated: 2026-07-10
---

## Counsel's question

Somewhere between the pilot's success and the production decision, the
general counsel asks the question the whole program has been orbiting:
*"Is this legal?"* — and receives, from the vendor, the least useful
possible answer: *"Our platform is fully compliant."*

Compliant with what? For a customs AI system, the honest answer is a
three-layer structure (Figure 8.1), and a leader who holds the structure
can direct
counsel, interrogate vendors, and plan investments across jurisdictions —
without pretending to be a lawyer. This chapter builds the structure,
maps the jurisdictions this book prioritizes onto it, and extracts the
design baseline that satisfies all of them at once. One reading note:
this is the book's most time-sensitive chapter. The legal cut-off is
**10 July 2026**; the decision frameworks are built to outlive the
dates.

![Figure 8.1 — The Three Regulatory Layers](/assets/diagrams/fig-ch08-three-layers.svg){width=100%}

## 8.1 The three-layer structure

**Layer 1 — Data protection law. Always on, everywhere.** Whatever the
jurisdiction says or does not say about AI, a customs system that
processes traveller or trader personal data answers to the data
protection regulator from day one. The recurring obligations: a lawful
basis for processing (for customs, usually legal obligation rather than
consent), purpose limitation, cross-border transfer controls (the legal
teeth behind Chapter 3's sovereignty rule), breach notification, and —
most AI-relevant — **rights concerning automated decisions**. Saudi
Arabia's PDPL grants an explicit right to object to solely-automated
decisions; the EU's GDPR Article 22 restricts them; Malaysia's amended
PDPA does not create a general statutory automated-decision right, but
its Commissioner published an Automated Decision-Making and Profiling
guideline in April 2026.[^ch08-1] The design consequence is uniform: a natural
person must not be subject to a purely automated adverse customs decision
without human involvement — which the Autonomy Ladder was built to
guarantee anyway.

**Layer 2 — AI-specific law. Binding in three regimes, arriving in more.**
As of the legal cut-off, binding AI-specific instruments that reach
customs systems operate in the EU, China, and Korea (each below).
Everywhere else in this book's
priority regions, AI-specific instruments are **soft law** — ethics
charters, model frameworks, adoption guidelines.

**Layer 3 — Soft law that hardens through procurement.** Non-binding
does not mean non-operative. The UAE's AI Charter and Dubai's Ethical AI
Toolkit, Saudi SDAIA's ethics principles and adoption framework,
Singapore's model frameworks, Malaysia's AIGE guidelines — these become
de facto requirements the moment they enter government tender criteria,
which is exactly how most customs administrations (and their vendors)
will actually encounter them.[^ch08-2] A vendor scoping the GCC who has never
read the SDAIA principles is telling you something about their regional
seriousness.

## 8.2 The EU AI Act: the reference regime

The EU's Regulation 2024/1689 matters to every reader of this book, for
three reasons: it is the reference other regimes borrow from; it reaches
**extraterritorially** (it can apply where a system's output is used in
the EU — relevant to any administration exchanging risk data with EU
counterparts, and to every vendor selling into Europe); and it names this
book's subject matter directly.

**Classification.** Annex III designates AI used in **law enforcement**
and in **migration, asylum and border management** as high-risk. Customs
risk-targeting of natural persons, biometric identification, and
document-fraud detection operated in a border-management context can fall
within scope. High-risk status triggers the full obligation set: a risk
management system, data governance, technical documentation,
record-keeping, transparency, **human oversight (Article 14)**, accuracy
and cybersecurity requirements, conformity assessment, and EU database
registration.[^ch08-3]

**Timing — settled weeks before this writing.** The Act entered into
force in August 2024 and applies in phases: prohibitions from February
2025; foundation-model obligations from August 2025. The high-risk
obligations were originally due 2 August 2026 — a date this book's own
research tracked as provisional through the spring of 2026, until the
"Digital Omnibus" reform received its final adoption in late June 2026.
The high-risk deadlines are now law: **standalone Annex III systems —
the customs-relevant category — comply by 2 December 2027**; embedded
high-risk by 2 August 2028. Figure 8.2 sets these dated obligations on
a single timeline, with the customs-relevant milestone — border
management as Annex III high-risk — flagged. The Omnibus also moved the
deadline for Article 50 transparency solutions to **2 December 2026**
and the deadline for national AI regulatory sandboxes to **2 December
2027**.[^ch08-4]

![Figure 8.2 — The EU AI Act Timeline](/assets/diagrams/fig-ch08-eu-ai-act-timeline.svg){width=100%}

Do not misread the deferral. Sixteen months of relief on the high-risk
deadline is time to build the Article 9/10/14 apparatus *properly* — the
risk-management file, the data governance record, the human-oversight
design — not permission to defer the discipline. An administration that
treats border-management AI as presumptively high-risk today will meet
December 2027 as a formality; one that banks the delay will meet it as a
crisis. And there is a cautionary lesson in the date itself: this
paragraph was rewritten once during the drafting of this book, because
the regulatory ground moved between two research passes weeks apart.
Assign the watch list (below) to a named owner.

For a non-EU administration, the Act functions two ways: as a
compliance question wherever EU data-exchange or EU-market vendors are
involved, and as a **free design template** — its high-risk obligation
set is, in substance, the governance apparatus Part III of this book
recommends on the merits.

## 8.3 The agentic frontier: regulation catches up to the subtitle

Three developments in the twelve months before this writing moved
regulation from "AI" to *agents specifically* — the strongest external
confirmation of this book's premise that agentic systems pose a distinct
governance problem.

**China** has made agents an explicit policy category, but the legal
distinction matters. The CAC/NDRC/MIIT *Implementation Opinions on the
Standardized Application and Innovative Development of Intelligent
Agents*, published in May 2026, define agents and set a national policy
direction — including nineteen application scenarios, standards work,
permission management, and lifecycle security. They are not, by
themselves, a sector-specific customs rule. Separately, the Interim
Measures for AI Anthropomorphic Interaction Services were scheduled to
take effect on 15 July 2026 — five days after this book's legal cut-off;
their scope is specific and should not be treated as a
generic filing, testing, or recall regime for every customs agent. A
deployment with a China nexus requires a use-case-specific review under
the PIPL/DSL/CSL stack, the applicable AI service rules, and any relevant
sector requirements.[^ch08-5]

**Korea's** AI Basic Act and its Enforcement Decree entered into force on
22 January 2026, with disclosure duties and impact assessments for
"high-impact" AI. MSIT announced an administrative-fine grace period of
at least one year; a customs enforcement context should be assessed for
high-impact status rather than presumed outside the regime.[^ch08-6]

**Singapore** published a Model AI Governance Framework **for Agentic
AI** in January 2026 and updated it with deployment cases and new
multi-agent guidance in May. It remains voluntary, but is the clearest
available statement of the controls regulators expect agentic deployments
to evidence; it will harden through procurement in exactly the Layer-3
pattern.[^ch08-7]

The pattern across all three matches Part III of this book: tiered
autonomy, human oversight, risk management, and auditability throughout.
The legal instruments differ, but the governance direction is clear:
agentic systems need more explicit boundaries than ordinary software.

## 8.4 The priority jurisdictions at a glance

Table 8.1 compresses the per-jurisdiction detail (the full profiles, with
dates and instruments, live in the appendix reference tables). The reading: **in the GCC, MENA,
and ASEAN, the operative constraint on customs AI today is data
protection law, with soft-law AI frameworks hardening through
procurement.**

**Table 8.1 — Regulatory posture, priority jurisdictions (legal cut-off:
10 July 2026).** Presented as stacked profiles; each carries four fixed
fields — *Binding AI law · Operative binding layer · Soft law shaping
procurement · Cut-off record*.

**UAE** — Binding AI law: none (no horizontal act). Operative layer:
PDPL 45/2021 (in force 2022) and DIFC Regulation 10 on autonomous
systems (enforced 2026) — the region's most AI-specific instrument.
Soft law shaping procurement: the AI Charter, the Dubai Ethical AI
Toolkit, the AI Seal. **Cut-off record:** the UAE Legislation portal
still linked the federal PDPL's regularisation period to future Executive
Regulations; no federal Executive Regulations were identified there by
10 July 2026. Do not infer their content from the six-month clause.

**Saudi Arabia** — Binding AI law: not yet. Operative layer: PDPL,
fully enforceable since September 2024, with an explicit
automated-decision objection right and an active enforcement wave.
Soft law shaping procurement: SDAIA ethics principles, GenAI
guidelines, and the AI Adoption Framework. **Cut-off record:** the
binding baseline is the PDPL and its implementing and transfer
regulations; no horizontal AI statute is treated as enacted in this
edition.

**Egypt** — Binding AI law: no. Operative layer: PDPL 151/2020 plus
Executive Regulations (Decree 816/2025, effective 2 November 2025). Soft
law: the National AI Strategy (2nd ed.). **Cut-off record:** the PDPC
identifies Law 151/2020 and Executive Regulations 816/2025 as the
operating framework; calculate licences, DPO and transition obligations
against the deploying entity and activity.

**Kuwait** — Binding AI law: no. Operative layer: the CITRA data
privacy regulation (2021). Soft law: the National AI Strategy
2025–2028 (draft). **Cut-off record:** CAIT's published strategy remains
marked *Draft*; this book does not treat it as an adopted binding AI
instrument.

**Malaysia** — Binding AI law: no. Operative layer: the PDPA as
amended 2024 (DPO duty, 72-hour breach notification, portability
phased through 2025) — with **no general automated-decision right in the
Act**. Soft law: the AIGE guidelines; the National AI Office. **Cut-off
record:** the Personal Data Protection Commissioner published its
Automated Decision-Making and Profiling Guideline in April 2026; use it
with DPIA and data-protection guidance, not as a new primary-law right.

**Singapore** — Binding AI law: no. Operative layer: the PDPA. Soft
law: the model frameworks — including the world-first **agentic**
framework (2026) — and AI Verify. **Cut-off record:** PDPC's 2024
advisory guidance already addresses personal data in AI recommendation
and decision systems; IMDA updated the voluntary agentic framework in
May 2026. Neither turns the framework into a horizontal AI statute.

**Korea** — Binding AI law: **yes** — the AI Basic Act (in force
22 January 2026), operating alongside PIPA. **Cut-off record:** its
Enforcement Decree is also in force; MSIT described at least a one-year
administrative-fine grace period. Treat January 2027 as a control-review
date, not an excuse to defer the underlying duties.

**China** — Binding AI law: **yes**, layered — the GenAI measures and
other applicable service rules over the PIPL/DSL/CSL stack
(localization, transfer control, algorithm filing). The May 2026 agent
Opinions are a policy framework, not a blanket customs-agent licence.
**Cut-off record:** service-specific rules still determine obligations;
the anthropomorphic-interaction measures scheduled for 15 July were not
yet in force at this book's cut-off.

**EU** — Binding AI law: **yes** — the AI Act, applying concurrently
with the GDPR. **Cut-off record:** the Digital Omnibus received final
Council approval on 29 June 2026, fixing the revised high-risk,
transparency and sandbox dates stated above.

The multilateral layer completes the picture: the WCO's 2025 AI/ML
report — non-binding, but the sector's common reference — establishes
human-in-the-loop, ethics, and MLOps capability as the baseline
administrations cite to each other, and notes the point every counsel
should internalize: customs data processing typically rests on **legal
obligation, not consent**, which simplifies one lawfulness question and
sharpens all the others (purpose limitation above all).[^ch08-8]

## 8.5 The portable baseline

> **A minimum design baseline — not a compliance guarantee.** The five
> controls below reduce redesign across jurisdictions; they do not certify
> a system, replace an applicability assessment, or make legal terms
> equivalent. Definitions of high impact, meaningful human involvement,
> automated decision-making, public authority, records, localisation, and
> review rights differ. Local counsel must confirm the rule, deploying
> entity, task, affected people, data path, and evidence before approval.

A program that must live across several of these jurisdictions — every
vendor's reality and many administrations' future — should not chase
compliance jurisdiction by jurisdiction. It should build once to the
strictest common denominator, which the three layers conveniently agree
on:

1. **Human oversight proportionate to autonomy** (EU Art. 14, the WCO
 baseline, Saudi automated-decision rights, Singapore's frameworks —
 and this book's Autonomy Ladder);
2. **Explainability sufficient for an affected party and an auditor** —
 the thread from GDPR Art. 22 to SDAIA's principles to SISAM's
 deliberately explainable design;
3. **Documentation and auditability by construction** — risk management
 files, data governance records, decision logs (the EU high-risk set,
 which Chapter 9 turns into an internal standard);
4. **Data residency and transfer discipline** — Chapter 3's sovereignty
 rule, here revealed as Layer-1 law rather than preference;
5. **Standards anchoring** — NIST AI RMF, ISO/IEC 42001 certification,
 and agent-specific profiles as the portable evidence that all of the
 above is real (Chapter 9 details the stack).

Build to this baseline and each new jurisdiction can begin with a delta
review rather than a program redesign. Whether the delta is small is a
legal conclusion for the named task, not an architectural assumption.

## 8.6 Turn legal requirements into operating controls

Counsel should not be asked to approve "the AI programme." That request
is too broad to answer and too vague to operate. The useful unit is a
**requirement-to-control record** for a named task. It translates a legal
or policy obligation into an observable operating fact: a requirement
for meaningful human oversight becomes a named decision owner, an
escalation threshold, a working interface, and a retained override log;
a transfer restriction becomes a deployment region, a subprocessor list,
an encryption boundary and a contract right to audit.

The record needs five columns: source and applicability; the concrete
obligation; the control that meets it; the evidence that proves the
control is operating; and the person who re-tests it when the workflow,
law or vendor changes. This is deliberately closer to an internal
control register than to a legal memo. It gives the programme office a
way to distinguish a requirement that has been read from one that has
been built. It also prevents a familiar procurement failure: accepting a
vendor's generic compliance statement when the administration needs
evidence for its own mandate, users and data.

Use a tiered review. A low-consequence Rung-1 extraction task may need a
privacy and records review plus security sign-off. A Rung-2
recommendation needs the same record, an explanation and contestability
design, and an operational owner. A Rung-3 workflow with write-capable
tools needs all of that plus an operational assurance record, a change-control path,
incident playbook and a periodic re-authorisation. The law may not say
"re-authorise" in those words; the control is still sound because an
agent's behaviour, dependencies and authority will change after the
original approval.

The programme board should see the exceptions, not every row. At each
quarterly meeting, ask: which tasks have a changed legal basis or data
flow; which controls failed their test; which vendor attestations are
overdue; which new jurisdiction creates a material delta; and which
workflow should be paused pending answer. This converts regulatory
watching from an anxious newsletter into a funded management process.
It is also the point at which the administration retains responsibility:
the vendor can supply evidence, but cannot own the applicability
judgment.

## 8.7 Regulatory proportionality: do not over-control the wrong task

The appropriate control burden follows the decision, not the technology
label. Requiring a full high-risk governance file for a read-only,
internal document extractor can delay value without adding meaningful
protection. Treating a trader-facing workflow with write-capable tools
as an ordinary chat service creates the opposite error. The portable
baseline is therefore a floor; each task receives additional controls
when its authority, affected parties, irreversibility, data sensitivity
or cross-border context demands them.

Make proportionality explicit in the applicability record. State which
controls are mandatory for this task, which are deliberately not
required and why. A Rung-1 task might have a strict data and records
control but no external notification because it does not influence an
outcome. A Rung-3 task may require an operational assurance record, release review,
contestability path and heightened retention because it changes how a
case moves. This explanation helps legal, operations and procurement
make consistent decisions across the portfolio.

Proportionality is not a shortcut around rights or security. It is a way
to direct finite assurance effort to the points where public authority
is actually exercised. The programme should periodically sample low-
risk classifications too: scope drift can turn a harmless assistant into
a consequential workflow without anyone calling it an autonomy increase.

## Decision Toolkit — Chapter 8

**The applicability checklist** (run per use case, with counsel):
1. Personal data? → record lawful basis and automated-decision duties.
2. Any adverse decision about a natural person? → keep a human decision;
   check the Ladder ceiling.
3. Data crossing a border or reaching a vendor endpoint? → apply transfer
   rules and Chapter 3's deployment patterns.
4. EU border-management nexus? → presume high risk: Annex III by 2 Dec
   2027; Article 50 transparency by 2 Dec 2026.
5. China or Korea nexus? → classify the applicable service and
   high-impact duties with local counsel.
6. Government soft-law instruments in the tender? → treat them as binding
   procurement requirements.

**Vendor regulatory questions:** Show the jurisdictional assessment, its
owner and evidence; show Article-14-class human oversight and decision
logging; show exactly where data resides. “Fully compliant” is returned
for completion.

**Standing regulatory review (after the cut-off):** EU implementing and
delegated acts; China’s sector-specific rules; Korea’s fine-enforcement
date; Kuwait’s strategy status; and UAE federal PDPL Executive
Regulations. Name an owner, record the source and review quarterly.

## Key Takeaways

- Regulation reaches customs AI in three layers: data protection law
 (binding everywhere, on day one), AI-specific statutes (EU, China,
 Korea — so far), and soft law that hardens through procurement.
- In the GCC, MENA, and ASEAN, the operative constraint today is data
 protection — above all the automated-decision provisions, which the
 Autonomy Ladder satisfies by design.
- Treat border-management AI as presumptively high-risk under the EU AI
 Act: Annex III compliance is due 2 December 2027 (post-Omnibus), with
 Article 50 transparency solutions due 2 December 2026 — and the
 obligation set
 doubles as a free governance template worth building now.
- Regulation and policy have reached *agents specifically* — China's
 national policy framework, Korea's high-impact duties, Singapore's
 agentic framework — and converge on tiered autonomy plus mandated
 oversight: external confirmation of this book's architecture.
- Build once to the portable baseline (oversight, explainability,
 auditability, residency, standards anchoring); handle each jurisdiction
 as a delta, and keep a named owner on the post-cut-off regulatory review.

---

## Endnotes

[^ch08-1]: Saudi PDPL (Royal Decree M/19 as amended; fully enforceable since
 14 Sep 2024): right to object to decisions based solely on automated
 processing. EU GDPR Art. 22. Malaysia PDPA: no general statutory
 automated-decision right; its Commissioner published the ADMP guideline
 in April 2026. <!-- bib: iclg_saudi_dp2025, gdpr2016679,
 malaysia_admp_2026 -->

[^ch08-2]: UAE Charter and Dubai Ethical AI Toolkit; SDAIA ethics principles,
 GenAI Guidelines and AI Adoption Framework; Malaysia AIGE; Singapore
 model frameworks. <!-- bib: ailawguide_uae2026,
 sdaia_regs, fpf_malaysia2025, lw_singapore2026 -->

[^ch08-3]: Regulation (EU) 2024/1689, Annex III (law enforcement; migration,
 asylum and border management) and Arts. 9–15 (high-risk obligations);
 extraterritorial scope; penalties to EUR 35 M / 7% of global turnover
 for prohibited practices. <!-- bib: ec_navigating_aiact -->

[^ch08-4]: Digital Omnibus on AI, final Council adoption 29 Jun 2026:
 standalone Annex III high-risk → 2 Dec 2027; embedded (Annex I) →
 2 Aug 2028; Article 50 transparency solutions → 2 Dec 2026; national
 regulatory sandboxes → 2 Dec 2027. <!-- bib:
 consilium_omnibus_final_2026 -->

[^ch08-5]: CAC/NDRC/MIIT, *Implementation Opinions* (May 2026): policy
 framework, agent definition and lifecycle-security direction—not a
 blanket customs-agent rule. The named anthropomorphic-service measures
 were scheduled for 15 Jul and outside the cut-off; local counsel must
 classify the use case. <!-- bib:
 cac_intelligent_agents_opinions2026,
 cac_anthropomorphic_services2026 -->

[^ch08-6]: Korea AI Basic Act (Framework Act on the Development of AI and
 Establishment of Trust) and Enforcement Decree, in force 22 Jan 2026;
 disclosure and impact assessment for high-impact AI; administrative fines
 subject to at least a one-year grace period. <!-- bib:
 cset_korea_ai_law_2025, msit_korea_ai_basic_inforce_2026 -->

[^ch08-7]: IMDA / AI Verify Foundation, Model AI Governance Framework for
 Agentic AI (launched Jan 2026; updated May 2026) — described as the
 first framework of its kind.
 <!-- bib: imda_mgf_agentic_2026 -->

[^ch08-8]: WCO Smart Customs Project, *Detailed Report on the Adoption of AI
 and ML in Customs* (Mar 2025): HITL as baseline; customs processing
 grounded in legal obligation rather than consent; anonymization vs.
 pseudonymization distinction. <!-- bib: wco_scp_report2025 -->
