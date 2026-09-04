# 04 — Customer & Account

**Status:** Active. Subordinate to `01-rule-register.md`: where this document and the Rule Register disagree, the Register is correct and this file is stale. Settled material only — unresolved questions are quarantined in `10-open-rulings.md` and must not be acted on as rules.
**Owner:** Matthew Rasheed (MD)
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns** — deciding whether the *customer* is right for SteedForm: account matching and linking, client-fit precedence, the account read, the commercial-disposition label, the A/B/C behaviour rating, minimum job size, and the disambiguation of the four separate axes that share the word "tier".
- **Does not own** — verdict definitions and routing (Qualified / Needs Info / Needs Review / Unqualified), drawings, material class, scope, technical suitability, site and access, pricing mechanics beyond naming the markup tiers, or the canonical statement of any rule. Rules are authored only in `01-rule-register.md`; this document cites them and carries the operative one-liner.

---

## What this document decides

Whether we quote this customer at all, and on what evidence. It fixes the corpus's single worst ambiguity — four unrelated things called "tier" — by naming each axis, its field, and its job. It sets the closed ladder by which a Lead is linked to an Account `[R-ACCTMATCH v5]`, establishes that client fit is decided *before* drawings, scope, material or value `[R-CLIENTFIT v1]`, and defines the minimum account read `[R-ACCT v3]` — including the mandatory Notes/Flags column, where DUMP markers, ten-year revenue and win rate now exclusively live. It carries the A/B/C behaviour rubric and the one-slab minimum `[R-C3 v1]`, states the client-type decline ground `[R-RETAIL v1]`, and carries the unknown-entity block `[R-ENTITY v1]`.

---

## 1. The four axes that share the word "tier"

This is the most load-bearing section in the document. The corpus uses "tier" for four unrelated things. Conflating any two of them produces a wrong verdict, and has already done so in production.

> ⚠ **The document that was supposed to reconcile these — `Tier & Rating Model — Reconciliation (DRAFT).md`, cited from the `Sales Qualification.md` banner — does not exist anywhere in the corpus and never did. This section replaces it.**

| # | Axis | Where it lives | What it measures | Values | Role in screening |
|---|---|---|---|---|---|
| **a** | **Customer Tier** | Accounts `5029570132`, `color_mm64t0aj` | Commercial **VALUE / disposition** — how much we want their work | `A - Anchor/VIP` · `A - Win Back` · `Gate - Selective` · `Do-Not-Quote` | The **disposition LABEL** `[R-C1 v4]`. `Do-Not-Quote` → Needs Review. A-tiers waive the one-slab minimum `[R-C3 v1]`. Gate-Selective → flag + Needs Review. |
| **b** | **Client Rating A/B/C** | Accounts `5029570132`, `color_mm64jqn0` (+ sub-ratings) | **BEHAVIOUR** — how smoothly they run operationally | A · B · C · blank | **Prices friction; never blocks.** Feeds the CLIENT risk lane. See §5. |
| **c** | **Pricing-markup tier** | `Pricing Rules.md` — Markup Decision Framework | The **starting markup factor** by customer type | Commercial x1.25–1.35 · Standard Residential x1.35 · Builder/Trade x1.40 · Direct Homeowner x1.55+ | A pricing lever, not a screening gate. Never a verdict input. **`Direct Homeowner x1.55+` survives `[R-RETAIL v1]`** — see §7.1. ⚠ The category list itself is an **outstanding MD action**, §1.4. |
| **d** | **Account Status** | Accounts `5029570132`, `color_mm64cbq0` | **LIFECYCLE** history | Active · Win-Back · Prospect · On Hold · Dormant · Do-Not-Quote | ⛔ **STALE. Must never block, qualify, score or describe a Lead** `[R-C1 v4]` `[R-ACCT v3]`. May be displayed as context only. |

⛔ **These four must never be conflated, merged into one field, or read as each other.** Tier says what they are *worth*; the rating says how smoothly they *run*; the markup tier says what we *charge*; Account Status says nothing screening may use.

**Why this matters, with evidence:**
- **(a) vs (d):** Weyland Cabinet Makers (`2827365291`) reads Customer Tier **B** / group B while stale Account Status still says Do-Not-Quote. Treating lifecycle as disposition produced a **false commercial block** on Lead `2829292974` `[R-C1 v4]` `[R-REF v2]`.
- **(a) vs (b):** stated directly in `Lead Risk Assessment Standard.md` §3.1 — *"Customer Tier = how much we VALUE them (commercial worth); A/B/C rating = how SMOOTHLY they RUN (operational behaviour). Never conflate them in one field."*
- **(a) vs (c):** `Sales Qualification.md`'s own banner conflates them, claiming "live tiers now on the monday Accounts board". Its tiers are **pricing-markup** tiers; the board carries **Customer Tier**. Different axes.

### 1.1 Customer Tier label set — resolved

`Decisions Log.md` 2026-07-26 records a re-lens ruling that Customer Tier would become *"value (Anchor/Standard/Gate-Selective, **with Win-Back and DNQ stripped OUT**)"*. That design is **not what the live board carries**: `[R-C1 v4]` (24 Aug 2026) reads `Do-Not-Quote` directly off `color_mm64t0aj`, and the four labels above are the current set. **The Register governs** — it is authoritative over every other file, and `Decisions Log.md` is a HISTORY–FROZEN carrier ("*evidence, not instructions*"). Treat the 26 Jul label design as a historical intent that was not implemented.

