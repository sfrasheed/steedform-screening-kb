# 06 — Evidence Requirements

**Status:** Active. Subordinate to `01-rule-register.md`: where this document and the Rule Register disagree, the Register is correct and this file is stale.
**Owner:** MD
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns:** what information must be present for a screen to reach a verdict; the LEAD / ORDER evidence bars and their asymmetric consequences; the drawings gate; the customer information requirements sent to an incomplete enquiry; what appliance evidence is required and where it is read from; the order-gate appliance delivery condition; the alfresco shadowline as a site-measure readiness precondition; the board-not-document principle.
- **Does not own:** the canonical statement of any rule (that is `01-rule-register.md`); the risk-scoring dimensions and andon strip; the verdict-precedence ladder; pricing; fabrication capability; the appliance verification workflow itself (stages, release automations, immutability) beyond what a screen must read.

---

## What this document decides

A screen reaches a verdict only when the facts it needs are actually present at the required standard of evidence. That standard depends on which of two gates is running — LEAD or ORDER — and the gate is told to the screen, never worked out by it. At LEAD, thin-but-generic evidence is priced and flagged; it never changes a verdict. At ORDER, a gap is blocking and nobody may waive it. Drawings are the one input that is mandatory at both gates for every tier. Appliance release verdicts are read off a board, never off a document.

---

## 1. The two-gate model `[R-EVIDENCE-BAR v2]`

**One criteria set, two evidence bars.** The gate decides what counts as satisfying a fact — never whether the fact matters. Both gates ask the same question (*is this project right for SteedForm*) with an identical fact vocabulary. Only the standard of evidence changes.

⛔ **THE GATE IS AN EXPLICIT INPUT AND IS NEVER INFERRED.** A screen that does not know which gate it is running is the failure that costs a slab: an Order screened at LEAD evidence commits on "white stone TBC". If the gate is not supplied, do not guess it — ask.

### The two bars

| Fact | LEAD bar — enough to price and quote | ORDER bar — enough to commit to manufacture |
|---|---|---|
| Material / colour | brand, range, category or commercial tier `[R-MATERIAL-TERMS v1]` | exact colour name + finish `[R-MATERIAL-TERMS v1]` |
| Thickness | nominal, by area | confirmed per piece |
| Edge profile | generic (pencil, mitred 40) | exact profile, material-checked against the Capability Matrix **and against `Print Construction` `color_mm6hz0dd`** `[R-PROFILE v5]` |
| Cut-outs | count + generic type | model number + Appliance Library link + QC Status |
| Appliances / sinks | generic description | model number, mounting type, linked Library record **+ QC Status** |
| Site | suburb / postcode | full SITE street address; **plus the DELIVERY address whenever it differs from site** (the supply-only / freight case, `[R-SUPPLYONLY v2]`). Billing is an accounts field and is never a screening bar |
| Drawing revision | any current set | the accepted revision, matching the quote baseline |

✅ **RULED 3 September 2026 — the Cut-outs and Appliances/sinks ORDER bars no longer differ** `[R-EVIDENCE-BAR v2]`. The Appliances/sinks row now carries **QC Status**, matching the adjacent Cut-outs row. The two rows had said different things inside this file, which is why "the Register wins" could not adjudicate between them. **Both rows require QC Status at ORDER**, and QC Status is resolved from the Appliance Library board, never asserted from a document (§4, §7).

### The two asymmetric consequences

| Gate | A gap below the ORDER bar is… | Who may waive it |
|---|---|---|
| **LEAD** | 🟡 — priced or confirmed. **Never a verdict change.** Generic terms alone must **never** produce Needs Info, Needs Review or Unqualified `[R-EVIDENCE-BAR v2]` `[R-MATERIAL-TERMS v1]` | n/a — there is nothing to waive; the job is to price an allowance |
| **ORDER** | **BLOCKING.** The order proceeds when the evidence exists and not before | **Nobody.** Not the screen, not a reviewer, **not the MD.** The release valve is obtaining the fact, never accepting its absence `[R-EVIDENCE-BAR v2]` |

**Why the asymmetry exists:** at LEAD, demanding exact specification jams the queue with Needs Info on work SteedForm wants. At ORDER, accepting an allowance is how a remake happens. The same fact judged at the wrong bar fails in both directions.

### This bar sits ALONGSIDE the order-gate appliance condition — it does not narrow it

