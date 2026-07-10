---
title: "GenAI First: Document Intelligence as the Entry Point"
part: "I — The Landscape"
chapter: 3
status: review
version: 0.3
last-updated: 2026-07-09
---

## The archive room

Every customs administration has one — sometimes physical, sometimes a file
share standing in for one. Scanned invoices attached to declarations as
image PDFs, unreadable by any system. Certificates of origin in three
languages, filed but not searchable. Ten years of classification rulings
that exist, technically, but that a duty officer cannot query at 2 a.m.
when a container is waiting. Post-clearance audit selecting cases from
spreadsheets because the documents behind the declarations are, for all
practical purposes, dark.

Now recall the vendor meeting from Chapter 2, with its autonomous agents
gliding across systems. Both realities are true at once, and the distance
between them is the most under-discussed fact in customs AI. Agents run on
information access. An agent asked to investigate a flagged declaration
must *read* the invoice, *search* the rulings, *check* the certificate —
and it can do none of that if the invoice is a photograph, the rulings are
a filing cabinet, and the certificate is in a language the pipeline never
handled.

This chapter makes the unfashionable argument that will save your program:
**start with generative AI applied to documents and knowledge — not with
agents.** Not because agents are hype (Part I has argued they are not), but
because document intelligence is where the value is fastest, the risk is
lowest, and every deliverable doubles as a prerequisite for the agentic
stage. And it makes a second argument that is not unfashionable so much as
non-negotiable: all of it runs on **sovereign deployment** — on-premises or
accredited government cloud. A customs administration does not send trade
data to a consumer subscription and an unvetted API. That territory is
excluded, and this chapter shows what to build instead.

## 3.1 The readiness gap nobody presents at conferences

International AI reports — including the WCO's own 2025 survey of AI/ML
adoption — describe an impressive frontier: image-based inspection in
Korea, risk analytics in China, data-driven targeting in the Netherlands.
What they describe less often is the median. Across the administrations
the author's practice touches — GCC, MENA, Southeast Asia — the honest
baseline usually includes several of the following:

- Supporting documents (invoices, packing lists, certificates) captured as
 scans or photographs, with no reliable text extraction;
- Institutional knowledge — rulings, internal circulars, procedure manuals
 — stored as files, searchable only by filename;
- Officers manually re-keying data that exists in a document two windows
 away;
- Multilingual traffic (Arabic–English, Malay–English–Chinese) handled by
 whoever on shift reads the language;
- Trader enquiries answered from memory, with response quality depending
 on which officer picks up the case.

None of this is a scandal; it is the normal state of document-heavy
government everywhere. But it has a strategic consequence: **an
administration in this state cannot deploy a trustworthy agent**, because
the agent's tools would be pointing at darkness. The good news is that the
same technology wave that produced agents also produced — first — the best
document-understanding capability in computing history. Use it in order.

## 3.2 The Maturity Ladder

This book's second framework (Figure 3.1) sequences the journey. Where the
Autonomy Ladder (Chapter 2) grades *how much an AI may decide*, the
Maturity Ladder grades *what your administration is ready to deploy*.

![Figure 3.1 — The Maturity Ladder](/assets/diagrams/fig-ch03-maturity-ladder.svg){width=100%}

**Rung 1 — Document Intelligence.** Machines that read: OCR and extraction
from declarations and supporting documents, classification of document
types, structured search over regulations and rulings, translation.
Value: hours returned to officers, data quality at the source, the end of
re-keying. Prerequisite: almost none beyond the documents themselves —
which is the point. Typical autonomy: L1, occasionally L2.

**Rung 2 — GenAI Assistants.** Machines that read *and* draft: assistants
that answer officers' questions from the regulation corpus with citations,
draft replies to trader enquiries, summarize case files, prepare first-cut
audit reports. Value: consistency and speed of knowledge work.
Prerequisite: Rung 1 — an assistant is only as good as the corpus it can
search. Typical autonomy: L1–L2.

**Rung 3 — AI Agents.** Machines that read, draft, *and act*: the
supervised and autonomous agents of Chapter 2, working across systems.
Value: end-to-end task completion. Prerequisite: Rungs 1 and 2, plus the
governance apparatus of Part III. Typical autonomy: L3, exceptionally L4.

