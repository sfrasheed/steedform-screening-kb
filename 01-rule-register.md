# 01 — Rule Register (screening scope)

> **STATUS: AUTHORITATIVE. This file WINS.**
> Where this Register and any other file disagree — the Deep Screen app, another document in this knowledge base, a monday column description, a memory file, or anything else — **the Register is correct and the other file is stale.** Act on the Register.
>
> **Established 27 July 2026** by MD decision, after a 64-agent audit found that every serious defect of the preceding week shared one cause: a rule decided in one place that never reached the file which executes it. Measured at the time: 20 files carried operational rules; the hottest single rule appeared in **17 files across 89 restatements**.

**Owner:** MD
**Last updated:** 3 September 2026 — rulings of 3 September 2026 (Stella Rasheed) incorporated; see `RULINGS-2026-09-03.md`
**Scope:**
- **Owns:** the canonical statement of every operational rule a screen applies. This is the only file in which a screening rule is authored.
- **Does not own:** reference data an agent merely looks up — capability tables, supplier figures, board IDs, templates. Those live in documents 03–09, which cite these rules but never restate them.

---

## What this document decides

Every operational rule the screen applies, stated once, with an ID and a version. A rule that is not here is not a rule: it is an orphan, and acting on it is how the previous knowledge base drifted. Where a document in this set explains or expands a rule, it must cite the rule ID and may never contradict the statement below.

---

## How this file works

**Scope — what belongs here.** Only **OPERATIONAL** rules: things an agent must *apply* to reach a verdict or take an action. Reference data an agent merely *looks up* — slab weights, brand overhang tables, machine specs, supplier manuals — does **not** belong here; it lives in documents 03–09. Mixing the two is how the predecessor skill reached 400 lines and stopped being read.

**The standing rule, from 27 July 2026:** *every NEW or AMENDED operational rule is written HERE FIRST, and only then propagated.* A rule that exists anywhere else but not here is, by definition, unregistered.

**IDs are permanent.** Never reused, never renumbered. A superseded rule keeps its ID, is marked `SUPERSEDED`, and points at whatever replaced it. Every historical record depends on this. **The complete ID index in §7 lists all 51 registered IDs**, including those outside screening scope, so that no ID is ever silently reissued.

**Versions are how drift is caught.** Each rule carries `vN`. Any document or executable restating a rule must carry the tag inline, e.g. `[R-D5 v5]`. A checker greps every carrier and reports:
- **MISSING** — a carrier that should enforce the rule never mentions it
- **STALE** — a carrier holds `v2` when the Register says `v3`
- **ORPHAN** — a rule stated somewhere with no ID at all, i.e. born in the wrong place

⚠ **A tag check is not an identifier check.** On 24 August 2026 a perfectly tagged, perfectly versioned LAW addressed a monday column that did not exist, and the drift checker reported it clean — it compares `[R-xxx vN]` tags, never board and column identifiers. Identifiers must be verified separately against `08-board-and-column-registry.md`.

**Carrier classes.**

| Class | Files | Obligation |
|---|---|---|
| **AUTHORING** | this Register (`01`) | the only place a rule is authored |
| **EXECUTABLE** | the `estimator-screening` skill · Claude deep scans · **the Deep Screen app when it lands** | must read this file first; may restate a rule inline **only** with its `[R-xxx vN]` tag |
| **REFERENCE** | `03` Risk Scoring · `04` Customer & Account · `05` Material & Capability · `06` Evidence Requirements · `07` Service Area & Site · `08` Board Registry · `09` Response Templates | may explain and expand a rule; must cite the ID; must never contradict the canonical statement |
| **QUARANTINE** | `10` Open Rulings | records questions that are NOT settled. Nothing in it may be applied as a rule |

⚠ **The two pipeline sweeps (`pipeline-daily-sweep`, `pipeline-scan-halfhourly`) were EXECUTABLE carriers and are RETIRED** — disabled 20–21 August 2026 (MD, 26 August 2026). They are not carriers, must not be re-added, and every reference to them below is historical. **Wherever a `Carriers` line in the source Register named a sweep — by the phrase "both sweeps" or by name — read it as retired.** The carrier lines in this file have been rewritten to name live carriers only; the historical carrier record is preserved in the archived original Register.

⚠ **Where screening enforcement actually lives now:** the `estimator-screening` skill and Claude deep scans — **until the Deep Screen app takes it.** The app does not exist yet; do not describe it as a live carrier. **Nothing screens automatically in the interim**: capture and screening are a human or Claude duty, by design, not a defect.

**Failure mode — if an executable cannot read this file: KEEP CAPTURING, REFUSE TO JUDGE.** Continue intake so no enquiry is lost; do not issue verdicts, do not write risk strips, and notify Matthew "🚨 Rule Register unreadable — screening halted". **Never fall back to an inline copy** — "probably right" is precisely what produced the 25 July faceting mis-sell.

---

## The rules

> **RULING ROUND — 3 SEPTEMBER 2026 (Stella Rasheed).** Thirty-four open questions were ruled and are now law. **Nine rules are new** — `R-RETAIL` · `R-DEKTON` · `R-OCCUPANCY` · `R-AREA` · `R-NATURAL` · `R-ENTITY` · `R-ALFRESCO` · `R-INTERSTATE` · `R-LEADTIME` — five of them registering conditions the screen had been applying for months with no rule behind them. **Ten rules were bumped.** Every open lead screened before this date was scored under superseded rules and is **stale by definition** `[R-RESCREEN v1]`.
>
> ⚠ **`[R-BLOCK v3]` restructures the blocking list, and this Register names an MD or GM as the amendment authority for that list.** The ruling is recorded as made; a countersign is outstanding.


## 1. Client and account

*Who is asking, and are they an account we act for?*

### R-CLIENTFIT · v1 · LAW
**Client fit is decided before drawings, scope, material, value or technical suitability.** First apply `[R-ACCTMATCH v4]`.

- **Recognised** means either: (a) `[R-ACCTMATCH v4]` tier 1–3 safely linked one Account, or (b) a human has explicitly approved the new customer in the Leads `Client Fit` column (`color_mm69h52c`).
- A free/generic address (gmail, hotmail, outlook, bigpond, internode, optusnet, yahoo, live, icloud and equivalents) can still be recognised by an **exact full-email** Contact/Account match. The shared domain alone is never recognition.
- If no Account is safely linked and `Client Fit` is not **Approved New**, set `Client Fit = Review Required`, set Lead Status = **Unqualified**, and write: `UNRECOGNISED SENDER — client-fit approval required before drawings are considered.`
- `Client Fit = Declined` always remains **Unqualified**. `Client Fit = Recognised` or **Approved New** allows the normal drawing/technical screen to continue.
- Drawing presence, readability, job size, material and technical merit must never upgrade an unresolved client-fit outcome. Preserve and file the supplied evidence, but do not convert the Lead or let a drawing rescan/reconciliation promote it.
- A human approval is recorded by setting `Client Fit = Approved New`; a known customer is recorded as `Recognised`. Re-runs must respect those explicit states and must not repeatedly reset an approved new customer.

**Precedence:** this gate runs after junk triage and safe account matching, but before DRAWINGS and every technical/commercial disposition rule. It therefore outranks `Needs Info` for missing drawings and `Qualified` for clean drawings.

**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account` · `06 Evidence Requirements` · `08 Board Registry & Mechanics`

**History:** **v1 16 Aug 2026 (MD)** — unrecognised senders route to Unqualified for a client-fit decision regardless of drawings.

### R-ACCTMATCH · v5 · LAW
*(v3 ratified by MD 10 Aug 2026, closing four incompatible definitions that were live across this Register, the estimator skill and both sweep prompts. A wrong link changes Customer Tier treatment, Gate-Selective, A-tier waivers, SLA and risk score — this is verdict-changing, not editorial.)*

**ONE CLOSED LADDER. Apply in order. Stop at the first tier that resolves.**

**THE AUTOMATIC LADDER ENDS AT TIER 3.**

| # | Test | Action |
|---|---|---|
| **1** | **Exact Contact email** resolving to **one distinct linked Account** | **AUTO-LINK** |
| **2** | **Exact Accounts main-POC email** (**`email_mm64cpfk`** on Accounts `5029570132`), full-string, case-insensitive | **AUTO-LINK** |
| **3** | **Unique, non-generic Account domain** — resolves to exactly one Account | **AUTO-LINK** · set Existing trade client = Yes |
| **4** | **Exact normalised company name** — from an explicitly extracted company name only | ⚠ **CANDIDATE ONLY. Never auto-link.** Surface it for human confirmation |
| **5** | Anything else | **Leave unlinked.** Flag for human resolution |

⛔ **TIER 4 IS A LOCATOR, NOT AN AUTHORITY.** An exact name match may *help a human find* the account. It must **never** by itself apply Customer Tier, Gate-Selective, A-tier waivers, markup or SLA. *(v2 said "never match on the account NAME" in its opening line and then permitted name matching in its fall-through — the contradiction that produced four different implementations.)*

⛔ **Full-address equality and domain equality are DIFFERENT TESTS — never merge them.** Count the domain's matches BEFORE linking; more than one → human.

⛔ **A DOMAIN SHARED BY TWO+ ACCOUNTS IS AMBIGUOUS — DO NOT LINK, FLAG IT.** Known collision: `farquhar.co` resolves to **both** Farquhar Kitchen Centre (`accounts@farquhar.co`, 2766405173) and KT3 Farquhar - Hickinbotham (`commercial@farquhar.co`, 2766521671).

⛔ **NEVER match a GENERIC domain. The closed list is ELEVEN:** gmail · hotmail · outlook · bigpond · internode · optusnet · yahoo · live · icloud · **people.net.au** · **adam.com.au**. On a generic domain, tiers 2–3 do not apply; go to tier 4 as a candidate only.

**Why the ambiguity rule matters:** guessing between two accounts of the same customer group silently attributes the job — and the tier — to the wrong entity, pointing a commercial job at the retail account or vice versa.

⛔ **A GENERIC DOMAIN DROPS TO TIER 4 — CANDIDATE ONLY, human confirmation required. It is NOT an automatic name match.** At least 8 accounts use a generic domain as their main address (Styleline, All Class, DeBoar, K H Kitchens, Saunders, Oskar Brezovic, Dylan Boehm, Zee) — matching on `gmail.com` would link every retail enquiry to whichever account happens to share it.
⛔ **Never match on contact name, or on a partial/fuzzy company name.**

**Why:** the matcher was comparing the sender's domain against the account NAME, so `farquhar.co` vs "Farquhar Kitchen Centre" read as a *near-miss* and the link was skipped — even though the account's own email carried the exact domain. **45 of 111 leads were unlinked when this was found, and every account-keyed rule (Customer Tier, Gate-Selective, A-tier waivers) silently no-ops on an unlinked lead.** A Gate-Selective job reached Qualified and converted because of it. At least four of the 45 were **byte-identical email matches** that tier 1 would have caught outright — KDA Build `nick@kdabuild.com.au`, Batescraft `enquiries@batescraftjoinery.com`, The Joinery Shop ×2 `service@thejoineryshop.com.au`. **The matcher's caution on `farquhar.co` was correct; its failure on exact matches was not. Both behaviours came from having no stated ladder.**
**Measured against live data, 10 Aug 2026** — 387 unique Contact emails, 153 Accounts:

| Tier | Unique emails resolved |
|---|---:|
| 1 · exact Contact email → one linked Account | **334** |
| 2 · exact Account POC email (after tier 1) | 0 |
| 3 · unique non-generic domain | 5 |
| — ambiguous non-generic domain (no link) | 2 |
| — no automatic result / name candidate only | 48 |

**Tier 1 carries nearly all safe matches. Exact name is not needed as an automatic tier** — which is the evidence for ending the automatic ladder at tier 3.

⚠ **42 Accounts have a BLANK `email` field** *(corrected from the earlier ~32 estimate, measured 10 Aug 2026)*, so tier 2 cannot fire for them. Populating that column is the highest-leverage data fix on the Accounts board — but its absence is **never** grounds to fall through to an automatic name match.

⚠ **Cynthia (agent `21307`) cannot execute this rule** — its knowledge set covers Leads, Accounts, Materials and Serviceable Areas but **not Contacts**, so tier 1 is structurally unavailable to it. Until that changes, Cynthia must not auto-link Accounts.

**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account` · `08 Board Registry & Mechanics`