⚠ **`[R-EVIDENCE-BAR v2]` and `[R-MA5 v3]` are two different requirements and BOTH apply.** The bar states **what facts must be present** at ORDER — model number, mounting type, linked Library record, QC Status. `[R-MA5 v3]` states **where the unit must physically be**, and when: at SteedForm, before measure (§5). **Satisfying the bar does not satisfy `[R-MA5 v3]`.** A complete evidence package on a unit that is still at the supplier has cleared one requirement and not the other.

### Consequences a screen must apply

- **Generic material terms are sufficient at LEAD.** An evidenced brand, range or commercial tier supports an allowance while exact colour remains TBC; exact colour/revision is required at Order commitment where the product requires it `[R-MATERIAL-TERMS v1]`. `M2`/`M4` are supplier commercial range labels, and bare `Zenith` is the engineered-stone brand — neither, alone, may ever trigger Needs Info, Needs Review or Unqualified.
- **A generic edge description is sufficient at LEAD.** "Pencil" or "mitred 40" meets the LEAD bar; the exact profile code is an ORDER-bar fact.
  **Stale — do not apply.** `Sales Qualification.md` Stage 3 makes exact material selection ("not 'something white' — the actual product") and a specific edge code **blocking at lead stage**. That is superseded and must not be applied: it is precisely the queue-jamming failure `[R-EVIDENCE-BAR v2]` and `[R-MATERIAL-TERMS v1]` were written to stop.
- **Sink and cooktop models are not "confirm at measure if needed".** `Sales Qualification.md` Stage 3 lists them as "nice to have but not blocking … can be confirmed at measure if needed". That is superseded and unsafe: it is directly contrary to the ORDER bar above and to the deliver-**before**-measure order gate at §5 `[R-MA5 v3]` `[R-EVIDENCE-BAR v2]`. At LEAD a generic description is enough; at ORDER the model, mount type and Library link are required, and an unverified unit must be at SteedForm before measure.
- **An ORDER screen requires the accepted quote evidence package as its baseline.** If the baseline is absent or stale: **keep capturing, refuse to judge, and say so** `[R-EVIDENCE-BAR v2]`. An Order screen without a baseline has not checked the thing it exists to check.

---

## 2. Drawings `[R-DRAWINGS v1]`

**Drawings are MANDATORY at screening — all tiers, no exceptions, including A-tier.** An A-tier account waives the minimum-job rule; it does not waive drawings.

| Question | Position |
|---|---|
| What if there are no readable plans? | After **every** extraction attempt — OCR, vision, opening the portal or attachment — the verdict is **Needs Info**, and **never Qualified** `[R-DRAWINGS v1]` |
| What does "readable" mean? | **The takeoff can actually be done from them.** Not merely that a file exists: a file column holding an unopenable, blank or illegible attachment is the same as no drawing |
| May a missing dimension be inferred? | **Never.** An assumed dimension becomes a cut piece |

### Needs Info and Needs Review are different verdicts and go to different people

| Route | Trigger | Verdict | Who acts |
|---|---|---|---|
| Drawings gate `[R-DRAWINGS v1]` | no readable plans after every extraction attempt | **Needs Info** | the **client** must supply something |
| Blocking list `[R-BLOCK v3]` | any item on **either layer** of the closed blocking list — the layer-1 base list, or the six-rule layer-2 addition set | **Needs Review** | a **human at SteedForm** decides |

⛔ **Do not collapse the two.** They are distinct verdicts with distinct owners and distinct next actions.

⚠ **The blocking list has TWO layers and both are closed** `[R-BLOCK v3]`. **Layer 1** is the base list applied since screening began and registered on 3 September 2026: occupancy · `Do-Not-Quote` or an unresolved account match · out of area while the Supply Only conversion is undecided · spec conflicts · below the one-slab minimum (non-A-tier) · the natural-stone rule set · unknown-entity checks. **Layer 2** is the 20 July 2026 addition set — **six** rules, and the one this document reads most often is **appliance QC Status `Rejected — Do Not Use`** (§4). ⛔ **"Seven" is stale wherever it appears**, and "curves >40mm" was struck from layer 2 on 23 July 2026 `[R-D5 v8]` — it must never be re-added.

**Precedence note:** client fit is decided before drawings are considered. An unresolved client fit is **Unqualified** even when the drawings are complete and technically clean, and drawing presence or quality must never upgrade it `[R-CLIENTFIT v1]`.

### Dimension confidence, once drawings are readable

Readability is the gate; dimension confidence is scored on top of it. Tiers carried from `Lead Risk Assessment Standard.md` Me4 (REFERENCE carrier, expanding `[R-DRAWINGS v1]`):

