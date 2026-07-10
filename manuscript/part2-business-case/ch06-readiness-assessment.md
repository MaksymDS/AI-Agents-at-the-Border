---
title: "Readiness Assessment"
part: "II — The Business Case"
chapter: 6
status: review
version: 0.3
last-updated: 2026-07-09
---

## Two assessments, one desk

They arrive in the same week. The vendor's readiness assessment — a
handsome document, delivered free — concludes that the administration is
"well positioned to begin its AI journey" and recommends, by remarkable
coincidence, beginning it with the vendor's platform. The internal IT
memo, written by people who maintain the declaration system at 2 a.m.,
concludes that the administration is not remotely ready and lists
eleven prerequisites, several of them multi-year.

Both documents are answering a badly posed question. "Are we ready for
AI?" has no answer, because *AI* is not one thing (Chapter 2) and
*ready* is not one threshold (Chapter 3). The vendor's document answers
"is there budget?"; the IT memo answers "could we run the frontier
tomorrow?" — and neither answers the question the Director General
actually needs answered: **ready for what, exactly, and what is the
evidence?**

This chapter builds the instrument that answers it: what the sector
already provides (use it), what an honest assessment measures (evidence,
not self-perception), and how to read the results as a routing decision
rather than a grade. The full instrument is Appendix A; this chapter is
its logic.

## 6.1 Readiness is a routing question, not a grade

Three design principles separate an honest instrument from a
sales-funnel questionnaire.

**Readiness belongs to a named use case, not to the administration as a
single permanent grade.** A weak enterprise data estate can coexist with
a production-ready, read-only procedure assistant over an approved
corpus. Conversely, a sophisticated analytics unit may still be unready
for one write-capable, trader-facing agent. The instrument identifies only
the gaps that bind the proposed task; it should never postpone every
low-risk use case until the institution is "ready for AI."

**Readiness is per rung and per use case.** The Maturity Ladder gave the
frame: an administration can be fully ready for document intelligence
(Rung 1 requires little beyond documents and will), partially ready for
grounded assistants (Rung 2 requires the corpus discipline of Chapter
11), and years from supervised agents (Rung 3 requires the governance
apparatus of Part III). A single readiness score averages these into
noise. The honest output is a **profile** — dimension by dimension
(Figure 6.1) — and a **ceiling**: the highest rung each dimension currently supports.

![Figure 6.1 — The Readiness Profile](/assets/diagrams/fig-ch06-readiness-profile.svg){width=100%}

**Evidence, not self-perception.** Self-assessments inflate; every
question in the instrument therefore demands an artifact, not an
opinion. Not "do we have leadership sponsorship?" but *"name the
executive owner; show the decision they made last quarter."* Not "is
our data ready?" but *"what share of last month's declarations had
machine-readable supporting documents — show the measurement."* The
artifact rule is the entire difference between the two documents on the
DG's desk.

**The result must route, not rank.** Nobody needs to know they scored
3.2 out of 5. The output that changes behavior is a routing decision:
which use cases can start now, at which rung, and which two dimensions
are the binding constraints to invest in. An assessment that ends in a
score has ended one meeting too early.

## 6.2 Use the sector's instruments first

Customs is unusually well served here, and an administration should
exhaust the shared infrastructure before commissioning anything bespoke.
The **WCO's AI/ML Readiness Self-Assessment Tool** (released January
2025 under the Smart Customs Project) exists precisely for this
diagnostic: it evaluates readiness, identifies weaknesses, surfaces
candidate use cases, and frames capacity-building. Its underlying
framework spans **eleven aspects** — strategy and vision, data
management, leadership and governance, policy arrangements, legal
framework, technology and tools, skills and training, stakeholder
engagement, costs, innovation, and future plans — and the companion
BACUDA assessment compresses preparedness into **five pillars**:
governance, data governance, technology infrastructure, organizational
culture and leadership, and analytical capabilities.[^ch06-1] The
interactive tool sits in the WCO Members' area — one request to the
national contact point away — and pairs naturally with the BACUDA
workshop track from Chapter 14.

One number from the tool's companion case study deserves permanent
residence in every readiness discussion, as a calibration against both
vendor optimism and internal despair: China's customs administration —
by any measure the sector's scale frontier — reported a portfolio of
**62 "smart models," of which 22 were in pilot and 2 fully
operational**.[^ch06-2] If the frontier converts models to production
at that ratio, an administration whose honest answer is "we have three
pilots and nothing in production" is not behind the field. It *is* the
field.

## 6.3 The instrument's six dimensions

Appendix A consolidates the WCO aspects, the BACUDA pillars, and this
book's frameworks into six dimensions, each scored against artifacts,
each expressed as a rung ceiling. In summary:

**1. Leadership and ownership.** A named executive owner (Chapter 1's
positioning snapshot asked; this dimension verifies); mandates being
signed by people, not committees; the ministry conversation of Chapter 5
survivable today. *Ceiling logic:* without a living owner, the ceiling
is Rung 1 regardless of everything else — nothing above it survives its
first incident.