**History:** **v5 **3 Sep 2026 (Stella Rasheed)**** — closes OR-25. `people.net.au` and `adam.com.au` are ruled generic and added to the closed list, taking it to eleven. The screening skill had been carrying both while simultaneously listing `adam.com.au` as a non-generic collision, and was short four of the original nine. · **v1 27 Jul 2026** · **v2 28 Jul 2026** — merged two divergent v1 blocks; v1's "domain = confident" tier was self-contradictory. · **v3 10 Aug 2026 (MD)** — closed the ladder. v2 opened by saying "never match on the account NAME" and then permitted exact-name matching in its fall-through; that contradiction produced **four incompatible implementations** across the Register, the estimator skill and both sweeps. v3 adds exact-Contact-email as tier 1, ends the AUTOMATIC ladder at unique non-generic domain, and demotes exact name to a human-confirmed candidate that may never apply Customer Tier, Gate, waivers, markup or SLA. · **v4 24 Aug 2026 (MD)** — **identifier repair, no change of method.** Tier 2 named the Accounts main-POC email column as `email`. That was the LEGACY board's column id; the **11 Aug 2026 CRM migration** re-issued every Accounts column, and live Accounts `5029570132` has **no `email` column at all** — the query returns `ResourceNotFoundException: Column not found`. **Tier 2 was therefore dead for all 166 accounts for ~13 days.** Measured damage: **nil** — all 7 in-window leads whose sender matches an Accounts POC email were still linked correctly by tier 1 or tier 3, so the closed ladder's redundancy absorbed it. That is also why nothing surfaced the defect. Corrected to **`email_mm64cpfk`**. ⚠ **A perfectly tagged, perfectly versioned LAW addressed a column that did not exist, and `rule-drift-check.py` reported it clean — it compares `[R-xxx vN]` tags, never identifiers. See Gap Register G30.**

### R-C1 · v4 · LAW
**Customer Tier is the only commercial-disposition LABEL — it is not the only commercial EVIDENCE `[R-ACCT v3]`.** Follow the Lead's `board_relation_mm64fq68` to Accounts `5029570132`, read `color_mm64t0aj` directly, and use its current value. If it is `Do-Not-Quote`, route the Lead to Needs Review and cite the Account item ID.
⛔ **A `DUMP STOP` / `DUMP LOCKED` marker in Notes/Flags `long_text_mm64njy4` blocks exactly as a `Do-Not-Quote` tier does — Needs Review, quoted verbatim, cite the item ID — even when the tier label reads A-Anchor/VIP.** The tier label may never be reported as the disposition while an unresolved DUMP marker or a contradicting group sits on the same record. **Fail toward the flag.**
**Account Status `color_mm64cbq0` is stale lifecycle data and must never block, qualify, score or describe a Lead.** Never use retired account shorthand; name the authoritative field and value instead.
**Why:** Weyland Cabinet Makers (`2827365291`) is live in Customer Tier B/group B while stale Account Status still says Do-Not-Quote. Treating lifecycle as disposition produced a false commercial block on Lead `2829292974`.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account` · `08 Board Registry & Mechanics`

**History:** v1 (tier only) · v2 26 Jul 2026 (dual-column) · **v3 16 Aug 2026 (MD: lifecycle retired as screening evidence; live Customer Tier restored as sole disposition authority)** · **v4 24 Aug 2026 (MD)** — v3's "sole disposition authority" was read as *sole evidence*, so a DUMP STOP account at a 7% win rate screened as A-Anchor/VIP (Inavogue `2827354824`). v4 separates **label** from **evidence**: the tier remains the disposition label, a DUMP marker blocks alongside it, and Notes/Flags is mandatory reading under `[R-ACCT v3]`.

### R-ACCT · v3 · LAW
⛔ **THE ACCOUNTS BOARD IS THE REFERENCE — NOT A COLUMN LIST IN THIS RULE (MD, 24 Aug 2026).** Read the account **record**, not a curated subset of it. The columns named below are the minimum, **not a closed set**: as customer screening evolves on the board, new evidence appears there first and this rule follows. **A screen that reports only the fields a rule happens to name will report the flattering field and omit the decisive one.**

**Minimum reads, direct from Accounts `5029570132`:**
① **VALUE / COMMERCIAL DISPOSITION** `color_mm64t0aj` Customer Tier · ② **BEHAVIOUR** `color_mm64jqn0` Client Rating A/B/C with sub-ratings `color_mm64kd3q` Payment, `color_mm64je94` Measure-ready, `color_mm647dxb` Install-ready · ③ **`long_text_mm64njy4` Notes / Flags — MANDATORY.** Blank ratings mean not populated; they are not evidence of either good or bad performance.

⛔ **NOTES / FLAGS IS EVIDENCE, NOT COLOUR.** It carries `DUMP STOP` / `DUMP LOCKED` markers, ten-year revenue, win rate and recorded MD analysis. **A `DUMP` marker, or any note contradicting the tier label, is a BLOCKING flag → Needs Review, and must be quoted verbatim in the screening output.** Never summarise it away, and never let a tier label outrank it.

⚠ **WHEN THE LABEL, THE GROUP AND THE NOTE DISAGREE, THAT IS THE FINDING — surface all three and route to a human.** Do not silently prefer one. *Worked example, verified 24 Aug 2026:* **Inavogue `2827354824`** reads Customer Tier `A - Anchor/VIP`, Payment `B`, Status `Active`, **group 🅱 B**, Notes/Flags **`DUMP STOP · 19k 10yr · 7% win · Active`**. Screened under v2 it reported *"Active · A - Anchor/VIP · Payment B"* — every word true, the commercial reality inverted.

**Account Status `color_mm64cbq0` is lifecycle history, is stale, and remains excluded as a DISPOSITION axis.** Do not use it to qualify or score. It may be displayed as context.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `04 Customer & Account` · `08 Board Registry & Mechanics`

**History:** v1 26 Jul 2026 · **v2 16 Aug 2026 (MD: lifecycle excluded as stale data)** · **v3 24 Aug 2026 (MD)** — v2 said *"historical account notes and board groups are context only; the direct Customer Tier and rating fields are the evidence."* **That sentence caused the defect it was meant to prevent**: it excluded the one column carrying the commercial story. v3 makes Notes/Flags mandatory evidence, makes the board — not this rule's column list — the reference, and treats label/group/note disagreement as a finding rather than a precedence puzzle. 14 accounts currently carry DUMP markers.

### R-CRMSOT · v2 · LAW
**monday.com is the single source of truth for CRM-class items.** When screening or auditing a Lead, follow its live Accounts relation (`board_relation_mm64fq68`) to the linked item on current Accounts `5029570132` and read that item directly.
**Account authority:** Customer Tier (`color_mm64t0aj`) is the current commercial-disposition field. Client Rating (`color_mm64jqn0`) and the Payment / Measure-ready / Install-ready sub-ratings are the current behaviour evidence. Account Status (`color_mm64cbq0`) is **stale lifecycle data and must never block, qualify, score or describe a Lead or Deal.** Historical notes, old portfolio lists, Lead narratives and copied snapshots are not authority.
⛔ **Notes / Flags `long_text_mm64njy4` IS authority and is MANDATORY reading `[R-ACCT v3]`.** A `DUMP STOP` / `DUMP LOCKED` marker blocks exactly as a `Do-Not-Quote` tier does, and must be quoted verbatim. **This overrides the line above:** "historical notes are not authority" means copied narratives and retired shorthand — it has never meant the Notes/Flags column.
**Output rule:** never use retired account shorthand. If Customer Tier itself currently reads `Do-Not-Quote`, state the exact field and value and cite the linked Account item ID. If it does not, **still read Notes/Flags before reporting a disposition** — do not infer a clean disposition from a clean tier label.
**Why:** Weyland Lead `2829292974` was falsely blocked by stale Account Status even though linked Account `2827365291` currently reads Customer Tier B / group B. Reading live current fields prevents that failure.
**Scope boundary:** Ninety remains the EOS-canon record; this rule governs CRM / customer / lead / material data. See `1-Brain/Systems/Customer Master.md` and `3-Projects/Monday-CRM/`.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `04 Customer & Account`

**History:** **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-21. v1's account-authority wording is the same sentence `[R-ACCT v3]` records as having *caused* the Inavogue defect it was meant to prevent: it excluded the one column carrying the commercial story. Notes/Flags is now named as mandatory evidence and cross-tagged. · **v1 19 Aug 2026** — promoted from AI memory entry `monday-single-source-of-truth` under brief SF-AI-NEUTRAL-001 §4.1. It had been carried only in private agent memory, which is not a carrier.

### R-C3 · v1 · LAW
**Minimum job = ONE SLAB, applied per job**, waived for A-tier accounts. Total material across the job must reach ≥ 1 slab of the specified material class. A galley kitchen of 2 pieces ≈ 1 slab passes. Vanity- or laundry-only jobs pass only if they TOTAL ≥ 1 slab.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account`

**History:** **v1** (pre-existing, registered 27 Jul 2026)

