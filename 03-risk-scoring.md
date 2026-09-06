# 03 — Risk Scoring: the six-dimension strip and its ladders

**Status:** Active. Consolidated from `Lead Risk Assessment Standard.md` v2.1, `Screening Philosophy — Distance from Optimum.md` v1.0 and the risk-scoring sections of `skill-estimator-screening/SKILL.md` v2026-07-25, corrected against the Rule Register wherever the Register governs.
**Owner:** Screening (Deep Screen app). Rule authorship stays with `01-rule-register.md`.
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:** This document owns the six-dimension risk strip — the dimensions, the lane codes, the scoring vocabulary, every scoring ladder, the distance-from-optimum lens, and the strip's emission format. It does **not** own verdicts (Qualified / Needs Review / Needs Info / Unqualified), account matching, client-fit gating, pricing, or any rule's canonical statement — those live in their own documents and in the Rule Register.

---

## What this document decides

- Every lead carries a six-lane risk strip: **Client · Material · Detail · Measure · Manufacture · Install**, each scored 🟢 / 🟡 / 🔴, rendered as one line plus six dimension lines.
- A lane's colour is **the worst criterion firing in that lane**. Ambers never change a verdict; any 🔴 means the verdict is already Needs Review or Unqualified.
- **⛔ CAPABILITY is a fourth, separate verdict and must never be blended with 🔴 RISK** `[R-ANDON v2]`. 🔴 means "far from our optimum — a human decides"; ⛔ means "we cannot make this", and no human call can authorise it. **`[R-ANDON v2]` classifies; `[R-SCOPE v2]` disposes** — the action on a ⛔ item is stated per item, DECLINE or RESET, and is never chosen here.
- The **five-axis distance-from-optimum table is a LENS, not the scorer.** The six-dimension strip is the operative engine and wins on any conflict. ⚠ **The lens stands, but its future is under review — see `10-open-rulings.md` OR-38.**
- The strip is written whole to a `long_text` column and is therefore governed by a **1,800-character composition budget** `[R-LONGTEXT v2]`.

---

## 1. The six dimensions

The six headings are the **canonical, closed taxonomy** for assessing every inbound lead (MD, 19 Jul 2026; locked at Q16). Consequences, all MD-confirmed:

1. **No orphan rules.** Every screening criterion homes under exactly one of the six headings. A seventh category does not exist without an MD decision.
2. **The strip is an index, not a second adjudicator.** Where a rule fires, the risk line **cites** the verdict; it never re-argues it.
3. **Litmus for every criterion:** it must be checkable from what a lead actually contains — drawings, email text, photos, the linked account record, the suburb. No criterion may depend on data we do not have at screening.