The rungs are not marketing tiers; they are dependencies. Rung 1 creates
the machine-readable substrate. Rung 2 creates the retrieval infrastructure,
the feedback loops, and — critically — an officer corps that has worked
with AI output daily and learned, at low stakes, when to trust it. Rung 3
consumes all of it. Administrations that skip to Rung 3 do not skip the
work; they discover it mid-project, at agent prices.

Rung 1 in the field looks like Indian Customs' recent work: unsupervised
machine learning that codifies free-text supplier names from declarations
into structured entities — unglamorous plumbing that then enables
cross-importer undervaluation comparison and network analytics, with the
administration reporting higher hit rates and reduced dwell time as the
downstream result.[^ch03-1] Note the shape of that sentence: the *document
work* enabled the *targeting value*. And note something else, visible
across the public record: verified Rung-1 metrics are scarce, because
administrations publish outcomes at the targeting and seizure layer, where
the headlines live — the document layer rarely gets its own press release.
That scarcity is not a reason to skip the rung; it is a reason to
instrument your own program properly (Chapter 5's measurement templates
exist for exactly this).

## 3.3 The quick-wins catalog

Five workloads deliver the fastest verified value at Rungs 1–2
(Figure 3.3). Each is
listed with its verification design — because GenAI's characteristic
failure is fluent error, and a use case without a verification pattern is
not a use case.

![Figure 3.3 — The Quick-Wins Catalog](/assets/diagrams/fig-ch03-quick-wins.svg){width=100%}

**1. Declaration-support document extraction.** Read invoices, packing
lists, bills of lading, certificates; extract line items, values, parties,
origins; reconcile against the declaration. Verification: extracted fields
are shown side-by-side with the source image for officer confirmation (L2);
discrepancies auto-flagged. This single workload attacks re-keying,
valuation data quality, and inspection preparation at once.

**2. Regulation and ruling search (retrieval-augmented).** A searchable,
citation-backed corpus of tariff schedules, national regulations, rulings,
and circulars, answering officers' questions with the *source paragraph
attached*. Verification: the citation is the verification — answers without
a retrievable source are displayed as "no grounded answer found," never
improvised. This is the single highest-leverage build, because every later
assistant and agent will stand on it.

**3. Trader correspondence drafting.** First drafts of replies to
enquiries, requests for information, and deficiency notices, grounded in
the corpus from workload 2. Verification: officer review before send (L1);
templates constrain tone and legal phrasing.

**4. Multilingual processing.** Translation and cross-lingual extraction
for document traffic in the administration's real language mix.
Verification: translated fields carry the original alongside; legally
consequential passages flagged for human translation.

**5. Case-file summarization.** Condense a post-clearance audit file or an
investigation dossier into a structured brief with pointers back to source
documents. Verification: every statement in the brief links to its source
page — the same "grounding" discipline as workload 2.

Two properties unite the five. First, each produces measurable before/after
numbers — minutes per document, enquiries per officer-day, retrieval
precision — which build the business-case muscle Chapter 5 needs. Second,
each fails safely: a wrong draft caught in review costs minutes, not a
seizure or a lawsuit. This is what "start where the blast radius is small"
means in practice.

The best-documented Rung-2 deployment is Korean. On top of a decade of
data infrastructure and a portfolio of eleven AI models, the Korea Customs
Service added a generative layer — "AI Innovation in Customs" — that lets
any officer query import data in natural language; the surrounding program
cut high-risk cargo analysis from roughly an hour to under a minute while
absorbing a near-tripling of e-commerce volume, with estimated annual
savings of about USD 92 million (2025, administration-stated).[^ch03-2] Two
readings of that case matter here. The obvious one: the value is real and
large. The instructive one: the GenAI layer *arrived last*, on top of
years of Rung-1 data work — Korea climbed the ladder in order, which is
precisely why the top rung held. Brazil points the same direction from the
other hemisphere: after a decade of running SISAM's explainable selection
models, the administration's stated next step is adding LLMs for product
descriptions — models first, language layer second.[^ch03-3]