### R-RETAIL · v1 · LAW
**A job with no approved SteedForm trade customer supplying and installing the cabinetry is a DECLINE.** SteedForm is a B2B fabricator; the work reaches the client through a trade account.
⚖ **The test is the TRADE ACCOUNT BEHIND THE JOB — never who sent the email.** A homeowner emailing on behalf of their cabinetmaker is fine. A builder, designer or joiner with no SteedForm account is a decline, however they present.
**The decline is PERMANENT** — no "try us later" language. The primary redirect is the trade route: the enquirer engages an approved trade customer, who deals with SteedForm.
**The Direct Homeowner x1.55+ markup tier SURVIVES** and continues to apply where a trade account is behind the job and the homeowner is driving the project. The tier prices hand-holding; it is not a route around this rule.
**Why:** this is the highest-volume decline SteedForm sends — four in one month in August 2026 — and until 27 Aug 2026 it had neither a rule nor a template. `T-DECLINE-01` is scope-outside-capability, which is a different thing from client type, and the two were being conflated.
⚠ The screening skill carries a different test — *"retail/homeowner-direct OK only for a new-build kitchen with a qualified cabinetmaker involved"*. **That is superseded: the test is an approved trade account, not a qualified cabinetmaker.**
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `04 Customer & Account` · `09 Response Templates` (T-DECLINE-08)
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-08. Ratifies the rule T-DECLINE-08 had been citing as "pending ratification as R-RETAIL v1" since 27 Aug 2026.

### R-ENTITY · v1 · LAW
**"Who is asking" is a BLOCKING check → Needs Review.** Where no account matches confidently, the enquiry is not scored as if it came from a known customer.
⛔ **A near-miss is NEVER silently matched and NEVER silently dropped** `[R-ACCTMATCH v5]`. Write the confirm flag **verbatim** — *"possible account match: X — unconfirmed"* — and treat the account as **UNTIERED** until a human confirms. A wrong tier match is worse than no match, in both directions.
**An untiered account gets no tier-dependent treatment:** no A-tier waiver, no Gate-Selective handling, no markup, no SLA.
⚠ **This check runs after `[R-CLIENTFIT v1]`, not instead of it.** Client fit decides whether SteedForm acts for this enquirer at all; this decides whether the account behind them is known well enough to score.
**Why:** applied as blocking with no rule behind it. Its absence is what let a near-miss be silently resolved either way.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (C2) · `04 Customer & Account`
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — registers one of the seven layer-1 conditions named in `[R-BLOCK v3]`.

---

## 2. Material and capability

*Can we physically make what has been specified?*

### R-INTERSTATE · v1 · LAW
**Interstate-sourced material is a CUSTOMER-CLASS GATE, owned by the CLIENT dimension — not a Material amber and not a decline trigger in its own right.**
**Interstate scope is considered ONLY for an A-customer OR a commercial project** — either qualifies on its own. **For a non-A residential job, interstate material is DECLINED on supply risk.**
⚠ **The dimension matters.** The old M3 rung scored interstate as a priced 🟡 under Material, which is where supply exposure lives. But the test is *who the customer is*, not what the material is — so it homes under **Client**, and a decline outcome sitting in a Material amber rung was unhomed under the closed six-heading taxonomy.
**`T-DECLINE-05` keeps its interstate trigger line.** Interstate-only material on a small scope with no existing supplier relationship remains a valid ground for that letter — sent, like every occupancy-class decline, only after a human review `[R-OCCUPANCY v1]`.
**Why:** ratification #93 (21 Jul 2026) converted the amber into a gate, and the delta was recorded in the Lead Risk Assessment Standard's header but never implemented in its body. Three positions were live at once — a decline trigger in the template, a 🟡 in the risk standard, a gate in the skill — with nothing ranking them.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (Client lane · M3) · `07 Service Area & Site` · `09 Response Templates` (T-DECLINE-05)
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-10. Ratification #93 stated as a rule for the first time, and homed in the Client dimension.

### R-LEADTIME · v2 · LAW
**Production lead time is TIER-DEPENDENT. The screen quotes the figure for the account in front of it, never a single house figure.**

| Account | Measure-to-install | Basis |
|---|---|---|
| **A-tier** | **10–12 days** | Scheduled to meet the SLA. A-tier accounts get the priority slot. |
| **Everyone else** | **14–16 days** | The current actual. |

⛔ **AN UNTIERED ACCOUNT TAKES THE NON-A FIGURE.** Where the account match is unconfirmed, the account is untiered until a human confirms `[R-ENTITY v1]` — so it gets **14–16 days**. **Never quote the A-tier figure to an account that has not been confirmed as A-tier.** Fail toward the longer date, never toward the promise.

⛔ **A BLANK TIER MEANS UNVERIFIED, AND THAT IS THE POINT — IT IS NOT A DATA BACKLOG** (v2, 3 Sep 2026). The 10–12 day figure is what SteedForm **schedules for A-tier customers it has committed to**; 14–16 is the actual. An account nobody has tiered is an account nobody has vouched for, so **14–16 is the correct answer for it, not a degraded one.** Customer Tier being 68% blank (128 of 188, measured 3 Sep 2026) is therefore **not a fault in the data** and must not be reported as one.

⛔ **NEVER BULK-ASSIGN A TIER TO CLEAR BLANKS.** A tier written to tidy a column converts an honest **unverified** into a false **verified**, and every fail-closed behaviour keyed to the tier — this rule, the waiver, the markup — silently starts trusting it. **The only legitimate work here is confirming the accounts SteedForm has actually committed to**, one at a time, by someone who knows the relationship. ⚠ **The real exposure is the reverse case:** a genuine A-tier customer left untagged and quoted about a working week longer than SteedForm would hit for them. **Spot-check the known A-tier relationships; do not process the 128.**

**The two-factor timeline threshold moves with the tier.** The flag fires when the requested install date falls inside *(measure booking notice ≈ 2 weeks) + (measure-to-install)*:
- **A-tier → ≈ 22 days from enquiry** (2 weeks + 10–12)
- **Everyone else → ≈ 24–26 days from enquiry** (2 weeks + 14–16)

⚠ **Using the A-tier threshold for a non-A job under-fires the flag by about a working week — on exactly the accounts least able to absorb a slipped date.** The flag must resolve the account tier before it computes.

**The flag DOES THE MATH.** It states the earliest realistic install date. Never "tight".

⚠ **UNIT NOT STATED.** These figures are recorded as **working days**, consistent with the two-factor rule they feed. The source SLA table is calendar-framed and anchored on sign-off rather than measure, so the two have never been reconciled. **If these are calendar days, every date the flag emits is wrong by roughly a third** — confirm before the app quotes a date to a customer.

**Why:** the corpus carried "10 days from sign-off to install" with a ">95% meet 12 days" KPI, and separately "12 working days measure-to-install", with no statement that the real figure varied by account. A single house figure quoted to every customer was understating the date for most of them by about a working week.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (C6) · `04 Customer & Account` · `07 Service Area & Site` · `08 Board & Column Registry` (§7 coverage) · `10 Open Rulings` (OR-20 unit)
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-20. The SLA and the actual are not a conflict: A-tier accounts are scheduled to meet the SLA, everyone else runs at the actual. Recorded with the intent to close the gap. · **v2 3 Sep 2026 (Stella Rasheed)** — added after the board export showed Customer Tier 68% blank and the finding was first written up as a data backlog. **It is not one.** A blank tier means the account is unverified, 14–16 days is the right answer for an unverified account, and bulk-assigning tiers to clear the column would destroy the fail-closed property this rule depends on. Behaviour unchanged; the guard against "fixing" the blanks is new.