| Evidence | Score |
|---|---|
| Scanned or hand-sketched, but dimensions complete and extractable | no flag — note only |
| Dimensions scaled from 1:100, or approximate | 🟡 |
| `?`-marked, TBC, or conflicting dimensions | 🟡 — confirm at measure |
| No readable drawings | not a score — the `[R-DRAWINGS v1]` **Needs Info** verdict |

---

## 3. The customer information requirements

Source: the **SteedForm Outlet Customer Information Requirements** PDF, **Rev2, 27 June 2024**, attached to `T-INFO-01 — Information Required Before Quoting` (`Communications.md`). The itemisation below exists only in `Sales Qualification.md`, a document being retired; it is captured here so it survives.

The PDF asks the customer to provide:

| # | Item | Detail |
|---|---|---|
| 1 | **Customer name and project address** | — |
| 2 | **Dimensioned cabinetry drawings** | Floor plan with dimensions. The PDF carries a worked example of what "good" looks like. Must be attached to the email response |
| 3 | **Photographs of completed cabinetry** | **The cabinetry must already be professionally installed.** Photos confirm the site is ready for measure |
| 4 | **Cutout specifications** | Cooktop model, sink or vanity basin model, **and all tapware**. Spec sheets must be attached |
| 5 | **Builder or joiner details** | Business name, contact name, phone number — who is coordinating the project, and a trade contact for site logistics |

**Hard disqualifier stated in the PDF:** if the cabinetry is existing, part of a DIY kit, re-used or relocated, **SteedForm will not perform the installation** — the tolerances required for quality stone installation cannot be met on non-professional cabinetry. The PDF states this as a polite decline. (Corroborated in `SteedForm Identity.md`.)

**SteedForm's stated commitment:** the PDF promises **a response within two business days** to confirm whether SteedForm can assist with the project (`Sales Qualification.md`). The `T-INFO-01` template body phrases the same two-business-day commitment as a quote turnaround once the complete set is received (`Communications.md`); both wordings are in live use.

**How a screen uses this list:** identify **which of the five items are missing** from the enquiry and request **only what is needed**. Do not send the full list back at a customer who has already supplied four of five items.

**Note.** Item 4 sets the *request*, not the ORDER bar. Receiving a spec sheet does not establish an appliance's QC Status — see §4 and §7.

---

## 4. Appliance evidence and the verification gate

**QC Status is the operative release verdict and it is resolved from the Appliance Library board `5029694677`, column `color_mm4zzgaq` — never asserted from a document** `[R-EVIDENCE-BAR v2]`. A screen **flags an appliance for lookup**; it never reports a release verdict it read in a PDF, a spec sheet, an email or a pasted snapshot. Read the board **live** every time (MD directive, 25 Jul 2026 — *"always refer to boards"*): if a model is not on the board, that is a finding, not a licence to assume.

### The live QC Status labels — exactly these five

| QC Status | Screening consequence |
|---|---|
| `Verified — Released` | Cutout is trusted data; the model has been measured, programmed, cut and dry-fitted once at SteedForm. **A released record means the physical unit is not required on site** (`Appliance Verification Standard.md`) |
| `In Verification` | Not yet released → 🟡 at LEAD, non-blocking `[R-MA5 v3]`; an ORDER-gate condition — see §5 |
| `Requested` | as above |
| `Legacy — Needs Review` | as above |
| `Rejected — Do Not Use` | 🔴 **BLOCKING — never quote around a rejected cutout** `[R-MA5 v3]` `[R-BLOCK v3]`. Routes to **Needs Review** |

**Carve-out:** the **Ropox Flexi Electric is APPROVED** (23 Jul 2026) — it is neither unverified nor first-of-kind. Do not flag it `[R-BLOCK v3]`.

✅ **The Appliance Verification Standard is RATIFIED (3 September 2026) and its DRAFT banner is dropped.** It is a **legitimate REFERENCE carrier** of `[R-EVIDENCE-BAR v2]` and `[R-MA5 v3]`, and may be cited as operative for the verification workflow it owns. The former caveat — that a document headed *"DRAFT for MD review"* was carrying a LAW, in a carrier taxonomy with no DRAFT class — **no longer applies and must be removed wherever it is still carried.** Ratification does not change the standard's rank: as a carrier it explains and expands, it never authors, and it may never contradict the Register (§5 records the one clause where it does).

### Two label traps that fail silently