> **Field note — HMRC, generative assistance at Rung 1–2.** The UK's tax
> and customs authority illustrates the entry rungs at national scale.
> As part of a decade-long, £175M digital-first transformation — and
> under a first-ever Chief AI Officer — HMRC rolled out Microsoft 365
> Copilot to some 50,000 staff for document summarization and routine
> administrative work, and reported a trial finding of roughly 26
> minutes saved per employee per day; alongside it, generative agents
> were piloted to summarize customer issues so that a human agent
> already has context before the conversation begins.[^ch03-4] Two
> things make this a Rung-1/2 exemplar rather than a cautionary one: the
> work is assistive (summarize, draft, retrieve) rather than
> autonomous, and it sits inside the UK Government's AI Playbook, which
> mandates meaningful human control and a "Scan, Pilot, Scale"
> progression — the ladder discipline of this book, in a national
> government's own words.

## 3.4 The deployment reality: sovereign or not at all

Here is the conversation that disqualifies more vendors than any other.
The demonstration ran beautifully — on the vendor's cloud tenant, against
a public frontier-model API, with your sample documents uploaded through a
browser. For a customs administration, that architecture is not a starting
point to negotiate from. It is **excluded territory**: consumer
subscriptions, developer API keys billed to a credit card, and any pathway
that moves trade data across borders to infrastructure your government has
not accredited.