### R-M1 · v2 · LAW
**Material class is read LIVE from the Materials Library `color_mm4qt817` Material Type — never inferred from the brand name.** Class scoring: **engineered 🟢 · porcelain + sintered 🟡 · natural 🔴.** This supersedes the earlier Q15 position that porcelain/sintered dropped to green.
**CERAMIC scores as porcelain / sintered — 🟡.** Vasari is ceramic and is scored on that rung. The Materials Library value for Vasari items is to be set to match.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `05 Material & Capability` · `08 Board Registry & Mechanics`
**History:** **v1 21 Jul 2026** (ledger #131) · **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-19. Vasari's class of record is ruled **ceramic**, and ceramic is given a rung: it scores as porcelain/sintered. v1's three-class ladder had no place for it, so a ceramic material had no score at all.

### R-SUBTYPE · v2 · LAW
**The natural-stone verdict forks on granite vs non-granite, read from the live Materials Library `5029570546` column `dropdown_mm4rq7jd` Stone Sub-Type. It is populated on only 3 of 392 materials as at 18 Aug 2026.** For every blank item, a blank sub-type is **NOT** a licence to guess and **NOT** a reason for the granite rules to silently not fire:
- Apply the **conservative** branch — score the hard-stone tooling flag ("hard stone — tooling cost, price with care") as if it were granite, and
- **Always add the visible flag: "⚠ Stone Sub-Type not recorded — confirm granite vs non-granite before quoting."**

Never resolve the fork from the brand or colour name. *(Dolomite is routinely sold as quartzite — that mis-marketing trap is exactly why the board column exists.)*
**Why:** the rule depended on a column with no data and no stated fallback, so behaviour was undefined — the failure mode is a granite-specific cost silently never being applied.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability` · `08 Board Registry & Mechanics`

**History:** v1 27 Jul 2026 (found by audit: 0/380 populated) · **v2 18 Aug 2026** (live board/column reverified; coverage now 3/392, conservative blank fallback retained)

### R-PROFILE · v5 · LAW
**Edge profile × material capability — do not price a combination this set rules out.** Arris: all materials, straight and curved (the default). Pencil: hand-finished at every size, offered on full-body materials, **but 🔴 NEVER ON A FACE-PRINTED SURFACE** — a pencil radius rolls over the face edge and cuts through the print. **CONSTRUCTION IS THE TEST, NOT CLASS.** Read `Print Construction` (`color_mm6hz0dd`) live off Materials Library `5029570546`: `Face-printed` is a hard 🔴, `Full body` permits pencil, and **blank FAILS CLOSED to review — never read blank as "not printed"** `[R-REF v2]`. Porcelain and sintered remain excluded as a class. ⚠ **An engineered-stone classification does NOT mean full-body:** Kaya Surfaces — **all ranges** — are engineered stone AND face-printed (NEOVENA digital print, face only). **Zenith is full-body, with no exceptions** (corrected 7 Sep 2026). Sharknose/Euro: all materials, **straight line only**. Bullnose and Provincial/Lamb's Tongue: CNC, straight and curved, **engineered + marble ONLY** → 🔴 elsewhere. Double bullnose: CNC 20mm polish then laminate the two polished pieces. Triple bullnose 60mm: **theoretical only — treat as first-of-kind**. **Ogee: NOT OFFERED, removed from all documents.**
**Lamination = 20mm layers only** (→40mm, →60mm). **A PRINTED FACE CANNOT BE LAMINATED:** porcelain, ceramic and sintered never, and neither does any material whose `Print Construction` reads `Face-printed` — the print is the reason, the class is only a proxy. **Full-body engineered and marble laminate. Limestone and travertine are ruled not laminable (MD 23 Jul 2026).** The rest of natural stone — granite, quartzite — is **case by case, resolved by a person per job**; no column will carry it. ⚠ **Laminability does not set a faceting threshold** — they are different operations and `[R-D5 v8]`'s table is unchanged. Nothing below 40mm is mitred. Waterfall ends at 12/20/30/40mm are a standard chargeable install; a boxed island that cannot be glued in the factory is an **assemble-on-site** in every material.
**Scope: these rules run to 40mm.** 50–80mm has its own cost step; **>80mm is a hard cost cliff — flag it.**
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability` · `06 Evidence Requirements` · `08 Board Registry & Mechanics`

**History:** **v5 **7 Sep 2026 (GM, recorded by Stella Rasheed)**** — Zenith Ottoman Grey and Rosè are **not** face-printed. v3 named them from the Zenith/Kaya Manual May 2026 §7.2; that is corrected, the two board rows were cleared the same day, and the rule now reads simply: **all Kaya is face-printed, all Zenith is full-body.** The by-name carve-out in `05` §9 is retired with it. · **v4 **7 Sep 2026 (Stella Rasheed)**** — lamination restated by construction rather than class, matching what MD did to the pencil rule in v3: a printed face cannot be laminated, whatever the material is called. Hard natural moves from "never" to **case by case per job**; limestone and travertine stay ruled not laminable per MD. The faceting thresholds are deliberately untouched — lamination and faceting are different operations, and the reasoning in `[R-D5 v8]` that ties the two together is flagged for review rather than acted on. · v1 23 Jul 2026 (MD profile audit) · v2 27 Jul 2026 (30mm rule split out to R-30MM) · **v3 24 Aug 2026 (MD: the pencil prohibition restated by CONSTRUCTION, not class.** Every carrier said "porcelain/sintered", which is a proxy for the real test — a printed face. QU-58883 priced a 20mm Pencil on **Kaya Sienna**, which reads `Engineered Stone` on the Materials Library and is face-printed per the Zenith/Kaya Manual May 2026 §7.2. Both the quote and a full screen cleared it, because both followed the rule as written. New Materials Library field `color_mm6hz0dd` **Print Construction** is now the authority for the fact; blank fails closed.)

### R-30MM · v1 · LAW
**30mm is a NATURAL-STONE-ONLY single thickness** (subject to slab availability). **🔴 spec conflict on engineered, porcelain or sintered.** There is no 30mm build-up and no faceting at 30mm. A 30mm engineered benchtop cannot be made — reset the spec, do not price it.
**Why:** reached both sweeps and the Profile Matrix on 23 Jul but **not** the master skill or Risk Standard, so a 30mm engineered top would have scored 🟢 routine and been quoted.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability`

**History:** **v1 23 Jul 2026**, gap closed 27 Jul 2026

### R-RANGE · v1 · LAW
**A RANGE IS ENOUGH AT LEAD. A COLOUR IS REQUIRED AT ORDER.** A customer who specifies
*"Caesarstone ICON"* without naming a colour has given a sufficient material specification for a
quote. **Read the range's own properties and quote against them** — ICON is Engineered Stone and
Full body, so a pencil profile is offered and there is nothing to flag. **⛔ A range-only
specification must NOT be flagged in a way that holds up quoting.**

**How a range answers.** Read the rows carrying that `Brand / Range` (`dropdown_mm4p7eja`, Materials
Library `5029570546`) and take the value where **they all agree**. Verified 7 Sep 2026: all
thirteen ranges are uniform on both Material Type and Print Construction, so every one of them
answers today. ⚠ **Where the rows DISAGREE the range answers nothing and the colour is required** —
this is a live test against the board, never a frozen list, because a face-printed colour added to
a full-body range would silently break a rule stated any other way.

**At ORDER the colour is required** and its absence is a gap like any other `[R-EVIDENCE-BAR v2]`.
A range cannot carry slab availability, vein character, part-slab waste or a price band, and those
are order facts.

**Why:** quoting is how SteedForm wins the job, and a customer naming a range has told us what they
want in the terms suppliers actually sell in. Treating that as missing information turns a normal
enquiry into a question, and the estimator who has to answer it already knows the range is full
body. **Missing evidence is never a match and never green — but a range is not missing evidence.**
**Carried by:** `05 Material & Capability` · `06 Evidence Requirements` · `03 Risk Scoring`

**History:** **v1 **7 Sep 2026 (Stella Rasheed)**** — registered after a range-only specification
was being treated as an unresolved material.

### R-D5 · v8 · LAW
**A curve is polished only up to that MATERIAL's limit; above it the curve is a FACETED MITRE — makeable, never a decline.** The limit is **material-dependent, not a flat 40mm**, because only engineered and marble can laminate:
- **Engineered · marble** — polished to a 40mm lamination (20+20); **faceted from 60mm**
- **Porcelain · sintered** — single thickness only (12/20), never laminated; **faceted from 40mm**
- **Hard natural (granite, quartzite, limestone, travertine)** — single thickness (12/20/30); **faceted from 40mm**. **Limestone and travertine are RULED not laminable (MD 23 Jul 2026) — this is not a pending question.**

**A curve on SINGLE THICKNESS (12 / 20 / 30) is ordinary work and scores nothing on its own** — the tooling is built for it. **A request for faceting BELOW 40mm scores 🟡:** below the lamination threshold there is nothing to facet, so the specification needs checking rather than pricing. Splayed and angled benches remain 🟡 always, unchanged.

⚠ **THE MARBLE-vs-HARD-NATURAL SPLIT IS RESOLVED BY A PERSON, PER JOB.** This rule needs to know whether a natural stone is **marble** (polished to 40mm, faceted from 60mm) or **hard natural** (faceted from 40mm).

✅ **CORRECTION, 7 Sep 2026.** Earlier versions of this rule said `dropdown_mm4rq7jd` Stone Sub-Type "is granite vs non-granite, which does not identify marble". **That was wrong.** The live column offers exactly five choices — **Granite · Marble · Quartzite · Travertine · Limestone** — which is every branch this rule needs. It is populated on **3 of 392** materials, so 50 of 53 naturals still say nothing.

⛔ **A populated value does NOT close the question.** The split stays a person's call per job (ruled 7 Sep 2026, reviewed and reaffirmed the same day after the correction above). The column is **evidence a screen may report, never the authority that settles it** — the coverage is 3 of 392 and unaudited, and the failure is one-sided: a wrong `Marble` promises a polished 40mm curve on granite that cannot be made, which is the mis-sell this rule exists for. A wrong `Granite` only quotes a facet where a polish was possible.
**Treat any natural stone as HARD NATURAL — faceted from 40mm — and flag "⚠ marble vs hard natural not derivable from the board; confirm before quoting the curve".**
**Why that direction:** assuming marble and being wrong means **promising a polished 40mm curve on granite that cannot be made** — the exact mis-sell this rule was written to stop. Assuming hard natural and being wrong means quoting a facet where a polish was possible: recoverable, and visible at sign-off. Never resolve it from the colour or brand name.

**Why this direction:** asking for a faceted sign-off you did not strictly need costs a conversation. Promising a polished radius that cannot be made costs a remake and a client. **When the data is missing, fail toward the flag, never toward the promise.**

**The flag string is fixed. Emit it verbatim:** *"⚠ marble vs hard natural not derivable from the board; confirm before quoting the curve"*.

A curve above the limit scores **🟡 + a MANDATORY documented client sign-off on the faceted appearance before fabrication**. It is **NOT blocking** and must never force Needs Review. **The document is the SIGNED ORDER CONFIRMATION** (ruled 7 Sep 2026) — so a screen never confirms a sign-off has happened; it states the condition and names what will carry it.

Faceting is also elective from 40mm on any material, and is frequently the *recommendation* on veined stone — a polished radius grinds through the vein, a facet preserves it. **On engineered and marble, "elective" means the vein is too clashy for lamination** (ruled 7 Sep 2026): two glue lines break the vein twice, and faceting is the alternative route. **The trade is that the curve will not necessarily be smooth, and that trade is the CUSTOMER's call** — offered by the estimator, decided by the client, and carried by the same signed order confirmation.
**Why:** v1 (blocking 🔴) → v2 (flat >40mm faceted) → v3. **v2 caused a live mis-sell**: a 40mm curved porcelain or granite edge passed with no sign-off, and the client would have been quoted a polished radius that cannot be made.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability`

**History:** **v8 **7 Sep 2026 (Stella Rasheed)**** — corrects a factual error carried since v4: Stone Sub-Type does express marble, and every branch of this rule is answerable from it. The ruling that a person resolves the split per job is **reviewed and kept**, deliberately and with the correction in front of it: a column at 3 of 392, where being wrong one way is a remake, is evidence and not authority. · **v7 **7 Sep 2026 (Stella Rasheed)**** — a curve on single thickness no longer scores on its own, and the 🟡 moves to a faceting request below 40mm; the sign-off document is named as the signed order confirmation; the marble split is recorded as a permanent human call rather than a wait for a field; and "if the vein justifies it" is defined, with the trade-off placed with the customer. · **v6 3 Sep 2026 (Stella Rasheed)** — closes OR-32 and OR-33. One canonical flag string is nominated; limestone and travertine are confirmed ruled rather than pending, so no carrier can reopen a settled question. · v1 20 Jul 2026 · v2 23 Jul 2026 (MD profile audit, supersedes Q18 blocking rule) · v3 25 Jul 2026 (material-dependent thresholds) · v4 27 Jul 2026 (conservative fallback) · **v5 18 Aug 2026** (live Materials identifiers and 3/392 coverage reverified; fallback unchanged)

### R-MA2 · v1 · LAW
**Vein-match Level-3, or match-to-existing installed stone, is BLOCKING → Needs Review.** Vein-continuity geometry below Level 3 is a **non-blocking** flag, triggered on **geometry alone** — a veined colour on 2+ adjacent visible faces (island + waterfall, book-match pairs, continuity runs) — and never waits for a stated client expectation. Feasibility is read live from `boolean_mm4r4qcp` Bookmatch Available.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability` · `08 Board Registry & Mechanics`

**History:** **v1 20 Jul 2026** (Q12 + Q18)

### R-SCOPE · v2 · LAW
**NOT OFFERED. Each item carries its OWN screening action — DECLINE or RESET. The two are never interchangeable.**

| Not offered | Action at screening |
|---|---|
| Flooring (any material) | **DECLINE or refer** |
| Stone shower bases and fall drainers | **DECLINE or refer** |
| Drainer grooves (any material) | **DECLINE or refer** |
| Bathroom hobs (raised wet-area kerbs — **not** cooktops) | **DECLINE or refer** |
| Machined recesses / chutes / glazing | **DECLINE or refer** |
| Replacement or remedial work on someone else's stone | **DECLINE or refer** |
| Client-supplied slabs | **DECLINE** — one carve-out, below |
| IKEA kitchens | **DECLINE or refer** |
| **Flush mounting** | **RESET** the spec to a supported mount, before the quote `[R-FLUSH v1]` |
| **Masons mitre as a standalone selection** | **RESET** the spec to SteedForm's standard mitred build. 🟡 substitute note, non-blocking |
| **The ogee profile** | **RESET** the spec to a **lamb's tongue** (Provincial) |

⛔ **A DECLINE item is not a specification to be corrected.** Do not price it, do not substitute around it, do not render it 🟡.
⛔ **A RESET item is not a decline.** The enquiry continues on a supported specification, and the client is told before the quote goes out.

**Client-supplied slabs — the ONLY carve-out.** A hard stop for every account **except an A-tier account, where it becomes a 🔴 RISK routed to Needs Review** for a named human to accept or decline. No other item in this table carries a carve-out.

⚠ **The CNC masons-mitre exception is a PRODUCTION decision, not a screening one.** Technical Standards records that a piece already on the CNC for profiling or lamination absorbs a masons mitre at no meaningful extra cost. **The screen must never promise it.** It is at production's discretion and is not decided until the job is in production.
**Why:** v1 stated one blanket action — "decline or refer, never quote" — for a list whose members need two different actions, while `[R-ANDON v1]` stated the opposite action for the same list. Two LAWs mandating opposite treatments left the screen unable to verdict any NOT-OFFERED item at all.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account` · `05 Material & Capability` · `09 Response Templates`
**History:** **v1 21 Jul 2026** (ledger #103/#116/#124/#31/#135/#136/#150/#85) · **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-01, OR-02 and OR-03. The blanket action becomes a per-item DECLINE/RESET table; ogee resets to lamb's tongue; client-supplied slabs gain an A-tier carve-out; the CNC masons-mitre exception is confirmed as production's call and excluded from screening.

### R-FLUSH · v1 · LAW
**Flush mounting is NOT OFFERED. Ever.** A sink or cooktop set flush into the stone (rather than top-mount, undermount or farmhouse) is a hard technical refusal, not a preference and not a pricing question: the stone edge chips, the silicone gap is unavoidable, and the brochure image cannot be reproduced in fabrication.
**At screening:** any appliance specified as flush-mount gets a **🔴 condition entry with the reason stated** (chipping · silicone gap · brochure vs reality) and the spec is reset to a supported mount. **The builder/client must be told BEFORE the quote goes out** — a flush-mount expectation discovered at install is a remake.
**Not an edge profile.** Flush mounting is a *mounting method*, so `[R-PROFILE]` does not cover it — that rule governs edge profile × material. This is a separate capability refusal and needs its own tag.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `05 Material & Capability` · `09 Response Templates`

**History:** **v1 28 Jul 2026** — registered on discovering it was stated in **three** places in the master skill and in **no** rule; it had been carried as an untagged orphan since the profile audit.

### R-MATERIAL-TERMS · v1 · LAW
**Supplier commercial ranges, slab format, finish and colour are separate evidence.**

- `M2` and `M4` are supplier commercial range/tier labels comparable to Essentials or Deluxe. They are not colour/material codes, material class, thickness, finish or slab size. Do not search them as library colours or infer material capability from them.
- Bare `Zenith`, `Zenith Surfaces`, or `Stone Ambassador – Zenith` means the Zenith engineered-stone brand/range. Only explicit `Dekton Zenith` means Dekton brand with Zenith colour. Bare Zenith must not trigger porcelain/sintered or printed-face restrictions.
- `GRANDE` is slab size/format, not supplier, brand, range, colour, finish or Material Sub-Type.
- `Polish` canonicalises only to `Polished`. It is never equivalent to `Matt` or another finish.
- At Lead/quoting stage, an evidenced brand/range or commercial tier may support an allowance while exact colour remains TBC. Exact colour/revision must be confirmed at Order commitment before manufacture when the accepted product requires it.
- Materials Library linking remains exact and unique; no fuzzy, contains or closest-result matching.

**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `05 Material & Capability` · `06 Evidence Requirements`

**History:** **v1 18 Aug 2026 (MD)** — consolidated rules that previously existed only in selected live agent plans.

### R-DEKTON · v1 · LAW
**Dekton is being phased out. Specified anywhere → 🔴; decline as specified, with a substitution steer.** Flag reads **verbatim**: *"Dekton — phase-out in progress, do not quote"*.
**The materiality exception is available to A-TIER ACCOUNTS ONLY.** For a B-tier account or below there is no exception: decline and substitute.
**The exception is a FOUR-CONDITION test, all four required:** Dekton is a minor component (≤ 1 room / 1–2 pieces) **AND** the bulk of the job is another material **AND** the job is substantial (~$10k+) **AND** the customer will not substitute. Met, on an A-tier account → **Needs Review**, and a named human decides.
⛔ **It is NOT "the client asked".** The looser wording *"do not quote on new Dekton work unless specifically requested by client"* is **RETIRED** wherever it appears.
**The exception converts the OUTCOME to a human call. It never lowers the colour** — the material line stays 🔴.
**Why:** SteedForm would rather substitute in every case. The exception exists so a substantial A-tier job is not lost over one room, not so that any client who insists gets Dekton.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `05 Material & Capability` · `09 Response Templates` (T-DECLINE-06)
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-09. Ratifies the rule T-DECLINE-06 and SteedForm Identity had both been citing as "pending ratification as R-DEKTON v1"; adds the A-tier gate, which no prior statement carried.

### R-NATURAL · v1 · LAW
**The natural-stone rule set. BLOCKING → Needs Review on every branch below except the last.** Replaces all former "minority of rooms" and volume language, everywhere.

**1 · GRANITE → passes clean for known trade**, in any room **including the kitchen**.
- **"Known trade"** = a tiered A-account, **OR** an established trade customer with an existing account or trading history.
- **NEVER** where the live Customer Tier is `Do-Not-Quote`.
- **NEVER** on a Gate-flagged account whose match is unconfirmed.
- **Retail-direct + granite → always Needs Review.**

**2 · NON-GRANITE naturals** (marble / Calacatta-class, quartzite, travertine, limestone):
- **Kitchen →** approved tiers only **AND** a style-of-work review — **Needs Review even for approved tiers**. Everyone else, Needs Review.
- **Other rooms →** Needs Review, **with the reason written in the flag**.

**3 · An ALL-NATURAL job from an unknown account → Needs Review**, flag **verbatim**: *"who is asking — is this a future client we want?"*

**4 · The FIRST natural-stone job on ANY account →** a **NON-BLOCKING** flag, **verbatim**: *"first natural job with this account — confirm slab-selection process"*.

⛔ **Soft natural (Mohs ≤ 5) in a kitchen, scullery, coffee station or heavy-wear wet area → 🔴 Needs Review, NEVER an auto-decline.** Technical Standards states DECLINE for this condition; **that is superseded** — a human makes the call.
**Volume and room count are RETIRED as verdict tests.** Slab count appears only as a pricing note. Complexity flags — curves, mitres, vein matching — still apply on top.
⚠ Where the granite fork cannot be resolved, `dropdown_mm4rq7jd` Stone Sub-Type is populated on only 3 of 392 materials: take the conservative branch and flag it `[R-SUBTYPE v2]`.
**Why:** every carrier applied this set and no rule stated it. `[R-SUBTYPE v2]` turns on a granite/non-granite fork it never itself defined, which meant the fork existed only in prose.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (M1) · `05 Material & Capability`
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-37 and registers one of the seven layer-1 conditions named in `[R-BLOCK v3]`. Set adopted 19 Jul 2026; stated as a rule for the first time here.

---

## 3. Evidence and verdicts

*Do we know enough to judge, and what verdict follows?*

### R-ALFRESCO · v1 · LAW
⛔ **ENGINEERED STONE CANNOT BE USED FOR AN ALFRESCO OR BARBECUE BENCHTOP.** Australian Standards require the benchtop in a barbecue area to be non-flammable. SteedForm makes alfresco tops in **natural stone, or ceramic / sintered** — nothing else. Engineered specified for an alfresco scope is a 🔴 **spec conflict**: reset the material before quote.
⚠ **THIS IS A CLASS TEST, NOT A BRAND TEST.** The prior rule named four indoor-only brands — Zenith, Kaya, Silestone QXeron, Caesarstone ICON. All four are engineered, so the brand list gave the right answer by accident, and **any engineered brand not on that list passed.** Read the class live off Materials Library `color_mm4qt817` `[R-M1 v2]`. Same defect shape as the pencil-on-a-printed-face rule before `[R-PROFILE v5]` moved it to the real test.

**The shadowline is a MEASURE precondition, not a preference.** A **12 mm thick × 50 mm wide** shadow line is installed **by the cabinetmaker** and **must be in place before site measure can be completed**. 12 mm compact, edged MDF or painted edge. **Not required where the benchtop is thicker than 40 mm.** Flag it at first builder contact — a measure that arrives to no shadowline is a wasted trip.

**Fibre cement** runs the entire alfresco surface behind the shadowline, protecting the stone as cabinetry moves and acting as the non-flammable barrier. **Thickness is 6 mm or 9 mm, selected by the gap between stone and carcass** — not a fixed figure.
⚠ **A 12 mm fibre cement sheet is a RETIRED offering.** Where a document or template says "12 mm fibre cement", it has conflated the sheet with the shadowline and is wrong.

**Barbecue well:** dimensions must account for the thickness of **both the fibre cement and the stone**, plus the barbecue's own dimensions. With a barbecue jacket, allow for stone and fibre cement **if the jacket is not insulated**. Stone is required only on **visible** portions; exposed fibre cement may be used elsewhere.
**Cutout allowances:** top-mount sink = manufacturer cutout **+10 mm** · undermount sink = manufacturer flange depth **+10 mm** · drop-in barbecue = manufacturer cutout **including radiused stone corners**, plus a **continuous** ventilation gap below, between appliance and stone.

**Why:** the class rule existed only as a brand list, and the substrate figure existed in the corpus as 9 mm in five places, 10 mm in one and 12 mm in a customer-facing template — three numbers for two different components. The controlled standard settles both.
**Source:** `STD-0017 Alfresco Standard`, Rev 1 — prepared and approved by James Hill, 14 August 2026. **Controlled document; it supersedes every earlier alfresco figure in this knowledge base.**
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (M6) · `05 Material & Capability` · `09 Response Templates` (T-TECHNICAL-02)
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — registered on receipt of STD-0017 Rev 1. Reverses the 3 Sep ruling on OR-18 that `T-TECHNICAL-02`'s 12 mm should stand: that ruling rested on the 12 mm being a deliberate clearance allowance, which STD-0017 shows it is not.

### R-EVIDENCE-BAR · v2 · LAW
**One criteria set, two evidence bars. The gate decides what counts as satisfying a fact — never whether the fact matters.** Screening asks the same question at both gates — *is this project right for SteedForm* — and the fact vocabulary is identical. What changes is the standard of evidence.

**THE GATE IS AN EXPLICIT INPUT AND IS NEVER INFERRED.** A screen that does not know which gate it is running is the failure that costs a slab: an Order screened at Lead evidence commits on "white stone TBC".

| Fact | LEAD bar — enough to price and quote | ORDER bar — enough to commit to manufacture |
|---|---|---|
| Material / colour | brand, range, category or commercial tier `[R-MATERIAL-TERMS v1]` | exact colour name + finish `[R-MATERIAL-TERMS v1]` |
| Thickness | nominal, by area | confirmed per piece |
| Edge profile | generic (pencil, mitred 40) | exact profile, material-checked against the Capability Matrix **and against `Print Construction` `color_mm6hz0dd`** `[R-PROFILE v5]` |
| Cut-outs | count + generic type | model number + Appliance Library link + QC Status |
| Appliances / sinks | generic description | model number, mounting type, linked Library record **+ QC Status** |
| Site | suburb / postcode | full SITE street address; **plus the DELIVERY address whenever it differs from site** (the supply-only / freight case, `[R-SUPPLYONLY v1]`). Billing is an accounts field and is never a screening bar |
| Drawing revision | any current set | the accepted revision, matching the quote baseline |

**At LEAD, a gap below the ORDER bar is 🟡 — priced or confirmed, never a verdict change.** Generic terms alone must never produce Needs Info, Needs Review or Unqualified.

**At ORDER, a gap below the ORDER bar is BLOCKING. There is no exception and nobody may waive it — not the screen, not a reviewer, not the MD.** The order proceeds when the evidence exists, and not before. The release valve is obtaining the fact, never accepting its absence.

**Two facts are resolved from the board, never asserted from a document.** Appliance and sink QC Status is the release verdict on Appliance Library `5029694677` — `Rejected — Do Not Use` is a hard block. A screen FLAGS these for lookup; it never reports a release verdict it read in a PDF.

**An ORDER screen requires the accepted quote evidence package as its baseline. If the baseline is absent or stale: keep capturing, refuse to judge, and say so.** An Order screen without a baseline has not checked the thing it exists to check.

⚠ **This rule SITS ALONGSIDE `[R-MA5 v3]`; it does not narrow it.** This bar states what facts must be present at ORDER. R-MA5 states where the appliance must physically be, and when. Satisfying this bar does not satisfy R-MA5.
**Why:** at Lead the job is to price an allowance and decide whether to quote — demanding exact specification there jams the queue with Needs Info on work SteedForm wants. At Order the job is to commit metal to a saw — accepting an allowance there is how a remake happens. The same fact, judged at the wrong bar, fails in both directions.

⚠ **RESOLVED 26 Aug 2026 (MD).** v1 recorded a contingency: the pipeline sweeps were deliberately not carriers, and *"if retirement slips, add them as carriers."* **Retirement did not slip** — both sweeps were disabled 20–21 Aug 2026. The contingency is closed and the sweeps must not be re-added. Enforcement of this rule now sits with the `estimator-screening` skill and Claude deep scans, until the Deep Screen app takes it.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability` · `06 Evidence Requirements` · `07 Service Area & Site`

**History:** **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-04. The Appliances/sinks ORDER bar gains QC Status, matching the adjacent Cut-outs row; the two rows had differed inside this file, so "the Register wins" could not adjudicate them. Confirmed as sitting alongside R-MA5, not narrowing it. · **v1 23 Aug 2026 (MD)** — generalises the Lead/Order evidence principle registered for material at `R-MATERIAL-TERMS v1`; absorbs the quote-stage appliance rule previously stated only in the Appliance Verification Standard.

### R-DRAWINGS · v1 · LAW
**Drawings are MANDATORY at screening — all tiers, no exceptions, including A-tier.** If there are no readable plans after every extraction attempt (OCR, vision, opening the portal/attachment), the verdict is **Needs Info** — **never Qualified**.
**"Readable" means the takeoff can actually be done from them**, not merely that a file exists: a file column with an unopenable, blank, or illegible attachment is the same as no drawing. **Never infer dimensions to get past this gate** — an assumed dimension becomes a cut piece.
**Distinct from the blocking list** `[R-BLOCK]`: that list routes to **Needs Review** (a human decides). This one routes to **Needs Info** (the client must supply something). Do not collapse the two verdicts — they go to different people.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `04 Customer & Account` · `06 Evidence Requirements` · `09 Response Templates`

**History:** **v1 28 Jul 2026** — registered as an untagged orphan; it is a verdict-determining gate that no rule owned.

---

### R-BLOCK · v3 · LAW
**The blocking list has TWO layers. Both are closed.**

**LAYER 1 — the base list.** Applied since screening began; **registered 3 Sep 2026** because it had never been written down.
occupancy `[R-OCCUPANCY v1]` · live Customer Tier `Do-Not-Quote`, or an unresolved account match `[R-C1 v4]` `[R-ACCTMATCH v5]` · out of area while the Supply Only conversion is undecided `[R-AREA v1]` · spec conflicts `[R-30MM v1]` `[R-PROFILE v5]` · below the one-slab minimum, non-A-tier `[R-C3 v1]` · the natural-stone rule set `[R-NATURAL v1]` · unknown-entity checks `[R-ENTITY v1]`.

**LAYER 2 — the 20 July 2026 addition set. SIX rules, not seven:** clad fireplace with no published brand rule · trench/rebate to receive joinery · first-of-kind fabrication with no fab rule · appliance QC Status `Rejected — Do Not Use` · vein-match Level-3 or match-to-existing · client-supplied stone.

⛔ **"Curves >40mm" was STRUCK from layer 2 on 23 Jul 2026 — see `[R-D5 v8]`.** It must never be re-added, and **"seven" is stale wherever it appears.**
**Ropox Flexi Electric is APPROVED and is NOT first-of-kind.**
Both layers are amended only by an **MD or GM** decision, recorded here with a version bump.
**Why:** the stale count "seven" has been found and fixed **four separate times** in different files; each time it silently revived the struck curves rule. v2 fixed the count but described layer 2 as "the blocking closed list", which read as the whole list — leaving seven conditions the screen applies every day with no rule behind them.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `06 Evidence Requirements` · `07 Service Area & Site` · `09 Response Templates`
**History:** v1 20 Jul 2026 (seven adopted) · **v2 23 Jul 2026** (curves struck → six) · **v3 **3 Sep 2026 (Stella Rasheed)**** — closes OR-06. The two layers are separated and named; layer 1 is registered for the first time, as six new rules.

### R-ANDON · v2 · LAW
**⛔ CAPABILITY and 🔴 RISK are two different verdicts and MUST NEVER BLEND (MD ruling 23 Jul 2026).** Both currently render as one undifferentiated 🔴, which is the bug.
- **⛔ CAPABILITY / NOT-OFFERED = "we cannot make this."** A **hard stop**. No human call can authorise it — the tooling, the material physics or the ruled scope simply is not there. *(Profiles we lack tooling for · flush mount · bathroom hobs · drainer grooves · flooring · shower bases · pencil on a printed face · lamination on porcelain/sintered/hard natural · 30mm on anything but natural · ogee.)* **The ACTION is per item — DECLINE or RESET — and is stated in `[R-SCOPE v2]`, not here.** This rule classifies; R-SCOPE disposes.
- **🔴 RISK = "this is far from our optimum."** A **human call**: take it and price it properly, or decline it as not for us. **Both answers are valid.** *(Natural stone · 50mm+ builds · vein · boxed islands · large splashbacks · non-standard details.)*

**Say which one it is, every time.** Blend them and one of two failures follows: treat a capability gap as risk and someone eventually **human-calls their way into promising a job that physically cannot be made**; treat risk as capability and screening starts **declining work SteedForm actively sells** — a boxed island is 🔴 on geometry but is standard, all-material, charged work.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `05 Material & Capability` · `07 Service Area & Site`

**History:** **v1 23 Jul 2026** (MD), registered 27 Jul 2026 after an audit found it had reached no executable as a scoring rule · **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-01. v1 said every capability item gets its spec reset, which directly contradicted R-SCOPE v1's "a reset treatment is wrong for all of them" over the same list. The capability/risk classification is unchanged; the action now lives in `[R-SCOPE v2]`, per item.

### R-MA5 · v3 · LAW
**An appliance or sink whose QC Status is `Rejected — Do Not Use` scores 🔴 BLOCKING — never quote around it.** A model **absent from the Appliance Library, or not `Verified — Released`,** scores 🟡 at the lead stage — but per #54/#91 it becomes a **hard ORDER-GATE condition: the unit must be physically delivered TO STEEDFORM — the factory, NOT the client's site — BEFORE MEASURE**, and the gate cannot close until either the library record reads `Verified — Released` or the unit is at SteedForm with a library record.
**Why:** we must measure, program, dry-fit and library-register the unit. A unit 40km away at the client's site satisfies none of that, so "on site" is not an acceptable gate condition. v1 said "to site" in the master skill and Risk Standard — and the master wins on conflict, so the *wrong* location was governing.
⚠ **A SUPPLIER CAD IS AN INTERIM ARTEFACT ONLY.** The appliance manufacturer's CAD may be obtained and used to measure and program ahead of the unit's arrival, but **it never closes the gate** — a CAD cannot be dry-fitted, and release requires a dry-fit pass. The physical unit is still required.
⚠ **This rule SITS ALONGSIDE `[R-EVIDENCE-BAR v2]`; it is not narrowed by it.** The evidence bar states what facts must be present at ORDER. This rule states where the unit must physically be. Both apply.
⚠ **Exact live labels are `Verified — Released` and `Rejected — Do Not Use`.** `Released — Verified` is a GROUP TITLE, not a status label; matching on it silently fails.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `06 Evidence Requirements` · `08 Board Registry & Mechanics`

**History:** v1 21 Jul 2026 · **v2 27 Jul 2026** (location corrected to SteedForm; exact label strings pinned) · **v3 **3 Sep 2026 (Stella Rasheed)**** — closes OR-05. The parenthetical "(or its supplier CAD)" is struck from the delivery clause: it opened a door the rule's own closing conditions never included, in a sentence written for physical units. A CAD is interim only.

### R-RESCREEN · v1 · LAW
**Every risk strip records the rules version it was scored under — but nothing compares that stamp to the CURRENT version, so a rule change never re-screens the leads it affects.** Two triggers must exist, and only the second currently does:
1. **RULES CHANGED → re-screen.** When a Register rule bumps its version, every open lead whose strip was stamped under the older version is **stale by definition**. The daily sweep must list them: *"N open leads scored under pre-<rule> rules — re-screen"*. Cite the rule ID so the scope is obvious.
2. **ACCOUNT CHANGED → re-screen** (Duty 3.5, already live) — a tier/status/rating change re-screens that account's open leads.

**Why it matters:** on 25 Jul the faceting threshold changed and **84 strips were stale**; they were only found because a human went looking. A rule can be corrected everywhere and still leave every previously-screened lead carrying the old verdict.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `07 Service Area & Site`

**History:** **v1 27 Jul 2026**

---

## 4. Site, service area and logistics

*Can we get to it, and can we work there?*

### R-SITE · v1 · LAW
**Whenever a street address is held, the screen LOOKS IT UP. Site access is assessed from the actual address — never reasoned from the suburb.** A postcode gives you distance. It does not tell you what the building is, who is trading in it, where the truck unloads, or whether the truck can stay.

**Four questions, answered and recorded in this order:**
1. **What is the building, and is it occupied?** Read the live tenant directory. A trading tenancy at street level makes it an occupied commercial building — that is a **C7 / Me1 fact established at screening**, not an assumption to confirm later.
2. **Where does the truck unload?** Street frontage, loading zone, dock or laneway — and whether a council permit, traffic management plan or insurance certificate is a **precondition with lead time**.
3. **Where does the truck GO during the works?** Check published clearances against the confirmed vehicle envelope — **Isuzu NNR 45-150: ~2.06 m wide, ~2.24 m cab, ≈2.5 m × ~3.0 m clear travel stowed, 4,500 kg laden** (Technical Standards §7). Most CBD car parks are ~2.0 m and **will not take it**. "The crew parks somewhere" is not an answer; no vehicle on site means no tools, and no removal of packaging, offcuts or silica-controlled waste.
4. **What is the path from unload point to the work area**, measured against the **largest piece**, not the average one.

**At LEAD the site bar is suburb/postcode `[R-EVIDENCE-BAR v1]` — this rule does not raise it.** Where only a suburb is held, no lookup is possible: say so and suffix the access lanes "— (insufficient info)". **Unknown is never 🟢.** Where a street address IS held, the lookup is **not optional**, and its absence is a defect in the screen, not a gap in the enquiry.

**Where a screen cannot browse**, it must FLAG the site assessment as outstanding and refuse to score Install or Measure green. Never substitute a suburb-level assumption for a lookup that was not done.

**Why:** Veriu Hotel, 80 King William Street, Adelaide (26 Aug 2026). The screen scored CBD access as a comfortable priced amber from the suburb alone. A four-minute lookup showed the building is the **trading William Grenfell Centre with a Westpac branch on the ground floor**, and that published clearances at every car park in the precinct (**1.96–2.06 m**) exclude the truck entirely. Three lanes moved — C7 and Me1 to 🔴, I1 to the top of 🟡 — and the question "where do we park for the day" turned out to have no answer. The **distance** audit was already mandatory in every brief. The **address** was not.

**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `07 Service Area & Site`

**History:** **v1 26 Aug 2026 (MD)** — registered at MD direction during the Veriu deep screen, verbatim: *"Important finding - always assess the address and logistics involved."*

### R-SUPPLYONLY · v2 · LAW
**A `Supply Only` zone is a DIFFERENT DELIVERY MODEL, not a degraded one — and never a decline reason (MD, 27 Jul 2026).** Confirmed zones: **Port Lincoln 5606** · **Kingscote / Kangaroo Island 5223**. Both are established regular customers.

**The process:** the **CLIENT sends their own A-frame**. We **manufacture off THEIR measurements — SteedForm does not measure.** Final **CAD goes to the customer for sign-off BEFORE manufacture.** We load the A-frame; **THEIR transport company ships it.**

**What that changes at screening:**
- **Distance is NOT a risk and NOT a decline.** 646km to Port Lincoln, and a **sea crossing to KI, are the CLIENT'S transport** — not a SteedForm freight, access or lifting problem. Do not score them as one.
- **The MEASURE dimension does not apply in the usual way.** We never attend site, so site access, measure-readiness and occupancy are irrelevant. **What replaces it: DIMENSIONAL RESPONSIBILITY SITS WITH THE CLIENT.** Record explicitly that dimensions are client-supplied, so liability for a mis-measure is unambiguous before anything is cut.
- **The INSTALL dimension does not apply.** No SteedForm install, no lifting, no site conditions, no install-readiness rating.
- ⛔ **A SEA CROSSING OUTSIDE A CONFIRMED SUPPLY ONLY ZONE ALWAYS ESCALATES TO A HUMAN, regardless of km.** Inside a confirmed zone the crossing is the client's transport and is not scored at all. Outside one, it is not ordinary distance and the zone board does not settle it.
- ⛔ **CAD SIGN-OFF BEFORE MANUFACTURE IS A HARD GATE.** Nothing is cut until the customer has signed off the final CAD. It is the only verification step left once SteedForm's own measure is out of the process — skip it and there is no check at all between the client's numbers and finished stone.

⚠ **Leads and deals in these zones screened BEFORE 27 Jul 2026 may carry wrong flags** — out-of-area, measure access, install lifting, sea crossing — because the zone board was silent and the fallback was "~100km road distance". ~8 live deals are affected (six Port Lincoln, two Kingscote). Re-screen them `[R-RESCREEN v1]`.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `02 Verdicts & Precedence` · `03 Risk Scoring` · `06 Evidence Requirements` · `07 Service Area & Site` · `09 Response Templates`

**History:** **v2 **3 Sep 2026 (Stella Rasheed)**** — closes OR-15. The skill's unconditional "a sea crossing always escalates" is scoped: it does not fire inside a confirmed zone, and it does fire everywhere else. · **v1 27 Jul 2026** (MD, closing the gap where the two busiest regional clusters had no zone row at all)

### R-OCCUPANCY · v1 · LAW
**An occupied dwelling or a trading ongoing concern is BLOCKING → Needs Review. It is NEVER an auto-decline** (occupancy carve-out, ratified #61). A stripped site in a CBD building scores 🟡.
**Occupancy is ESTABLISHED BY THE ADDRESS LOOKUP, never assumed** `[R-SITE v1]`. A trading tenancy at street level makes it an occupied commercial building — a fact at screening, not something to confirm later.
⛔ **The decline letter may only be sent AFTER a human review.** `T-DECLINE-05` is what a person sends once they have decided to decline; it is never a triage output.
**Why:** the condition has been applied as blocking since screening began with no rule behind it. SteedForm Identity separately carried *"Tenanted occupied residential building → DECLINE"*, which is **retired** — a machine may not turn away an occupied job on keyword evidence.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (C7 · Me1) · `07 Service Area & Site` · `09 Response Templates`
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-11 and registers one of the seven layer-1 conditions named in `[R-BLOCK v3]`.

### R-AREA · v1 · LAW
**Out of area is BLOCKING while the Supply Only conversion is undecided → 🔴, Needs Review. It is NEVER a decline reason** `[R-SUPPLYONLY v2]`.
Once `Job Type` is set to **`Supply Only [− FREIGHT]`** the lane drops to 🟡 and the job proceeds on that delivery model.
**The Serviceable Areas board decides the zone wherever it lists the area.** Where it is silent, the fallback is **~100 km ROAD distance** from Wingfield — never straight-line.
**The install-range frame has two levels:** an outer boundary of approximately **1 to 1.5 hours' drive** from Wingfield, and internal flags at the **30 km / 60 km** bands (≤30 km standard · 30–60 km flag · >60 km assess). **The bands flag; they never decline.**
**Why:** the condition has been applied as blocking with no rule behind it, while Identity separately carried a ">60 km → decline" branch that `[R-SUPPLYONLY v1]` had already killed. Distance changes the delivery model, not whether SteedForm wants the work.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` (I6) · `07 Service Area & Site`
**History:** **v1 3 Sep 2026 (Stella Rasheed)** — closes OR-29 and registers one of the seven layer-1 conditions named in `[R-BLOCK v3]`.

---

## 5. Reading and writing the boards

*How a screen obtains and records a fact without losing it.*

### R-REF · v2 · LAW
**Reference data comes from the BOARD, on every screen — never from memory, an earlier pass, a historical note, a pasted snapshot, or a value copied onto the lead.** Applies to customers/accounts (current Accounts `5029570132`, reached through the Lead's `board_relation_mm64fq68`), materials (5029570546), appliances and sinks (5029694677), and serviceable areas (5029634649). For account-based decisions, read Customer Tier, the current rating fields **and Notes / Flags `long_text_mm64njy4`** `[R-ACCT v3]`, and ignore Account Status lifecycle as a disposition. **Cite the board item id** so the read is auditable.
⛔ **"From the board" means the RECORD, not a column list.** A rule naming columns states the minimum, never the maximum — the board evolves faster than this Register does, and evidence added there is in scope from the day it exists. **If a field on the record would change a human's decision and no rule names it, that is a gap in the rule, not permission to ignore the field.**
⚠ **Mirror columns are API-blind** — every `lookup_*` returns "Column value type is not supported". They are for human eyes only; agents must follow the `board_relation` and read the linked item directly.
**Why:** account fields change and copied narratives persist. Weyland Lead `2829292974` was falsely blocked by stale lifecycle text even though linked Account `2827365291` is currently Customer Tier B.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `04 Customer & Account` · `05 Material & Capability` · `07 Service Area & Site` · `08 Board Registry & Mechanics`

**History:** **v1 25 Jul 2026** (MD directive: "Always refer to boards") · **v2 24 Aug 2026 (MD)** — "refer to the board" was being satisfied by reading the columns a rule named while ignoring the rest of the record. Adds Notes/Flags to the account read and states that a named column list is a minimum, not a closed set, because customer screening will keep evolving on the board.

### R-READ · v1 · LAW
**Three monday read traps that return a plausible-but-wrong answer. All three produce "nothing found" when something IS there.**
1. **`board_relation` columns can read NULL for ordinary `text` and `value` even when correctly linked.** On current Leads, use `board_relation_mm64fq68` and obtain its linked item IDs/items with the connector's relation-aware read or typed GraphQL fragment. **Reading it as an ordinary text value makes every linked account look unlinked** and silently disables every account-keyed rule.
2. **PAGINATE EVERY BOARD SCAN.** The default page is 25 items. Contacts holds 226, Leads 111, Materials 380. An unpaginated "scan the board" check silently inspects the first 25 and reports clean.
3. **Status-label filters can return zero matches even when matching items exist** — prove a filter works on a known-positive before believing an empty result.
**The shared failure shape:** all three return an empty or null answer that reads as "nothing to do". Never treat an empty result as proof of absence until the read itself is proven.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `08 Board Registry & Mechanics`

**History:** **v1 27 Jul 2026** (board_relation trap rediscovered by the half-hourly sweep in production; pagination gap found in the hygiene checks written the same day)

### R-WRITE · v2 · LAW
**A monday write returning success does NOT mean the value persisted. Verify by re-reading.** Known traps:
- **(a) Text containing `<`** — sanitised to an EMPTY STRING, write returns success `[R-INTAKE-ID v3]`.
- **(b) `long_text` over ~2000 chars** — silently truncated, and the read-back shows the truncated value so it looks fine `[R-LONGTEXT v2]`.
- **(c) `board_relation`** — reads null for `text` AND `value` even when correctly linked; only `linked_item_ids` shows it `[R-READ v1]`.
- **(d) `email` and `phone` columns REJECT `change_simple_column_value`.** It sends `text: null` and monday raises `ColumnValueException` — *"invalid value… column_value: {email => "x", text => nil}"*. **Use `change_multiple_column_values` with BOTH fields: `{"email":{"email":"x@y.com","text":"x@y.com"}}`.** *(Hit 27 Jul 2026 backfilling 8 account emails — the whole mutation failed on all 8 at once.)*
- **(e) `status` labels cannot be created by `change_column_metadata`** — use `create_labels_if_missing: true` on a value write. Labels can be **created** this way but never **deleted or renamed** by API.

**The shared shape: monday fails LOUDLY on malformed structure and SILENTLY on content it dislikes.** A rejected mutation is the good case — you find out immediately. The dangerous cases are (a), (b) and (c), which all report success.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `08 Board Registry & Mechanics`

**History:** v1 27 Jul 2026 (generalised from R-INTAKE-ID v2) · **v2 27 Jul 2026** (email/phone structure + label-creation route added after both were hit in practice)

### R-LONGTEXT · v2 · LAW
**monday `long_text` silently truncates at ~2000 characters and the read-back hides it — the write returns SUCCESS, the value simply ends mid-word, and the truncated value is what you read back.** So it looks correct. This is live and already costing data.

**Which end you lose depends on how you write, and BOTH ends matter:**
- **PREPEND** (Duty 3.5 → Screening Flags) drops the **TAIL** — which is where the **ORIGINAL blocking flags and the decline reasoning live.** The newest account note survives; *why the lead was blocked* is what gets cut. That is exactly backwards.
- **APPEND** (Quote Notes) drops the **NEWEST** content — the thing just learned.

**THE RULE: a long_text column holds CURRENT STATE, never an unbounded log.**
1. **BUDGET BEFORE YOU WRITE.** If the composed value would exceed **1,800 characters**, do not write it whole — write a trimmed version ending `… full detail in updates` and post the remainder as an **item update** (updates have no cap).
2. **Compact, don't drop:** keep every ACTIVE flag and the verdict reasoning; move superseded or historical entries into an item update, leaving a one-line pointer in the column.
3. ⛔ **NEVER PREPEND to current Leads `Screening Flags / Decline Reason` (`long_text_mm64zg50`).** Append, and if you must cut, trim from the MIDDLE with an explicit `[…earlier detail in updates]` marker — never off either end silently.
4. **Verify by re-reading and comparing `len()` against the cap** `[R-WRITE v2]`. **Checking only the final line is not a truncation check**: a truncated append loses the END (final line looks wrong), a truncated prepend loses the BEGINNING (final line looks right). Length is the only test that catches both. **A value of exactly 2000 characters is a truncation signature, not a coincidence** — treat it as data loss and digest it.

**Live at registration (27 Jul 2026) — THREE leads had already lost content:**
- `Screening Flags` — **Classique — Freeman (2806574058)** at exactly 2000, cut mid-word at *"…because the sheet says pull ou"*. **The lost text was the qualification that it is NOT a replacement-on-existing decline** — on a job installing 31 Aug. A verdict-changing sentence, gone.
- `Quote Notes from Drawing` — **Vellotti — Henley Beach (2765462063)** and **The Joinery Shop — Tyley #1744 (2796063849)**, both at exactly 2000. *(This column was initially left out of the cap-watch and is the worst affected — three more sit above 1940.)*
- Near the cap: Rowe — Aberfoyle Park 1995 · Farquhar — Thomas 1968 · St Georges 1930 (Risk Profile 1943) · Juncken 1769 · Sterling Homes 1758.

**The two newest leads are among the longest — strips grow every run, so this worsens with time, not improves.** Watch all THREE long_text columns in three bands: **AT CAP (=2000, already lost)** · **CRITICAL (≥1900)** · **WATCH (≥1750)**. At 1900+, compact in that run: snapshot the full text to an item update first, then rewrite the column as active flags + verdict reasoning with a pointer.
**Carried by:** the `estimator-screening` skill and Claude deep scans (EXECUTABLE) · `03 Risk Scoring` · `08 Board Registry & Mechanics`

**History:** **v1 27 Jul 2026** (found live: 1 lead truncated mid-word, 4 more within 100 chars) · **v2 28 Jul 2026** — merged two divergent v1 blocks that both sat in this Register; no behaviour conflict between them, v2 is the union (1,800-char budget + the Screening-Flags prepend ban + the three watch bands + the exactly-2000 signature).

---

## 6. Superseded

*A superseded rule keeps its ID for ever. It is never deleted and never renumbered.*

### R-ACCTVALUE · v1 · SUPERSEDED
**Superseded by the 11 August 2026 CRM migration, recorded 24 August 2026.** The live Accounts board has no `Account Value` column, so there is nothing left to misread. **Its consequence is carried by `[R-ACCT v3]`**, which makes Notes/Flags mandatory reading because ten-year revenue and win rate now live only there. *(The source Register left this entry headed `LAW` among the live rules while its own body declared it superseded, and its `## Superseded` section read "None yet". It has been moved here under the Register's own IDs-are-permanent protocol; no ruling was required, the entry states its own disposition.)*
**`Account Value` (the `mirror` column on Accounts) is BROKEN and reads $0 on all 144 accounts. Never report from it.** Three independent faults: it mirrors `deal_actual_value` (a dead, undeletable monday template formula); that formula only fires at Stage **"Won"**, which by ratified design **never occurs** (Order Confirmed IS the win); and it sums through `account_deal`, which is empty on every account because the Deals↔Accounts link exists only on the Deals side. **Account revenue comes from Xero, not this board**, until the relation architecture is decided.
⚠ **SUPERSEDED BY MIGRATION, 24 Aug 2026.** Live Accounts `5029570132` has **no `Account Value` column** — the 11 Aug cutover did not carry it across, so there is nothing left to misread. **The consequence that matters: with no value column, ten-year revenue and win rate exist ONLY in Notes/Flags `long_text_mm64njy4`**, which is precisely why `[R-ACCT v3]` now makes that column mandatory reading. ⚠ This rule's stated carrier was *"the column's own description on the board"* — the migration dropped every column description, so this rule had **no surviving carrier at all** until this note.
**Carried by:** this entry only — retained as the record of a removed column.

**History:** **v1 27 Jul 2026** · **note 24 Aug 2026** — column absent post-migration; entry is now historical.

---

## 7. Complete rule ID index

*All 51 registered IDs. IDs are permanent and must never be reissued, including those outside screening scope.*

### In screening scope — stated in full above

| ID | Version | Section |
|---|---|---|
| `R-CLIENTFIT` | v1 | §1 Client and account |
| `R-ACCTMATCH` | v5 | §1 Client and account |
| `R-C1` | v4 | §1 Client and account |
| `R-ACCT` | v3 | §1 Client and account |
| `R-CRMSOT` | v2 | §1 Client and account |
| `R-C3` | v1 | §1 Client and account |
| `R-RETAIL` | v1 | §1 Client and account |
| `R-ENTITY` | v1 | §1 Client and account |
| `R-INTERSTATE` | v1 | §1 Client and account |
| `R-LEADTIME` | v2 | §1 Client and account |
| `R-M1` | v2 | §2 Material and capability |
| `R-SUBTYPE` | v2 | §2 Material and capability |
| `R-PROFILE` | v3 | §2 Material and capability |
| `R-30MM` | v1 | §2 Material and capability |
| `R-D5` | v6 | §2 Material and capability |
| `R-MA2` | v1 | §2 Material and capability |
| `R-SCOPE` | v2 | §2 Material and capability |
| `R-FLUSH` | v1 | §2 Material and capability |
| `R-MATERIAL-TERMS` | v1 | §2 Material and capability |
| `R-DEKTON` | v1 | §2 Material and capability |
| `R-NATURAL` | v1 | §2 Material and capability |
| `R-ALFRESCO` | v1 | §2 Material and capability |
| `R-EVIDENCE-BAR` | v2 | §3 Evidence and verdicts |
| `R-DRAWINGS` | v1 | §3 Evidence and verdicts |
| `R-BLOCK` | v3 | §3 Evidence and verdicts |
| `R-ANDON` | v2 | §3 Evidence and verdicts |
| `R-MA5` | v3 | §3 Evidence and verdicts |
| `R-RESCREEN` | v1 | §3 Evidence and verdicts |
| `R-SITE` | v1 | §4 Site, service area and logistics |
| `R-SUPPLYONLY` | v2 | §4 Site, service area and logistics |
| `R-OCCUPANCY` | v1 | §4 Site, service area and logistics |
| `R-AREA` | v1 | §4 Site, service area and logistics |
| `R-REF` | v2 | §5 Reading and writing the boards |
| `R-READ` | v1 | §5 Reading and writing the boards |
| `R-WRITE` | v2 | §5 Reading and writing the boards |
| `R-LONGTEXT` | v2 | §5 Reading and writing the boards |

*(`R-ACCTVALUE v1` is registered and SUPERSEDED — its entry is in §6, not above.)*

### Outside screening scope — registered, not applied by the screen

*These govern email intake, CRM pipeline operations and build governance. They are real, live rules; they are simply not applied when screening a quote or job. Their full text is in the archived original Rule Register.*

| ID | Version | What it governs |
|---|---|---|
| `R-INTAKE-ID` | v3 | The intake idempotency key is the email's `internetMessageId`, stored BARE in `text_mm64cjv2` on current Leads board `5029570131` — angle brackets STRIPPED |
| `R-INTAKE-ATTACH` | v1 | Every genuine email-origin Lead must reconcile the exact source message's substantive attachments into the Leads Files column using the verified bare Internet Message-ID as the only join key |
| `R-INTAKE-CONTACT` | v3 | The duplicate key is EMAIL *plus* ACCOUNT — never email alone |
| `R-QUOTESENT` | v2 | Deals `date_mm64e491` Quote Sent is the anchor for follow-up cadence and the 30-day quote-validity clock, and that clock starts only after the Quote Gate passes while Stage is `Quoted - Send to Client` |
| `R-INTAKE-ORDER` | v1 | Process the intake batch in ASCENDING received-time order, oldest first |
| `R-PERMANENT-FIX` | v1 | A fix is not complete when the visible symptom disappears. It is complete only when the source of recurrence is controlled, existing drift is reconciled, and the result is independently verifiable |
| `R-REP-HANDOFF` | v1 | Lead ownership is review accountability; Deal Rep is a separate quoting claim |
| `R-ORDER-TXN` | v1 | One Deal, one immutable key, one Order |
| `R-EMAIL-ASSOC` | v1 | Contacts and Accounts are the master relationship history. Lead/Deal email timelines are job-specific evidence, not a sender-wide mailbox mirror |
| `R-LEADLINK` | v2 | Every new Deal must receive both current `Originating Lead` (`board_relation_mm64xgbc`) and exact `Source Lead ID` (`text_mm656wzh`) at conversion, and the two must resolve to the same current Lead |
| `R-QUOTEMAIL` | v2 | A scheduled check cannot gate an event-driven client send. Quote evidence must be structurally complete before sending |
| `R-SIGNAL` | v1 | A stated rule that nothing verifies is not a rule |
| `R-NINETY` | v1 | Never create, update, or delete anything in Ninety.io / Success.co — the EOS system: Rocks, Scorecard measurables, Issues, To-dos, V/TO — without Matthew's explicit, in-the-moment permission |
| `R-GATE` | v1 | No phase advances on intent, design confidence, or a green-looking implementation. It advances only when the defined evidence for that phase has been produced and independently checked |

---

*Related: `00-README-and-authority.md` (how to use this set) · `10-open-rulings.md` (questions this Register does NOT settle).*
