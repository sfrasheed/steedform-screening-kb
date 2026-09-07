# 05 — Material & Capability

**Status:** v1.0 — clean extraction for the Deep Screen app. Reference layer; the Rule Register (`01-rule-register.md`) is authoritative over everything here.
**Owner:** Matthew Rasheed (MD) — capability rulings. Technical Standards / Edge Profile Capability Matrix are the reference carriers.
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns** — what SteedForm can and cannot make: material classes and their scoring inputs, print construction, the edge profile × material capability matrix, thickness and build rules, curves and faceting, the NOT-OFFERED list, the capability-vs-risk separation, the Dekton phase-out, vein matching, and material vocabulary. This is the *"is the JOB right for us"* half of screening.
- **Does not own** — the canonical statement of any rule (that is `01-rule-register.md`); customer/account fit, tiering and A/B/C rating; pricing, markup and cost bands; site access, install and measure standards; intake, board IDs and CRM write mechanics; appliance verification beyond the mounting/cutout facts that bear on capability.

---

## What this document decides

Whether a specified job can physically be made by SteedForm, and if so how far it sits from the optimum. It answers four questions in order: *what class is the material* (read live, never inferred), *how is it constructed* (face-printed or full body — this, not class, governs the pencil prohibition), *does the specified profile × material × thickness combination exist*, and *is what remains a capability stop or a risk call*. Capability stops cannot be human-called; risk reds are a human decision where both answers are valid. **What the screen then DOES with a NOT-OFFERED item is ruled per item — DECLINE or RESET, never interchangeably** `[R-SCOPE v2]` (§6). A DECLINE item is not a specification to be corrected; a RESET item is not a decline.

---

## 1. Material classes and scoring

**Material class is read LIVE from the Materials Library `5029570546`, column `color_mm4qt817` Material Type — never inferred from a brand or colour name** `[R-M1 v2]`. The class score is **engineered 🟢 · porcelain + sintered 🟡 · natural 🔴** `[R-M1 v2]`; this supersedes the earlier Q15 position that porcelain/sintered dropped to green.

**CERAMIC scores as porcelain / sintered — 🟡** `[R-M1 v2]` (ruled 3 September 2026). The three-class ladder had no rung for ceramic, so a ceramic material had no score at all.