The reasons are not technophobia. Customs data is commercially sensitive
(traders' prices, suppliers, volumes), legally protected (national data
protection law, and in many jurisdictions customs secrecy provisions), and
strategically revealing (a country's trade flows in fine grain).
Cross-border transfer rules, government cloud accreditation regimes, and —
increasingly — AI-specific regulation (Chapter 8) all bite here. So does
procurement law: a subscription click-through is not a government contract.

What remains is a genuine engineering choice among three sovereign
patterns:

**On-premises models.** Open-weight models (the capable mid-size class has
crossed the "good enough for documents" threshold) running on
administration hardware. Full control and jurisdiction; the cost is
hardware, MLOps skill, and accepting that on-prem models trail the
frontier. Best fit: the most sensitive workloads, air-gap requirements,
administrations with an existing data-center practice.

**Sovereign / government cloud.** Frontier or near-frontier models hosted
in an in-country region that the competent government authority has
recognised for the relevant data class and use — where such a lawful,
accredited option exists. A commercial region, a data-centre address, or a
vendor's use of the word *sovereign* is not accreditation. Access to
stronger models and managed operations; the cost is dependence on the
accreditation regime and contractual rather than physical control. Best
fit: the default for administrations whose counsel and security authority
have confirmed the provider, service, subprocessors, data path, and
contract for the named workload.

**Hybrid.** Sensitive extraction on-premises; heavier reasoning on
de-identified or non-sensitive content in the sovereign cloud. The
realistic end-state for most administrations — and the pattern that
requires the most explicit data-classification discipline, because the
boundary is now a policy, not a wall.

The decision is a matrix, not an ideology: classify the workload's data
sensitivity, check the jurisdiction's transfer and accreditation rules,
then choose the *least restrictive pattern that is lawful and accreditable*
— because unnecessary restriction has a cost too, paid in model quality
and delivery speed. Figure 3.2 (deployment decision tree) walks the
sequence; Chapter 10 deepens the security architecture.

![Figure 3.2 — Deployment Decision Tree](/assets/diagrams/fig-ch03-deployment-tree.svg){width=100%}

One vendor-facing consequence deserves its own sentence: **"which models,
running where, under whose jurisdiction, with what data residency
guarantees" is a mandatory RFP question**, and "our platform is
cloud-based" is not an answer to it.

**Move the excluded territory into daylight.** A strict policy without a
transition path can drive experimental use underground. Give teams a
sanctioned route: inventory existing subscriptions and API keys; stop new
sensitive uploads; preserve evidence needed for investigation; offer a
time-boxed sandbox using public, synthetic, or properly de-identified
data; then migrate, replace, or retire each workflow against a named date.
Where immediate shutdown would interrupt a critical service, counsel and
security approve a documented containment plan with minimum data,
restricted identities, monitoring, and expiry. This is not permission to
continue an unlawful transfer. It is the operating mechanism that turns
an excluded-territory rule into observable risk reduction rather than
shadow IT.

## 3.5 What GenAI-first buys the agentic future

Return to the archive room, eighteen months into a GenAI-first program.
The documents are machine-readable at ingestion. The rulings corpus
answers questions with citations. Officers have confirmed, corrected, and
occasionally overruled AI output thousands of times — generating exactly
the feedback data that measures reliability per task. Legal has approved
grounding-and-citation as a verification standard. IT operates a model
serving stack with logging and change control. The business case file
contains real before/after numbers from five workloads.

Now read Chapter 2's conditions for granting L3 autonomy, and notice that
this administration has quietly met the prerequisites: the tools an agent
would use exist and are governed; the evidence base for "one rung at a
time" is accumulating in production; the officers who will supervise
agents have already developed calibrated trust. The GenAI-first program
was never a detour from the agentic strategy. It *is* the agentic
strategy, stage one.

## 3.6 The first agent should close a loop, not open a frontier

The useful distinction for an administration is not between a "GenAI
project" and an "agentic project." It is between a system that makes a
person's next action easier and a system that can complete a **bounded,
observable loop**. The first loop should be deliberately small: watch a
defined exception queue; gather already-authorized evidence; draft a
case summary with citations; ask an officer for a decision; then write
only the approved result back to the case-management system. It may save
time, but its real output is operational evidence: where data is
missing, which exceptions recur, how often the officer changes the
recommendation, what each completed case costs, and which tool
permission created value.

This is the frontier model applied with enterprise discipline.
McKinsey's 2025 review describes a gap between broadly deployed
horizontal copilots and workflow-specific vertical systems that can be
measured; Deloitte's government outlook makes the same observation in
public-sector language: most early agent programs automate a legacy
process rather than redesigning it.[^ch03-5] For customs, the answer is
neither a generic chat interface nor a fictional autonomous border. It
is a sequence of case loops with a named owner, baseline, escalation
point, and write permission. A loop that cannot be measured or stopped
is not a first agent; it is an unpriced liability.

The WCO's 2025 AI/ML report supplies the older but indispensable half
of this design: data management, legal and ethical controls,
cost-benefit analysis, cybersecurity, interoperability, pilot testing,
and workforce capability.[^ch03-6] Agentic AI does not replace that
foundation. It adds a harder operating question: *after the model has
read the record, what may it do next?* The answer must remain a business
rule, not a vendor default. That is why the first loop has a human gate
and why each later loop earns, rather than assumes, one additional
permission.

## 3.7 Treat the GenAI layer as a public-service product

The most reliable early gains come from products that officers use every
day, not from a demonstration available only to an innovation team.
Give each GenAI service a product owner, a defined user group, a service
promise and a backlog fed by real corrections. For a grounded procedure
assistant, the promise might be: current approved sources, citations on
every answer, an explicit "I do not know" route, and a response time
that fits the shift. For document intelligence, it might be: a source
image next to every extracted field, an exception queue, and a feedback
mechanism that improves recurring errors.

This product framing makes adoption measurable. Track eligible users,
unprompted repeat use, time saved on the named step, correction reasons,
unanswered questions and source freshness. Interview both frequent and
non-users. A low adoption rate may signal poor quality, but it can also
reveal an interface that does not fit the actual desk workflow, a
missing language, or a supervisor who has not authorised use. These are
operating facts with owners, not evidence that the model is magical or
useless.

It also creates the governance habit needed for agents. A product
backlog separates harmless usability improvements from changes to data,
sources, tools or authority that require a formal gate. A release note
lets supervisors know what changed. A service-level review keeps the
knowledge base alive. By the time the administration introduces its
first bounded agent, it already knows how to run AI as a public-service
product rather than an installed software package.

## Decision Toolkit — Chapter 3

**Quick-wins selection matrix.** Score each candidate workload 1–5 on:
(a) officer-hours consumed today, (b) document/data readiness, (c) failure
tolerance (can a wrong output be caught cheaply?), (d) measurability of
the outcome. Deploy the top scorers; defer anything scoring low on (c)
regardless of its score elsewhere.

**Deployment pattern selector (summary of Figure 3.2):**
1. Classify the workload's data (public / internal / sensitive trade data /
 legally protected).