| Trap | What it actually is | Consequence of matching on it |
|---|---|---|
| `Released — Verified` | a **GROUP TITLE** on the board, not a status label | the match silently fails — nothing errors, the appliance simply never reads as released `[R-MA5 v3]` |
| `Failed — Rework` | a value of the **separate Verification-Stage column** `color_mm4zvvhg` — the stage a unit passes through after a failed dry-fit | it is **not a QC verdict**; never cite it as the QC block. The QC verdict lives only in `color_mm4zzgaq` |

The gate keys off the **release verdict (QC Status)**, not the workflow stage.

### What sits behind a `Verified — Released` record

For context when reading the board — a release requires, on the library record: Cutout Spec (dimensions/offsets from the dry-fit), Program/Template Ref, **Dry Fit Result = Pass** with date, Dry Fit Photo, Approved By (a named QC approver — an approval is a signature, not a checkbox), Spec Sheet file, Source Job. Release is impossible unless Dry Fit Result = Pass, and a manual flip of QC Status without the workflow auto-reverts to `Legacy — Needs Review` (`Appliance Verification Standard.md`). A screen does not run this workflow; it reads its verdict.

---

## 5. The order-gate appliance condition `[R-MA5 v3]`

An appliance or sink **absent from the Appliance Library, or not `Verified — Released`, scores 🟡 at the lead stage** — non-blocking. It does **not** stay a soft note downstream. Per #54/#91 (ratified 21 Jul 2026) it becomes a **hard ORDER-GATE condition**:

> The unit must be **physically delivered TO STEEDFORM — the factory, NOT the client's site — BEFORE MEASURE**, and the gate cannot close until either the library record reads `Verified — Released`, **or the unit is at SteedForm with a library record** `[R-MA5 v3]`.

**Why the location matters:** we must measure, program, dry-fit and library-register the unit. A unit 40 km away at the client's site satisfies none of that, so **"on site" is not an acceptable gate condition**.

### A supplier CAD is an INTERIM artefact only `[R-MA5 v3]`

✅ **RULED 3 September 2026.** The appliance manufacturer's CAD **may** be obtained and used to **measure and program ahead of the unit's arrival** — that is useful work and it should be done. **It never closes the gate.**

| | Position |
|---|---|
| What a CAD may be used for | measuring and programming ahead of the unit arriving at SteedForm |
| What a CAD can never do | **close the order gate.** A CAD cannot be dry-fitted, and release requires a **dry-fit pass** |
| What is still required | **the physical unit, at SteedForm, before measure** — unchanged |

⛔ **Do not read "we have the CAD" as "the gate is satisfied".** The parenthetical *"(or its supplier CAD)"* that formerly sat inside the delivery clause above is **struck**: it opened a door the rule's own closing conditions never included, in a sentence written for physical units. The closing conditions are `Verified — Released`, or the unit at SteedForm with a library record — a CAD is neither.

### The bar and the gate are separate requirements

⚠ **`[R-EVIDENCE-BAR v2]` SITS ALONGSIDE this rule; it does not narrow it.** The bar (§1) states what facts must be present at ORDER — model number, mounting type, linked Library record and QC Status. **This rule states where the unit must physically be, and when.** Both apply, and clearing one is not clearing the other.

### The stale wording to reject on sight

| Stale carrier text | Correct position |
|---|---|
| "…the gate cannot close until the record is Verified — Released **or the unit is on site**" — still present in `Lead Risk Assessment Standard.md` Ma5 and `Appliance Verification Standard.md` | "…or **the unit is at SteedForm with a library record**" `[R-MA5 v3]` |

This is the exact v1 wording that the 27 July 2026 correction (registered as `R-MA5 v2`, carried forward unchanged into `[R-MA5 v3]`) exists to kill; v1's "to site" was governing through the master skill, which is why the correction was registered. Ma5 contradicts itself inside a single sentence ("not to the client's site … or the unit is on site") and the Appliance Verification Standard propagates the wrong half. Neither carrier's stale clause has any force.

### May an order lock with an unverified appliance?

**No — the ORDER-gate condition above governs.** `Appliance Verification Standard.md` carries a 7 Jul 2026 bullet stating an order "may lock" with unverified appliances under a "verification required before production" stamp, and flags its own three-way conflict as unresolved. That leg **is** resolved, against the bullet, on four independent grounds:

| Evidence | Effect |
|---|---|
| `01-rule-register.md` is AUTHORITATIVE — "this file WINS … the other file is stale" | `[R-MA5 v3]` governs |
| Dates | the location correction is 27 Jul 2026 (`R-MA5 v2`) and the current statement is 3 Sep 2026 (`R-MA5 v3`); the bullet is 7 Jul 2026 |
| `R-MA5` does not appear in the Register's `## Superseded` section | `[R-MA5 v3]` is live LAW, not retired |
| Carrier class | the Appliance Verification Standard is a **carrier** of `[R-EVIDENCE-BAR v2]`, not an authoring source — a carrier "must never contradict the canonical statement" |

