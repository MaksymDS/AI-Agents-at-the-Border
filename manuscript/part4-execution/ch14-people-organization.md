---
title: "People and Organization"
part: "IV — Execution"
chapter: 14
status: review
version: 0.3
last-updated: 2026-07-09
---

## The question from the floor

Forty minutes into the staff town hall, after the strategy slides and
the pilot results, an inspector with twenty-two years of service stands
up and asks the only question the room actually came for: *"Will the
agent take my job?"*

Every AI program in every customs administration arrives at this
microphone, and most arrive unprepared — armed either with evasive
comfort ("nothing will change") or with consultant physics ("humans will
move up the value chain"). Both answers are heard as what they are: not
answers. This chapter builds the real one, and the organization that
makes it true. It has an unusual amount of evidence behind it, because
the people side of customs AI is — by the OECD's and the national audit
offices' independent findings — not the soft part of the program. It is
the binding constraint.[^ch14-1]

## 14.1 The constraint is skills, not servers

Across the public-sector evidence, **internal skills gaps rank as the
single biggest barrier to AI adoption — ahead of technology and ahead of
budget**.[^ch14-1] The finding should reorganize how leaders read their
own program plans: the GPU line and the vendor line are usually
generously sized, while "training" appears as a late row absorbing
whatever remains. The evidence says the proportions are backwards — and
the private sector shows the same tools-outrun-capability gap at scale.
Deloitte's *State of AI in the Enterprise* 2026 survey of more than
3,200 leaders across 24 countries found that while worker access to
sanctioned AI tools reached roughly 60% — a jump of about 50% in a
single year — only about a quarter of organizations had 40% or more of
their AI initiatives in production, and only around one in five reported
mature governance of AI agents.[^ch14-2] The provisioning races ahead;
the capability to use and govern what has been provisioned lags behind,
in government and industry alike. The EU has begun
converting the point from advice into obligation: Article 4 of the AI
Act legally requires deployers to ensure staff have a *sufficient level
of AI literacy*, which for an EU-member customs administration makes the
training plan a compliance artifact, not a perk.[^ch14-7]

The workforce splits into three groups with three different needs — a
framing the OECD formalizes and this chapter adopts[^ch14-1]:

- **General employees** — every officer who will touch AI output: needs
 working literacy, awareness of failure modes, and above all **critical
 judgment over AI outputs** — the calibrated-trust skill Chapter 12
 tested with seeded errors.
- **Leaders** — need strategic understanding sufficient to own mandates,
 read gate evidence, and remain accountable; a Director General who
 cannot interrogate an autonomy proposal has delegated the decision to
 whoever can.
- **Digital and data professionals** — a small specialist cadre, built
 deliberately (14.3), never assumed.

Three audiences, three curricula, one budget conversation to have before
the procurement one.

## 14.2 The role shift the Ladder already promised

Chapter 2 named the officer's roles up the Autonomy Ladder — Operator,
Pilot, Supervisor, Governor — and Chapter 13 handed this chapter the
consequence: at L2 and above, the *content of customs work changes
shape*. The queue becomes an exception stream. Checking becomes
supervising. The skill that mattered most — fast, accurate processing of
the routine — yields the center to skills that were always present but
never central: judging an ambiguous case, articulating why the system's
answer is wrong, handling the trader's challenge with the trajectory on
screen (Chapter 9's contestability path ends at exactly this officer).

Two design consequences follow, both routinely missed.

**Exception work is senior work.** The cases that reach a Supervisor are
by construction the hard ones — the routine was cleared below. Staffing
the exception stream with junior officers because "the AI does the work
now" inverts the logic: autonomy *raises* the average difficulty of the
human's caseload. Grading, workload norms, and quality sampling must be
rebuilt to that reality (the process redesign Chapter 13 mandated).

**Judgment must be trained, not presumed.** Critical evaluation of AI
output is a teachable skill with a known failure mode — automation
complacency, the drift toward rubber-stamping that Chapter 12's seeded
probes exist to catch. The training that counters it is practical and
contextual: officers working *their* document types against *their*
system's real outputs, including planted failures — and the evidence is
clear that this kind of trainer-led, work-contextual instruction
outperforms self-paced modules for retention and application.[^ch14-1]

## 14.3 The specialist cadre: build the hub, staff the spokes

For the third group, customs has one blueprint documented deeply enough
to copy, and it comes from the administration with the field's strongest
verified results. Korea Customs Service began with a 2017 roadmap and a
commitment most administrations still find radical: a six-month training
program aimed at raising **300 big-data experts — roughly 7% of the
entire workforce — over five years**, motivated by data volumes no
outsourced arrangement could serve.[^ch14-3] The organizational form
that emerged is **hub-and-spoke** (Figure 14.1): a designated central team develops
and operates the analytical tooling (the hub), while trained
officer-analysts sit paired with clearance domain experts in the
operational units (the spokes), with private-sector IT expertise brought
in to refine tools rather than to own them. Field staff raise problems;
the hub analyzes and returns results; the loop repeats.[^ch14-4]

![Figure 14.1 — Hub and Spoke](/assets/diagrams/fig-ch14-hub-and-spoke.svg){width=100%}

Three features make the model worth copying precisely rather than
loosely. It **pairs, never replaces**: the analyst does not substitute
for the domain expert — the two are a unit, which is also why KCS
deploys assisted threat recognition explicitly to *support* its
chronically scarce image analysts rather than to displace
them.[^ch14-4] It **keeps the hub inside the administration**: vendors
refine tools; the administration owns the capability — the anti-lock-in
argument of Chapter 7 wearing an org chart. And it **gives the spokes a
career**: analyst training is a path upward inside customs, not a exit
ramp out of it — which is what makes the 7% target recruitable from
within.

One honest gap, recorded rather than papered over: public, primary
job-profile documents for customs AI roles barely exist — administrations
are building these positions faster than they are publishing them.
Appendix templates in this book (role profiles for the hub lead, the
officer-analyst, the corpus custodian of Chapter 11, and the mandate
owner of Chapter 9) are the author's synthesis, offered as starting
points, not as sector standards.[^ch14-5]

## 14.4 Literacy at scale: reach and depth are different products

The training plan's central trade-off is **reach versus depth** — short
self-paced courses scale to thousands cheaply; intensive facilitator-led
programs cost more and change behavior more.[^ch14-1] The resolution is
not to choose but to assign: reach instruments for the general
workforce's literacy floor, depth instruments for the cadre and the
supervisors of high-autonomy tasks.

Customs administrations do not have to build the reach layer alone. The
WCO's capacity-building stack is the sector's shared infrastructure:
**CLiKC!** e-learning in data analytics (thousands of enrollments
across Members, open to any customs official through the national
coordinator) as the scalable floor, and **BACUDA** workshops as the
depth layer — a two-module design of mandatory e-learning pre-work
followed by a five-day in-person workshop structured around the same
five readiness pillars Chapter 6 assesses.[^ch14-6] The sequencing
lesson embedded in that design generalizes: literacy before workshop,
workshop before tooling, tooling before autonomy.

> **Field note — BACUDA, the depth layer in practice.** The program's
> third scholarship cohort (January–April 2026) shows exactly who the
> depth instrument reaches: twelve customs officials from Botswana, El
> Salvador, Eswatini, Fiji, Honduras, Kenya, Malaysia, Maldives,
> Mauritius, Turkmenistan, Uzbekistan, and Zambia — a deliberately
> global, largely smaller-administration group — completed a twelve-week
> curriculum spanning Python, machine learning for risk profiling,
> natural-language processing, and the WCO's own algorithms (LITE-DATE,
> AI-HS), with modules on data strategy and governance and field visits
> to working customs operations.[^ch14-8] The design is the chapter's
> argument made concrete: the scalable e-learning floor feeds an
> intensive, facilitator-led, case-based program, and the graduates
> return as the analyst spokes of Chapter 14's hub-and-spoke — evidence
> that the specialist cadre is buildable even where a national AI academy
> is not.

Whatever the mix, two findings should shape it. Training sticks when it
is **contextual** — built on the administration's own documents,
systems, and cases — and when it is **sustained**: communities of
practice, innovation competitions, and performance reviews that
recognize AI-era skills keep the capability alive after the workshop
ends.[^ch14-1] A one-off vendor training at go-live satisfies the
contract line and almost nothing else.

## 14.5 The answer from the podium

Now return to the inspector's question, with everything this book has
established, and give the answer that is both honest and defensible:

*"Not your job — your job description. Here is what I can commit to.
The volume curve means we need every officer we have: the work that is
disappearing is the re-keying and the routine checking, and the work
that is growing is the judgment — exceptions, investigations,
supervision of the systems. Decisions about people follow the same rule
as decisions about autonomy: one step at a time, on evidence, in the
open. Training comes before deployment, not after it — and it is paid,
on work time, in your own document language. And accountability stays
with us, the leadership: no officer will be blamed for a system's
error, and no system will overrule an officer within their authority
without a path to challenge it."*

Every clause of that answer is load-bearing, and every clause is only as
good as the program behind it. The volume argument is Chapter 1's
arithmetic — and Korea's verified experience of absorbing a tripled
e-commerce load with augmented rather than replaced staff.[^ch14-3] The
one-step rule is the Ladder. The training commitment is this chapter.
The accountability clause is the book's refrain. Workforce dialogue —
with staff associations and unions where they exist — is where these
commitments get written down and audited; treating it as an obstacle
rather than an enforcement mechanism for your own promises is a
strategic error. Externally, the same discipline as Chapter 12:
communicate outcomes, not launches, and never let a press release
promise a headcount reduction the strategy does not actually contain.

## 14.6 Redesign the supervisory job before scaling the agent

The workforce question is often framed as headcount: how many hours will
the agent save, and what happens to the people? That framing is too late
and too narrow. At L2 and above, the job changes before the headcount
does. Officers move from reading every document to supervising
exceptions; team leaders move from allocating queues to calibrating
thresholds and sampling; policy units move from writing prose guidance
to maintaining decision-ready rules and evidence corpora.

Write the redesigned job explicitly for every scaled workflow: what the
officer no longer does; what they now verify; what override authority
they hold; how many exceptions they can reasonably supervise; which
signals trigger escalation; how their quality is measured; and where
their feedback changes the system. Without that document, efficiency
targets turn into rubber-stamping pressure and a valuable agent becomes
a source of silent operational risk.

The business upside is not fewer people at the border; it is more scarce
judgment applied where it has consequence. That is the case to make to
officers and unions: the programme must show the supervisor's new
authority, training, workload standard and route for challenging a bad
system—not merely promise that humans remain "in the loop." The WCO's
capacity-building baseline and recent public-workforce evidence point in
the same direction: skills, operational ownership and feedback loops are
production controls, not change-management decoration.[^ch14-9]

## 14.7 Capacity planning: supervision has a queueing limit

The phrase "human in the loop" hides a capacity problem. A supervisor
can review only a finite number of exceptions per hour, and the rate is
not constant: complex documents, new policies, adverse decisions and
system disruptions take longer. If the agent refers more cases than the
team can absorb, the queue grows, service levels fall and officers are
pressured to approve recommendations too quickly. That is a governance
failure expressed as an operations metric.

Set a workload standard before scale. For each workflow, measure the
median and upper-range review time, the expected escalation rate, peak
arrivals, availability, training time and the reserve needed for
incidents. Translate this into a maximum safe queue and a trigger that
automatically lowers the agent's authority or narrows its scope. Review
the forecast weekly during early production; revise it from actual
trajectories rather than an assumption made in the business case.

This is also how to discuss productivity credibly. The benefit of a
Rung-2 assistant is not "one agent replaces one officer." It may let a
team clear routine questions while allocating experts to exceptions, or
it may reveal that service capacity is limited by a different step such
as inspection slots or external data. Report the released hours, the
new supervision hours and the service outcome separately. Only then can
leaders decide whether to redeploy capacity, improve compliance work or
change staffing over a responsible time horizon.

Finally, build progression into the roles. Officers who become strong
supervisors, evidence curators or control-room analysts need recognised
skills, authority and a career path—not an extra responsibility added
to their existing queue. The best feedback often comes from precisely
these people; treating their work as a temporary project assignment is
how an administration loses its scarce institutional memory to the next
vendor deployment.

## 14.8 The workforce compact for agentic operations

Before a workflow scales, write a compact between the programme and the
unit that will operate it. It should state the purpose of the workflow;
what work is removed, redesigned and newly created; the authority and
workload standard of the supervisor; training and protected learning
time; quality and safety expectations; how feedback changes the system;
the escalation route for a suspected bad outcome; and the commitment on
redeployment or staffing where one can honestly be made. Share it with
staff representatives early, not after the new interface is live.

The compact protects delivery as well as trust. Officers are the first
to see whether a source is stale, an exception category is changing or a
recommendation is subtly unhelpful. They will not provide that feedback
consistently if the system feels like an unacknowledged headcount
exercise or if raising a problem simply creates more work. Make feedback
part of the job, give it a route to a named product owner, and show
which changes resulted. The programme earns adoption by demonstrating
that professional judgment has more consequence, not less.

Leaders should report workforce outcomes next to productivity: people
trained and authorised; supervision load; quality-review results;
feedback resolved; redeployed capacity; and unresolved capability gaps.
This keeps the public conversation grounded. The objective is not to
promise a frictionless transition. It is to make the operational change
visible enough that it can be governed, resourced and improved.

## Decision Toolkit — Chapter 14

**The capability roadmap** (one page): three audiences × two instrument
classes. General workforce → literacy floor (reach: e-learning, CLiKC!-
class), refreshed annually, Article-4-compliant where applicable.
Leaders → executive sessions on mandates, gates, and evidence reading
(depth, short, mandatory for mandate signers). Specialist cadre →
selection from serving officers + intensive program (depth,
BACUDA-class or national equivalent) + hub-and-spoke placement + career
track. Budget rule of thumb: if training is under a tenth of the
technology line, revisit the proportions before the OECD finding
revisits you.

**The hub-and-spoke starter kit:** name the hub team and its owner ·
select the first spokes from the units running Chapter 12 pilots ·
pair every analyst with a domain expert by name · route all vendor tool
work through the hub · publish the analyst career path before asking
for volunteers.

**The town-hall test:** leadership can deliver the podium answer — all
five clauses — without a slide, and every clause maps to a funded line
in the program plan. Any clause that doesn't map is removed from the
speech or added to the plan; saying it without funding it is how trust
is spent.

## Key Takeaways

- Skills, not servers, are the binding constraint on public-sector AI —
 and AI literacy is becoming a legal duty, not a perk. Size the
 training line accordingly, before procurement.
- Three audiences, three curricula: general workforce (literacy +
 critical judgment over AI output), leaders (mandates and evidence),
 specialist cadre (built deliberately, from within).
- The Ladder's role shift is a staffing reality: exception work is
 senior work, and calibrated judgment is trained on the
 administration's own cases — trainer-led, contextual, sustained.
- Copy the hub-and-spoke blueprint precisely: pair analysts with domain
 experts, keep the hub inside the administration, give the spokes a
 career — augment, never replace, and mean it structurally.
- Have the podium answer ready, fund every clause of it, and use
 workforce dialogue as the enforcement mechanism for your own
 promises. Externally: outcomes, not launches.

---

## Endnotes

[^ch14-1]: OECD, *Building an AI-ready public workforce* (Jan 2026):
 internal skills gaps as the most significant barrier to
 public-sector AI adoption; the three workforce groups (general
 employees / leaders / digital-data professionals); trainer-led
 instruction outperforming self-paced for retention and application;
 the reach-versus-depth trade-off; sustainment via communities of
 practice, competitions, and performance reviews. Corroborated on
 the skills barrier by the UK NAO, *Use of AI in Government*
 (Mar 2024).
 <!-- bib: oecd_ai_ready_workforce2026, uknao_ai_gov2024 -->

[^ch14-2]: Deloitte, *State of AI in the Enterprise* (2026 edition;
 3,235 leaders across 24 countries, fielded Aug–Sep 2025, published
 21 Jan 2026 — the series renamed from the quarterly *State of
 Generative AI in the Enterprise*): ~60% of workers with access to
 sanctioned AI tools (a ~50% year-on-year rise); ~25% of
 organizations with ≥40% of AI initiatives in production; roughly
 one in five reporting mature AI-agent governance. Cross-industry
 enterprise data, cited as corroboration of the public-sector
 skills-and-governance gap. <!-- bib: deloitte_stateofai2026 -->

[^ch14-7]: EU AI Act, Article 4: providers and deployers must take
 measures to ensure a sufficient level of AI literacy among staff and
 others dealing with the system on their behalf; applicable from
 2 Feb 2025. <!-- bib: ec_navigating_aiact -->

[^ch14-3]: Korea Customs Service: 2017 Roadmap for Big Data Analysis;
 six-month training program; target of 300 big-data experts (~7% of
 the workforce) over five years; daily data volumes ~45 GB
 structured + ~30 GB unstructured (WCO News 86, Jun 2018). Volume
 absorption without matching headcount growth per WCO News 108 (2025).
 <!-- bib: wconews86_kcs2018,
 wconews108_korea -->

[^ch14-4]: KCS hub-and-spoke model: designated central team developing
 and operating analytical tools; officers trained in data mining
 paired with clearance domain experts; private-sector IT expertise
 refining rather than owning tools; ATR deployed to assist
 chronically scarce image analysts; stated lessons on ICT–customs
 feedback loops and top-management backing (WCO News 96, 2020).
 Field-staff-to-hub loop corroborated by Korea Herald interview
 (Jan 2022, secondary). <!-- bib: wconews96_kcs_bigdata, koreaherald_kcs_bigdata2022 -->

[^ch14-5]: Public primary job-profile documents for customs AI roles
 were not found as of 2026-07-09 — recorded as an evidence gap; the
 Appendix role templates
 are the author's synthesis.

[^ch14-6]: WCO capacity-building stack: CLiKC! data-analytics e-learning
 (4,000+ enrollments, open to Members via national coordinators);
 BACUDA two-module delivery (mandatory CLiKC! pre-work + five-day
 in-person workshop organized around the five readiness pillars:
 governance, data governance, technology infrastructure, culture &
 leadership, analytical capabilities); funded by the Customs
 Cooperation Fund of Korea; part of the WCO Strategic Plan
 2025–2028.
 <!-- bib: wco_bacuda, wco_bacuda_madagascar2026 -->

[^ch14-8]: BACUDA Scholarship Programme, 3rd edition (Hanyang
 University, Seoul, 26 Jan–23 Apr 2026): twelve customs officials
 from Botswana, El Salvador, Eswatini, Fiji, Honduras, Kenya,
 Malaysia, Maldives, Mauritius, Turkmenistan, Uzbekistan, and Zambia;
 twelve-week curriculum (Python, ML risk profiling, NLP, WCO
 algorithms incl. LITE-DATE and AI-HS, data strategy and governance,
 field visits to Incheon Airport and Busan Customs). WCO BACUDA /
 CCF-Korea, 2026. <!-- bib: wco_bacuda_scholarship2026 -->

[^ch14-9]: WCO's detailed report emphasizes data literacy, operational
and technical capacity-building, and cross-departmental collaboration;
OECD's 2026 public-workforce work identifies skills and organizational
readiness as a central adoption constraint. This chapter's redesigned
supervisor role turns those observations into a workflow control.
<!-- bib: wco_scp_report2025, oecd_ai_ready_workforce2026 -->