| Class | Score | What it means at screening |
|---|---|---|
| **Engineered** (current compliant lines) | 🟢 | Fullest capability. Laminable, mitrable, all profiles subject to print construction (§2). Old high-silica engineered stone is banned/gone from AU. |
| **Porcelain** | 🟡 | Quotable, not "all-clear" — handling/edge/install fragility (#119). Never laminated. |
| **Sintered** | 🟡 | As porcelain — surface-decorated, follows the porcelain rules. Never laminated. |
| **Ceramic** | 🟡 | **Scores on the porcelain / sintered rung** `[R-M1 v2]`. **Vasari is ceramic** — that is its class of record, and the Materials Library value for Vasari items is to be set to match. Never laminated. |
| **Natural** | 🔴 | Variation, vein-match exposure, human sign-off. Forks further on granite vs non-granite `[R-SUBTYPE v2]` and on marble vs hard natural (§5). Every branch is **Needs Review, never an auto-decline** `[R-NATURAL v1]`. |

**The natural-stone fork.** `[R-SUBTYPE v2]` — the verdict forks on granite vs non-granite, read from `dropdown_mm4rq7jd` Stone Sub-Type, populated on only **3 of 392** materials as at 18 Aug 2026. A blank sub-type is not a licence to guess: score the hard-stone tooling flag as if it were granite **and** always add the visible flag `"⚠ Stone Sub-Type not recorded — confirm granite vs non-granite before quoting."` Never resolve the fork from the brand or colour name — dolomite is routinely sold as quartzite, which is exactly why the board column exists.

**Natural stone risk review (locked April 2026, Technical Standards §1).** Every natural item must be assessed on five points before a verdict is assigned; a category-level "natural stone REVIEW" tag is not sufficient. The brief must record: geological category · Mohs hardness · acid reactivity · porosity/sealing burden · application appropriateness.

| Situation | Verdict (Technical Standards §1) |
|---|---|
| Soft natural (Mohs ≤ 5 — marble, dolomite, travertine, limestone, onyx) in kitchen / scullery / coffee station / heavy-wear wet area | **🔴 Needs Review — NEVER an auto-decline** `[R-NATURAL v1]`. ⛔ **Technical Standards' DECLINE for this condition is SUPERSEDED** (ruled 3 September 2026) |
| Soft natural in dry decorative application (WIR, feature wall, vertical cladding) | **ASSESS** — case-by-case; slab selection + maintenance briefing required |
| Hard natural (Mohs ≥ 6 — quartzite, granite, hard serpentinites) in any standard application | **ASSESS / PROCEED** — single thicknesses, handled selectively |
| Bespoke composite / artisan work (marble + cement, terrazzo, hand-carved integrated basins, decorative offcut pieces) | **DECLINE** |

> ⛔ **RULED, 3 September 2026 — soft natural in a kitchen or wet area is 🔴 Needs Review, NEVER an auto-decline** `[R-NATURAL v1]`. Technical Standards' DECLINE for that condition is **superseded**; a human makes the call.
>
> **The five-point risk review above remains mandatory** — geological category · Mohs hardness · acid reactivity · porosity/sealing burden · application appropriateness — and the brief must record all five. What is no longer applied is the automatic DECLINE verdict. **Bespoke composite / artisan work is unaffected and remains a DECLINE.**

**Dolomite — application-dependent rule (locked April 2026, SteedForm Identity).** Calcium-magnesium carbonate, Mohs 3.5–4, acid-reactive, porous, frequently mis-sold as "quartzite"; its performance category sits with marble, not quartzite. **In any kitchen, scullery, coffee station or heavy-wear wet area → 🔴 Needs Review** — dolomite is a soft natural (Mohs ≤ 5), so `[R-NATURAL v1]` governs it and the former DECLINE is **superseded**. **ASSESS in dry decorative applications**, unchanged. Frame the substitution conversation as a performance/maintenance mismatch with client expectations, not as a fabrication capability gap.

**Brands in active use (as at April 2026, Technical Standards §1)** — reference only; the class still comes from the board `[R-M1 v2]`.

| Brand | Stated type | Notes |
|---|---|---|
| Zenith Surfaces | Engineered | Dominant by volume. Indoor only. **Full-body throughout** — no printed ranges (corrected 7 Sep 2026). |
| Caesarstone ICON | Advanced Mineral (silica-free), 20mm only | Indoor only; 40mm "thick" tops are laminated build-ups. |
| Neolith | Sintered | **Preferred sintered product.** Outdoor approved. |
| Caesarstone Porcelain | Porcelain | Outdoor approved with conditions. |
| Smartstone Sintered | Sintered | Second preference after Neolith. **Smartstone is sintered-only as a brand** — no engineered, no porcelain, no quartz variant. Any spec naming "Smartstone" reads as Smartstone Sintered (locked April 2026). |
| Sensa (Cosentino) | Natural — protected granite and quartzite | No Cosentino design/installation guide exists; SteedForm applies engineered-stone defaults. |
| Granite (unbranded) | Natural | |
| Vasari Surface | **Ceramic** `[R-M1 v2]` — ruled 3 Sep 2026, scores 🟡 on the porcelain/sintered rung | 12mm single thickness. Factory de-tensioned. |
| Lavistone (Gen Surfaces) | Engineered | No supplier manual held. |
| Silestone QXeron (Cosentino) | Engineered quartz | Indoor only. Supplier thicknesses 12/20/30 — see §4 for the 30mm annotation. |
| Marble | Natural | Bianco Carrara most common. The one natural that laminates. |
| Dekton (Cosentino) | Sintered | **PHASING OUT** — see §8. |
| Kaya Surfaces | Engineered | **All ranges face-printed** (NEOVENA digital print). Indoor-only and heat-sensitive (thermal-shock crack risk). |

### 1.1 BBQ / outdoor ventilation gaps — the figures `SKILL.md` Step 4 checks

**`SKILL.md` Step 4 (Outdoor / Alfresco) requires:** *"Check whether a ventilation gap is specified in Technical Standards for that brand."* These are those figures. They are the gap between the stone and the BBQ unit, and they belong in the builder/cabinetmaker communication **before the cabinet is built** (dimensions · ventilation · stone overhang · cutout · gas access).

| Brand | Ventilation gap | Source |
|---|---|---|
| **Dekton** | **2 mm** | SteedForm Alfresco Requirements, 2024. *(Dekton is separately phasing out — §8; check the substitution steer first.)* |
| **Vasari** | **10 mm** | SteedForm Alfresco Requirements, 2024 — **SteedForm-applied, not manufacturer-specified** |
| **Caesarstone Porcelain** | **10 mm** | SteedForm Alfresco Requirements, 2024 |
| **Neolith** | **5 mm** | SteedForm Alfresco Requirements, 2024 |
| **Smartstone Sintered** | **10 mm** | Smartstone Quickstart V1.05, May 2024 — **manufacturer-specified** |

*Source: `Technical Standards.md` §1, "SteedForm BBQ Ventilation Gaps (outdoor)".*

⚠ **Caveat — a sixth row that is not carried here.** Technical Standards' §1 version of this table also lists **Atlas Plan | 10 mm | SteedForm Alfresco Requirements, 2024 (SteedForm-applied)**. **Atlas Plan appears nowhere else in the corpus** — it is not in Technical Standards' own *Brands in Active Use* list, not in the slab-specification table, and not in the outdoor-suitability table. It is carried here as an observation, **not as a brand row**: if a spec names Atlas Plan, treat the brand as unknown (read the class live off the Materials Library `[R-M1 v2]`, and see the supplier-proximity check in §1.2) rather than reading a 10mm gap off a brand nobody can otherwise evidence.

⛔ **Before any of these gaps matter, check the class:** an alfresco benchtop may not be engineered `[R-ALFRESCO v1]`. A ventilation gap for an engineered brand is a question that should never arise.

**Related outdoor facts held elsewhere in this document:** Smartstone Sintered outdoor is **Conditional**, and its three conditions go into the flag **verbatim** — *"300°C max · non-combustible/fibre-cement backing · 10mm grill clearance"* (§8.2). Indoor-only brands (Zenith, Kaya, Silestone QXeron, Caesarstone ICON) are an outdoor **spec conflict**, not a ventilation question.

#### 1.1.1 Alfresco — the controlled standard `STD-0017 Rev 1`

**Source: `STD-0017 Alfresco Standard`, Rev 1, prepared and approved by James Hill, 14 August 2026 — a controlled document.** It supersedes every earlier alfresco figure in the corpus.

⛔ **ENGINEERED STONE CANNOT BE USED FOR AN ALFRESCO BENCHTOP** `[R-ALFRESCO v1]`. Australian Standards require a barbecue-area benchtop to be non-flammable. SteedForm's alfresco tops are made in **natural stone, or ceramic / sintered** — nothing else.

⚠ **This is a CLASS rule, and the corpus previously stated it only by BRAND.** The old outdoor test named four indoor-only brands (Zenith, Kaya, Silestone QXeron, Caesarstone ICON). Those four happen to be engineered, so the brand list produced the right answer by accident — but **an engineered brand not on that list would have passed.** Same defect shape as the pencil-on-printed-face rule, which was also stated by proxy until `[R-PROFILE v5]` moved it to the real test. Read the class live off the Materials Library `[R-M1 v2]`.

⚠ **There IS an `Outdoor Suitability` column on the Materials Library — and it must stay SUPPLEMENTARY, not authoritative.** Verified against the 3 September 2026 export: `Outdoor Suitability`, `UV Resistance` and `Technical Reviewed` are populated on **41 of 392 rows**, all reviewed 18 August 2026, and **all 41 are Lavistone**. Every one reads `Prohibited` / `No`.

⛔ **A screen that read that column live today would let Zenith outdoors.** Zenith (57 rows), Caesarstone ICON (45), Silestone QXeron (25) and Kaya (3) are all engineered stone and **none is marked prohibited** — the technical review covered one brand. The column is the right field for this job and should eventually be the authority; **reading it today would produce the exact mis-sell `[R-ALFRESCO v1]` exists to prevent.**

**So the order is: class first, column second.** `[R-M1 v2]` class = Engineered → alfresco is refused, whatever `Outdoor Suitability` says or does not say. A `Prohibited` value on a non-engineered material is an additional block and must be honoured. A **blank** `Outdoor Suitability` means *not reviewed* — never *approved*. The column becomes authoritative only when the technical review extends beyond Lavistone; until then it cannot relax the class rule, only tighten it. *(Recorded action 4, `DATA-VERIFICATION-2026-09-03.md`.)*

**The shadowline — this is where "12 mm" comes from.**
A shadow line **12 mm thick × 50 mm wide** is installed **by the cabinetmaker**, and **must be in place before site measure can be completed**. It may be 12 mm compact, edged MDF, or painted edge. Its job is to hide the fibre cement. **It is not required where the benchtop is thicker than 40 mm.**

**The fibre cement.**
Fibre cement sheeting runs along the **entire alfresco surface behind the shadow line**. It does two jobs: it protects the stone from breakage as the cabinetry shrinks and expands, and it is a non-flammable barrier between flammable cabinetry and the heat source.
**Thickness is 6 mm or 9 mm, chosen by the gap between the stone and the carcass.** It is not a single fixed figure.

⚠ **The 12 mm and the fibre cement are two different things, and conflating them is the error that has been travelling.** 12 mm is the cabinetmaker's shadowline. The fibre cement is 6 or 9. A **12 mm fibre cement sheet was a legacy offering and is no longer used** — so `T-TECHNICAL-02`, which tells customers *"a 12mm fibre cement sheet"*, is **wrong and must be corrected**, not preserved. See `09-response-templates.md`.

**The barbecue well.** Where the barbecue is not inset into the benchtop, a well is created. Its dimensions must account for **the thickness of both the fibre cement and the stone**, on top of the barbecue's own dimensions. Where the customer has chosen a barbecue jacket, allow for stone thickness and fibre cement **if the jacket is not insulated**. Stone is required only on the **visible** portions of the well — exposed fibre cement may be used elsewhere to save space.

**Cabinetry design — closed tops and oversized cutouts.**

| Item | Cutout allowance |
|---|---|
| Top-mount sink | Manufacturer's specified cutout **+ 10 mm** |
| Undermount sink | As required by the manufacturer's flange depth **+ 10 mm** |
| Drop-in barbecue | Manufacturer's cutout size, **including allowance for radiused stone corners**, plus a ventilation gap below, **continuous between appliance and stone** |

**What this changes for screening.** An alfresco or barbecue scope raises three things before the cabinet is built: the material class must not be engineered; the cabinetmaker must install the shadowline before measure can proceed; and the well and cutout allowances have to reach the builder in the same conversation as the ventilation gap (§1.1) and the gas clearance (§1.1.2).

⚠ **The 25 / 33 mm lining stack** figures depend on stone thickness — 25 mm for 12 mm stone, 33 mm for 20 mm stone — and were confirmed to stand as written. They are not affected by the substrate figure.

#### 1.1.2 Caesarstone Porcelain gas clearance — 200 mm

**RULED, 3 September 2026: the governing gas-burner-to-splashback clearance for Caesarstone Porcelain is 200 mm.** The **65 mm entries are WRONG for that brand** and must not be quoted — including the cutout-to-edge table entry and the comparison note that cites *"Caesarstone Porcelain 65 mm"*.

⛔ **SteedForm's conservative 200 mm rule does NOT override every brand figure.** Other brands keep their own published figures; read the brand's figure and apply it. The 200 mm here is Caesarstone Porcelain's ruled number, not a blanket substitution.

*(The gas clearance is a heat-clearance figure and is a different measurement from the BBQ ventilation gaps tabled above; do not read one off the other.)*

### 1.2 Local suppliers — the list behind the no-substitution rule

**`SKILL.md` Axis 2 (Supplier Proximity) — the closed list of brands with a local Adelaide presence:**

> **Smartstone · Stone Ambassador · Cosentino (Sensa / Silestone) · Caesarstone · Lavistone · CDK · Complete Marble and Granite · Neolith · Zenith · Vasari**

**The rule this list drives:** *"**Never propose substitution when the specified brand has a local supplier.**"* `SKILL.md` records this as a hard-learned rule — unrequested substitution language on a locally-available brand is **noise that does not help the estimator**. If the specified brand is on this list, supplier proximity is **ALL CLEAR** and must not be raised at all. `07-service-area-and-site.md` carries that outcome; this is the list that decides it.

Notes carried with the list: **Smartstone** is sintered-only (§1) · **Neolith** is the preferred sintered product · **Cosentino** is local, but **Dekton is phasing out and must not be recommended for new work** (§8) — local availability does not override the phase-out. Supplier proximity is only flagged when the brand is **not** on the list, must be sourced **interstate**, or is **unknown**.

> ⚠ **This list is about SUBSTITUTION NOISE, not capability.** A local supplier does not make a combination makeable: §3's profile × material matrix and §4's thickness rules still govern. Equally, a brand being absent from this list is not a decline — it is a proximity flag.

> ⚠ **Technical Standards §1 describes Smartstone Sintered as "full-bodied — vein colour matched into slab body, visible on 20mm edge profile" in its slab-specification table. That descriptor is not carried here.** It would permit a pencil profile on a sintered material, which the Edge Profile Capability Matrix §3a/§4 and `[R-PROFILE v5]` both exclude — porcelain and sintered remain excluded as a class regardless of what a slab table calls them. Where a Smartstone item's `Print Construction` reads blank, it fails closed to review like any other (§2).

---

## 2. Print construction — the pencil prohibition is by CONSTRUCTION, not class

**The test is construction, not class** `[R-PROFILE v5]` (corrected by the MD, 24 Aug 2026). Read **`Print Construction` (`color_mm6hz0dd`) live off Materials Library `5029570546`** `[R-REF v2]`:

✅ **THE COLUMN IS FULLY POPULATED — 392 of 392, no blanks** (verified 7 Sep 2026, populated by Stella Rasheed). 228 `Full body` · 164 `Face-printed`. **OR-40 is closed by the data**: the column was maintained as a positive marker while this rule read blank as unknown, and with no blanks left there is nothing for the two readings to disagree about. The fail-closed branch stays exactly as written — it now guards a **new** material added without being marked, which is the case it was always for. Coverage in `08` §7.1.

| `Print Construction` value | Effect |
|---|---|
| **`Face-printed`** | Hard 🔴 for pencil, regardless of Material Type. Triggers the whole face-printed rule set below. |
| **`Full body`** | Pencil permitted (still hand-finished at every size). |
| **Blank** | **FAILS CLOSED to review. Never read blank as "not printed."** |

**One fact, three consequences (Edge Profile Capability Matrix §3a).** A face-printed material carries a thin printed/decorated surface layer; anything worked *into* that layer shows:

1. **A polishing pad cannot touch the face** → curves are **faceted from 40mm** (§5).
2. **No pencil — arris only.** A pencil radius rolls over the face edge and digs into the print, cutting through to what is beneath; it is also hand-finished, putting variability on the most visible edge. An **arris** works because it is a narrow flat chamfer cut on the EdiPlus — minimal intrusion, machine-consistent.
3. **No lamination** — a laminated joint cannot be worked or finished into the printed face.

> **The face-printed profile menu is SHORT: Arris (any size, per the build rules) + Sharknose/Euro (20mm, straight). That is it.** No pencil at any size · no bullnose / double bullnose / provincial · no lamination · no 30mm · curves faceted from 40mm. The live picker currently offers all of it — the single biggest mis-sell exposure in the profile list.

> ⚠ **ENGINEERED ≠ FULL-BODY.** An `Engineered Stone` classification on the Materials Library does **not** mean full body. Known face-printed engineered ranges *(Zenith/Kaya Fabrication & Installation Manual, May 2026 §7.2)*:
> - **Kaya Surfaces — ALL ranges** (NEOVENA digital print, face only). The manual recommends a 40mm+ mitred edge with a drop-in sink to showcase the pattern.
> This list is the named evidence, not the test. The test is the board value.

**Worked example — QU-58883.** A **20mm Pencil** was priced on **Kaya Sienna**. The item reads `Engineered Stone` on the Materials Library and is face-printed per the Zenith/Kaya Manual May 2026 §7.2. **Both the quote and a full screen cleared it** — because both followed the rule exactly as it was then written: every carrier scoped the prohibition to "porcelain / sintered", which is a *proxy* for the real fact. `color_mm6hz0dd` Print Construction is now the authority for the fact, and blank fails closed `[R-PROFILE v5]`.

> ⚠ **Carrier note for the app.** Edge Profile Capability Matrix **§1a, §5.5, §5.6 and §6** still scope the pencil and lamination rules by CLASS ("porcelain / sintered") — those sections predate the 24 Aug 2026 correction that was applied to §3a. **Apply the construction-based test everywhere**, including wherever a class-scoped restatement appears. The class exclusion of porcelain and sintered still stands `[R-PROFILE v5]`; it is a floor, not the whole test.

---

## 3. Edge profile × material capability matrix

> **The `Edge Profile Capability Matrix` is the governing document for profile × material × machine capability.** Technical Standards §3 says so itself: *"The governing document is `Edge Profile Capability Matrix.md` … The rules below are the summary; **the matrix wins on any conflict.**"* `[R-PROFILE v5]` is the canonical rule; **do not price a combination this set rules out.**

### 3.1 The profile menu — capability by family

| Family | Sizes on the menu | Straight | Curved | Materials |
|---|---|---|---|---|
| **Arris** | 12 · 20\* · 30 · 40\* · 50 · 60 · 70 · 80 · 90 · 100 · 150 · 200 | ✓ EdiPlus (≤80 calibrated; >80 hand) | per §5 | **All materials** (build path per §4). The default. |
| **Pencil** | 12 · 20 · **30 (to add)** · 40 · 50 · 60 · 70 · 80 · 90 · 100 · 150 · 200 | ✓ flat polish + **HAND pencil** | per §5 | **🔴 NOT on any FACE-PRINTED surface** (§2) — read `Print Construction` live, blank fails closed `[R-PROFILE v5]`. Excludes all porcelain and sintered, **and the face-printed engineered ranges — Kaya, all ranges.** Full-body engineered, marble and hard natural only. Hand-finished at every size (#157) — "routine" ≠ "no labour". |
| **Bullnose** | 20mm | ✓ | ✓ (CNC tooling does curves too) | **ENGINEERED + MARBLE ONLY** → 🔴 elsewhere |
| **Double Bullnose** | 40mm (20+20) | ✓ | ✓ (CNC) | **ENGINEERED + MARBLE ONLY.** Build sequence is **REVERSED**: CNC-polish each 20mm piece FIRST, then laminate the two together (each radius must be reachable while the piece is separate). Consequence: the polish cannot be corrected after assembly, and the glue line sits at the waist between the two radii — **designed in, not a defect**. |
| **Provincial (Lamb's Tongue)** | 40mm | ✓ | ✓ (CNC) | **ENGINEERED + MARBLE ONLY** |
| **Triple Bullnose** | *60mm (20+20+20)* | — | — | **THEORETICAL ONLY — not on the menu, never made.** Constructible in principle by extending the Double Bullnose sequence, so engineered + marble only. If requested: **treat as FIRST-OF-KIND → 🔴, a human accepts the gap in writing before quote (#133), plus a first-article setup/trial allowance (#141).** Not a decline — the Ropox path: once made and proven, the MD rules it and it becomes a known profile. |
| **Sharknose / Euro** | 20mm | ✓ | ✗ **straight line only** | **ALL materials** |
| **Lamination** | 40mm (tooling: pencil + arris) · 60mm (conditional) | ✓ | 40mm = CMS-polishable | **Engineered + marble only** (§4) |
| **Waterfall end — regular** | 12 · 20 · 30 (if available) · 40 | ✓ | — | **ALL materials — STANDARD chargeable install.** Routine at these thicknesses (30mm natural-only per §4). Veined stone still adds the vein-continuity line (#123). |
| **Assemble On Site** | — | method, not a shape | — | **ALL materials — geometry-driven, NOT material-restricted.** A boxed island that cannot be glued up in the factory is an Assemble On Site: the factory cuts the 45°, the box is glued on site. QC note below. |
| **~~Ogee~~** | — | — | — | **NOT OFFERED — removed from all documents 23 Jul 2026 (MD).** Never quote it. **RESET the spec to a lamb's tongue (Provincial)** `[R-SCOPE v2]` `[R-PROFILE v5]` — which is 40mm CNC, straight and curved, engineered + marble only, so check the material before offering it. |

\* asterisked on the live menu (standard/default sizes).

**Default when no profile is nominated: ARRIS** — lowest cost, most chip-resistant, baseline price. Any other profile is a quoted variation and must be requested.

⚠ **StonePro's Standard Profiles product list (Product Group 300) is not a capability statement** — it does not encode the material restrictions. Screen against this matrix, not against the picker.

### 3.2 Machine homes and finishing routes

| Geometry | Build | Route | Machine / hand |
|---|---|---|---|
| Straight | 12 / 20mm single thickness | EdiPlus — arris + polish | machine (**pencil = flat polish then HAND**) |
| Straight | mitred **≤ 80mm** | EdiPlus **calibrates the rail** + arris + polish | machine |
| Straight | mitred **> 80mm** | **cannot be calibrated — saw rail accuracy is the limit** | **HAND finish** ⚠ cost cliff |
| Straight | **60mm lamination** | CNC flat polish only | **+ HAND** arris / pencil |
| **Curved** | 12 · 20 · 30 single thickness · **40mm lamination** | **CMS Brembana** polishing | CMS |
| **Curved** | above that | **faceted mitre** (§5) | — |
| Any | **Assemble On Site** | factory cuts the 45°; **glued ON SITE**, not in the factory | site glue-up |

**Machine homes:** EdiPlus = straight-line inline profiles, and can calibrate a mitred rail to 80mm. **CMS Brembana** = curves, at 20mm and 30mm. **Genya** = CNC profiles and cutouts. Hand finish = pencil, and the arris after flat polish.

### 3.3 Assemble On Site — heightened field-join QC

Assemble On Site is not material-restricted, **but the risk is not equal across materials, and this is an install-QC item, not a screening block.** On **porcelain/sintered a site-glued mitre joint cannot be dressed or polished after glue-up** (the printed face, §2) — the joint has to be right **off the saw, first time, in site conditions.** The same applies to **veined stone**: vein continuity across a site joint cannot be corrected. Flag Assemble On Site on porcelain / sintered / veined as a heightened field-join QC case — install-report join/seal checklist with photos (#77), and crew-complexity allocation (#142).

### 3.4 Screening consequences (Edge Profile Capability Matrix §6)

| Situation | Verdict |
|---|---|
| **Pencil specified on a face-printed surface** — the highest-frequency profile error to expect, since pencil is a common default request | **🔴 spec conflict — not offered. Steer to ARRIS** (or Sharknose/Euro) `[R-PROFILE v5]` |
| **Shaped profile on the wrong material** — Bullnose / Double Bullnose / Provincial specified on porcelain, sintered or hard natural | **🔴 spec conflict** |
| **Curved edge above the material's polish limit** | **🟡 specification + expectation step — never a decline.** The client is told it will be a faceted mitre and signs off the appearance. On veined stone, *recommend* faceted `[R-D5 v8]` |
| **>80mm build** | **🟡 hand-finish labour band** — cost cliff, price accordingly |
| **60mm lamination** | **🟡** — confirm the aesthetic carries two glue lines; never on veined stone; offer mitred 60mm as the cleaner face |
| **30mm specified on engineered, porcelain or sintered** | **🔴 spec conflict — not available** `[R-30MM v1]` |
| **Ogee specified** | **NOT OFFERED — RESET to a lamb's tongue (Provincial)** `[R-SCOPE v2]` `[R-PROFILE v5]`. A reset, not a decline: the enquiry continues on the supported profile and the client is told before the quote goes out (§6) |

### 3.5 Processing complexity — where the time actually lands (Matrix §9, MD 23 Jul 2026)

**Scope: builds up to 40mm.** Anything above sits outside this ladder as additional load. This is not one ladder — it is **three levers loading three different resources**, so which one "costs more" depends on the week's bottleneck.

| Lever | Where the time lands | Detail |
|---|---|---|
| **Mitred edge** (vs arris single thickness) | **SAW** + **glue bench** | Glue-up is relatively fast, and once glued the piece runs the inline (EdiPlus) at single-thickness speed — **no penalty at the polishing stage** |
| **Undermounts** | **CNC** — routing + handling | The driver is CNC processing/handling, not the cutout per se |
| **Butt joins** (incl. L / U shapes) | **SITE / install time** (predominantly) | More pieces to carry, set and seam on site. Small factory add when the edge is **mitred** — the built-up rail must align across the join |

**Factory processing ladder (≤40mm builds, ascending):** 1. Arris, single thickness, straight-line polish — inline only ← **the optimum** · 2. + undermounts (adds CNC) · 3. + mitred to 40mm (adds saw + glue; inline speed unchanged) · 4. mitred + undermounts (loads both).

**Stacked load, on top of the ladder:** butt joins (site/install time) · 50–80mm builds (additional tier, still machine-calibrated) · **>80mm builds (hand finish — the step cost cliff)** · waterfall ends 12/20/30/40 (standard chargeable install) · curves and faceting (§5).

"Complexity" splits into **FACTORY cost and INSTALL cost** — two quote lines, two independent capacity constraints. A single 1–6 complexity score would hide which resource is the bottleneck.

---

## 4. Thickness and build rules

### 4.1 The two build paths

Slabs come in single thickness, so any edge deeper than the slab is built one of two ways:

| Method | How | Sizes possible | Materials |
|---|---|---|---|
| **Mitred** | fold the return from the same slab (45°) | **any height ≥ 40mm** (rail cut to size) | **ALL materials** — and the only build path for porcelain / sintered and any face-printed surface |
| **Laminated** | glue **20mm layers** | **40mm (20+20) and 60mm (20+20+20) ONLY** — no 50 / 70 / 90 | **Full-body engineered + marble.** Other natural stone **case by case** (below). Never on a printed face, nor limestone or travertine |

- **Mitre minimum = 40mm. Nothing below 40mm is mitred — the minimum mitred build-up is ALWAYS 40mm** (reconfirmed by ruling, 3 September 2026).
- **Lamination is 20mm layers only.** There is no 30mm layer and no 20+40 combination. **A 50mm laminated build does not exist.**
- **A PRINTED FACE CANNOT BE LAMINATED** `[R-PROFILE v5]`. Ceramic, porcelain and sintered are never laminated, and neither is any material whose `Print Construction` (`color_mm6hz0dd`) reads `Face-printed`. **The print is the reason; the class is only a proxy** — the same correction MD made to the pencil rule on 24 Aug 2026, for the same reason.
- **Limestone and travertine are ruled not laminable — MD 23 Jul 2026** (§5). Unchanged and not a pending question.
- **The rest of natural stone — granite, quartzite, marble — is CASE BY CASE, resolved by a person per job** (ruled 7 Sep 2026, Stella Rasheed). It is not a property of the material recorded on a board, and no column will answer it: the answer is about the slab in front of you. ⚠ **This does not move any faceting threshold.** Lamination and faceting are different operations, and `[R-D5 v8]`'s table is unchanged — a stone that laminates still facets from 40 unless a rule says otherwise.
- **60mm lamination is CONDITIONAL** — three layers = **two glue lines on the edge face**; only where the aesthetic and the chosen profile carry them. **Not on veined stone** (the joints break the vein twice). A mitred 60mm gives a continuous face with no glue line and is usually the better look.
- **Straight thick edges are MITRED, not laminated.** Mitre is the default method for any straight thick edge above 20mm — 40 / 50 / 60 / 80mm profile fronts as standard, reinforced with the SteedForm 40mm Whiteboard HMR three-run cleat standard (front / middle / back, full length, **every material, no per-material variation** — included in the standard build price, nothing to flag).
- **Scope: these rules run to 40mm.** 50–80mm has its own cost step; **>80mm is a hard cost cliff — flag it** `[R-PROFILE v5]`. 50mm and 60mm are *common*, not *free*: flag the thickness so it is priced, not as a risk. **A 50–80mm engineered mitred build scores 🟡 AMBER at D1, on the cost difference** (ruled 3 September 2026; the rung is stated in `03-risk-scoring.md` §3.3). **Engineered ≤ 40mm is 🟢.**

### 4.2 30mm — natural stone only

**30mm is a NATURAL-STONE-ONLY single thickness** (subject to slab availability) and is a **🔴 spec conflict on engineered, porcelain or sintered** `[R-30MM v1]`. There is no 30mm build-up and no faceting at 30mm; a 30mm engineered benchtop cannot be made.

Menu corrections that follow (Matrix §5): "30mm Arris (Mitred)" is **mislabelled** — 30mm is a single-thickness natural slab, not a mitred build; drop "(Mitred)". 30mm must not be selectable for engineered / porcelain / sintered. Add **30mm Pencil** on the same natural-only basis. Porcelain/sintered must not offer 30mm, any lamination, or 60mm lamination.

### 4.3 Supplier thicknesses — reference, with the capability annotation

Supplier fact from Technical Standards §1. **A supplier offering a thickness does not make it makeable at SteedForm.**

| Brand | Type | Supplier thicknesses (mm) | Capability annotation |
|---|---|---|---|
| Zenith | Engineered | 20 ± 1 | |
| Kaya | Engineered (face-printed) | 20 | Face-printed → §2 menu applies |
| Caesarstone ICON | Advanced Mineral | 20 ± 1 | 40mm "thick" = 20+20 lamination |
| Silestone QXeron | Engineered (quartz) | **12, 20, 30** | ⚠ **30mm is NOT OFFERED on engineered** `[R-30MM v1]` — a 30mm QXeron top cannot be made; reset the spec, do not price it. Indoor only. |
| Vasari | **Ceramic** `[R-M1 v2]` | 12 ± 0.5 (single thickness) | Scores 🟡 as porcelain/sintered. Never laminated. Factory de-tensioned |
| Caesarstone Porcelain | Porcelain | 12 ± 0.5, 20 ± 0.5 | Never laminated |
| Neolith | Sintered | 12, 20 | Never laminated |
| Smartstone Sintered | Sintered | 20 ± 0.3 | Never laminated. Requires 20mm trim off all sides (de-tensioning cut per V6, not an exception) |
| Dekton | Sintered | **4, 8, 12, 20, 30** | ⚠ **30mm is NOT OFFERED on sintered** `[R-30MM v1]`. Dekton is separately phasing out — §8. |
| Sensa (granite / quartzite) | Natural (protected) | 20, 30 | 30mm permitted — natural `[R-30MM v1]` |
| Marble / granite (unbranded) | Natural | 12 / 20 / 30 typical | 30mm permitted — natural |

*All slabs require perimeter trimming before fabrication (20–30mm off each edge) to release tension and square the edges — universal across brands. Exception: Vasari and Smartstone Sintered slabs are supplied de-tensioned.*

---

## 5. Curves and faceting `[R-D5 v8]`

**A curve is polished only up to that MATERIAL's limit; above it the curve is a FACETED MITRE — makeable, never a decline** `[R-D5 v8]`. The limit is **material-dependent, not a flat 40mm**, because only engineered and marble laminate.

| Material | Polished curve up to | Faceted **elective** from | Faceted **mandatory** from |
|---|---|---|---|
| **Porcelain / sintered** *(printed face — a polishing pad cannot touch it; never laminated)* | single thickness (12 / 20) | 40 | **40** |
| **Hard natural — granite, quartzite** *(non-laminable by hardness)* | single thickness (12 / 20 / 30) | 40 | **40** |
| **Limestone · travertine** *(**RULED not laminable — MD 23 Jul 2026** `[R-D5 v8]`. This is settled, not pending: no carrier may reopen it, and it may be stated as MD law in a client-facing brief)* | single thickness | 40 | **40** |
| **Engineered · marble** *(laminable to 60)* | **40 (20+20 lamination)** | **40 — if the vein justifies it** | **60** |

*Why there is no 50mm curve to argue about: there is no 50mm lamination (20mm layers only), and a 50mm mitred curve is faceted by definition.*

**A curve above the limit scores 🟡 plus a MANDATORY documented client sign-off on the faceted appearance before fabrication. It is NOT blocking and must never force Needs Review** `[R-D5 v8]`.

**The document is the SIGNED ORDER CONFIRMATION** (ruled 7 Sep 2026). A screen therefore never confirms that a sign-off has happened — it states the condition and names what will carry it.

**A curve on single thickness (12 / 20 / 30) is ordinary work and scores nothing on its own** — the tooling is built for it. **A request for faceting below 40mm is 🟡**: below the lamination threshold there is nothing to facet, so the specification needs checking rather than pricing. Splayed and angled benches remain 🟡 always.

**Faceting is not a compromise.** On veined product a polished radius **grinds through the vein**; a faceted mitre folds the face and **preserves it**. It is frequently the better aesthetic outcome and should be offered as such, not apologised for. Faceting is also **elective from 40mm on any material**.

**What "elective" means on engineered and marble** (ruled 7 Sep 2026): the vein is too clashy for lamination. Two glue lines break the vein twice, so faceting is the alternative route. **The trade is that the curve will not necessarily be smooth — and that trade is the CUSTOMER's call**, offered by the estimator and decided by the client, carried by the same signed order confirmation.

### 5.1 The mandatory conservative fallback — carry this, it is often dropped

The marble-vs-hard-natural split **is not derivable from the board, and no field is coming.** Material Type says only "Natural Stone", and `dropdown_mm4rq7jd` Stone Sub-Type records granite vs non-granite (not marble vs hard natural) and is populated on only **3 of 392** materials as at 18 Aug 2026 `[R-SUBTYPE v2]`.

**It is resolved by a person, per job. This is the standing position, not an interim one** (ruled 7 Sep 2026): nobody is waiting on a field, and the flag below is permanent. `[R-D5 v8]` requires:

> **Treat ANY natural stone as HARD NATURAL — faceted from 40mm — unless a human has confirmed it is marble.**

and a visible flag on the output. **There is now ONE flag string, and it is fixed** `[R-D5 v8]` (ruled 3 September 2026). Emit it **verbatim**:

> `"⚠ marble vs hard natural not derivable from the board; confirm before quoting the curve"`

*(The former second string — "natural sub-type not recorded — faceting threshold assumed 40mm…" — is retired. Do not emit it.)*

**Why this direction** `[R-D5 v8]`: assuming marble and being wrong means **promising a polished 40mm curve on granite that cannot be made** — the exact mis-sell this rule was written to stop. Assuming hard natural and being wrong means quoting a facet where a polish was possible: recoverable, and visible at sign-off. An unnecessary sign-off costs a conversation; a promised polished radius that cannot be made costs a remake and a client. **When the data is missing, fail toward the flag, never toward the promise. Never resolve it from the colour or brand name.**

⚠ **Several carriers state the material-dependent limits without this fallback.** A 40mm curved porcelain or granite edge **is** faceted and **does** need the sign-off — the flat-40mm reading is what caused the 25 Jul faceting mis-sell.

---

## 6. NOT OFFERED

**NOT OFFERED** `[R-SCOPE v2]` — the complete list. **Each item carries its OWN screening action — DECLINE or RESET. The two are never interchangeable** (ruled 3 September 2026).

⛔ **A DECLINE item is not a specification to be corrected.** Do not price it, do not substitute around it, do not render it 🟡.
⛔ **A RESET item is not a decline.** The enquiry continues on a supported specification, and the client is told **before** the quote goes out.

| Item | Action at screening | Note | Ledger |
|---|---|---|---|
| **Flooring** — any material | **DECLINE or refer** | Including Smartstone, whose own manual does not recommend the Sintered Collection for flooring (PTV dry 80 / wet 9). A scope decline, not a screening flag — the old "Smartstone flooring → reset spec" is superseded | #116 |
| **Stone shower bases and fall-requiring drainer boards** | **DECLINE or refer** | SteedForm does not machine falls or gradients. **Lane home: `03-risk-scoring.md` D12**, the new Detail rung alongside D7 (ruled 3 Sep 2026) | #103 |
| **Drainer grooves** — the whole category, any material or thickness | **DECLINE or refer** | Distinct from shower bases: grooves stay at D8 | #136 |
| **Bathroom hobs** — raised wet-area kerbs | **DECLINE or refer** | ⚠ **NOT cooktops.** Bathroom vanity and benchtop work is fine | #124 |
| **Machined recesses / chutes / glazing channels** | **DECLINE or refer** | "Other machined features" beyond cutouts | #135 / #31 |
| **Replacement or remedial work on someone else's stone** | **DECLINE or refer** | Includes benchtop replacement on existing cabinetry — new cabinetry only | #150 (the skill cites #60/#64 for benchtop-replacement-on-existing) |
| **Client-supplied slabs** | **DECLINE — the ONLY carve-out in this table** | A hard stop for every account **except an A-tier account, where it becomes a 🔴 RISK routed to Needs Review** for a named human to accept or decline. Policy locked May 2026, regardless of who the customer is or which supplier they source from, including SteedForm-relationship suppliers. Full supply-and-fabricate is what lets SteedForm manage slab selection, handle variation and back the workmanship guarantee. Frame as protecting the client's project and SteedForm's standards, not as a capability gap. Template T-DECLINE-07 | #85 / #60 / #64 |
| **IKEA kitchens** | **DECLINE or refer** | Including via a cabinetmaker | #60 / #64 |
| **Flush mounting** — sinks or cooktops set flush into the stone | **RESET** the spec to a supported mount, before the quote | See §6.1 `[R-FLUSH v1]` — `[R-FLUSH v1]` stands unchanged | #31 |
| **Masons mitre as a standalone selection** | **RESET** the spec to SteedForm's standard mitred build | 🟡 substitute note, non-blocking. ⚠ **The CNC masons-mitre exception is PRODUCTION'S DISCRETION and must NEVER be promised by the screen** — a piece already on the CNC for profiling or lamination may absorb it at no meaningful extra cost, but that is decided in production, not at screening | — |
| **The ogee profile** | **RESET** the spec to a **lamb's tongue (Provincial)** | Removed from all documents 23 Jul 2026 (MD) `[R-PROFILE v5]`. Provincial is 40mm CNC, **engineered + marble only** — check the material before offering it (§3.1) | — |

⚖ **Client-supplied slabs — classification, now settled.** `[R-SCOPE v2]` places the item in the DECLINE column and `[R-BLOCK v3]` keeps *"client-supplied stone"* in the layer-2 blocking set. Those are not in conflict: **the default is a DECLINE, and the single A-tier carve-out is the 🔴 that routes to Needs Review.** No other item in the table has one. T-DECLINE-07 remains the decline, and the $20k remake (§9) is the reason behind it.

Also NOT OFFERED, from adjacent rulings:

- **45° mitred corner join on an L-shaped benchtop** (MD, 18 June 2026 — Farquhar / Zenith Vanilla Sky; supersedes an earlier "yes, if" framing). The default at an internal corner is a **butt joint**. This is a commercial/risk decision, not a capability limit: the mitre seam is the corner diagonal (≈ leg depth × 1.41 — a 650mm-deep corner is ~920mm, ~40% longer than a 650mm butt), the acute tip is the most common full-mitre failure mode, seam-setter access reduces into the corner so the seam **cannot be guaranteed level**, and a long diagonal over a corner cabinet is more prone to post-install movement. Where a mitre is sought to carry vein around the corner, that is only achievable on designated vein-match products. **Scope:** L-shaped corner joins only — full mitres for waterfall ends and built-up/laminated edge details, fabricated in the factory, are unchanged.

**APPROVED — do NOT flag as first-of-kind:** the **Häfele Ropox Flexi Electric height-adjustable benchtop frame** (Häfele P-01499319), APPROVED MD 23 Jul 2026. Stone fabricated onto this motorised adjustable frame is a proven engineered system, not an unruled first-of-kind; do not score the #133 first-of-kind blocking red. *This clears the adjustable FRAME only — integrated motorised APPLIANCE lifts still need appliance verification (#91).*

### 6.1 Flush mounting `[R-FLUSH v1]`

**Flush mounting is NOT OFFERED. Ever.** `[R-FLUSH v1]` — a hard technical refusal, not a preference and not a pricing question. The operative reasons, which must be stated in the condition entry:

1. **CNC tooling limitation** — a flush mount requires a rebate machined into the surface; CNC tooling cannot achieve a perfectly sharp clean internal edge, and the process inherently leaves fine chipping along the rebate edge, particularly in engineered stone, porcelain and sintered surfaces.
2. **The silicone gap is unavoidable** — the brochure "seamless" look cannot be reproduced in fabrication.
3. Caesarstone Porcelain explicitly prohibits it.
4. **Default rule:** if a supplier manual does not explicitly state that flush mounting is approved for a material, assume it is not possible.

At screening: a **🔴 condition entry with the reason stated** (chipping · silicone gap · brochure vs reality), and propose overmount/drop-in `[R-FLUSH v1]`. **The builder/client must be told BEFORE the quote goes out** — a flush-mount expectation discovered at install is a remake. Communication template: **T-TECHNICAL-01**.

**Flush mounting is a mounting method, not an edge profile** — `[R-PROFILE v5]` governs edge profile × material and does not cover it; this is a separate capability refusal with its own tag `[R-FLUSH v1]`.

**Mounting type is ORDER-bar evidence, and it is a board field.** `[R-EVIDENCE-BAR v2]`'s ORDER bar for *Appliances / sinks* requires **model number, mounting type, linked Library record** — so at Order a mount must be a *recorded value*, not an assumption, and "flush" surfacing there is a reset, not a variation to price. The Appliance Library `5029694677` column carrying it is **`color_mm4zdfnd` Mount Type** (being added to `08-board-and-column-registry.md`), alongside **Cutout Spec `long_text_mm4zayzp`**. Read both live — never screen a mount or a cutout from memory or from a snapshot pasted into a document. **That same ORDER-bar row now also requires QC Status** `[R-EVIDENCE-BAR v2]` (ruled 3 September 2026), matching the adjacent Cut-outs row. *(Evidence-bar mechanics are owned by `06-evidence-requirements.md`; what is carried here is the capability half — a mount SteedForm cannot make.)*

### 6.1b Overhang limits — the table `[D11]` compares against

**Reference data, read off the manufacturers' own fabrication manuals, 7 September 2026.**
`03-risk-scoring.md` §3.3 **D11** scores a drawn overhang *at or over* the brand-and-thickness
limit — and until today that table existed nowhere in this knowledge base, so the rung had no
threshold and fired on **every** drawn overhang. These are the thresholds.

🟠 **EVERY TABLE HERE IS AMBIGUOUS AT ITS OWN THRESHOLD, AND THAT IS WHERE D11 FIRES.** Three
manuals, three different ways of not quite saying it: Caesarstone ICON prints `<300 mm` in one
band and `300-500 mm` in the next, so 300 falls in both readings depending on which row you
trust. Neolith prints **"≤ 350 mm (less than 350 mm)"** — inclusive and exclusive in a single
cell. Larona prints `A < 150mm` then `A = 150mm - 300mm`, the same overlap as Caesarstone.

**One SteedForm ruling should settle all of them and every table added later**, rather than a
separate reading per brand:

> **At the exact figure — does it pass, or does it flag?**

⛔ **NOT YET RULED.** Until it is, a drawn overhang landing exactly on a published figure is
**flagged and confirmed with the builder**, which is what D11 already does with everything.

#### Rules that apply to every brand below

- ⛔ **The unsupported overhang must be no greater than ONE THIRD of the complete surface
  depth.** This sits on top of every figure below: a 300mm overhang needs 900mm of surface,
  whatever the millimetre table permits.
- **The fabricator determines the required support.** The manuals state the limits; they place
  the responsibility for the support design with the fabricator.
- Do not load more than **100 kg** on any part of an overhang; do not sit or stand on it.
- Laminating the edge and bonding a second slab underneath adds strength and moves the job into
  the laminated row.

#### Caesarstone ICON — engineered *(CSA NZ F&I ICON Ed 3, Dec 2025, §9.7)*

| Support required | 20mm slab | 40mm laminated top |
|---|---|---|
| **None** | **< 300 mm** | **< 400 mm** |
| **Support brackets at 600mm intervals** | **300 – 500 mm** | **400 – 600 mm** |
| **Legs, columns or panels at 600mm intervals** | **> 500 mm** | **> 600 mm** |

*(Corrected 7 Sep 2026 against the printed table. An earlier reading of this section carried only
two laminated bands and stopped at "over 400mm — brackets", which understated the allowance: a
laminated top runs to 600mm on brackets and only needs legs beyond that.)*

⚠ **300mm is the first millimetre of the bracket band, not the last of the free one.** A 300mm
overhang on 20mm ICON requires brackets at 600mm intervals **and** 900mm of supported depth to
satisfy the one-third rule. It is a boundary case in both tests at once, which is exactly why
D11 flags it rather than letting it through.

#### Zenith Surfaces · Kaya Surfaces *(Zenith & Kaya F&I Manual, May 2026, §8.9)*

| Overhang depth | Support required |
|---|---|
| **< 300 mm** | None |
| **300 – 500 mm** | Support brackets at 600 mm intervals |
| **> 500 mm** | Legs, columns or panels at 600 mm intervals |

**Identical to Caesarstone ICON's 20mm column** — same bands, same intervals, same wording. ICON
additionally publishes a 40mm laminated column; Zenith and Kaya publish none. Two
engineered-stone brands landing on the same structure is worth knowing, but they remain separate
rows here: a shared table today is not a promise of a shared table at the next revision.

⚠ **THIS TABLE STATES NO THICKNESS.** Caesarstone gives 20mm and 40mm-laminated columns; this one
gives a single set of bands. **Do not assume the laminated allowance carries across** — a 40mm
laminated Zenith top has no published figure here, and an unstated thickness is not a permission.

Same guidance as Caesarstone on either side of it: laminating the edge and bonding a second slab
underneath adds strength, the fabricator determines the support, and a two-direction overhang
whose outside corner exceeds the limit takes flat brackets in addition.

#### Caesarstone Porcelain *(CSA EN Porcelain F&I Ed 4, Nov 2025, §7.10)*

**The number of overhanging sides changes the limit.** One side is treated more generously than
two or three, and the manual gives both.

| Overhang | Maximum unsupported | Supported depth needed |
|---|---|---|
| 12mm, one side | **≤ 300 mm** | ≥ 600 mm |
| 12mm, two or three sides | **≤ 250 mm** | ≥ 500 mm |
| 20mm, one side | **≤ 450 mm** | ≥ 900 mm |
| 20mm, two or three sides | **≤ 400 mm** | ≥ 800 mm |

⚠ **READ THE FRACTION AGAINST THE COMPLETE DEPTH, NOT THE SUPPORTED DEPTH.** §7.10's prose says
each overhang must be "no greater than 1/3 of the **supported** surface depth", and its own
worked pairs contradict that: 300 with 600, 450 with 900, 250 with 500, 400 with 800 — every one
of them is **half** the supported depth. They are all exactly **one third of the COMPLETE depth**
(overhang + supported), which is what page 50 of the same document says. So:

> **overhang ≤ ⅓ of (overhang + supported depth)** — equivalently **overhang ≤ ½ of the
> supported depth**.

Applying the prose as printed makes SteedForm **twice as conservative as Caesarstone intends**
and would decline work the manufacturer permits.

⛔ **Single-thickness edge profiles must not overhang on OPEN cabinets.** Where a mitred edge is
used, a support panel under the entire benchtop is recommended.

**When support is needed** *(§7.10, All Slabs)*: non-flexible material — **wedi Building Board,
Whiteboard HMR, or a support construction**. A Porcelain panel used as vertical support from the
end of the overhang to the floor must be **two slabs joined back-to-back**, never one. **Do not
remove the mesh backing from the underside of an overhang** (it may be removed from exposed side
panels, but Caesarstone warrants no appearance on the back of a slab).

🟠 **UNRESOLVED — the 12mm section contradicts itself.** After allowing 300mm on one side, it
adds *"Overhangs longer than 250 mm always require support."* Unscoped, that cancels the 300mm
allowance two lines above it. The 20mm section directly below scopes both of its equivalents —
*"longer than 450 mm **on one side**"*, *"longer than 400 mm **on two or three sides**"* — so by
parallel construction the 12mm line is missing *"on two or three sides"*. **That reading is not
yet ruled.** Until it is, a 12mm one-side overhang between 250 and 300mm is confirmed with the
builder rather than passed.

#### Neolith *(Neolith Technical Guide APAC)*

| Thickness | Maximum unsupported overhang |
|---|---|
| **12 mm** | **≤ 350 mm** |
| **20 mm** | **≤ 500 mm** |

Reinforcement at **600mm centres** where support is used, with additional reinforcement at the
X sections of a full-perimeter frame.

#### Vasari Porcelain *(Vasari Surfaces Fabrication & Installation Guide 2025)*

| Overhang | Support |
|---|---|
| **≤ 150 mm** | None — 150mm is stated as *the maximum unsupported overhang* |
| **150 – 300 mm** | Sufficient support must be provided |
| **> 300 mm** | Adequate support from the base, **at least every 600–620 mm** |

⚠ **VASARI IS THE ONE MANUAL THAT SETTLES ITS OWN BOUNDARY.** It states 150mm *is* the maximum
unsupported overhang rather than printing overlapping bands, so 150 passes and 151 does not. Worth
weighing when the ruling above is made.

⛔ **CUTOUTS NEAR AN OVERHANG ARE A SEPARATE HAZARD, AND ONLY THIS MANUAL RAISES IT.** Vasari's
static weight tolerance *"depends on the presence of holes in the immediate area"*, and excessive
weight near a hole can break the surface — a specific assessment is recommended. **A tap hole or
a cutout landing near an overhang is therefore a condition in its own right**, separate from the
overhang distance, and the distance table alone does not clear it.

#### Larona Porcelain *(manufacturer table, supplied 7 Sep 2026)*

| Overhang | Support |
|---|---|
| **< 150 mm** | None required |
| **150 – 300 mm** | Adequate support required from the base |
| **> 300 mm** | Adequate support from the bases, **at least every 600 mm** |

⚠ **Larona's bands are identical to Vasari's** — 150 / 150–300 / >300 at 600mm centres. Recorded
as observed, not as a claim that they are the same product.

⚠ **Larona is roughly twice as conservative as Caesarstone Porcelain.** Support begins at
**150mm** here, where Caesarstone allows 300mm unsupported on one side at 12mm. **Never carry a
Caesarstone figure onto a Larona job** — this is the reason D11 compares against a *brand* table
and not a single number.

⛔ **LARONA IS NOT ON THE MATERIALS LIBRARY** (`5029570546`), confirmed 7 Sep 2026. So a drawing
naming Larona resolves to **no material record at all**: `[R-MATERIAL-TERMS v1]` matches exactly
with no fuzzy fallback, so the lookup fails **silently** rather than reporting an unknown brand.
Class, print construction and outdoor suitability are all unreadable for it. **Until the brand is
added to the library, a Larona job cannot satisfy `[R-REF v2]`** and the material lane is
scored on what the documents say, flagged as unresolved — never as clean.

#### Not yet extracted — treat as unknown, never as unlimited

Zenith · Kaya · Neolith · Lavistone · Vasari · Smartstone Sintered · Dekton · Cosentino Silestone
and Eclos. Their manuals are held and carry permitted-overhang tables, several of them as
diagrams rather than text. **Until a brand appears above, D11 has no threshold for it and the
overhang is confirmed with the builder** — the same answer as before, but now it is a known gap
rather than the whole rule.

---

### 6.2 Appliance corner radii — the R5 vs R10 conflict check

**`SKILL.md` Step 4 requires it explicitly:** *"Flag any known conflicts (e.g., appliances that specify R5 corners when stone minimum is R10)."*

The appliance manufacturer specifies the cutout it wants; the stone specifies the smallest internal radius that can be cut without an unacceptable stress riser. **An appliance calling for R5 corners against a stone minimum of R10 is a conflict, and the appliance spec does not win by default.** Flag it at screening as a condition to be resolved before programming — the cutout has to be agreed against the Appliance Library record (`long_text_mm4zayzp` Cutout Spec, §6.1), not discovered on the CNC.

⚠ **This is a per-appliance check, not a per-brand argument.** Do **not** convert it into a Dekton talking point: Dekton's own radii are sink R10 / hob R10 / other R5, close to the industry R10 default, and §8.3 explicitly bars citing radii in the selling-against argument.

---

## 7. The capability-vs-risk separation `[R-ANDON v2]`

**⛔ CAPABILITY and 🔴 RISK are two different verdicts and MUST NEVER BLEND** `[R-ANDON v2]` (MD ruling 23 Jul 2026). Say which one it is, **every time**.

| | Meaning | Resolution | Examples |
|---|---|---|---|
| **⛔ CAPABILITY / NOT-OFFERED** | *"We cannot make this."* | **Hard stop.** No human call can authorise it — the tooling, the material physics or the ruled scope simply is not there. **The ACTION is per item — DECLINE or RESET — and is stated in `[R-SCOPE v2]` (§6), not here. This rule classifies; R-SCOPE disposes** | Profiles we lack tooling for · flush mount · bathroom hobs · drainer grooves · flooring · shower bases · **pencil on any face-printed surface** · lamination on porcelain/sintered/hard natural · 30mm on anything but natural · ogee |
| **🔴 RISK** | *"This is far from our optimum."* | **A human call**: take it and price it properly, or decline it as not for us. **Both answers are valid** | Natural stone · 50mm+ builds · vein · boxed islands · large splashbacks · non-standard details |

**Why the line matters** `[R-ANDON v2]`: blend them and one of two failures follows.

- Treat a **capability gap as risk** → someone eventually **human-calls their way into promising a job that physically cannot be made.**
- Treat **risk as capability** → screening starts **declining work SteedForm actively sells.** A boxed island is 🔴 on geometry but is standard, all-material, charged work (assemble on site: the factory cuts the 45°, it is glued in situ).

### 7.1 The optimum, and what "distance from it" means

**Green is not "safe" — green is OPTIMAL.** There is one setup that runs fastest through the factory, cheapest, with the least that can go wrong:

> **Engineered · single thickness · straight lines · flat colour · arris edge**

That is the same optimum the processing model (§3.5) reaches from the factory side. **Every red is one step away from it. Accumulating reds is the signal** — a *pattern* of reds says the work is drifting out of SteedForm's sweet spot and someone should decide whether we want it. That is a **gradient, not a gate**: no single red condemns a job.

| Axis | 🟢 optimal | 🟡 step away | 🔴 far from it |
|---|---|---|---|
| **1. Material class** | engineered | sintered / porcelain | natural |
| **2. Build** | single thickness | mitred 40mm | 50mm+ |
| **3. Geometry** | straight lines | curves | boxed islands · large splashbacks · non-standard |
| **4. Colour / pattern** | flat colour | movement | vein |
| **5. Profile** | arris | pencil · CNC-tooling profiles | *(capability, not risk — see the table above)* |

> ⚠ **This table is a LENS, not the scoring engine.** It measures *distance from our optimum*; it does not set verdicts. The distinction matters most on **axis 2**: a 60mm mitred engineered island edge sits at 🔴 *distance* here, yet it is **routine work sold every week**. Reading axis 2 as a verdict trigger would push ordinary thick-edge jobs into Needs Review — exactly the "risk treated as capability" failure above. **The strip scores that edge 🟡 at D1** (ruled 3 September 2026).
>
> ⚠ **The lens stands as written, and its future is under review — `10-open-rulings.md` OR-38**, which holds for scoping whether Screening Philosophy is retired and whether all stone moves to one ladder. **Nothing in OR-38 may be applied as a rule; keep using the lens exactly as described here.**

On a risk red the question is never *"can we?"* — it is **"do we want this one, at a price that respects what it costs us?"** Axis 1–2 reds point at cost and fabrication exposure; axis 3 reds at install exposure; axis 4 reds at **client-expectation** exposure (vein match, faceted vs polished appearance — the outcomes disputed at handover). A job red on one axis is usually a good job priced correctly. A job red on four will consume estimating, factory, install *and* relationship capacity at once — that is the pattern that says *not for us*.

---

## 8. Dekton phase-out

**Dekton → DECLINE as spec'd, and recommend substitution** `[R-DEKTON v1]`. Do not quote Dekton on new work. **The Dekton line is declined as specified and the substitution steered; the lead itself is never auto-Unqualified** — it routes to a human with the steer attached. On an **A-tier** account the four-condition materiality exception (§8.1) converts the decision to a named human's call. Decline template: **T-DECLINE-06**.

**The flag string is verbatim** (`SKILL.md` Axis 1, step 1) — emit it exactly:

> `"Dekton — phase-out in progress, do not quote"`

*(Unless the four-condition materiality exception in §8.1 applies — **A-tier accounts only** — in which case Needs Review, a human call, and the item still scores 🔴 on the material dimension.)*

**Rationale (19 Jul 2026):** supply and lead-time pain, factory history with the material, and range consolidation — **not** a claim that Dekton is unfabricatable.

### 8.1 The exception is a FOUR-CONDITION materiality test, A-TIER ONLY — not "the client asked"

⛔ **The exception is available to A-TIER ACCOUNTS ONLY** `[R-DEKTON v1]` (ruled 3 September 2026). **For a B-tier account or below there is no exception at all: decline and substitute.** Read the tier from the linked Account record `[R-C1 v4]` before considering the test.

On an A-tier account, when **ALL FOUR** of the following hold, do **not** steer to decline/substitute — set **Needs Review** for a human decision:

1. Dekton is a **minor component** — ≤ 1 room / 1–2 pieces; **AND**
2. the **bulk of the job is other material**; **AND**
3. the job is **substantial** (~$10k+); **AND**
4. the **customer will not substitute**.

**Rationale:** do not walk away from a substantial A-tier job over one room. **The exception converts the OUTCOME to a human call. It never lowers the colour — the material line stays 🔴 either way** `[R-DEKTON v1]`. SteedForm would rather substitute in every case; the exception is not a route for any client who insists.

> ⚠ **Superseded wording.** Several documents still carry the looser sentence *"Do not quote on new Dekton work **unless specifically requested by client**"* (SteedForm Identity §Materials and §Definite No; Technical Standards §1 brand list). The corpus explicitly names and rejects that form: SteedForm Identity's own Job Screening Framework Axis 1 states the exception is the four-condition materiality test *"— **not** simply 'the client asked'"*, and Communications directs *"⚖ The exception is a four-condition test, not 'if the client insists.' … **Apply that test, not the looser wording.**"* The four-condition test is what this document carries, **and it is now registered as `[R-DEKTON v1]`** (3 September 2026), with the A-tier gate that no prior statement carried. ⛔ **The looser wording is RETIRED wherever it appears.**

### 8.2 Substitution recommendations by application

| Application | Recommend | Why |
|---|---|---|
| Outdoor / BBQ | **Neolith** | Proven outdoor rating, simpler fabrication; SteedForm's preferred sintered |
| Indoor benchtops | **Caesarstone Porcelain** | Better overhang allowances, standard adhesive |
| General use | **Smartstone Sintered** | Outdoor is **Conditional**, not approved — where the substitution is outdoors, the three conditions must be written **VERBATIM** into the flag: **"300°C max · non-combustible/fibre-cement backing · 10mm grill clearance"** *(Smartstone Quickstart V1.05, via Technical Standards §1)* |

### 8.3 The technical selling-against argument (verified against Dekton REV 09)

For the *"Why This Job Doesn't Fit (as spec'd)"* section:

- **12mm overhang restrictions** — at 12mm, Dekton L-shaped overhangs max **250mm**, restrictive against comparable porcelain at that thickness. ⚠ **At 20mm Dekton allows 500mm L-shaped — do NOT claim Dekton is the most restrictive brand at 20mm.** The overhang argument lives at 12mm.
- **Blanket mitre reinforcement** — Dekton requires reinforcement on **all** mitre edges regardless of application. Other brands require it situationally or not at all.
- **Proprietary adhesive** — Dekton mandates **Mastidek + Colordek** (brand-specific, limited colour range). All other brands use standard epoxy or polyester-based systems.
- **Tighter joint-near-cutout constraints** — Dekton requires 100mm at 20mm / 150mm at 12mm between a joint and any cutout. Standard for other brands is 50mm.
- ⚠ **Corner radii are NOT a differentiator** — Dekton's are sink R10 / hob R10 / other R5, close to the industry R10 default. **Do not cite radii in the argument.**

Frame the recommendation positively: *"The alternatives give the client better overhang flexibility, simpler fabrication, and faster turnaround — with no compromise on appearance or durability."*

---

## 9. Vein matching `[R-MA2 v1]`

**Level-3 vein match, or match-to-existing installed stone, is BLOCKING → Needs Review** `[R-MA2 v1]`. Feasibility is read live from `boolean_mm4r4qcp` **Bookmatch Available** on the Materials Library. The blocking reason to state: *feasibility and the 20–50% uplift are a human call before quote.*

**Below Level 3 the flag is NON-BLOCKING and fires on GEOMETRY ALONE** `[R-MA2 v1]` — a **veined colour on 2+ adjacent visible faces** (island + waterfall, book-match pairs, continuity runs) → 🟡. **Never wait for a stated client expectation:** the $20k job had none.

**Applies to ALL veined materials, not just natural stone.** Engineered (Zenith, Caesarstone, Lavistone) and sintered/porcelain (Dekton, Neolith, XTone) all use print technology that creates visible pattern differences between slabs. When a customer sees a join where the vein pattern breaks, they see a defect.

**The three-level framework (Technical Standards §9.3):**

| Level | When it applies | What changes | Cost impact | Communication |
|---|---|---|---|---|
| **1 — Standard awareness** | All veined materials, all jobs | At order entry confirm pattern expectations; at slab allocation aim for sequential slabs from the same batch; at programming orient pieces to minimise pattern break at joins | None — baseline good practice | Verbal at order confirmation |
| **2 — Planned matching** | Premium engineered/sintered, or customer-requested | Proactive slab selection for print compatibility; layout plan showing seam positions vs vein direction; possible extra half-slab if material waste is needed for alignment | Half-slab surcharge if extra material required; possible programming uplift | "What to Expect" one-pager at quote stage |
| **3 — Full vein match** | Natural stone, high-value projects, feature walls/floors | Block selection, sequential cutting, digital layout, client approval at multiple stages, dry-lay with photography, extended lead time | **20–50% material uplift, 20–50% labour uplift**, extended timeline | Full vein-match agreement with sign-off checkpoints |

**Why this is enforced — the $20k lesson (root cause, 28 April 2026).** SteedForm absorbed ~$20k in remake material on a single natural-stone job where **all** controls were missing: client-supplied natural stone (no control over block matching or slab pairing) · no layout plan or vein-orientation agreement before fabrication · slab selection *and* programming both wrong · the expectation surfaced only at install · SteedForm wore the full cost despite the material being client-supplied, because the fabrication/orientation error was on SteedForm's side. **On any job where vein matching matters, at least THREE controls must be in place: (1) upfront discussion documented, (2) layout plan with vein direction, (3) client sign-off before cutting.**

**Interim rules (Technical Standards §9.3, effective immediately):** on every job with 2+ slabs of a veined material, confirm at order entry whether the customer has pattern-continuity expectations; if yes, note it on the order and allocate sequential slabs from the same batch where available; at programming, orient pieces to align vein direction across joins and photograph the layout plan; a Level-3 request is quoted separately with material and time uplift, **never absorbed in the standard quote**; on any declined vein-match request use the *"Capability Is Not Offering"* principle — explain what SteedForm does offer (Levels 1–2) rather than just saying no.

**Interactions.** Boxed islands and waterfalls are 🟡 always, and **in a veined colour add the vein-continuity line**. Faceting is often the *recommendation* on veined stone (§5). **60mm lamination is never used on veined stone** (two glue lines break the vein twice). Assemble On Site on veined stone is a heightened field-join QC case (§3.3). **Kaya face-printed vein → 🟡 note: it cannot be re-polished.**

---

## 10. Material vocabulary `[R-MATERIAL-TERMS v1]`

**Supplier commercial ranges, slab format, finish and colour are separate evidence** `[R-MATERIAL-TERMS v1]`. The operative distinctions:

| Term | What it is | What it is NOT |
|---|---|---|
| **`M2`, `M4`** | Supplier commercial **range/tier labels**, comparable to Essentials or Deluxe | Not colour/material codes, not material class, not thickness, not finish, not slab size. **Do not search them as library colours and do not infer material capability from them** |
| **Bare `Zenith`, `Zenith Surfaces`, `Stone Ambassador – Zenith`** | The **Zenith engineered-stone brand/range** | **Must NOT trigger porcelain/sintered or printed-face restrictions.** Zenith is full-body throughout; the by-name carve-out for Ottoman Grey and Rosè was retired 7 Sep 2026. Still read `color_mm6hz0dd` live — the column is the authority for the fact, not the brand |
| **`Dekton Zenith`** (explicit) | **Only** this form means Dekton brand with Zenith colour → the Dekton phase-out applies (§8) | A bare "Zenith" is never Dekton |
| **`GRANDE`** | **Slab size / format** | Not supplier, brand, range, colour, finish or Material Sub-Type |
| **`Polish`** | Canonicalises **only** to `Polished` | **Never** equivalent to `Matt` or any other finish |

Two further clauses of `[R-MATERIAL-TERMS v1]`:

- **At Lead/quoting stage**, an evidenced brand/range or commercial tier may support an allowance while exact colour remains TBC. **Exact colour/revision must be confirmed at Order commitment** before manufacture, where the accepted product requires it.
- **Materials Library linking remains exact and unique** — no fuzzy, "contains", or closest-result matching.

Related vocabulary facts held elsewhere in this document: **"Smartstone" always means Smartstone Sintered** (sintered-only brand, §1); **an `Engineered Stone` Material Type does not mean full-body** (§2); **mitre ≠ lamination** — they are different techniques and briefs and quotes must use the correct term (§4.1).

---

## 11. What NOT to flag — the silence half of the screen

**`SKILL.md`: "The estimator knows the standard rules. Only flag what breaks them."** A screen that reports standard practice back to an estimator buries the one line that mattered. These are standard and are **not** flagged:

| Do NOT flag | Why it is standard |
|---|---|
| **Standard edge treatments** | All straight edges >20mm are mitred — that is the default build path (§4.1), not a finding. Don't mention it. |
| **Standard thicknesses — 20mm splashbacks** | Baseline product. |
| **Standard sink cutouts** | Routine CNC work; the cutout only becomes a finding when it breaks a rule (narrow web, cutout-to-joint clearance, flush mount, a radius conflict per §6.2). |
| **Standard corner radii** | The industry R10 default is not news. The finding is the *conflict* (§6.2), not the radius. |

⚠ **The carve-out — 50mm and 60mm are NOT in this "don't mention it" bucket** `[R-PROFILE v5]`. The ratified profile/build rules are scoped **to 40mm**: 50–80mm carries its own cost step and >80mm is a hard cost cliff (§4.1). A 60mm engineered island edge is routine work that still prices differently from 40mm. **Flag the thickness so it is priced — do not flag it as a *risk*.** *(The earlier "50mm vanities, 60mm kitchen edges → do not flag" wording suppressed the cost step and is superseded.)* **RULED 3 September 2026: D1 scores a 50–80mm engineered mitred build 🟡 AMBER, on the cost difference** — an amber that prices the step, never a doubt about wanting the job. **Engineered ≤ 40mm is 🟢**, and the minimum mitred build-up is always 40mm.

**Content Rule 8** (`SKILL.md`): *"**CS Porcelain caveats are only relevant if CS Porcelain is specified.**"* Do not raise Caesarstone Porcelain restrictions on a job in another material — it is noise. The principle generalises across this whole document: **flag anomalies, not standard practice**, and never a brand caveat for a brand that is not in the spec. The same discipline governs supplier proximity (§1.2 — a local brand is ALL CLEAR and is not raised at all) and the outdoor caveats (§1.1).

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed every other item this document used to carry — OR-01, OR-02, OR-03, OR-04, OR-07, OR-09, OR-17, OR-18, OR-19, OR-32, OR-33 and OR-37 are **ruled**, and their positions are stated plainly in the sections above. Two items remain:

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-38** | The wider implications of the OR-07 ruling, **held for scoping**: is the Screening Philosophy / distance-from-optimum lens retired, and does all stone move to one ladder? The owner's notes *"screening philosophy now redundant"* and *"all stone to follow same rules"* are **wider than the question that was asked and are NOT ruled** | §7.1 — the lens stands and is used exactly as written until this is scoped |
| **OR-26** | The CRM boards could not be reached, so **no column identifier has been verified against the live board** — `color_mm4qt817`, `dropdown_mm4rq7jd`, `color_mm6hz0dd`, `boolean_mm4r4qcp`, `color_mm4zdfnd`, `long_text_mm4zayzp` | §1, §2, §6.1, §9 — every live read this document instructs. A tag check is not an identifier check: confirm against `08-board-and-column-registry.md` before relying on an id |