The standard never cites `[R-MA5 v3]`, which is why it read the question as open. Apply `[R-MA5 v3]`. Until obtained, **fail toward the flag**: obtain the link *and* the verification, and escalate rather than lock.

*(The second leg of that same conflict — the two differing `R-EVIDENCE-BAR` rows — is **closed**. Both rows now require QC Status at ORDER `[R-EVIDENCE-BAR v2]`; see §1.)*

---

## 6. The alfresco shadowline — a measure-readiness precondition `[R-ALFRESCO v1]`

**On an alfresco or barbecue scope, the cabinetmaker's shadowline must be installed BEFORE site measure can be completed.** This is an evidence and readiness precondition, not a preference, and it belongs in this document because it is a **fact that must exist before the measure happens** — the same class of requirement as an unverified appliance being at SteedForm before measure (§5).

| Item | Position |
|---|---|
| What it is | a shadow line **12 mm thick × 50 mm wide** — 12 mm compact, edged MDF or painted edge |
| Who installs it | the **cabinetmaker**, not SteedForm |
| When | **in place before site measure can be completed** |
| When it is not required | where the benchtop is **thicker than 40 mm** |
| When to raise it | **at first builder contact** — not at booking, and never on the day |

⛔ **A measure that arrives to no shadowline is a wasted trip.** Flag the requirement in the first builder conversation on any alfresco scope, so the readiness fact exists before a measure slot is spent on it.

⚠ **Do not confuse the shadowline with the fibre cement.** The 12 mm figure is the **cabinetmaker's shadowline**; the fibre cement behind it is **6 mm or 9 mm**, selected by the gap between stone and carcass. A "12 mm fibre cement sheet" is a **retired offering** and conflating the two is the error that has been travelling through the corpus `[R-ALFRESCO v1]`. The alfresco material and substrate rules themselves live in `05-material-and-capability.md`; only the measure precondition is recorded here.

---

## 7. Evidence that must come from a board, never a document

**Two facts are resolved from the board and never asserted from a document** `[R-EVIDENCE-BAR v2]`: **appliance and sink QC Status** on Appliance Library `5029694677`. A screen flags them for lookup; it never reports a release verdict it read in a PDF.

The principle generalises, and it fails **closed**:

| Situation | Required behaviour |
|---|---|
| A spec sheet, PDF, email or pasted snapshot asserts an appliance is verified | Do not accept it. Look up `color_mm4zzgaq` on `5029694677` |
| The model is not on the board | That is a **finding**, not permission to assume. 🟡 at LEAD; an ORDER-gate condition per §5 |
| The screen cannot read the board | Do not substitute memory or a document. Flag the lookup as outstanding and do not report a release verdict |
| The ORDER baseline (accepted quote evidence package) is absent or stale | **Keep capturing, refuse to judge, and say so** `[R-EVIDENCE-BAR v2]` |
| The Rule Register cannot be read | **KEEP CAPTURING, REFUSE TO JUDGE.** Continue intake so no enquiry is lost; issue no verdicts; notify Matthew. **Never fall back to inline copies** of a rule |

**The direction of failure is fixed: when the data is missing, fail toward the flag, never toward the promise.**

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed every item this document used to carry — **OR-04** (the Appliances/sinks ORDER bar now includes QC Status, §1), **OR-05** (a supplier CAD is interim only and never closes the gate, §5), **OR-18** (the alfresco figures, now settled by `[R-ALFRESCO v1]`, §6) and **OR-31** (the Appliance Verification Standard is ratified, §4) are **ruled**, and their positions are stated plainly in the sections above.

**One item remains, and it is not a question about evidence — it is a question about identifiers:**

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-26** | The CRM boards could not be reached on 3 September 2026, so **no board or column identifier has been verified against a live board** — including Appliance Library `5029694677`, QC Status `color_mm4zzgaq` and Verification Stage `color_mm4zvvhg` | §4, §5 and §7 — every live lookup this document instructs. **A tag check is not an identifier check**: see the warning at the head of `08-board-and-column-registry.md` before relying on an id |

**Also unresolved and scoped elsewhere:** **OR-38** — whether the Screening Philosophy / distance-from-optimum lens is retired and all stone moves to one ladder, **held for scoping**. It does not touch the evidence bars, and nothing in it may be applied as a rule.