| Lane | Dimension | What it measures (MD's definition, verbatim where quoted) | Lane codes |
|---|---|---|---|
| **C** | **Client** | The customer's **track record** first, this lead's signals second. Account-level behaviour inherited via the account link, plus lead-specific commercial signals. | C1 – C8 (+ Layer 1 inherited rating) |
| **M** | **Material** | Material class ladder, then supply, waste, vein and suitability modifiers. | M1 – M7 |
| **D** | **Detail** | *"Profile 20, 30, 40, 100mm, Rounded fascited edges polished, boxed islands, 60mm Lambs tongue, clad fireplaces, bathroom hobs — technical elements to the job."* | D1 – D12 |
| **Me** | **Measure** | *"Assessing access and ability to measure."* | Me1 – Me8 |
| **Ma** | **Manufacture** | *"Machines, time, chips, cracks, risks cutting and handling in the factory."* | Ma1 – Ma5 |
| **I** | **Install** | *"Access ability to get into the building, pantry, two stories."* | I1 – I7 |

**One fact, several lanes.** An underlying fact may colour more than one dimension. It is **adjudicated once**, and every line touching it carries the same citation. Declared echo pairs:

| Owner | Echo | Shared fact |
|---|---|---|
| C7 Occupancy | Me1 | occupied / trading premises |
| D5 Curves & splays | Me5 | template capture of the geometry |
| D6 Clad fireplace | I5 | vertical fixing is an install-method risk |
| D9 Splashbacks | Me8 | scribe-to-existing datum risk (Me8 owns it, D9 carries breakage) |
| D10 Forced joins | Ma4 | factory handling of the forced join |
| M5 Vein geometry | Ma2 | vein-sequenced nesting |
| I1 Address lookup `[R-SITE v1]` | Me1 | the same lookup answers occupancy |
| Client work-type decline | Me8 | substrate risk on existing carcasses is the underlying *why* |

**Deliberately not re-housed here:** the one-slab minimum and its tier waiver `[R-C3 v1]` — a verdict rule owned end-to-end elsewhere. It surfaces at C8 as a citation, never as fresh adjudication.

---

## 2. Scoring vocabulary

### 2.1 The three risk colours

The colours are anchored to the codified blocking test (19 Jul 2026): ***does resolving this change whether we WANT the job, or only what we charge/confirm?***

| Colour | Meaning | Flag class | Consequence |
|---|---|---|---|
| 🟢 **Routine** | Nothing fires. Standard work. | No flag | — |
| 🟡 **Priced-in risk** | Changes what we charge or must confirm — never whether we want the job. Travels to the deal and is priced or confirmed at quote. | Non-blocking | Never changes a verdict |
| 🔴 **Decision risk** | Changes whether we want the job. A human decision is required before effort is spent. | Blocking (closed list) | Lead is already Needs Review or Unqualified |

**Scoring rules (all MD-confirmed at Q1/Q4):**

1. **A dimension's colour = the worst criterion firing in that dimension.**
2. **The consistency invariant (absolute):** any 🔴 anywhere in the strip ⇒ the lead's verdict is already Needs Review or Unqualified. A strip showing 🔴 against a Qualified verdict is a **bug in the screen, not a new verdict** — escalate the discrepancy in the digest; never silently flip the status.
3. **The two rendering rules that keep the invariant true** (source standard rules 2a and 2b):
   - **2a — proposed-blocking rendering (⭐🔴):** any criterion *proposed* for the blocking list renders **🟡 with escalation text** — `⭐ proposed-blocking: [rule] — MD adoption pending` — until it is adopted. It can never paint a 🔴 before adoption. *(The class is currently empty; the mechanism stands for the next proposal.)*
   - **2b — out-of-area rendering:** **I6 is 🔴 only while the Supply Only conversion is UNDECIDED.** Once `Job Type` is set to `Supply Only [− FREIGHT]` the decision is made: I6 renders **🟡** *"supply-only conversion applied — freight/packaging priced"* and the invariant is satisfied. **Out-of-area's authority to paint that 🔴 is registered** — it is a layer-1 blocking condition `[R-AREA v1]` `[R-BLOCK v3]`, and it never declines.
4. **Ambers never escalate.** One soft rule only: **4+ amber dimensions → a daily-digest line, "heavy-amber lead — estimator eyes before quote"** — a mention, never a verdict change and never a status write.
5. **Unknown is never 🟢.** Where a dimension cannot be evaluated, score what is known and suffix the line `— (insufficient info)`.

**The blocking list has TWO layers, both closed** `[R-BLOCK v3]` — cited, not restated here; both layers are enumerated in the Rule Register.

- **Layer 1 — the base list**, applied since screening began and **registered on 3 September 2026**: occupancy `[R-OCCUPANCY v1]` · `Do-Not-Quote` or an unresolved account match `[R-C1 v4]` `[R-ACCTMATCH v5]` · out of area while the Supply Only conversion is undecided `[R-AREA v1]` · spec conflicts `[R-30MM v1]` `[R-PROFILE v3]` · below the one-slab minimum, non-A-tier `[R-C3 v1]` · the natural-stone rule set `[R-NATURAL v1]` · unknown-entity checks `[R-ENTITY v1]`.
- **Layer 2 — the 20 July 2026 addition set: SIX rules, not seven.**

**Nothing the strip does changed on 3 September — only the authority behind layer 1, which is no longer a set of unregistered conditions.** Amendment authority for both layers is an **MD or GM** decision, recorded with a version bump. The strip must never revive the struck "curves >40mm" rung; that rule now lives at `[R-D5 v7]` as a 🟡 with sign-off.

### 2.2 ⛔ CAPABILITY — the fourth verdict, which never blends with 🔴

`[R-ANDON v2]` — operative one-liner, cited not restated: **⛔ CAPABILITY and 🔴 RISK are two different verdicts and MUST NEVER BLEND.** Say which one it is, every time.

| | Meaning | Resolution | Examples named by the rule |
|---|---|---|---|
| **🔴 RISK** | *"This is far from our optimum."* | **A human decides**: take it and price it properly, or decline it as not for us. **Both answers are valid.** | natural stone · 50mm+ builds · vein · boxed islands · large splashbacks · non-standard details |
| **⛔ CAPABILITY / NOT-OFFERED** | *"We cannot make this."* | **A hard stop. No human call can authorise it** — the tooling, the material physics or the ruled scope is not there. **The action is per item — DECLINE or RESET — and is stated in `[R-SCOPE v2]`, not here** | profiles we lack tooling for · flush mount · bathroom hobs · drainer grooves · flooring · shower bases · pencil on a printed face · lamination on porcelain / sintered / hard natural · 30mm on anything but natural · ogee |

**Why the line matters.** Blend them and one of two failures follows: treat a capability gap as risk and someone eventually **human-calls their way into promising a job that physically cannot be made**; treat risk as capability and screening starts **declining work SteedForm actively sells** — a boxed island is red on geometry but is standard, all-material, charged work (assemble on site, factory cuts the 45°, glued in situ).

⚠ **Known live defect, recorded not fixed:** `[R-ANDON v2]` states that both currently render as one undifferentiated 🔴 — *"which is the bug"* — and the rule was registered after an audit found it had reached no executable as a scoring rule. The strip specification below carries the separation; any emitter that collapses ⛔ into 🔴 is non-conformant.

### 2.3 Where the corrected classification differs from the legacy lane text

**Twelve lanes or rungs** in the source standard are read differently here from the legacy lane text. The Register classes nine of them as **capability** rather than risk; **D1 masons mitre** and **M7 client-supplied slabs** are now ruled `[R-SCOPE v2]`; and **I6** keeps its legacy colour, whose authority is now registered `[R-AREA v1]`. The corrected reading is carried in the ladders below.

⚖ **Classification and action are two separate columns, by ruling.** `[R-ANDON v2]` says whether the fact is ⛔ CAPABILITY or 🔴 RISK; `[R-SCOPE v2]` says what the screen then does with it — **DECLINE or RESET, per item, never interchangeably.** A DECLINE item is not a specification to be corrected: do not price it, do not substitute around it, do not render it 🟡. A RESET item is not a decline: the enquiry continues on a supported specification, and the client is told **before** the quote goes out.

| Lane | Legacy text | Governing rule | Carried as | Action `[R-SCOPE v2]` |
|---|---|---|---|---|
| D8 flush mounting | *"🔴 spec conflict, ON the blocking list"* | `[R-BLOCK v3]` (flush mounting is in neither layer) + `[R-FLUSH v1]` (a separate capability refusal, expressly *"not an edge profile"*) | **⛔ CAPABILITY** | **RESET** to a supported mount, before the quote `[R-FLUSH v1]` |
| D8 machined recesses / chutes / glazing channels | not separated from the 🔴 cutout material | `[R-SCOPE v2]`; `[R-ANDON v2]` | **⛔ CAPABILITY** | **DECLINE or refer** |
| D8 drainer grooves — the whole category | not separated from the 🔴 cutout material | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #136 | **⛔ CAPABILITY** | **DECLINE or refer** |
| D7 bathroom hobs | *"🔴 NOT OFFERED"* (Q5 ladder) | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #124 | **⛔ CAPABILITY** | **DECLINE or refer** |
| **D12 stone shower bases and fall drainers** | ratified as NOT-OFFERED with **no lane home at all** | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #103 | **⛔ CAPABILITY** | **DECLINE or refer.** Now homed at **D12** (§3.3) |
| D3 pencil on a face-printed surface | not distinguished from the 🟡 shaped-profile class | `[R-ANDON v2]`; `[R-PROFILE v3]`; ledger #157 | **⛔ CAPABILITY** | **RESET** the profile — steer to arris (or Sharknose/Euro) |
| D2 ogee | carried as a profile option | `[R-PROFILE v3]` (removed from all documents 23 Jul 2026); `[R-SCOPE v2]`; `[R-ANDON v2]` | **⛔ CAPABILITY** | **RESET** to a **lamb's tongue (Provincial)** |
| D1 30mm on anything but natural | *"any build ≥30mm … → 🟡, MATERIAL NAMED"* | `[R-30MM v1]`; `[R-PROFILE v3]`; `[R-ANDON v2]` | **⛔ CAPABILITY** (cannot be priced) | **RESET** the spec — do not price it `[R-30MM v1]` |
| M6 flooring, any material | *"🔴 spec conflict"* | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #116 | **⛔ CAPABILITY** | **DECLINE or refer** |
| D1 masons mitre as a standalone selection | *"🟡 SUBSTITUTE NOTE"* | `[R-SCOPE v2]` — **ruled 3 Sep 2026** | **RESET, not a decline** — 🟡 substitute note, non-blocking | **RESET** the spec to SteedForm's standard mitred build. ⚠ The CNC exception is **production's discretion and must never be promised by the screen** |
| M7 client-supplied slabs | *"🔴 — a human declines or excepts"* | `[R-SCOPE v2]` — **ruled 3 Sep 2026**; the **only** carve-out in the NOT-OFFERED table | **⛔ DECLINE**, except on an **A-tier account**, where it is a **🔴 RISK → Needs Review** | **DECLINE.** On an A-tier account only, route to Needs Review for a named human to accept or decline |
| I6 out-of-area | *"conversion UNDECIDED → 🔴 by the blocking list"* | source rule **2b** (§2.1) — retained, and its authority now registered `[R-AREA v1]` `[R-BLOCK v3]`; `[R-SUPPLYONLY v2]`'s *"Distance is NOT a risk and NOT a decline"* is scoped to the two **CONFIRMED Supply Only zones** (Port Lincoln 5606 · Kingscote 5223), not to all out-of-area work | **🔴 while the conversion is UNDECIDED → 🟡 once `Job Type = Supply Only [− FREIGHT]`** (see I6) | **NEVER a decline** — out of area converts the delivery model `[R-AREA v1]` |

---

## 3. The scoring ladders

Legend: **⭐ trial** = emits in strips but is not yet a skill rule; fold-in decided on evidence, not on faith. `[R-xxx vN]` tags are citations to the Rule Register, which is authoritative over every statement below.

### 3.1 CLIENT (C)

Client risk is the customer's **track record**. The A/B/C rating is **worst-of the two critical streams — Site-readiness and Payment**.

⛔ **The Paperwork stream is ABOLISHED (ruled 3 September 2026).** The `Rating — Paperwork` and `Rating — Communication` columns were deleted from the Accounts board, they were never in the composite, and **no downgrade-a-notch flag survives them.** Nothing in this document may route to a Paperwork / lead-quality flag. Communication quality on an individual lead is still scored, at **C5**, as a 🟡 on that lead alone.

⚠ **Structural point:** these are **account-level** attributes, not per-lead facts. The A/B/C rating lives on the Accounts board and every new lead **inherits it via the account link, exactly like tier**. Keep the two account lenses distinct: **Customer Tier = how much we VALUE them**; **A/B/C rating = how SMOOTHLY they RUN**. Never conflate them in one field.

**Per-lead scoring: CLIENT = the worst of Layer 1 (inherited rating) and Layer 2 (lead signals).** Layer 1 activates only once the MD bootstrap pass lands; until then score Layer 2 only, annotated `(A/B/C pending bootstrap)`.

⛔ **Client fit precedes everything in this lane** `[R-CLIENTFIT v1]` — operative one-liner, cited: an unresolved client fit is **Unqualified before drawings are considered**, and drawings, scope, material, value and technical merit may never upgrade it. Score the C lane after that gate, never as a way around it.

**Layer 1 — inherited account rating:**

| Rating | Colour | Reading |
|---|---|---|
| A | 🟢 | Runs clean — paperwork back, sites ready, pays on terms |
| B | 🟡 | Price the friction — chase time, occasional repeat visits |
| C | 🟡 | Known friction on most jobs — deposit/terms tightened, visits priced. **Friction-pricing, never blocking**: tier decides *wanting*, rating decides *pricing* |
| Unrated / new account | 🟡 | *"First job — no track record"* — the default for every new relationship. Blank ratings mean **not populated**; they are not evidence either way `[R-ACCT v3]` |

**Layer 2 — lead-specific signals:**

| # | Criterion | Score | Basis |
|---|---|---|---|
| **C1** | **Tier disposition** (account link → Customer Tier): DNQ match unconfirmed → 🔴 · `Gate - Selective` → 🔴, flag reads verbatim **"Gate account — quote selectively"** · `A - Anchor/VIP` / `A - Win Back` → 🟢 · untiered established → 🟡. ⛔ **Tier is the disposition LABEL, not the whole evidence:** a `DUMP STOP` / `DUMP LOCKED` marker in Notes/Flags `long_text_mm64njy4` — or any note contradicting the tier label — → 🔴, quoted **verbatim**, item ID cited, **even when the tier reads A-Anchor/VIP**. Where label, group and note disagree, **that disagreement is the finding**: surface all three, route to a human, never silently prefer one. Account Status is stale lifecycle data and must never block, qualify, score or describe a lead | 🔴 / 🟡 / 🟢 | `[R-C1 v4]` `[R-ACCT v3]`; skill Axis 0 tier rules (cite the verdict) |
| **C2** | **Unknown entity — a BLOCKING check → Needs Review** `[R-ENTITY v1]`**:** no confident account match → the unrated 🟡 above, subject to the client-fit gate · **all-natural job from an unknown account → 🔴**, flag **verbatim**: *"who is asking — is this a future client we want?"* `[R-NATURAL v1]`. ⛔ **A near-miss is NEVER silently matched and NEVER silently dropped** `[R-ACCTMATCH v5]`: write the confirm flag **verbatim** — *"possible account match: X — unconfirmed"* — and treat the account as **UNTIERED** until a human confirms. **An untiered account gets no tier-dependent treatment: no A-tier waiver, no Gate-Selective handling, no markup, no SLA** `[R-ENTITY v1]`. A wrong tier match is worse than no match, in both directions. ⚠ This check runs **after** the client-fit gate, not instead of it, and material merit must never move the line: an unresolved client fit is Unqualified regardless of what the job is made of | 🔴 / 🟡 | `[R-ENTITY v1]`; `[R-CLIENTFIT v1]`; `[R-ACCTMATCH v5]` |
| **C3** | **Retail vs trade — the test is the TRADE ACCOUNT BEHIND THE JOB, never who sent the email** `[R-RETAIL v1]`**:** no approved SteedForm trade customer supplying and installing the cabinetry → **DECLINE**, and the decline is **permanent** (no "try us later"); the redirect is the trade route. A homeowner emailing on behalf of their cabinetmaker is fine; a builder, designer or joiner with no SteedForm account is a decline however they present. ⚠ **The older test — *"retail/homeowner-direct OK only for a new-build kitchen with a qualified cabinetmaker involved"* — is SUPERSEDED.** The **Direct Homeowner ×1.55+ markup tier survives** where a trade account is behind the job and the homeowner is driving it; it prices hand-holding and is not a route around this rule. · IKEA kitchens → **DECLINE** `[R-SCOPE v2]` · replacement-on-existing → **DECLINE** `[R-SCOPE v2]`, MD canonical sentence, verbatim: *"SteedForm does not offer a benchtop replacement service, we only measure, manufacture and install on new cabinetry."* **Evidence standard:** dims marked on existing tops, or existing cabinetry staying = replacement **CONFIRMED**; the burden of proof sits on evidence of NEW cabinetry; a minor carcass modification is not new cabinetry | 🔴 / DECLINE | `[R-RETAIL v1]`; `[R-SCOPE v2]`; Rowe calibration #1 |
| **C4** | **Who manages the end client:** an intermediary between SteedForm and the party controlling the site or the decision → 🟡 | 🟡 | ⭐ trial |
| **C5** | **Communication quality of THIS lead:** referenced-but-missing attachments, chasing required, contradictory instructions → 🟡 as a lead (chase / ask). ⛔ **It routes nowhere else — the Paperwork stream is abolished** (§3.1), so this 🟡 stands on its own lead and never touches the account rating. At **order** confirmation, incomplete is a hard no-go | 🟡 | `[R-DRAWINGS v1]`; `[R-EVIDENCE-BAR v2]`; ledger #150 |
| **C6** | **Timeline pressure — two-factor, and TIER-DEPENDENT** `[R-LEADTIME v2]`. The flag fires when the requested install date falls inside *(measure booking notice ≈ 2 weeks) + (measure-to-install)*. **A-tier → 10–12 days, threshold ≈ 22 days from enquiry. Everyone else → 14–16 days, threshold ≈ 24–26 days.** ⛔ **An untiered account takes the non-A figure** `[R-ENTITY v1]` — never quote the A-tier date to an unconfirmed account. ⚠ Using the A-tier threshold on a non-A job **under-fires by about a working week**; resolve the tier before computing. **The flag does the math** — it states the earliest realistic install date, never "tight". Read from prose; the Client Required-By column is retired | 🟡 | `[R-LEADTIME v2]`; `[R-ENTITY v1]`; Q7 decision |
| **C7** | **Occupancy / trading premises** `[R-OCCUPANCY v1]`**:** occupied dwelling or trading ongoing concern → 🔴 (**occupancy carve-out — Needs Review, NEVER an auto-decline**) · stripped CBD site → 🟡. Occupancy is **established by the address lookup, never assumed**. ⛔ **The decline letter (T-DECLINE-05) may only be sent AFTER a human review — it is never a triage output**, and the retired *"tenanted occupied residential building → DECLINE"* line must not be applied | 🔴 / 🟡 | `[R-OCCUPANCY v1]`; `[R-SITE v1]`; `[R-BLOCK v3]` layer 1 |
| **C8** | **Below one-slab minimum:** pieces total under the minimum with no tier waiver → 🔴, citing the minimum-job verdict; A-tier waiver applies where it applies | 🔴 | `[R-C3 v1]` (cite verdict, never re-adjudicate) |

### 3.2 MATERIAL (M)

**The class axis, re-baselined on ratification (21 Jul 2026, ledger #131) and extended to ceramic on 3 September 2026** `[R-M1 v2]`. Engineered = 🟢 (current compliant / reformulated lines only — old high-silica engineered stone is banned and gone from AU) · Porcelain / sintered = 🟡 (handling, edge and install fragility per #119 — **not** thickness; the cutting tech gives a quality cut) · **Ceramic = 🟡 — it scores on the porcelain / sintered rung** · Natural = 🔴 (variation, vein match, human sign-off).

⚠ **This supersedes the earlier Q15 position that porcelain/sintered dropped to 🟢** `[R-M1 v2]`. Any strip, example or reality-test record showing a sintered material at `M 🟢` is stale and must be re-scored to `M 🟡`.

**Vasari is CERAMIC** `[R-M1 v2]`, so it scores 🟡 on that rung; the Materials Library value for Vasari items is to be set to match. The former "stated four different ways" ambiguity is closed.

⚠ **Note:** the risk band is not the silica-control level. **Full RCS controls apply to ALL materials regardless of band.**

**Data feed** `[R-M1 v2]` — operative one-liner, cited: **material class is read LIVE from the Materials Library `color_mm4qt817` Material Type and is never inferred from a brand or colour name.** The legacy instruction in the source standard to *"categorise by BRAND"* is superseded by this rule. Where the natural-stone fork needs granite vs non-granite, `dropdown_mm4rq7jd` Stone Sub-Type is populated on only **3 of 392** materials `[R-SUBTYPE v2]`: apply the **conservative branch** (score the hard-stone tooling flag as if granite) and always add the visible flag **"⚠ Stone Sub-Type not recorded — confirm granite vs non-granite before quoting."**

| # | Criterion | Score | Basis |
|---|---|---|---|
| **M1** | **Material class ladder.** **NATURAL → 🔴** per the natural-stone rule set `[R-NATURAL v1]`: non-granite (marble / Calacatta-class, quartzite, travertine / limestone) → 🔴 · granite, known trade → 🟡 (with the first-natural-job confirm flag) · granite, retail-direct → 🔴 · **soft natural (Mohs ≤ 5) in a kitchen, scullery, coffee station or heavy-wear wet area → 🔴 Needs Review, NEVER an auto-decline** `[R-NATURAL v1]`. **Technical Standards' DECLINE for that condition is SUPERSEDED** — a human makes the call, and `05-material-and-capability.md` §1 carries the same position. **PORCELAIN / SINTERED / CERAMIC → 🟡** — quotable, not "all-clear". **ENGINEERED (compliant lines) → 🟢** | 🔴 / 🟡 / 🟢 | `[R-M1 v2]`; `[R-NATURAL v1]`; `[R-SUBTYPE v2]`; ledger #131 / #119 |
| **M2** | **Dekton** `[R-DEKTON v1]`**:** specified anywhere → 🔴 (phase-out; decline-as-spec'd plus a substitution steer), flag reads **verbatim**: *"Dekton — phase-out in progress, do not quote"*. ⛔ **The materiality exception is available to A-TIER ACCOUNTS ONLY.** For a B-tier account or below there is **no exception**: decline and substitute. On an A-tier account the exception is a **four-condition test, all four required**: minor component (≤ 1 room / 1–2 pieces) **AND** the bulk of the job is other material **AND** the job is substantial (~$10k+) **AND** the customer will not substitute. Met → **Needs Review**, a named human decides. **The exception converts the OUTCOME; it never lowers the colour — the material line stays 🔴.** It is *not* "the client asked" | 🔴 | `[R-DEKTON v1]`; REV 09 arguments; T-DECLINE-06 |
| **M3** | **Supply & specification exposure:** brand not local / interstate / unknown → 🟡 · discontinued colour → 🟡 · **colour or material TBC** → 🟡, line reads *"material unknown — class ladder and supply unassessable; re-score when named"* | 🟡 | Skill Axis 2; `[R-MATERIAL-TERMS v1]`; TBC tier ⭐ trial |
| **M4** | **Part-slab waste:** any colour whose pieces total under one slab → 🟡, *"part-slab — price the waste"* (a pricing note, never a verdict driver) | 🟡 | `[R-C3 v1]` non-blocking waste flag |
| **M5** | **Vein / finish match exposure — GEOMETRY ALONE triggers:** a veined colour on **2+ adjacent visible faces** (island + waterfall, book-match pairs, continuity runs) → 🟡 — never wait for a stated client expectation. **Full vein match (Level 3), or match to existing installed stone → 🔴** (blocking): *"feasibility and the 20–50% uplift are a human call before quote."* Kaya face-printed vein → 🟡 note (cannot be re-polished). Feasibility is read live from `boolean_mm4r4qcp` Bookmatch Available | 🔴 / 🟡 | `[R-MA2 v1]`; Technical Standards §9.3; Q12 |
| **M6** | **Outdoor / alfresco suitability** `[R-ALFRESCO v1]`. ⛔ **ENGINEERED STONE CANNOT BE USED FOR AN ALFRESCO OR BBQ BENCHTOP** — Australian Standards require a non-flammable benchtop; natural or ceramic/sintered only. Engineered on an alfresco scope → 🔴 **spec conflict**, reset the material. ⚠ **This is a CLASS test read live off the Materials Library — not the old brand list.** Zenith, Kaya, QXeron and Caesarstone ICON are all engineered, so the brand list gave the right answer by accident and let any engineered brand not on it through. · **Smartstone Sintered outdoor → 🟡 Conditional**, three conditions **verbatim**: *"300 °C max · non-combustible / fibre-cement backing · 10mm grill clearance"* · rated ceramic/sintered or natural outdoors → 🟡 (BBQ comms + vent gap + substrate + **the 12×50 shadowline, which is a MEASURE precondition**). **FLOORING, any material → ⛔ NOT OFFERED** | 🔴 / 🟡 / ⛔ | `[R-ALFRESCO v1]`; `[R-M1 v2]`; `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #116 |
| **M7** | **Client-supplied stone — DECLINE, with ONE carve-out** `[R-SCOPE v2]`**:** client buying the slab themselves → a **hard stop** for every account: *"we do not fabricate client-purchased slabs."* **On an A-TIER account only, it becomes a 🔴 RISK routed to Needs Review** for a named human to accept or decline. No other NOT-OFFERED item carries a carve-out. Client-supplied stone is also a layer-2 blocking condition `[R-BLOCK v3]` | ⛔ DECLINE / 🔴 on A-tier | `[R-SCOPE v2]`; `[R-BLOCK v3]` (layer 2); T-DECLINE-07 |

#### The natural-stone rule set `[R-NATURAL v1]` — carried in full

M1 cites this rule set as its scoring basis, so it is carried here in full. **It is now REGISTERED as `[R-NATURAL v1]`** (adopted 19 July 2026, stated as a rule 3 September 2026) and is one of the layer-1 blocking conditions `[R-BLOCK v3]`. It replaces all former "minority of rooms" and volume language, everywhere. **Every branch below is BLOCKING → Needs Review except branch 4.**

1. **GRANITE → passes clean for known trade**, in any room **including the kitchen**.
   - **"Known trade"** = a tiered A-account, **OR** an established trade customer (existing account / trading history).
   - **Never** when the live Customer Tier is **Do-Not-Quote**.
   - **Never** a **Gate-flagged account whose match is unconfirmed**.
   - **Retail-direct + granite → always Needs Review.**
2. **NON-GRANITE naturals** (marble / Calacatta-class, quartzite, travertine / limestone):
   - **KITCHEN →** approved tiers only **AND** a style-of-work review — **Needs Review even for approved tiers**; everyone else → Needs Review.
   - **OTHER ROOMS →** Needs Review, **with the reason written in the flag**.
3. **ALL-NATURAL job from an unknown account → Needs Review**, flag **verbatim**: *"who is asking — is this a future client we want?"*
4. **FIRST natural-stone job on ANY account →** a **non-blocking** flag, **verbatim**: *"first natural job with this account — confirm slab-selection process"*.
5. **SOFT NATURAL (Mohs ≤ 5) in a kitchen, scullery, coffee station or heavy-wear wet area → 🔴 Needs Review, NEVER an auto-decline.** Technical Standards' DECLINE for this condition is **superseded** — a human makes the call.

**Volume / room-count is RETIRED as a verdict test.** Slab count appears only as a pricing note in flags. Complexity flags (curves, mitres, vein-matching) still apply on top. Where the granite fork cannot be resolved, take the conservative branch and flag it `[R-SUBTYPE v2]`.

### 3.3 DETAIL (D)

Governing logic: **material changes the build risk** (engineered builds are routine where porcelain / sintered / natural builds are not), **shaped profiles always cost hand-finish time**, and **weight is its own flag at 100mm**.

**Profile scope boundary** `[R-PROFILE v3]` — cited: the ratified profile and build rules **run to 40mm**. **50–80mm carries its own cost step; >80mm is a hard cost cliff — flag it.** A 60mm engineered island edge is routine work that still prices differently from 40mm: **flag the thickness so it is priced; do not flag it as a risk.**

**RULED, 3 September 2026 — D1 now has a rung for that band: a 50–80mm engineered mitred build scores 🟡 AMBER, on the cost difference.** Engineered **≤ 40mm is 🟢**, and **the minimum mitred build-up is always 40mm** — nothing below 40mm is mitred.

| # | Element | Score | Basis |
|---|---|---|---|
| **D1** | **Profile build height.** engineered ≤ 40mm build → **🟢** (routine mitred work) · **engineered mitred build 50–80mm → 🟡, on the COST DIFFERENCE** (ruled 3 Sep 2026) — it is routine work that prices differently from 40mm, so the amber is a pricing flag, never a doubt about wanting the job · any permitted build ≥ 30mm in porcelain / sintered or natural → **🟡, MATERIAL NAMED in the line** (brittle mitre stock / hard-material lamination) · **100mm+ build → 🟡 ALWAYS regardless of material — weight; NAME THE PIECE** (cleats, handling, hand-finish hours) · the double-lever case (100mm + big piece + chip-prone material) **stays 🟡** — it stacks flags, not colours. ⚠ **The minimum mitred build-up is ALWAYS 40mm — nothing below 40mm is mitred.** **Client-spec'd masons mitre — RULED `[R-SCOPE v2]`: RESET the spec to SteedForm's standard mitred build, 🟡 substitute note, non-blocking.** It is a reset, not a decline: the enquiry continues on the supported build and the client is told before the quote goes out. ⚠ **The CNC exception is PRODUCTION'S DISCRETION and must NEVER be promised by the screen** — a piece already on the CNC for profiling or lamination may absorb a masons mitre at no meaningful extra cost, but that is decided in production, not at screening. ⚠ **The ≥30mm rung is bounded by `[R-30MM v1]` and `[R-PROFILE v3]`:** 30mm is a natural-stone-only single thickness, there is no 30mm build-up, and lamination is 20mm layers, engineered + marble only — so a 30mm engineered, porcelain or sintered spec is **⛔ CAPABILITY, not a 🟡**, and cannot be priced | 🟢 / 🟡 / ⛔ | Q5 ladder; `[R-30MM v1]`; `[R-PROFILE v3]`; `[R-SCOPE v2]`; Technical Standards §3 |
| **D2** | **Shaped profiles — ALL of them → 🟡 ALWAYS** (machine profile + hand-finish time). **Capability set:** Bullnose and Provincial / Lamb's Tongue = CNC tooling, straight **and** curved, but **engineered + marble ONLY** → the combination is **ruled out elsewhere** and must not be priced. Sharknose (Euro) = all materials, **straight line only**. Double bullnose = CNC 20mm polish, then the two polished pieces laminated. Triple bullnose at 60mm is **theoretical only — treat as first-of-kind**. **Ogee = ⛔ NOT OFFERED**, removed from all documents — **RESET the spec to a lamb's tongue (Provincial)** `[R-SCOPE v2]`, which is CNC, straight and curved, engineered + marble only | 🟡; ⛔ on a ruled-out combination | `[R-PROFILE v3]`; `[R-SCOPE v2]`; `[R-ANDON v2]`; MD profile audit 23 Jul 2026 |
| **D3** | **Rounded / faceted edges, polished → 🟡 ALWAYS** (shaped-profile class — polish time). **Arris stays 🟢** (every material, straight and curved — the default). **PENCIL on any FACE-PRINTED surface → ⛔ NOT OFFERED** — a pencil radius rolls over the face edge and cuts through the print; steer to ARRIS. ⚠ **CONSTRUCTION IS THE TEST, NOT CLASS:** read `Print Construction` (`color_mm6hz0dd`) live off Materials Library `5029570546` — `Face-printed` is a hard refusal, `Full body` permits pencil, and **blank FAILS CLOSED to review; never read blank as "not printed."** ⛔ **The column is 99% blank as at 3 Sep 2026** — so this rung currently sends nearly every pencil job to review. **The rung is right; the data is not there.** Open as **OR-40**; do not soften the rule to make the queue shorter. Interim flag wording: *"print construction not recorded"* — `08` §7.1. Porcelain and sintered remain excluded as a class. ⚠ **An `Engineered Stone` classification does NOT mean full body** — Kaya Surfaces (all — NEOVENA print, face only), Zenith Ottoman Grey and Zenith Rosè are engineered **and** face-printed. Pencil on full-body materials is offered but hand-finished at every size | 🟡 / 🟢; ⛔ on a printed face | `[R-PROFILE v3]`; `[R-REF v2]`; `[R-ANDON v2]`; ledger #157 |
| **D4** | **Boxed islands & waterfalls → 🟡 ALWAYS** — mitre pricing noted; in a veined colour, add the vein-continuity line (→ M5 geometry trigger, same citation). Waterfall ends at **12 / 20 / 30 *(if available)* / 40mm** are a **standard chargeable install** — the qualifier is load-bearing: 30mm is a **natural-stone-only single thickness, subject to slab availability** `[R-30MM v1]`, so a 30mm waterfall end is neither available on engineered, porcelain or sintered nor guaranteed on natural; a boxed island that cannot be glued in the factory is an **assemble-on-site** in every material | 🟡 | Q5 ladder; §9.3 Level-1 orientation rule; `[R-PROFILE v3]` |
| **D5** | **Curves & shapes.** A curve polishes only up to **that MATERIAL's** limit; above it the curve is a **FACETED MITRE — makeable, never a decline**. ⚠ **The limit is MATERIAL-DEPENDENT, not a flat 40mm.** Above the limit → **🟡 + a MANDATORY documented CLIENT SIGN-OFF on the faceted appearance before fabrication.** It is **not blocking** and must never force Needs Review. **The document is the SIGNED ORDER CONFIRMATION** — a screen states the condition and names what will carry it; it never confirms a sign-off happened. **A curve on single thickness (12/20/30) is ordinary work and scores nothing on its own** — the tooling is built for it — while **a request for faceting below 40mm is 🟡**, because below the lamination threshold there is nothing to facet. **Splayed or angled benches → 🟡 ALWAYS.** Faceting is elective from 40mm on any material and is **frequently the recommendation on veined stone** — a polished radius grinds through the vein, a facet preserves it. On engineered and marble, elective means **the vein is too clashy for lamination**; the trade is a curve that will not necessarily be smooth, and **that trade is the customer's call**. D5 is the single owner of splay / curve geometry; Me5 carries the template-capture echo | 🟡 + sign-off | `[R-D5 v7]`; `Edge Profile Capability Matrix` §2 |
| **D6** | **Clad fireplaces:** no published brand rule → **🔴** *"heat + vertical fixing is an unruled install class; a human accepts the known gap in writing before quote."* **Echoes into Install** (I5, vertical fixing, same citation) · brand-ruled (e.g. Caesarstone Porcelain fireplace rules) → 🟡 | 🔴 / 🟡 | `[R-BLOCK v3]` (layer 2); Technical Standards |
| **D7** | **Bathroom HOBS → ⛔ NOT OFFERED, DECLINE or refer** — the raised wet-area kerb, **not** cooktops. *(Shower bases and fall drainers are the adjacent rung, **D12**.)* Wet-area details on work we **do** do (vanities, benchtops) → **🟡 = a TRADE INTERFACE flag**: tiling / waterproofing / sealing sequence, existing surfaces — **name the interfacing trade**; site-verify datums | ⛔ hobs / 🟡 wet-area | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #124 |
| **D8** | **Cutouts & machined features.** Flush-mount cooktop or sink → **⛔ NOT OFFERED** (see §2.3): the stone edge chips, the silicone gap is unavoidable, the brochure image cannot be reproduced — state the reason, reset to a supported mount, and tell the builder/client **before the quote goes out** · **trench / rebate to receive joinery → 🔴** *"unruled machining class; a human accepts the known gap in writing before quote"* · **≥ 3 cutouts on one piece, or a cutout in a fragile position** (GPO in a waterfall panel, within 100mm of a join) → **🟡** (cutout density) · **machined recesses, chutes, glazing channels → ⛔ NOT OFFERED** · **drainer grooves — the whole category is off the menu → ⛔ NOT OFFERED** | ⛔ / 🔴 / 🟡 | `[R-FLUSH v1]`; `[R-BLOCK v3]`; `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #31 / #136 |
| **D9** | **Splashbacks — tall or scribed → 🟡:** > 600mm high, window-opening interfaces, scribed runs (breakage + template risk). Scribe-to-existing datum risk is **owned by Me8**; D9 carries the breakage echo, same citation | 🟡 | Q5 ladder |
| **D10** | **Forced joins in visible runs → 🟡:** a run exceeding the **specified brand's usable slab length** — brand-specific, **never a generic 3200mm** — forces a join → 🟡 **plus the client-expectation line**: *"join will fall in this run — position agreed before fab"* · joins in island or feature faces → 🟡. D10 **owns** the forced-join determination; Ma4 carries the factory-handling echo | 🟡 | Q5 ladder; Technical Standards seam/join placement + slab specs by brand |
| **D11** | **Overhangs vs brand / thickness limits → 🟡 + MANDATORY FLAG-UPFRONT (the April rule):** a drawn overhang at or over the brand + thickness limit table → 🟡, support / steel / substrate confirmed and priced, and **raised at first builder contact, always**. Over-limit with no support shown is exactly the April failure mode | 🟡 | Q5 ladder; Technical Standards overhang limit tables |
| **D12** | **Stone SHOWER BASES and FALL DRAINERS → ⛔ NOT OFFERED, DECLINE or refer** — SteedForm does not machine falls or gradients. **New rung, ruled 3 September 2026** (D12 is the next free Detail code): the condition was ratified as NOT-OFFERED but had **no home in any of the six dimensions**, which is the orphan §1 rule 1 forbids. It sits alongside D7 because both are wet-area details SteedForm does not make; D8 keeps drainer **grooves**, M6 keeps flooring | ⛔ | `[R-SCOPE v2]`; `[R-ANDON v2]`; ledger #103 |

#### D5 — the faceting thresholds and the mandatory conservative fallback

`[R-D5 v7]` — thresholds, carried in full because they are reference data:

| Material | Polished ceiling | Faceted from |
|---|---|---|
| **Engineered · marble** | polished to a **40mm lamination** (20 + 20) | **60mm** |
| **Porcelain · sintered** | single thickness only (12 / 20) — never laminated | **40mm** |
| **Hard natural** (granite, quartzite, **limestone and travertine — RULED not laminable, MD 23 Jul 2026**) | single thickness (12 / 20 / 30) — no polished 40mm curve exists | **40mm** |

⛔ **The conservative fallback is MANDATORY and several carriers omit it** `[R-D5 v7]` — operative one-liner, cited:

- **The marble vs hard-natural split is NOT derivable from the board.** Material Type says only "Natural Stone"; Stone Sub-Type records granite vs non-granite, which does not identify marble, and is populated on **3 of 392** materials as at 18 Aug 2026 `[R-SUBTYPE v2]`.
- **Until a field exists: treat ANY natural stone as HARD NATURAL — faceted from 40mm** — unless a human has confirmed it is marble.
- **ONE flag string, and it is fixed. Emit it verbatim:** `⚠ marble vs hard natural not derivable from the board; confirm before quoting the curve`. *(The former second string — "natural sub-type not recorded…" — is retired: `[R-D5 v7]` nominates a single canonical string.)*
- **Never resolve it from the colour or brand name.**
- **Why this direction:** assuming marble and being wrong means **promising a polished 40mm curve on granite that cannot be made** — the exact mis-sell this rule exists to stop. Assuming hard natural and being wrong means quoting a facet where a polish was possible: recoverable, and visible at sign-off. **When the data is missing, fail toward the flag, never toward the promise.** An unnecessary sign-off costs a conversation; a promised polished radius that cannot be made costs a remake and a client.
- A **40mm curved porcelain or granite edge IS faceted and DOES need the sign-off.**

### 3.4 MEASURE (Me)

| # | Criterion | Score | Basis |
|---|---|---|---|
| **Me1** | **Can we get in — occupied premises:** measuring in an occupied or trading site → 🔴 (same fact as C7, same citation) · CBD site-hours or parking constraints on the measure visit → 🟡. **Occupancy is ESTABLISHED BY THE ADDRESS LOOKUP, not assumed** — where a street address is held, read the live tenant directory; a trading tenancy at street level is a 🔴 fact **at screening**. Where only a suburb is held, suffix `— (insufficient info)`; **never 🟢** | 🔴 / 🟡 | `[R-SITE v1]`; skill Axis 3 / Axis 4 |
| **Me2** | **Is the site in a measurable state — and when:** cabinetry not installed, staged dwellings, a "site ready by" date, more than one visit implied → 🟡 (price the visits). Feeds C6's two-factor math: if the site is **not** measurable now, the ≈ 22-working-day clock applies | 🟡 | ⭐ trial |
| **Me3** | **Upper-floor measure logistics** (equipment carry, Prodim setup) → 🟡 | 🟡 | Skill Axis 4 upper-floor flag class |
| **Me4** | **Can we capture — dimension confidence (TIERED):** scanned or hand-sketched but dims complete and extractable → **no flag** (note only) · dims scaled from 1:100 or approximate → 🟡 · `?`-marked, TBC or **conflicting** dims → 🟡 (confirm at measure) · **no readable drawings → cite the Needs Info verdict** | 🟡 | `[R-DRAWINGS v1]`; skill dimension-gap class |
| **Me5** | **Template complexity:** curved walls, asymmetric fillers, window sills in stone → 🟡. Splays and curves are **owned by D5**, scribes by **Me8** — Me5 carries only the template-capture echo, same citation | 🟡 | Gate 1 flag set; ⭐ trial as a screening-time rule |
| **Me6** | **Multi-dwelling logistics:** 2+ dwellings or units → 🟡 (sequencing, mirror-image risk, staged handover) | 🟡 | ⭐ trial (MD-named) |
| **Me7** | **We don't measure at all — responsibility transferred:** Supply Only — the client or their cabinetmaker supplies final dims → 🟡, with a **written dims-responsibility line**. ⚠ Under `[R-SUPPLYONLY v2]` the Measure dimension does not apply in the usual way (we never attend site); what replaces it is the explicit record that **dimensional responsibility sits with the client**, so liability for a mis-measure is unambiguous before anything is cut | 🟡 | `[R-SUPPLYONLY v2]`; expectation-reset flag class |
| **Me8** | **Existing-surface capture — the SINGLE OWNER:** replacement-on-existing → cite the auto-decline (🔴; the substrate risk of working onto existing carcasses is the underlying *why* of that decline, and this echo is where it lives) · in-scope new work butting, scribed to, or matched against existing finished surfaces → 🟡 *"site-verify the existing datum"* | 🔴 / 🟡 | Skill CUSTOMER TYPE auto-decline (cite); 🟡 tier ⭐ trial |

### 3.5 MANUFACTURE (Ma)

| # | Criterion | Score | Basis |
|---|---|---|---|
| **Ma1** | **MACHINES — capability & capacity:** a piece the specified brand's slab format cannot yield → 🔴 (spec conflict — cite) · **a detail needing machine capability or first-of-kind programming the factory has no rule for → 🔴** *"a human accepts the known gap in writing before quote"* · **quartzite / granite scope → 🟡**, flag reads **verbatim**: *"hard stone — tooling cost, price with care"* (the priced tooling **number** is parked to the material deep-dives; the flag carries the judgment until the number exists) | 🔴 / 🟡 | `[R-BLOCK v3]` (layer 2); `[R-SUBTYPE v2]`; Technical Standards machine capabilities |
| **Ma2** | **TIME — machining hours:** > 10 pieces in one colour, mixed thicknesses of one colour, feature-dense pieces, multi-dwelling repeats → 🟡 (nesting and sequencing planned before programming) · vein-sequenced nesting, where M5 fires → echo, same M5 citation. Part-slab waste itself is **M4**, not here | 🟡 | ⭐ trial; M5 → Ma2 echo |
| **Ma3** | **CHIPS & CRACKS — defect exposure.** Re-baselined to **MATERIAL CLASS + geometry, NOT thickness** (the cutting tech gives a quality cut, so thin ≠ brittle): **porcelain + sintered** at any thickness (handling / fab / install fragility, edge chip) · narrow webs (< 150mm) around cutouts · cutout-dense pieces · soft naturals → 🟡 | 🟡 | Ledger #119; brand cutting rules; 50mm cutout-clearance rule |
| **Ma4** | **CUTTING & HANDLING risk in the factory:** oversize or heavy pieces against brand weight limits, long thin fragile pieces (sills, hob caps), 100mm+ laminated builds double-handled → 🟡. Forced joins are **owned by D10**; Ma4 carries the factory-handling echo, same citation | 🟡 | Technical Standards handling / transport / storage + slab weight table |
| **Ma5** | **Appliance cutout verification — always read the Appliance Library board LIVE (`5029694677`); never score from memory or a pasted snapshot.** A sink or cooktop model **absent from the library, or whose QC Status is not yet `Verified — Released`** (Requested / In Verification / Legacy — Needs Review) → **🟡, non-blocking at the LEAD stage** · **QC Status `Rejected — Do Not Use` → 🔴** *"never quote around a rejected cutout."* **Carve-out:** the **Ropox Flexi Electric is APPROVED** — not unverified, not first-of-kind; do not flag it | 🔴 / 🟡 | `[R-MA5 v3]`; `[R-BLOCK v3]`; `[R-REF v2]` |

**Ma5 order-gate consequence** `[R-MA5 v3]` — operative one-liner, cited: the lead-stage 🟡 becomes a **hard ORDER-GATE condition** — **the physical unit must be delivered TO STEEDFORM — the factory, NOT the client's site — BEFORE MEASURE**, and the gate cannot close until **either the library record reads `Verified — Released` or the unit is at SteedForm with a library record.** ⚠ **A supplier CAD is an INTERIM ARTEFACT ONLY** `[R-MA5 v3]`: it may be used to measure and program ahead of arrival, but it **never closes the gate** — a CAD cannot be dry-fitted. The parenthetical *"or its supplier CAD"* carried by older versions is struck. ⚠ **This sits ALONGSIDE `[R-EVIDENCE-BAR v2]`, which is not narrowed by it** — the evidence bar states which facts must exist at ORDER, this rule states where the unit must physically be; both apply. *(The wording "or the unit is on site" appears in older carriers; it is the exact error v2 corrected — a unit 40 km away at the client's site satisfies none of the measure / program / dry-fit / register requirement.)*

⚠ **Exact live label strings are `Verified — Released` and `Rejected — Do Not Use`.** `Released — Verified` is a **group title**, not a status label; matching on it silently fails. `Failed — Rework` is a **Verification-Stage** workflow state (`color_mm4zvvhg`), **not** the QC verdict — never cite it as the QC block. The block keys off `color_mm4zzgaq` QC Status.

### 3.6 INSTALL (I)

| # | Criterion | Score | Basis |
|---|---|---|---|
| **I1** | **GETTING INTO THE BUILDING:** carry paths, doorways, internal lifts (car dimensions vs piece sizes), site obstacles, restricted parking or loading, CBD site hours → 🟡. **PRIMARY HOME of the address lookup — assessed from the actual address, never reasoned from the suburb.** Cannot browse → flag the site assessment **outstanding**; never score 🟢 | 🟡 | `[R-SITE v1]`; skill Axis 4; Technical Standards §7 |
| **I2** | **TIGHT INTERNAL SPACES — the pantry case:** butler's pantries, WIPs, powder rooms — confined rooms where slab length approaches room width or diagonal → 🟡 | 🟡 | Skill Axis 4 room-geometry flag |
| **I3** | **TWO STOREYS + CRANE — BOTH 🟡, never 🔴:** stone above ground floor, crane / hoist / telehandler need, builder-provided vertical path → 🟡 **(FLAG UPFRONT — raise at first builder contact; cost priced at quote)**. *"Vertical by builder, horizontal by SteedForm"* is the standard term. **Needing a crane changes the price, never whether we want the job.** Stairwell carry is restricted to vanity-sized pieces; kitchen benchtops on upper floors likely require a crane or hoist | 🟡 | Q2 + Q3 decisions; skill Axis 4 |
| **I4** | **Site readiness dependencies:** install waits on other trades — cabinetry install, steel-frame acceptance checklist, substrate by others, fibre-cement for outdoor 12mm → 🟡 | 🟡 | Technical Standards §9.1.7; substrate rules (cite) |
| **I5** | **Trade coordination interfaces:** BBQ cabinetry comms, glazing channels on stone, gas access, plumber-dependent fit → 🟡 · **clad-fireplace install echo from D6** (vertical fixing — same citation) | 🟡 | Skill content rule 7; T-TECHNICAL-02; D6 echo |
| **I6** | **Out-of-area / Supply Only — scored by source rule 2b (§2.1).** Outside the service area with the **Supply Only conversion UNDECIDED → 🔴**, routing to **Needs Review, never a decline**; the citation is the Supply Only − FREIGHT conversion, not a disqualifier. **Conversion APPLIED (`Job Type = Supply Only [− FREIGHT]`) → 🟡**, line reads *"supply-only conversion applied — freight / packaging priced."* A **sea crossing** outside a confirmed zone → human escalation; packaging / freight priced. ⛔ **Out of area NEVER declines** at any km — it converts. ⚠ **Scope correction:** `[R-SUPPLYONLY v2]`'s *"Distance is NOT a risk and NOT a decline"* — the 646 km to Port Lincoln and the sea crossing to Kangaroo Island being the **client's** transport, never scored as SteedForm freight, access or lifting risk — is **scoped to the two CONFIRMED Supply Only zones** (**Port Lincoln 5606 · Kingscote / Kangaroo Island 5223**), and does **not** exempt all out-of-area work from scoring. **Out-of-area's authority to render that 🔴 is REGISTERED** `[R-AREA v1]` — it is a layer-1 blocking condition `[R-BLOCK v3]`, and once `Job Type` is set the lane drops to 🟡. **The Serviceable Areas board decides the zone wherever it lists the area; where it is silent the fallback is ~100 km ROAD distance from Wingfield, never straight-line. The 30 km / 60 km bands flag; they never decline.** **Inside a confirmed zone, once converted: the INSTALL dimension does not apply** — no install, no lifting, no site conditions, no install-readiness rating. ⛔ **CAD sign-off before manufacture is a hard gate** — with SteedForm's own measure out of the process it is the only check between the client's numbers and finished stone | 🔴 → 🟡 | `[R-AREA v1]`; `[R-SUPPLYONLY v2]`; source rule 2b; `07-service-area-and-site.md` §1 |
| **I7** | **Environmental exposure:** corrosion zone (coastal), alfresco exposure, thermal movement on outdoor frames → 🟡 | 🟡 | §9.1.6; corrosion-allowance precedent; ⭐ trial sentence |

#### The four site-lookup answers `[R-SITE v1]`

Cited, because the lane text above depends on them and they are reference detail, not the rule's canonical statement. Whenever a **street address** is held the lookup is **not optional**; its absence is a defect in the screen, not a gap in the enquiry.

1. **What is the building, and is it occupied?** Read the live tenant directory. A trading tenancy at street level makes it an occupied commercial building — a **C7 / Me1 fact established at screening**, not an assumption to confirm later.
2. **Where does the truck unload?** Street frontage, loading zone, dock or laneway — and whether a council permit, traffic management plan or insurance certificate is a **precondition with lead time**.
3. **Where does the truck GO during the works?** Check published clearances against the confirmed vehicle envelope — **Isuzu NNR 45-150: ~2.06 m wide, ~2.24 m cab, ≈ 2.5 m × ~3.0 m clear travel stowed, 4,500 kg laden.** **Most CBD car parks are ~2.0 m and will not take it.** *"The crew parks somewhere"* is not an answer: no vehicle on site means no tools, and no removal of packaging, offcuts or silica-controlled waste.
4. **What is the path from unload point to the work area**, measured against the **largest piece**, not the average one.

**At LEAD the site evidence bar remains suburb / postcode** `[R-EVIDENCE-BAR v2]` — this rule does not raise it. Where only a suburb is held, say so and suffix the access lanes `— (insufficient info)`. **Unknown is never 🟢.** Where the screen cannot browse, flag the site assessment outstanding and **refuse to score Install or Measure green.**

---

## 4. The distance-from-optimum lens (NOT the scorer)

> ⚠ **This section is a LENS for understanding a job's shape. It is NOT the scoring engine. The six-dimension strip in §3 is the operative scorer and WINS on any conflict.**
>
> ⚠ **The lens stands as written — and its future is under review.** The 3 September 2026 ruling round settled what D1 scores a 50–80mm build (§3.3) but expressly held over the wider questions it raised: whether Screening Philosophy is retired altogether, and whether all stone moves to a single ladder. Those are held for scoping as **`10-open-rulings.md` OR-38**. **Nothing in OR-38 may be applied as a rule; keep using this lens exactly as described below.**

**Green is not "safe" — green is OPTIMAL.** There is one setup that runs fastest through the factory, cheapest, with the least that can go wrong:

> **Engineered · single thickness · straight lines · flat colour · arris edge**

That is the same optimum the processing model reaches from the factory side (arris, single thickness, straight-line polish, inline only). **The risk map and the processing model are one statement read two ways** — *green = optimal to make · red = far from what we're built for.*

**Every red is one step away from that optimum. Accumulating reds is the signal.** That is a **gradient, not a gate**: no single red condemns a job; a *pattern* of reds says the work is drifting out of SteedForm's sweet spot, and someone should decide whether we want it.

### 4.1 The five axes

| Axis | 🟢 optimal | 🟡 step away | 🔴 far from it |
|---|---|---|---|
| **1. Material class** | engineered | sintered / porcelain | natural |
| **2. Build** | single thickness | mitred 40mm | 50mm+ |
| **3. Geometry** | straight lines | curves | boxed islands · large splashbacks · non-standard |
| **4. Colour / pattern** | flat colour | movement | vein |
| **5. Profile** | arris | pencil · CNC-tooling profiles | *(capability, not risk — see §2.2)* |

These are not new rules — they are the shape *behind* the ratified ones: axis 1 **is** ledger #131 · axis 5 **is** the profile capability matrix · axes 3–4 **are** the faceting and vein rules.

⚠ **The axes measure distance from the optimum; they do not set verdicts.** The distinction matters most on **axis 2**: a 60mm mitred engineered island edge sits at 🔴 *distance* here, yet it is **routine work we sell every week**. Reading axis 2 as a verdict trigger would push ordinary thick-edge jobs into Needs Review and jam the queue — exactly the "risk treated as capability" failure §2.2 warns about. **Use the axes to *understand* a lead's shape; use the strip to *score* it.** **The strip now has the rung that scores that example: D1 gives a 50–80mm engineered mitred build 🟡, on the cost difference** (§3.3, ruled 3 Sep 2026) — so the axis-2 🔴 and the D1 🟡 are the lens and the scorer saying different things about the same edge, by design.

### 4.2 What a human is actually deciding on a red

On a risk red the question is never *"can we?"* — it is **"do we want this one, at a price that respects what it costs us?"** The reds tell the human where the cost and the exposure sit:

| Reds on… | The exposure they point at |
|---|---|
| **Axes 1–2** | **Cost and fabrication** — hard-stone tooling, hand-finish above 80mm, breakage / recovery contingency on naturals |
| **Axis 3** | **Install** — site glue-up, field joins that cannot be dressed after, crew allocation |
| **Axis 4** | **Client expectation** — vein match, faceted vs polished appearance: the outcomes that get disputed at handover |

**A job red on one axis is usually a good job priced correctly. A job red on four is a job that will consume estimating, factory, install *and* relationship capacity at once — and that is the pattern that says *not for us*.**

### 4.3 How the lens reaches the board

- **Screening verdict is unchanged:** any red → **Needs Review**, never an auto-decline. A human sees it. Ambers never escalate.
- **Pricing:** the red *count* is also a pricing signal — worst-of throws away the difference between one red and four. It feeds the labour bands and the factory-vs-install cost split.

---

## 5. Emitting the strip

### 5.1 When and where

**When:** the risk block is produced **during** screening — after the flags, before the verdict write — wherever a screen runs. **Zero extra reads:** the criteria are computed from facts the screen has already established.

⚠ **Enforcement today:** the pipeline sweeps that previously emitted the strip were **retired 26 Aug 2026** and are no longer carriers. Screening enforcement lives in the `estimator-screening` skill and Claude deep scans until the Deep Screen app takes it. **Nothing screens automatically in the interim** — that is by design, not a defect.

**Where:** the `⚠ Risk Profile` **`long_text`** column on the **current** Leads board `5029570131`, written as a **whole-column REPLACE on every screen and re-screen** — current state, not an archive. ⛔ **The retired Leads board `5029570430` and its `long_text_mm5ddgqa` are historical only and must never be written** `[R-INTAKE-ID v3]`. *(The live column ID is still not pinned. The CRM boards could not be reached, so no column identifier in this document has been verified against the live board — `10-open-rulings.md` **OR-26**. A tag check is not an identifier check: confirm the id against `08-board-and-column-registry.md` before writing.)*

**Update discipline:**
- **Version-stamp every block** with the rules version it was scored under. A strip whose stamp is older than the current rule version is **stale by definition** and must be re-screened when a rule bumps `[R-RESCREEN v1]`.
- **Strip-change update stamp:** when a regeneration *changes* the strip, post an update on the lead — old → new strip, plus which lane moved and why. History lives in the timeline; the column stays current state.
- **4+ amber lanes** → the daily digest carries *"heavy-amber lead — estimator eyes before quote."*
- **At conversion: translate, never copy.** The 🟡 lines become Deal Desk CHECK / INCLUDE / CONFIRM prompt items — the strip is a triage surface, the Deal Desk is the work surface. No fourth rendering of the same risk knowledge.

### 5.2 The fixed format (machine-parseable, 7 lines)

```
RISK: C🔴 M🟡 D🟡 Me🟡 Ma🟢 I🟢  (<standard version> · <date> · rules <current rules version>)
C 🔴 — retail-direct, cabinetmaker unconfirmed (CUSTOMER TYPE → verdict); unrated account, first job (A/B/C pending bootstrap)
M 🟡 — Smartstone sintered = class amber [R-M1 v2]
D 🟡 — splayed corner (D5) + 1400mm splashback (D9)
Me 🟡 — hand sketch, '?' 640mm dim (dimension-gap class, Me4)
Ma 🟢 — routine
I 🟢 — ground floor assumed (— insufficient info on access)
```

⚠ **The M line above is the corrected form.** The source standard's §4 example prints `M 🟢 — Smartstone sintered = baseline (Q15)`; that is the reversed Q15 position, superseded by `[R-M1 v2]` — **porcelain and sintered are 🟡.** Any emitter or example still printing a sintered material at `M 🟢` is stale.

### 5.3 Parse contract

| Rule | Requirement |
|---|---|
| **Line 1** | Matches `^RISK: ` + six lanes in the **fixed order C · M · D · Me · Ma · I** + the parenthesised version stamp |
| **Lines 2–7** | The six dimension lines, **same fixed order, one each** |
| **Insufficient info** | `(insufficient info)` is a **SUFFIX on a scored line, never a line replacement** — all seven lines are always present |
| **Invalid block** | A block failing this contract — missing lines, reordered lanes, unanchored header — is treated as **ABSENT**. **Regenerate it whole; never partially parse or patch it.** |

### 5.4 The 1,800-character budget `[R-LONGTEXT v2]`

The strip is written to a monday `long_text` column, so the truncation rule governs it. Operative one-liners, cited:

- **`long_text` silently truncates at ~2,000 characters and the read-back hides it** — the write returns SUCCESS, the value simply ends mid-word, and the truncated value is what you read back. So it looks correct.
- **BUDGET BEFORE YOU WRITE.** If the composed value would exceed **1,800 characters**, do not write it whole — write a trimmed version ending `… full detail in updates` and post the remainder as an **item update** (updates have no cap).
- **Compact, don't drop:** keep every ACTIVE flag and the verdict reasoning; move superseded or historical entries into an item update, leaving a one-line pointer in the column.
- **Verify by re-reading and comparing `len()` against the cap.** Checking only the final line is **not** a truncation check. **A value of exactly 2,000 characters is a truncation signature, not a coincidence** — treat it as data loss and digest it.
- **Watch bands:** **AT CAP (= 2000, already lost)** · **CRITICAL (≥ 1900)** · **WATCH (≥ 1750)**. At 1900+, compact in that run: snapshot the full text to an item update first, then rewrite the column as active flags + verdict reasoning with a pointer.

⚠ **Strips grow every run, so this worsens with time, not improves.** A live example at registration: the `⚠ Risk Profile` value on the St Georges lead stood at **1,943 characters** — inside the CRITICAL band.

### 5.5 Known gap — the strip has no pattern summary

**The strip prints six dimension lines and never summarises the pattern.** There is **no red count, no amber count and no fit line.** If accumulation is the signal (§4), the estimator should see *"4 reds — drifting, do we want this?"* at a glance rather than reading six lines and forming an impression.

**Status: a proposed BUILD ITEM — add a count / fit line to the strip. It is not implemented and must not be described as if it were.** The only accumulation mechanism that exists today is the **4+ amber daily-digest line** (§2.1 rule 4), which is a digest mention, not a line in the strip, and counts ambers only.

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed every other item this document used to carry — OR-01, OR-02, OR-03, OR-06, OR-07, OR-13, OR-22, OR-23 and OR-37 are **ruled**, and their positions are now stated plainly in the sections above. Three items remain:

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-38** | The wider implications of the OR-07 ruling, **held for scoping**: is the Screening Philosophy / distance-from-optimum lens retired, and does all stone move to one ladder? The owner's notes *"screening philosophy now redundant"* and *"all stone to follow same rules"* are **wider than the question that was asked and are NOT ruled** | §4 — the lens stands and is used exactly as written until this is scoped |
| **OR-20** | Whether the screen quotes the **10–12 day SLA** or the **14–16 day actual** to a customer. The internal two-factor math is unaffected | §3.1 C6 — the earliest-realistic-install-date flag |
| **OR-26** | The CRM boards could not be reached, so **no column identifier has been verified against the live board** | §5.1 — the `⚠ Risk Profile` column id, and every board identifier cited in the ladders |

**Two live defects, recorded and not fixed** — these are defects in the emitters, not open questions: **DEF-01**, capability and risk still render as one undifferentiated 🔴 (§2.2); **DEF-04**, the strip has no red/amber count line (§5.5).