2. Map lawful hosting options in your jurisdiction (accredited in-country
 cloud region? transfer restrictions? customs secrecy provisions?).
3. Choose the least restrictive lawful pattern; document the reasoning.
4. Re-validate when regulation, accreditation, or workload sensitivity
 changes — the choice is a standing decision, not a one-off.

**The verification rule.** No GenAI workload ships without a named
verification pattern (side-by-side confirmation, grounding with citations,
review-before-send, sampling). "The model is very accurate" is not a
verification pattern.

## Key Takeaways

- Agents run on information access; most administrations' documents and
 knowledge are not yet machine-accessible. Fix that first — it is fast,
 low-risk, and measurable.
- The Maturity Ladder — Document Intelligence → GenAI Assistants → AI
 Agents — is a dependency chain, not a menu. Skipping rungs defers the
 work to the most expensive stage.
- Five quick wins carry the entry phase: document extraction, grounded
 regulation search, correspondence drafting, multilingual processing,
 case-file summarization. Each ships with a verification design or not
 at all.
- Sovereign deployment is non-negotiable: on-premises, accredited
 government cloud, or hybrid. Consumer subscriptions and unvetted APIs
 are excluded territory — put the question in every RFP.
- A GenAI-first program is not a delay to the agentic strategy; it builds
 the substrate, the evidence, and the workforce trust that L3 autonomy
 will later require.
- The first agent should complete a bounded case loop with a named owner,
  baseline, human gate and reversible write-back — not imitate an
  autonomous border in a demo.

---

## Endnotes

[^ch03-1]: Indian Customs (NCTC), reported in WCO News 109 (Issue 1, 2026) and
 WCO News 108 (Issue 3, 2025): unsupervised ML codification of
 free-text supplier entities within the Integrated Risk Management
 System; KPI gains reported qualitatively (no single headline
 percentage published). <!-- bib: wconews109_india2026 -->

[^ch03-2]: Korea Customs Service, WCO News 108 (Issue 3, 2025) and APEC SCCP
 (2025): analysis time ~1 hour → under 1 minute (≈98%) against a 2.85×
 e-commerce volume surge; estimated savings KRW 125.7 bn (~USD 92 M,
 2025). Figures administration-stated; technology precisely identified
 (ML/DL fusion of X-ray imagery and manifest data; GenAI query layer).
 <!-- bib: wconews108_korea -->

[^ch03-3]: Brazil Receita Federal, WCO News 105 (2024): stated plan to extend
 SISAM (Bayesian-network selection system in production since 2014)
 with deep learning and LLMs for product descriptions. Primary.
 <!-- bib: wconews105_brazil2024, jambeiro2019_sisam -->

[^ch03-4]: HMRC generative-AI deployment: £175M decade-long digital-first
 transformation; Microsoft 365 Copilot rolled out to ~50,000 staff
 with a trial finding of ~26 minutes saved per employee per day;
 generative agents piloted for customer-issue summarization; governed
 under the UK Government's *AI Playbook* (Feb 2025) mandating
 meaningful human control and a "Scan, Pilot, Scale" methodology.
 UK government / trade-press reporting, 2025–2026; cited as an
 adjacent government exemplar. <!-- bib: hmrc_genai2026,
 ukgov_ai_playbook2025 -->

[^ch03-5]: McKinsey, *Seizing the Agentic AI Advantage* (2025), frames
workflow-specific vertical agents as the route out of the "GenAI
paradox"; Deloitte, *GovTech Trends 2026*, reports that only 11% of
surveyed organizations had agentic systems in production and attributes
much of the gap to legacy-process automation rather than redesign. Both
are practice-reported, cross-sector context rather than customs forecasts.
<!-- bib: mckinsey_agentic_advantage2025, deloitte_govtech2026 -->

[^ch03-6]: WCO Smart Customs Project, *Detailed Report on the Adoption of
AI and ML in Customs* (2025), covers the ML-era foundations—data, legal
and ethical controls, cybersecurity, interoperability, cost-benefit
analysis, pilots and skills—that agentic workflows inherit.
<!-- bib: wco_scp_report2025 -->