### 1.2 The pricing-markup tiers are NOT superseded — the method of identifying them is

The four markup tiers in `Sales Qualification.md` match `Pricing Rules.md` §The Markup Decision Framework **exactly** and remain current. What is dead is the identification method:

| `Sales Qualification.md` (pre-Big-Reset / Anthill-era, self-declared stale) | Current position |
|---|---|
| *"The tier is identified at triage — it's **known from the source of the enquiry**, not from a formal scoring process."* | ⛔ **Killed.** Reference data comes from the **BOARD, on every screen — never from memory, an earlier pass, a historical note, a pasted snapshot, or a value copied onto the lead** `[R-REF v2]`. The account is reached only through the closed ladder `[R-ACCTMATCH v5]`; **an exact name match may never by itself apply Customer Tier, Gate-Selective, A-tier waivers, markup or SLA.** |
| Verdicts **PROCEED / REQUEST INFO / DECLINE** | **Qualified / Needs Info / Needs Review / Unqualified** — the Leads board vocabulary, with `[R-CLIENTFIT v1]` precedence. |
| *"Minimum job size … parked until Production Intelligence matures."* | `[R-C3 v1]` — one slab per job. See §6. |

⚠ **`Direct Homeowner x1.55+` is not repealed by the client-type decline.** `[R-RETAIL v1]` decides *whether there is a job*; the markup tier decides *what it is priced at* once a trade account is behind it. See §7.1.