**2. Legal and sovereignty environment.** The Chapter 8 applicability
checklist run and answered; a lawful deployment pattern identified
(Chapter 3's tree has a terminating node in this jurisdiction);
data-sharing agreements inventoried for AI clauses (Chapter 11). *The
artifact:* counsel's written opinion, not counsel's verbal comfort.

**3. Data estate.** The Chapter 11 readiness check per candidate use
case: machine-readable share measured, corpus inventory drafted, system
interfaces listed, feedback capture designed. This dimension is scored
per use case — it is where "readiness" most sharply refuses to be a
single number.

**4. Technology and operations.** Not "do we have GPUs" but: an
identity and permissions fabric agents could run under (Chapters 9–10);
logging that could hold a trajectory; a change-control process that
could absorb the four-change rule (Chapter 13); and an honest statement
of what the estate's integration surfaces look like. Hardware is the
purchasable part; these are not.

**5. People and skills.** The three audiences of Chapter 14 mapped:
literacy floor status, mandate-signer fluency, and the specialist cadre
— existing, planned, or absent. Given the evidence that skills are the
binding constraint sector-wide, this dimension gets double weight in
the routing decision.[^ch06-3]

**6. Governance apparatus.** The Part III paperwork in whatever state
it exists: an AI inventory (even empty — its existence is the
artifact), a draft oversight routing rule, an incident path that names
a freezer. Administrations rarely score high here before their first
deployment — the dimension exists to make the gap visible and sized,
not to shame it.

## 6.4 Reading the profile honestly

The routing patterns recur across administrations, and three deserve
naming.

**High technology, low governance — the dangerous quadrant.** The
infrastructure exists, often from the analytics wave; the mandate
discipline does not. This profile *feels* ready and produces the
incidents Part III exists to prevent. Routing: cap at Rung 2 until
dimension 6 catches up — the constraint is deliberately artificial and
deliberately visible.

**Low everything — the honest start.** No owner confirmed, data dark,
cadre absent. Routing: Rung 1 anyway. This is Chapter 3's entire
argument — document intelligence requires little, repairs the data
estate as it runs, and manufactures the artifacts every other dimension
needs. "Not ready" is a reason to start at the bottom rung, never a
reason to wait; readiness-as-procrastination is the failure mode of
administrations that commission assessments annually and deploy
nothing.

**Ready in patches — the normal case.** Declarations data strong,
rulings corpus absent; owner engaged, counsel unbriefed. Routing: match
use cases to the patches (the Chapter 4 scoring already weights data
readiness) and aim the next two quarters' investment at the two lowest
dimensions. The profile is a portfolio input, not a verdict.

However it reads, the assessment is a **delta tracker, not a
certificate**: re-run it at a fixed cadence, score movement against the
prior profile, and treat a dimension that hasn't moved in a year as a
leadership finding — because by construction, every dimension in this
instrument is movable by decisions, and five of the six are movable
without a procurement.

## 6.5 Readiness is a portfolio constraint, not a score

The assessment is often misused as a verdict: a low score becomes a
reason to wait; a high score becomes permission to buy a large platform.
Both readings lose the point. Readiness is a **constraint map**. A weak
data foundation may block L3 case closure but not a grounded regulation
assistant. Missing sovereign hosting may block sensitive inference but
not on-premises document extraction. Limited agent-security capability
may prohibit write tools while still allowing a read-only case-preparation
loop. The answer is not "ready" or "not ready"; it is *ready for which
workload, at which rung, with which guardrails?*

This creates a deliberate **green-light path**. An internal document
search or summarisation service can start at Rung 1/L1 when its corpus is
approved, access is read-only, sources are cited, retention is controlled,
and a human uses the output. It does not wait for enterprise-wide
knowledge graphs, perfect historical labels, or an L3 governance board.
The same administration may simultaneously cap a trader-facing or
write-capable task at pilot. Readiness should sequence value and control,
not convert caution into paralysis.

Translate each weak dimension into a funded enabling workstream with an
owner and a date. Data weakness becomes a selected corpus and feedback
loop; architecture weakness becomes identity, APIs and logging; skills
weakness becomes named operational supervisors and a training cycle;
governance weakness becomes mandates, safety cases and a gate panel.
Then let the readiness profile shape the first portfolio. This is how a
smaller administration moves now without pretending it has the estate
of Korea Customs, and how a larger administration avoids funding a
frontier pilot that its own controls cannot yet contain.[^ch06-4]

## 6.6 The 90-day readiness sprint

The assessment should end with a short programme of evidence, not a
long list of maturity aspirations. Pick the two binding constraints for
the chosen first case loop and define a 90-day readiness sprint. A
typical sprint produces a named corpus with an owner and update rule; a
data-flow and residency map; a minimum identity and logging pattern; a
mandate card and review panel; a representative evaluation set; and a
trained operational supervisor. These are modest deliverables, but they
decide whether a pilot can be trusted.

Give every deliverable a test, not merely a status. The corpus is ready
when an officer can find a current source and identify its owner. The
data flow is ready when counsel and security can see every transfer. The
evaluation set is ready when its cases reflect the document types and
exceptions that matter, not only clean examples. The supervisor model is
ready when a real shift can absorb the anticipated exception queue.
Where a test fails, reduce scope or rung rather than relabeling the gap
as a risk accepted by default.

At day 90, leadership chooses among three legitimate outcomes: begin a
bounded pilot; extend a specific enabling workstream with a named owner;
or defer the use case and choose another that fits current constraints.
None is a wasted result. What wastes time is beginning a technical build
while the legal, data and operating conditions remain unnamed.

## 6.7 Readiness review is an executive operating rhythm

Once the first pilot begins, readiness stops being a preparatory
exercise. It becomes a recurring operating review. Hold a brief monthly
task review and a quarterly portfolio review. The task review asks
whether the live evidence still supports the current rung: are the
sources current, the interfaces reliable, the supervisors available,
the security controls working and the mandate unchanged? The portfolio
review asks where common constraints are slowing several workflows and
whether a shared investment—identity, corpus stewardship, evaluation or
training—will remove more friction than a new isolated pilot.

Use a simple rule for escalation: a failed readiness artifact reduces
authority before it becomes an incident. If the corpus owner cannot
confirm a material source is current, the assistant may need to abstain.
If the data contract breaks, a task may continue only on the route that
does not rely on that feed. If human review capacity falls below the
safe queue threshold, the agent narrows its scope. These are not signs
that the enterprise was never ready; they are the designed controls that
let it operate responsibly under changing conditions.

The executive benefit is focus. A quarterly heat map that names the two
constraints per priority task gives finance and leadership an investment
agenda anchored in service outcomes. It also makes progress observable:
the programme is not "maturing" because it bought a platform, but
because a documented constraint no longer caps a named decision.

## Decision Toolkit — Chapter 6

**The assessment protocol** (full instrument in Appendix A): six
dimensions · every answer an artifact · scored as rung ceilings per
dimension · data estate scored per candidate use case · skills
double-weighted · output = routing table (start-now use cases at their
rungs; two binding constraints; next review date). Run internally
first; use the WCO tool via the national contact point as the external
calibration; accept vendor assessments as market intelligence about the
vendor.

**The artifact rule** (adopt verbatim): no readiness answer without a
named document, measurement, or decision behind it. "We have leadership
support" is replaced by the owner's name and their last AI decision;
"our data is good" is replaced by last month's machine-readable share.

**The calibration line** (for the meeting where despair or hype
appears): the sector's scale frontier runs 62 models to 2 in full
production (the funnel of Figure 1.2). Readiness is not about being ahead of that — it is about
knowing your profile and routing accordingly.

## Key Takeaways

- "Are we ready for AI?" is unanswerable; "ready for which rung, per
 dimension, on what evidence" is the honest question — and the output
 is a routing decision, not a score.
- Use the sector's shared instruments first: the WCO Readiness
 Self-Assessment Tool (eleven aspects, via the national contact point)
 and the BACUDA five-pillar frame; commission nothing bespoke until
 they are exhausted.
- Six dimensions, every answer an artifact: leadership, legal and
 sovereignty, data estate (per use case), technology and operations,
 people and skills (double-weighted), governance apparatus.
- Read profiles as routing: high-tech/low-governance caps at Rung 2 by
 design; low-everything starts Rung 1 anyway — "not ready" is never a
 reason to wait, only a reason to start at the bottom rung.
- The frontier converts 62 models into 2 production systems: calibrate
 ambition and despair against that ratio, and re-run the assessment as
 a delta tracker, not a certificate.

---

## Endnotes

[^ch06-1]: WCO Smart Customs Project: AI/ML Readiness Self-Assessment
 Tool released January 2025 (Members' website and Smart Customs
 Community Portal; access via national contact points); stated aims
 (evaluate readiness, identify weaknesses, explore use cases, build
 capacity); the eleven-aspect framework from the China study
 mission; the BACUDA five-pillar readiness frame (governance, data
 governance, technology infrastructure, organizational culture &
 leadership, analytical capabilities). <!-- bib:
 wco_scp_report2025, wco_bacuda, wco_bacuda_madagascar2026 -->

[^ch06-2]: WCO Smart Customs Project case study on AI/ML adoption in
 China Customs (Jan 2025): 62 "smart models" reported across
 maturity stages — 22 in pilot, 2 fully operational. <!-- bib:
 wco_china_aicasestudy2025 -->

[^ch06-3]: Internal skills gaps as the top barrier to public-sector AI
 adoption: OECD, *Building an AI-ready public workforce* (Jan 2026);
 corroborated by UK NAO, *Use of AI in Government* (Mar 2024). <!-- bib:
 oecd_ai_ready_workforce2026, uknao_ai_gov2024 -->

[^ch06-4]: WCO's AI/ML readiness and detailed-adoption materials are
designed to help Members stage implementation against their own data,
infrastructure, governance and skills conditions. This chapter applies
that staging logic to autonomy: readiness constrains specific task/rung
combinations rather than serving as a pass-fail score.
<!-- bib: wco_scp_report2025 -->