**Floor and approval (from `Pricing Rules.md`, carried here only as context for axis (c)):** x1.25 (20% GP) is the absolute minimum; no job leaves the building below it. Pricing below x1.35 requires Matthew or Sarah (GM). *(The overlap between "below x1.35" and the Commercial band's x1.25–1.35 top is a pricing-document question, not a customer-screening one.)*

### 1.3 A fifth field to be aware of — the account Markup number

Accounts `5029570132` also carries `numeric_mm64mvp3` **Markup**, listed among the live customer decision fields in `SKILL.md`. It is a per-account pricing value, not a tier label and not a screening gate. It is in scope for the account read under `[R-REF v2]`'s record-not-column-list principle, but it never drives a verdict.

### 1.4 The markup-category list — an outstanding MD action

⚠ **The markup-category list is STILL TO BE SET. That is an outstanding action on the MD, not a gap in this document** (OR-30, 3 September 2026).

**What this means in practice:**

- The four tiers above are what `Pricing Rules.md` documents as operational, and they are what axis (c) names today. **Use them.**
- **Do not treat the absence of a settled category list as a defect to be worked around**, and do not invent, extend or reconcile categories to fill it. This document is not missing a section; the decision is with the MD.
- How the categories map onto the per-account `numeric_mm64mvp3` **Markup** field (§1.3) is part of the same outstanding action and is likewise not for a screen to resolve.
- **Nothing in screening turns on the answer** — markup is a pricing lever and never a verdict input. Where a match is unconfirmed, no markup is applied at all `[R-ENTITY v1]`.

---

## 2. The account-matching ladder `[R-ACCTMATCH v5]`

**Operative one-liner:** one closed ladder, applied in order, stop at the first tier that resolves; **the automatic ladder ends at tier 3**. The link is what every account-keyed rule depends on — Customer Tier, Gate-Selective, A-tier waivers, markup, SLA — so a missed match silently disables all of them and a wrong match applies them to the wrong entity.

| # | Test | Action |
|---|---|---|
| **1** | Exact **Contact** email resolving to **one distinct linked Account** | **AUTO-LINK** — collapse duplicate Contact rows by email + linked Account; record multiplicity is not multiple votes |
| **2** | Exact **Accounts main-POC email** — `email_mm64cpfk` on Accounts `5029570132`, full-string, case-insensitive | **AUTO-LINK** |
| **3** | **Unique, non-generic Account domain** resolving to exactly one Account | **AUTO-LINK** + set Existing trade client = Yes |
| **4** | Exact normalised **company name**, from an explicitly extracted company name only | ⚠ **CANDIDATE ONLY — never auto-link.** Surface for human confirmation |
| **5** | Anything else | **Leave unlinked**, flag for human resolution |

⛔ **TIER 4 IS A LOCATOR, NOT AN AUTHORITY.** An exact name match may help a human *find* the account. It may **never** by itself apply Customer Tier, Gate-Selective, A-tier waivers, markup or SLA.

⛔ **Never match on** contact name · a partial or fuzzy company string · a generic domain.

⛔ **Full-address equality and domain equality are DIFFERENT TESTS — never merge them.** Count the domain's matches **before** linking; more than one → human.

### 2.1 The generic-domain prohibition (closed list of ELEVEN)

**gmail · hotmail · outlook · bigpond · internode · optusnet · yahoo · live · icloud · people.net.au · adam.com.au**

⚠ **The list is ELEVEN, and it is closed** `[R-ACCTMATCH v5]`. `people.net.au` and `adam.com.au` were ruled generic on 3 September 2026. Do not treat `adam.com.au` as a non-generic collision — that reading is retired — and do not carry a short list of nine.

On a generic domain, tiers 2–3 **do not apply**; the sender drops to **tier 4 — candidate only, human confirmation required**. It is not an automatic name match. At least 8 accounts use a generic domain as their main address (Styleline, All Class, DeBoar, K H Kitchens, Saunders, Oskar Brezovic, Dylan Boehm, Zee), so matching on `gmail.com` would link every retail enquiry to whichever account happens to share it.

⚠ **A generic address can still be recognised for client fit by an exact full-email Contact/Account match** `[R-CLIENTFIT v1]`. The shared domain alone is never recognition.

### 2.2 Shared-domain ambiguity

⛔ **A domain shared by two or more Accounts is AMBIGUOUS — do not link, flag it.**

| Collision | Accounts |
|---|---|
| `farquhar.co` | Farquhar Kitchen Centre — `accounts@farquhar.co`, item `2766405173` **and** KT3 Farquhar - Hickinbotham — `commercial@farquhar.co`, item `2766521671` |

**Why it matters:** guessing between two accounts of the same customer group silently attributes the job — and the tier — to the wrong entity, pointing a commercial job at the retail account or vice versa.

### 2.3 Known data conditions (reference, dated)

| Condition | Measured | Consequence |
|---|---|---|
| **42 Accounts have a blank main-POC email** | 10 Aug 2026 | Tier 2 cannot fire for them. This is a data-quality backlog — **never** grounds to fall through to an automatic name match. |
| Tier yields against live data — 387 unique Contact emails / 153 Accounts: tier 1 = **334** · tier 2 (after tier 1) = **0** · tier 3 = **5** · ambiguous non-generic domain = 2 · no automatic result = 48 | 10 Aug 2026 | Tier 1 carries nearly all safe matches; exact name is not needed as an automatic tier. This is the evidence for ending the automatic ladder at tier 3. |
| 45 of 111 leads unlinked, at least four byte-identical email matches (KDA Build, Batescraft, The Joinery Shop ×2) | 27 Jul 2026 | The failure that produced the closed ladder. A Gate-Selective job reached Qualified and converted because of it. |
| Tier 2 addressed a column that did not exist post-migration (`email` → `email_mm64cpfk`) for ~13 days | 24 Aug 2026 | Measured damage **nil** — the closed ladder's redundancy absorbed it, which is also why nothing surfaced the defect. |

⚠ **An executor without access to the Contacts board cannot run tier 1 and must not auto-link Accounts.** The Register records this for the Cynthia agent (`21307`), whose knowledge set covers Leads, Accounts, Materials and Serviceable Areas but not Contacts.

⚠ **Mirror / lookup columns are API-blind** — every `lookup_*` returns "Column value type is not supported". They are for human eyes. Follow the Lead's `board_relation_mm64fq68` and read the linked Account item directly `[R-REF v2]`.

---

## 3. Client fit precedence `[R-CLIENTFIT v1]`

**Operative one-liner:** client fit is decided **before drawings, scope, material, value or technical suitability**. Apply it immediately after the matching ladder and before every other commercial or technical rule.

**Precedence:** the gate runs after junk triage and safe account matching, but **before DRAWINGS and every technical/commercial disposition rule. It therefore outranks `Needs Info` for missing drawings and `Qualified` for clean drawings.**

**Recognised** means either (a) `[R-ACCTMATCH v5]` tier 1–3 safely linked one Account, or (b) a human has explicitly approved the new customer.

| `Client Fit` — Leads `color_mm69h52c` | Set by | Effect |
|---|---|---|
| **Recognised** | Automatic, on a safe tier 1–3 link | Continue to the normal drawing/technical screen |
| **Approved New** | Human only | Continue **without** requiring an Account link |
| **Review Required** | Automatic, when no Account is safely linked and fit is not Approved New | Lead Status = **Unqualified**; write `UNRECOGNISED SENDER — client-fit approval required before drawings are considered`; preserve and file the supplied evidence; stop before drawing or technical disposition |
| **Declined** | Human only | Always **Unqualified** |

⛔ **Drawing presence, readability, job size, material and technical merit must never upgrade an unresolved client-fit outcome.** A later scan, rescan or reconciliation cannot promote the Lead until Client Fit reads Recognised or Approved New. Re-runs must respect explicit human states and must never reset an approved new customer.

### 3.1 The unknown-entity check `[R-ENTITY v1]`

**Operative one-liner:** *"who is asking"* is a **BLOCKING** check → **Needs Review**. Where no account matches confidently, the enquiry is **not scored as if it came from a known customer**. It is one of the layer-1 blocking conditions `[R-BLOCK v3]`.

⚠ **This check runs AFTER `[R-CLIENTFIT v1]`, not instead of it.** Client fit decides whether SteedForm acts for this enquirer at all; this decides whether the account behind them is known well enough to score. Both apply, in that order.

⛔ **A near-miss is NEVER silently matched and NEVER silently dropped** `[R-ACCTMATCH v5]`. A tier-4 name candidate, an ambiguous shared domain, a generic-domain sender — each is a near-miss, and each takes the same treatment.

**Write the confirm flag VERBATIM. The string is fixed:**

> *"possible account match: X — unconfirmed"*

**Treat the account as UNTIERED until a human confirms.** An untiered account gets **no tier-dependent treatment whatever**:

| Treatment | On an unconfirmed match |
|---|---|
| A-tier waiver of the one-slab minimum `[R-C3 v1]` | ⛔ **Not applied** |
| Gate-Selective handling | ⛔ **Not applied** |
| Markup (axis (c), §1) | ⛔ **Not applied** |
| SLA | ⛔ **Not applied** |

**Why the flag is written both ways round:** a wrong tier match is worse than no match **in both directions** — matching up gives an unknown enquirer an anchor client's waivers and SLA; matching down applies a Do-Not-Quote or a friction price to somebody who has earned neither. Neither error is visible afterwards, because both produce a screen that looks decided.

⚠ **This condition was applied as blocking for months with no rule behind it, and its absence is precisely what let a near-miss be silently resolved either way.** It is now registered; there is no discretion left in it.

---

## 4. The account read `[R-ACCT v3]`

**Operative one-liner:** read the account **record**, not a curated subset of it. **monday.com is the single source of truth for CRM-class items** `[R-CRMSOT v2]` — follow the Lead's `board_relation_mm64fq68` to Accounts `5029570132` and read the linked item directly, on every screen `[R-REF v2]`. **Cite the board item ID so the read is auditable.** Historical notes in *files*, old portfolio lists, Lead narratives and copied snapshots are **not** authority `[R-CRMSOT v2]`; `long_text_mm64njy4` Notes / Flags on the account **record** is live board data and is **mandatory evidence** `[R-ACCT v3]` `[R-CRMSOT v2]`.

⛔ **The two rules no longer conflict — that was ruled on 3 September 2026 (OR-21).** `[R-CRMSOT v2]` now names Notes / Flags as mandatory reading and cross-tags `[R-ACCT v3]`. **"Historical notes are not authority" means copied narratives and retired shorthand; it has never meant the Notes / Flags column.** Never infer a clean disposition from a clean tier label — read Notes / Flags before reporting any disposition.

⛔ **The column list below is the MINIMUM, not a closed set.** As customer screening evolves on the board, new evidence appears there first and the rules follow. **If a field on the record would change a human's decision and no rule names it, that is a gap in the rule, not permission to ignore the field.** A screen that reports only the fields a rule happens to name will report the flattering field and omit the decisive one.

| # | What | Column | Read as |
|---|---|---|---|
| ① | **VALUE / commercial disposition** | `color_mm64t0aj` Customer Tier | The disposition **label** `[R-C1 v4]` |
| ② | **BEHAVIOUR** | `color_mm64jqn0` Client Rating A/B/C, with sub-ratings `color_mm64kd3q` Payment · `color_mm64je94` Measure-ready · `color_mm647dxb` Install-ready. ⛔ **Only Payment holds data — the other three are 0 of 188** (§5.2, OR-41) | Friction pricing, never a block |
| ③ | **NOTES / FLAGS — MANDATORY** | `long_text_mm64njy4` | Evidence, not colour. See below. |
| — | Excluded as a disposition | `color_mm64cbq0` Account Status | Stale lifecycle. Context only; never blocks, qualifies, scores or describes |

**Blank ratings mean not populated. They are not evidence of either good or bad performance.**

### 4.1 Notes / Flags is evidence, not colour

⛔ **`long_text_mm64njy4` carries `DUMP STOP` / `DUMP LOCKED` markers, ten-year revenue, win rate and recorded MD analysis. A DUMP marker — or any note contradicting the tier label — is a BLOCKING flag → Needs Review, and must be quoted VERBATIM in the screening output.** Never summarise it away, and never let a tier label outrank it.

⛔ **A DUMP marker blocks exactly as `Do-Not-Quote` does** `[R-C1 v4]` — Needs Review, quoted verbatim, cite the Account item ID — **even when the tier label reads `A - Anchor/VIP` and the Payment rating is clean.** The tier label may never be reported as the disposition while an unresolved DUMP marker or a contradicting group sits on the same record. **Fail toward the flag.**

⛔ **Never auto-Unqualify on a tier match or a DUMP marker.** `Do-Not-Quote` and DUMP both route to **Needs Review** with the exact Account item ID and current field value — a human confirms before any customer is turned away.

**14 accounts carried DUMP markers as at 24 August 2026.**

### 4.2 When the label, the group and the note disagree, THAT IS THE FINDING

Surface all three and route to a human. Do not silently prefer one, and do not treat it as a precedence puzzle.

**Worked example — Inavogue `2827354824`, verified 24 August 2026:**

| Field | Value |
|---|---|
| Customer Tier `color_mm64t0aj` | `A - Anchor/VIP` |
| Payment `color_mm64kd3q` | `B` |
| Account Status `color_mm64cbq0` | `Active` |
| Board group | 🅱 B |
| Notes / Flags `long_text_mm64njy4` | **`DUMP STOP · 19k 10yr · 7% win · Active`** |

Screened under the previous rule this reported *"Active · A - Anchor/VIP · Payment B"* — **every word true, the commercial reality inverted.** A DUMP STOP account at a 7% win rate screened as an anchor client. This single failure is the reason `[R-ACCT v3]` makes Notes/Flags mandatory and `[R-C1 v4]` separates the disposition **label** from the commercial **evidence**.

### 4.3 Where ten-year revenue and win rate live now

⛔ **There is no Account Value column.** `R-ACCTVALUE v1` described a broken mirror column reading $0 on all accounts; the **11 August 2026 CRM migration did not carry that column across**, and the rule is marked superseded by migration (24 Aug 2026). **The consequence that matters for screening: ten-year revenue and win rate exist ONLY in Notes/Flags `long_text_mm64njy4`** — which is precisely why `[R-ACCT v3]` makes that column mandatory reading. Account revenue otherwise comes from Xero, not this board.

⚠ **All Accounts column IDs changed in the 11 August 2026 migration.** Legacy IDs belong to the retired board `5029570423` and must never be addressed `[R-REF v2]`. The migration also dropped every column description, so any rule whose only carrier was a column description lost it.

---

## 5. The A/B/C rating rubric

*The rubric is reference material owned by this document; it is not a Register rule and carries no rule ID. `[R-ACCT v3]` governs how the resulting fields are read.*

### 5.1 The model — rate by irrecoverable cost of failure

The rating answers one question: **"does this account cost us irrecoverable capacity or cash?"**

| Stream | Class | Why | Effect on the rating |
|---|---|---|---|
| **Site-readiness** | **CRITICAL** | A "ready" site we can't finish, or must walk away from, is a **lost slot we can't reclaim** — pure muda: wasted trip, wasted capacity, bumps the next job | **Worst-of cap** |
| **Payment** | **CRITICAL** | Bad debt / cash tied up. Irrecoverable | **Worst-of cap** |

⛔ **There are TWO streams and no third.** The Paperwork stream is **ABOLISHED** — see §5.4. It is not a capper, not a flag, and not a judgement input to the rating.

**Overall rating = worst of {Payment, Site-readiness}. Nothing downgrades it after that.**
*Example: A-payment + A-site-readiness = **A**, whatever the account's paperwork is like. A-payment + C-site-readiness = **C**.*

**Site-readiness is itself a composite: the worst of {Measure-ready, Install-ready}** — see §5.2. On a **supply-only** job it is **N/A** and drops out, leaving Payment alone as the rating.

⛔ **NOT in the quality rating: value / volume — how much they spend.** That is the markup layer (axis (c) in §1), kept deliberately separate so "good to work with" and "worth a lot" do not corrupt each other.

⛔ **An unfilled sub-rating is a gap to fill, not a factor to skip.** A live board column description once read "worst of the FILLED sub-ratings", which is wrong against the ratified composite (Decisions Log 2026-07-25). Blank means not populated — not evidence either way `[R-ACCT v3]`.

**The composite `color_mm64jqn0` is MD- or GM-overridable and human-set.** Ratings are earned and decayed by jobs, not vibes.

### 5.2 Stream 1 — Site-readiness *(CRITICAL, confirmed MD 22 Jul 2026)*

| Band | Criteria |
|---|---|
| **A** | Site ready as confirmed essentially every time; measure/install completes first visit; rare, well-flagged exceptions. |
| **B** | Occasional not-ready or partial; usually recoverable on the day or with a short wait; no pattern. |
| **C** | Repeatedly says "ready" when not; has caused a walk-away or a return trip / lost slot. → the **drop-them signal**; site-readiness failures feed this rating, and the rating **is** the enforcement mechanism. |

**How the two board columns collapse into this stream — ruled 3 September 2026 (OR-14):**

**Site-readiness = the WORST of {`color_mm64je94` Measure-ready, `color_mm647dxb` Install-ready}.** Read both columns, take the worse grade, and report both alongside the collapsed value so the reader can see which column drove it. That makes the overall composite arithmetically *worst of {Payment, Measure-ready, Install-ready}* — the two statements are the same statement.

⛔⛔ **BOTH COLUMNS ARE EMPTY. VERIFIED 3 SEPTEMBER 2026 — `color_mm64je94` Measure-ready is 0 of 188, `color_mm647dxb` Install-ready is 0 of 188, and `color_mm64jqn0` Client Rating is 0 of 188 too.** The ruling above is sound and **it currently scores on nothing.** Only `color_mm64kd3q` Payment carries data (109 of 188), which means **the A/B/C rating is payment-only in practice** — A-VIP 15 · A 16 · B 53 · C 25.

**That is not a criticism of the rubric.** The A/B/C standard says plainly it was *"built criteria-first because the data doesn't exist yet."* But the audit it was written to enable has not happened, and **a screen cannot score site-readiness on nothing.** ⛔ **An empty read is not an A** `[R-READ v1]` — until this is settled, report site-readiness as **not scored** and say the composite is running on Payment alone. Do not let a blank column quietly become a good grade. Raised as **OR-41** in `10-open-rulings.md`; coverage figures in `08-board-and-column-registry.md` §7.2.

⛔ **On a SUPPLY-ONLY job, site-readiness is N/A — SteedForm does not measure** `[R-SUPPLYONLY v2]`. **Neither column applies**: there is no SteedForm measure and no SteedForm install, so there is no site-readiness behaviour to grade. **The stream drops out of the composite entirely** and the overall rating is the Payment grade alone. Do **not** read a blank or stale Measure-ready / Install-ready value as a C, and do **not** substitute the client's own measure performance for it — dimensional responsibility sits with the client on those jobs, and that is recorded as a liability fact, not as a rating.

**Blank is not N/A.** A blank column on an ordinary job means *not populated* and is not evidence either way `[R-ACCT v3]`; N/A applies only where the delivery model removes the dimension.

### 5.3 Stream 2 — Payment *(CRITICAL, confirmed MD 22 Jul 2026)*

Measured as **days paid past terms**, on `color_mm64kd3q`, banded by **annual volume × days** — the scale set by the MD on **1 August 2026** and ratified 3 September 2026 (OR-12).

**The band scale — the only live scale:**

| Annual volume | A-VIP | A | B | C |
|---|---|---|---|---|
| **100k+** | 0 days over terms, or early | 1–7 days | 8–14 days | 15+ days |
| **Under 100k** | — | — | 0–7 days | 8+ days |

⛔ **An under-100k account is CAPPED AT B. There is no A band for it, and no A-VIP band.** An under-100k account paying strictly within terms is a **B**. That is the scale working as intended, not a data error to correct.

⛔ **The 22 July 2026 bands are RETIRED as a live position** — *"A = within terms · B = 1–7d · C = 8–14d"*, with no volume axis. The 1 August scale **replaces them outright**; it did not merely re-seed the data behind them. Do not apply the old bands, do not quote them as an alternative reading, and do not reconcile a board grade against them.

**⛔ The over-14-days CREDIT HOLD SURVIVES — as an overlay on top of the scale, not as a band within it.** More than 14 days past terms puts the account on **CREDIT HOLD: no new work is released, and prepayment is required until it is cleared.** On the 100k+ row 15+ days is *also* graded C; on the under-100k row 15+ days is *also* graded C. **The grade and the hold are different things and both apply** — a C grade prices friction, the hold stops work. Never let "15+ is merely C" read as the hold having lapsed.

What else is settled about Payment:

- ⛔ **The grade is the authority, not the formula.** Individual accounts have been moved by MD judgement. **Do not recompute a grade from any formula and treat the result as correcting the board.**
- ⚠ **The caveat that must travel with the number:** Collection Days measures **only invoices that were paid**. It is **blind to unpaid balances** — correlation with percent outstanding is **−0.10** — so a prompt payer can still be holding a large receivable. **Check outstanding separately; a clean Payment grade is not a clean exposure position.**
- ⛔ **The rating is not the whole account read** `[R-ACCT v3]`. A clean Payment grade never outranks a DUMP marker. *Tier says what they are worth and the rating says how smoothly they run; the note can still say do not quote them.*
- **Provenance (historical, not addressable):** grades originated from a 20 Jul 2026 seed off the legacy board's Pay Grade column (58 of 144 accounts seeded — 35 A · 19 B · 4 C), then were re-derived 1 Aug 2026 from `CustomerInsights_Aug-01-2026` Collection Days plus Xero 3-year average income (FY24–FY26). **Pay Grade does not exist on the live board — the migration dropped it.**

### 5.4 Paperwork — ABOLISHED *(ruled 3 September 2026, OR-13)*

⛔ **The Paperwork stream is ABOLISHED. It is NOT retained as a judgement flag.**

**Removed from the rating model entirely.** The composite is **worst of {Payment, Site-readiness}** with **no downgrade flag** of any kind sitting on top of it. There is no third stream, no "chase-his-docs" capper, no one-notch nudge, and no band table.

- ⛔ **Do not compute, record or report a Paperwork grade** — not on the account, not on the lead, not as narrative.
- ⛔ **`Rating — Paperwork` and `Rating — Communication` were deleted from the board on 26 July 2026 and must never be re-created.** The live sub-ratings are three and only three: Payment · Measure-ready · Install-ready `[R-ACCT v3]`.
- ⛔ **Nothing downgrades the composite after the worst-of is taken.** A rubric that says otherwise is stale wherever it appears — the 22 July 2026 "SECONDARY / flag, downgrade-only, at most one notch" wording included.

**Chasing a customer for missing information remains an ordinary operational fact**, and where it bears on an enquiry it belongs in the screening narrative or in Notes / Flags on the account `[R-ACCT v3]` — as evidence a human reads, never as an input to the A/B/C rating.

### 5.5 How the rating reaches a lead — the CLIENT lane

The A/B/C rating is an **account-level** attribute, not a per-lead fact. Every new lead **inherits it via the account link, exactly like tier**.

**CLIENT score = the worst of Layer 1 (inherited rating) and Layer 2 (lead signals).**

**Layer 1 — inherited account rating:**

| Rating | Colour | Reading |
|---|---|---|
| **A** | 🟢 | Runs clean — paperwork back, sites ready, pays on terms |
| **B** | 🟡 | Price the friction — chase time, occasional repeat visits |
| **C** | 🟡 | Known friction on most jobs — deposit/terms tightened, visits priced. ⛔ **FRICTION-PRICING, NEVER BLOCKING — tier decides wanting, rating decides pricing.** |
| **Unrated / new account** | 🟡 | *"first job — no track record"* — the default for every new relationship |

⛔ **A C rating is never a decline and never a block.** The only account-side blocks are `Customer Tier = Do-Not-Quote` and a DUMP marker, both → Needs Review `[R-C1 v4]`.

**Bootstrap and activation:** Layer 1 activates only once the MD's one-off rating pass over the ~30 active trade accounts has landed; until then score Layer 2 only, annotated *"(A/B/C pending bootstrap)"*. While only Payment is seeded, quote the composite as *"(Payment only)"*. **Read the current seeding state off the board — never assume it from this document.**

**Update loop:** the rating is nudged **manually at job close**; **MD confirms every rating change for the first quarter**, then delegation is revisited. ⚠ The original mechanism — *"the sweep PROPOSES a nudge as an update on the account (never a silent write)"* — is dead: `pipeline-daily-sweep` and `pipeline-scan-halfhourly` were retired 26 August 2026 and are no longer carriers. **Nothing proposes rating nudges automatically; the nudge is a human duty by design, not a defect.**

### 5.6 Lead-level CLIENT signals that are account-derived

These sit in the CLIENT risk lane and are listed here only where they turn on the account read. Their full definitions belong to the risk-strip document.

| # | Signal | Score |
|---|---|---|
| **C1** | **Tier disposition** via the account link: unconfirmed Do-Not-Quote match → 🔴 · `Gate - Selective` → 🔴, flag **"Gate account — quote selectively"** (this exact text, nothing appended) → Needs Review, never a clean Qualify · `A - Anchor/VIP` / `A - Win Back` → 🟢 · untiered established → 🟡 | 🔴 / 🟡 / 🟢 |
| **C2** | **Unknown entity** — no confident account match → **BLOCKING, Needs Review** `[R-ENTITY v1]`. Write *"possible account match: X — unconfirmed"* verbatim and treat the account as **untiered**: no A-tier waiver, no Gate-Selective handling, no markup, no SLA. ⚠ Under `[R-CLIENTFIT v1]` an unrecognised sender is **Unqualified** before any material or drawing consideration; material merit must never upgrade an unresolved client-fit outcome. | 🔴 — see §3.1 |
| **C8** | **Below the one-slab minimum** with no tier waiver → 🔴 `[R-C3 v1]` | 🔴 |

**Any label on `color_mm64t0aj` that is not one of the four tier labels — template cruft, blank — is treated as untiered, and all standard rules apply in full.**

---

## 6. Minimum job size `[R-C3 v1]`

**Operative one-liner:** minimum job = **ONE SLAB, applied per job**, waived for A-tier accounts. Total material across the job must reach ≥ 1 slab of the specified material class.

| Case | Treatment |
|---|---|
| Galley kitchen of 2 pieces ≈ 1 slab | Passes |
| Vanity- or laundry-only job | Passes **only if it totals ≥ 1 slab** |
| BBQ / outdoor pieces | **Excluded from the count** — they run under their own rules |
| Many small pieces nesting under one slab (e.g. ~6 lm of hob caps) | **Fails** the minimum |
| Failed minimum, matched-but-untiered **trade** account | **Needs Review** — "human call on scope acceptance" |
| Failed minimum, unknown or retail | **Unqualified** |
| Any single **colour** whose pieces total under a slab | Non-blocking flag *"part-slab — price the waste"* — a pricing note, never a verdict driver |

**Waiver:** `A - Anchor/VIP` and `A - Win Back` waive the minimum, are treated as trade, and count as "known trade" / "approved tier" in the natural-stone rule set `[R-NATURAL v1]`. **The waiver does not relax anything else** — drawings remain mandatory for all tiers `[R-DRAWINGS v1]`, and material rules still fire.

⛔ **The waiver may only be applied off a tier 1–3 link** `[R-ACCTMATCH v5]`. A tier-4 name candidate never waives the minimum.

---

## 7. Trade account behind the job `[R-RETAIL v1]`

**Operative one-liner:** **a job with no approved SteedForm trade customer supplying and installing the cabinetry is a DECLINE.** SteedForm is a B2B fabricator; the work reaches the client through a trade account. **Ratified 3 September 2026 (OR-08)** — it is a registered rule, not a dated position, and it carries full Register authority.

⚖ **The test is the TRADE ACCOUNT BEHIND THE JOB — never who sent the email.**

| Who is in front of you | Verdict |
|---|---|
| A homeowner emailing on behalf of the approved cabinetmaker building their kitchen | **Fine** — a normal trade job, routed through that cabinetmaker |
| A homeowner whose kitchen is being built by an approved cabinetmaker, writing themselves | **Fine** — same job, same account behind it |
| A builder, designer or joiner with **no SteedForm account**, however they present | **Decline** |
| DIY, kit or IKEA cabinetry | **Decline** (IKEA also `[R-SCOPE v2]`) |

⛔ **The decline is PERMANENT.** No "try us later" language — that framing belongs to a capacity decline and nowhere else. The primary redirect is the **trade route**: the enquirer engages an approved trade customer, who deals with SteedForm.

⛔ **It is a CLIENT-TYPE decline, not a capability one.** Never imply SteedForm cannot do the work — we can, and saying otherwise is untrue and invites argument. `T-DECLINE-01` is scope-outside-capability, which is a different thing; the two were being conflated before this rule existed.

**Recorded as the highest-volume decline SteedForm sends** — four in one month in August 2026 — and until 27 August 2026 it had neither a rule nor a template. The template is `T-DECLINE-08` in `09-response-templates.md`.

### 7.1 The Direct Homeowner markup tier SURVIVES

**The `Direct Homeowner x1.55+` markup tier (axis (c), §1) is NOT abolished by this rule.** It continues to apply **where a trade account is behind the job and the homeowner is driving the project** — the tier prices the hand-holding that comes with a homeowner-led job. **It is not a route around this rule**: no trade account behind the job means a decline, at any markup.

### 7.2 The "qualified cabinetmaker" test is SUPERSEDED

⛔ **The screening skill's Axis 0 test — retail / homeowner-direct is OK *"only for a new-build kitchen with a qualified cabinetmaker involved"* — is SUPERSEDED.** The test is **an approved SteedForm trade account**, not a qualified cabinetmaker. A competent, licensed cabinetmaker with no SteedForm account does not satisfy it.

**What survives from that Axis unchanged:**

- **Trade** (cabinetmaker / builder / designer) with an approved account is OK.
- **Auto-decline:** IKEA `[R-SCOPE v2]` · DIY · benchtop replacement on existing cabinetry — MD canonical, verbatim, 19 July 2026: *"SteedForm does not offer a benchtop replacement service, we only measure, manufacture and install on new cabinetry."*
- **Evidence standard:** dimensions marked on the existing tops, or existing cabinetry staying, = replacement **confirmed**. The burden of proof is on evidence of NEW cabinetry, never on "confirming" the replacement. A minor carcass modification (e.g. one rebuilt sink base for a farmhouse sink) does **not** constitute new cabinetry.

---

## 8. Population counts — never state one as live fact

The corpus carries mutually incompatible counts for the same populations, measured on different dates and across the 11 August 2026 migration. **Do not quote a population count as a current fact. If a count is needed, quote it with its measurement date and its source.**

| Population | Figures in the corpus |
|---|---|
| Accounts | **144** (27 Jul 2026) · **153** (10 Aug 2026) · **166** (24 Aug 2026) |
| Leads | **101** (17 Aug 2026) · **111** (10 Aug 2026 and 27 Jul 2026) |
| Contacts | **226** records · **387** unique Contact emails (10 Aug 2026) — 387 unique emails cannot come from 226 records |

*Figures used elsewhere in this document (42 blank POC emails · 14 DUMP accounts · 58 of 144 Payment seeded · 8+ generic-domain accounts) are dated at the point of use and are historical measurements, not live counts.*

---

## 9. Failure mode

**If the Rule Register cannot be read: KEEP CAPTURING, REFUSE TO JUDGE.** Continue intake so no enquiry is lost; do not issue verdicts, do not write risk strips, and notify Matthew *"🚨 Rule Register unreadable — screening halted"*. **Never fall back to inline copies** — including this document. This file explains and cites; it never authors.

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed every item this document used to carry — **OR-08, OR-12, OR-13, OR-14, OR-21 and OR-25 are ruled**, and their positions are now stated plainly in the sections above.

⚠ **One NEW item was raised the same afternoon and it lands squarely here: OR-41.** The board exports show `Client Rating`, `Rating — Measure-ready` and `Rating — Install-ready` are **all 0 of 188** — so OR-14's ruling, made that morning, scores on two empty columns and the composite has no data. **The ruling is not withdrawn and the rubric is not wrong;** what is open is whether site-readiness drops out of the composite until the columns are populated, or the columns are populated first. See §5.2. **Customer Tier is separately 68% blank**, which under `[R-LEADTIME v2]` now sets the quoted lead time as well as the waiver — `07` §6.

Items remaining open across the knowledge base; these are how they bear on this document.

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-30** | **The markup-category list is still to be set.** This is an **outstanding MD action**, not a gap in this document — the four operational tiers stand and are used exactly as §1 states them | §1 axis (c) · §1.3 the per-account `numeric_mm64mvp3` Markup field · §1.4, which records the action |
| **OR-26** | **The CRM boards could not be reached, so no column identifier has been verified against the live board** — `color_mm64t0aj`, `color_mm64jqn0`, `color_mm64kd3q`, `color_mm64je94`, `color_mm647dxb`, `long_text_mm64njy4`, `color_mm64cbq0`, `email_mm64cpfk`, `numeric_mm64mvp3`, `board_relation_mm64fq68`, `color_mm69h52c`. The corpus population counts are unreconciled on the same evidence | §2, §4, §5 — every live read this document instructs, and §8. **A tag check is not an identifier check:** confirm against `08-board-and-column-registry.md` before relying on an id |
| **OR-20** | Whether a customer is quoted the **10–12 day SLA** or the **14–16 day actual**. The internal timeline math is unaffected | §2 and §3.1 name SLA among the account-keyed treatments a confirmed match applies — *whether* an account gets an SLA is settled here; *what figure is said to a customer* is not |
| **OR-38** | The wider implications of the OR-07 ruling, **held for scoping**: is the Screening Philosophy / distance-from-optimum lens retired, and does all stone move to one ladder? | Indirect. §6 defines the "known trade" / "approved tier" waiver that the natural-stone set consumes `[R-NATURAL v1]`; if all stone moves to one ladder that consumer changes shape. **Nothing in OR-38 may be applied as a rule** — keep using §6 exactly as written |
