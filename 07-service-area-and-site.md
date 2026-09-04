# 07 — Service Area, Site Access and Timeline

**Status:** Active — screening reference for the Deep Screen app
**Owner:** Estimating / MD
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns:** service-area determination and its sources; the install-range frame and its bands; the Supply Only delivery model at screening; the address-lookup and site-access assessment; **the confirmed vehicle, crane and lifting figures — this document is now their authoritative home**; occupancy as a screening fact; site-readiness preconditions for a measure; the two-factor timeline rule; the interstate-material question and which position the screen currently applies.
- **Does not own:** freight, travel and delivery *pricing* (pricing document); measure procedure and on-site install procedure (measure and installation standards); material, edge-profile and appliance capability; account tiering and client fit; decline/expectation-reset comms templates. Rule statements themselves are authored only in `01-rule-register.md`.

---

## What this document decides

Whether SteedForm can physically reach, park at, get into and work on a given site — and, where it cannot, which delivery model the job converts to. It never produces a decline on geography: out of area converts to Supply Only, it does not disqualify — **at any km, and on either level of the install-range frame** `[R-AREA v1]`. It also decides whether the requested install date is achievable. It also carries the interstate gate: **whether interstate material may be sourced is a CUSTOMER-CLASS question owned by the Client dimension** `[R-INTERSTATE v1]`, and §7 states it. Where a street address is held, it requires the address to be looked up rather than reasoned from the suburb.

---

## 1. Service area determination

**The Serviceable Areas board `5029634649` is read live on every screen and is authoritative wherever it lists the suburb or area** `[R-REF v2]`. Only where the board is silent does the road-distance fallback apply.

*(Board and column identifiers are registered in `08-board-and-column-registry.md` and should be cited from there. This document quotes the board id for readability; it does not own it, and if the two ever disagree the registry is the one to check and correct.)*

| Board Zone label | Screening outcome |
|---|---|
| **Full Service** | In area. Full measure + fabricate + install scope. |
| **Boundary — verify** | **Needs Review** to confirm before proceeding. |
| **Supply Only** | Supply Only delivery model — see §2 `[R-SUPPLYONLY v2]`. |
| **Board silent (suburb/area not listed)** | Apply the fallback below. |

**Fallback, only where the board is silent:** approximately **100 km ROAD distance from Wingfield** (163–165 Cormack Rd, Wingfield SA 5013). **Never straight-line.**

### What the board actually holds — verified 3 September 2026

**608 rows**, seeded from the Australian Postcodes dataset and imported **16 August 2026**, with driving distance computed by **OSRM from 163–165 Cormack Road, Wingfield**.

| Zone | Rows |
|---|---|
| Full Service | 504 |
| **Supply Only** | **103** |
| **Boundary — verify** | **1** |

Three things follow, and each corrects something this document used to say:

**1 · The board is comprehensive, and the 100 km line is what it RUNS ON — not a fallback for its silence.** The board's own note states it: *">100 km records are classified Supply Only under SteedForm operating policy."* **Zero rows disagree between their zone and their distance.** So `[R-AREA v1]`'s description of ~100 km road distance as *"the fallback where the board is silent"* **understates the board**: the heuristic and the board are the same rule, applied by the board across 608 postcodes. ⚠ **The order of precedence does not change** — read the board, and use the 100 km line only where a postcode genuinely is not listed. What changes is the expectation: **a silent board should now be rare, and a miss is worth investigating rather than routinely falling through.**

**2 · There are 103 Supply Only zones, not two.** Port Lincoln (639 km) and Kingscote (196 km) are both there and both correctly zoned — **they are simply two of a hundred.** §2 names them as the *confirmed established-customer* zones, and that is what they are; it must not be read as the extent of the Supply Only map. ⛔ **The zone-scoped half of `[R-SUPPLYONLY v2]` — "distance is NOT a risk" — still scopes to those two established-customer zones only** (see the scoping note above), **not to all 103.** An unfamiliar Supply Only postcode is still an out-of-area conversion with freight and packaging priced in.

**3 · The 30 / 60 km bands do not exist on the board.** They are a document-only construct — real as a pricing and staffing frame, but **nothing reads them off a column.** Do not go looking for a band field.

⚠ **`Boundary — verify` — one row, and NO RULE HANDLES IT.** The zone table above routes it to Needs Review, which is the right instinct, but **no registered rule states it.** Raised as an open question in `10-open-rulings.md` (**OR-39**). **Interim, and it is an interim, not a ruling:** treat it as **Supply Only pending confirmation** and flag it — fail toward the flag `00`. ⛔ **Never read it as Full Service.**

⚠ **Coverage is not identity.** The export confirms what the board *holds*; it confirms **no identifier**. The Serviceable Areas board id `5029634649` remains **unverified** — OR-26 stands. See `08-board-and-column-registry.md` §7.

**Always record which source decided** — board Zone label, or road-km estimate — in the flag, with the board item id cited `[R-REF v2]`.

⛔ **Out of area NEVER declines.** The job becomes **Supply Only (− FREIGHT)**, noted `[R-AREA v1]` `[R-SUPPLYONLY v2]`. Distance is not a decline reason at any km.

**Rendering while the conversion is pending — RULED, and its authority now registered** `[R-AREA v1]`. Out of area with the Supply Only conversion **undecided** renders **🔴, a blocking flag routing to Needs Review — never a decline**; the citation is the Supply Only conversion, not a disqualifier. Once `Job Type` is set to `Supply Only [− FREIGHT]` the conversion is **applied** and the lane drops to **🟡** *"supply-only conversion applied — freight/packaging priced"*. (Lead Risk Assessment Standard, I6, and its rendering rule 2b.)

✅ **OR-06 and OR-29 are CLOSED (3 September 2026).** The question *"is out-of-area authorised to render red at all?"* is answered **yes**: out of area while the Supply Only conversion is undecided is a **layer-1 blocking condition** on `[R-BLOCK v3]`'s closed list, registered as `[R-AREA v1]`. The earlier doubt arose because the blocking list was read as a single six-rule set; **it has two layers, and out-of-area sits on layer 1.** The undecided-conversion 🔴 is authorised, and the conversion-applied lane is 🟡.

### The install-range frame — TWO LEVELS, both ruled `[R-AREA v1]`

The three frames that used to coexist are resolved into one structure. **The Serviceable Areas board still decides wherever it lists the area; ~100 km road distance is the fallback where the board is silent.** The frame below sits underneath that, and describes how far SteedForm installs.

| Level | Figure | Screening effect |
|---|---|---|
| **Outer boundary** | approximately **1 to 1.5 hours' drive** from Wingfield | the practical edge of the install range. Beyond it, expect the Supply Only conversion — **not a decline** |
| **Internal bands** | **≤ 30 km** standard · **30–60 km** flag · **> 60 km** assess | recorded on the distance audit and reflected in the I6 lane |

⛔ **THE BANDS FLAG; THEY NEVER DECLINE.** *"> 60 km = travel cost, overnight crew, freight priced in **or the job declined**"* is **retired**: the decline branch does not survive `[R-AREA v1]` or `[R-SUPPLYONLY v2]`. A band is a pricing and staffing input and a visible flag — it is never a verdict on whether SteedForm wants the work.
⚠ **The two levels do not compete with the board.** Where the Serviceable Areas board lists the suburb, its Zone label decides `[R-REF v2]`; the boundary and the bands describe distance, and distance changes the **delivery model**, never the answer.

⚠ **Scope of "distance is not a risk".** `[R-SUPPLYONLY v2]`'s sentence *"Distance is NOT a risk and NOT a decline"* sits inside that rule's *what changes at screening* block, which describes the **two confirmed Supply Only zones only** — **Port Lincoln 5606** and **Kingscote / Kangaroo Island 5223** (§2). It means that **in those zones** the 646 km and the KI sea crossing are the **client's** transport and are never scored as SteedForm freight, access or lifting risk. It does **not** say distance goes unscored on out-of-area work generally: elsewhere, out-of-area still fires I6, still records the road distance, and still carries freight and packaging as a priced input. **The "never a decline" half of the rule is general; the "not a risk" half is zone-scoped.** Reading the zone-scoped half as universal is a live misreading in the set.

**Distance audit — mandatory on every screen.** Record the **actual road distance** from Wingfield to the **build-site** address (not the client's residential or billing address) as a header-level field, e.g. "Distance from SteedForm (Wingfield): ~20 km — Adelaide metro". Verify with Google Maps or equivalent. Distance is a *recorded fact and a pricing input*; on its own it is never the verdict.

**Superseded positions — do not carry:**

| Stale position | Where it still appears | Correct position |
|---|---|---|
| "Outside geographic range with no install solution → **Decline**", listed as a hard disqualifier | `Sales Qualification.md` | Out of area is **never a decline reason**; it converts to Supply Only `[R-SUPPLYONLY v2]` |
| ">60 km = ASSESS — travel cost, overnight crew, freight priced in **or the job declined**" | `SteedForm Identity.md` §Job Screening Framework Axis 2 | The **band survives; the decline branch does not.** >60 km is an assess-and-flag band `[R-AREA v1]`, and out of area converts rather than declines `[R-SUPPLYONLY v2]` |
| "Supply only isn't something we offer on residential work" | `Communications.md` T-DECLINE-08 optional block | Superseded for the confirmed Supply Only zones, which are established regular customers `[R-SUPPLYONLY v2]` |

⚠ **Legacy data.** Leads and deals in the confirmed Supply Only zones screened **before 27 Jul 2026** may carry wrong flags (out-of-area, measure access, install lifting, sea crossing) because the zone board was silent and the fallback was the ~100 km road heuristic. Approximately **8 live deals** are affected — six Port Lincoln, two Kingscote — and are due a re-screen `[R-RESCREEN v1]`. Nothing screens automatically in the interim, so this is a human/Claude duty.

---

## 2. Supply Only `[R-SUPPLYONLY v2]`

**Supply Only is a different delivery model, not a degraded one, and never a decline reason.**

**Confirmed zones — these are the ESTABLISHED-CUSTOMER zones, not the extent of the map:**

| Zone | Postcode | Standing |
|---|---|---|
| Port Lincoln | 5606 | Established regular customer |
| Kingscote / Kangaroo Island | 5223 | Established regular customer |

⚠ **The board zones 103 postcodes as Supply Only** (§1). These two are the ones with a standing relationship behind them, and the special treatment below — distance not scored as risk, sea crossing not scored at all — **attaches to that relationship, not to the zone label.** A Supply Only postcode SteedForm has never worked in is an ordinary out-of-area conversion: still never a decline, but freight, packaging and handling are priced and flagged.

**The process, in order:**

| # | Step | Owner |
|---|---|---|
| 1 | Client sends their own A-frame | Client |
| 2 | Manufacture off **the client's measurements** — SteedForm does **not** measure | SteedForm (off client dims) |
| 3 | ⛔ Final CAD to the customer for sign-off **before** manufacture — **hard gate** | Customer |
| 4 | SteedForm loads the A-frame | SteedForm |
| 5 | The **client's** transport company ships it | Client |

**What changes at screening:**

| Dimension | Effect |
|---|---|
| **Distance / freight** | Not a risk and not a decline. The 646 km to Port Lincoln, and the sea crossing to Kangaroo Island, are the **client's** transport — never scored as SteedForm freight, access or lifting risk, and never as out-of-area. ⚠ **This applies to the two confirmed zones in the table above, not to out-of-area work generally** — see the scoping note in §1. |
| **MEASURE** | Does not apply in the usual way — SteedForm never attends site, so site access, measure-readiness and occupancy are irrelevant. **What replaces it:** dimensional responsibility sits with the **CLIENT**, and must be **recorded explicitly** ("dimensions are client-supplied") so liability for a mis-measure is unambiguous before anything is cut. Renders 🟡 with a written dims-responsibility line (Lead Risk, Me7). |
| **INSTALL** | Does not apply. No SteedForm install, no lifting, no site conditions, no install-readiness rating. |
| **CAD sign-off** | ⛔ **Hard gate.** Nothing is cut until the customer has signed off the final CAD. With SteedForm's own measure out of the process it is the only check between the client's numbers and finished stone. |

### Sea crossings — RULED `[R-SUPPLYONLY v2]`

✅ **OR-15 is CLOSED (3 September 2026).** The skill's unconditional *"a sea crossing always escalates"* is **scoped**, and the scope is the confirmed zone:

| Where | Treatment |
|---|---|
| **Inside a confirmed Supply Only zone** (Port Lincoln 5606 · Kingscote / Kangaroo Island 5223) | The crossing is the **client's transport** and is **not scored at all** — not as freight, not as access, not as lifting risk |
| **Outside a confirmed Supply Only zone** | ⛔ **ALWAYS escalates to a human, regardless of km.** It is not ordinary distance, and the Serviceable Areas board does not settle it |

⛔ **Do not resolve an out-of-zone sea crossing on kilometres.** A short crossing is not a short trip: the escalation exists because a water leg changes handling, timing and liability in ways road distance does not describe. **Escalation is not a decline** — a human decides, and out of area still converts rather than disqualifies `[R-AREA v1]`.

---

## 3. Site assessment `[R-SITE v1]`

⛔ **Whenever a street address is held, the screen LOOKS IT UP.** Site access is assessed from the **actual address**, never reasoned from the suburb. A postcode gives distance; it does not tell you what the building is, who trades in it, where the truck unloads, or whether the truck can stay. Where an address is held the lookup is **not optional** — its absence is a defect in the screen, not a gap in the enquiry.

**Four questions, answered and recorded in this order:**

| # | Question | What counts as an answer |
|---|---|---|
| 1 | **What is the building, and is it occupied?** | Read the live tenant directory. A trading tenancy at street level makes it an **occupied commercial building** — a C7 / Me1 fact **established at screening**, not an assumption to confirm later. |
| 2 | **Where does the truck unload?** | Street frontage, loading zone, dock or laneway — **and** whether a council permit, traffic management plan or insurance certificate is a **precondition with lead time**. |
| 3 | **Where does the truck GO during the works?** | Published clearances checked against the confirmed vehicle envelope (§4). "The crew parks somewhere" is not an answer: no vehicle on site means no tools, and no removal of packaging, offcuts or silica-controlled waste. |
| 4 | **What is the path from unload point to the work area?** | Measured against the **LARGEST piece**, never the average one. |

**Evidence bar and unknowns:**

- At **LEAD** the site bar remains **suburb / postcode** `[R-EVIDENCE-BAR v2]` — **this rule does not raise it**.
- Where only a suburb is held, no lookup is possible: **say so** and suffix the access lanes **"— (insufficient info)"**.
- 🟢 **Unknown is never green.**
- Where the screen **cannot browse**, flag the site assessment as **outstanding** and refuse to score Install or Measure green. Never substitute a suburb-level assumption for a lookup that was not done.
- At **ORDER** the site bar rises to the full **SITE street address**, plus the **DELIVERY address whenever it differs from site** — the supply-only / freight case `[R-EVIDENCE-BAR v2]` `[R-SUPPLYONLY v2]`. Billing address is an accounts field and is never a screening bar.

**Where the lookup lands in the risk strip:** I1 is the primary home of the address lookup; Me1 carries the occupancy answer from the same lookup, on the same citation (Lead Risk Assessment Standard).

### Worked example — Veriu Hotel, 80 King William Street, Adelaide (26 Aug 2026)

The screen scored CBD access as a comfortable priced amber **from the suburb alone**. A four-minute lookup showed:

- the building is the **trading William Grenfell Centre**, with a **Westpac branch on the ground floor** — an occupied commercial building, established as fact at screening;
- published clearances at **every car park in the precinct are 1.96–2.06 m**, which **excludes the truck entirely**.

**Three lanes moved** — C7 and Me1 to 🔴, I1 to the top of 🟡 — and the question "where do we park for the day" turned out to have no answer. The **distance** audit was already mandatory in every brief; the **address** was not. That is the gap this rule closes.

### Access flag classes (non-blocking, priced)

| Condition | Screening treatment |
|---|---|
| Ground floor, straight run from road | Ideal — no flag, do not mention |
| Ground floor with turns, corridors or tight doorways | 🟡 additional person / lift — minor surcharge |
| Upper floor, anything heavier than a vanity | 🟡 **flag upfront at first builder contact.** Builder confirms the vertical access method; cost priced at quote |
| Internal / residential lift | 🟡 check car dimensions against piece sizes — benchtops over ~2500 mm will not fit a standard residential lift |
| Tight internal rooms (butler's pantry, WIP, powder room) where slab length approaches room width or diagonal | 🟡 room-geometry flag (Lead Risk, I2) |
| Stairwell carry | Acceptable for **vanity-sized pieces only** (typically ≤1500 mm, 20 mm, ≤35 kg). Kitchen benchtops, islands, splashbacks and feature pieces escalate to a mechanical lift |
| Crane / hoist / telehandler required | 🟡 — **needing a crane changes the price, never whether we want the job** (Lead Risk, I3) |

**The contract term:** *"Vertical movement by builder, horizontal movement by SteedForm."* It must be agreed at order/quoting stage and written into the contract; if it is not agreed before install day the install may not complete and a return visit is chargeable.

**Optimal handling baseline** (every job and every piece is assessed against it): piece up to **3000 × 1200 mm**, clear line of sight from truck to install location with no turns or level changes, trolley or jockey wheel, **exactly two lifts** (truck→trolley, trolley→cabinets), **two people minimum**. Any deviation requires additional labour, mechanical lift, or both.

### Site readiness — preconditions that must exist BEFORE a measure

A site can be reachable, parkable and enterable and still not be measurable. These are the conditions that must be true before a measure slot is spent.

| Precondition | Position |
|---|---|
| **Cabinetry professionally installed** | Photographs of the completed cabinetry confirm the site is ready to measure (`06` §3). Existing, DIY-kit, re-used or relocated cabinetry is a stated disqualifier for installation |
| **Alfresco scope — the cabinetmaker's shadowline** `[R-ALFRESCO v1]` | A **12 mm thick × 50 mm wide** shadow line, installed **by the cabinetmaker**, **must be in place before site measure can be completed**. 12 mm compact, edged MDF or painted edge. **Not required where the benchtop is thicker than 40 mm** |
| **Unverified appliance or sink** | The physical unit must be **at SteedForm before measure** `[R-MA5 v3]` — a supplier CAD is interim only and never closes the gate (`06` §5) |

⛔ **A MEASURE THAT ARRIVES TO NO SHADOWLINE IS A WASTED TRIP.** On any alfresco or barbecue scope, **flag the shadowline at first builder contact** — not at booking, and never on the day. It is the cabinetmaker's work, it sits behind the stone, and its absence is only visible once someone is standing there. ⚠ **Do not confuse it with the fibre cement**, which is **6 mm or 9 mm** and runs the whole alfresco surface behind it; "12 mm fibre cement" is a retired offering and conflating the two is a live error in the corpus. The alfresco material and substrate rules are in `05-material-and-capability.md`; only the measure precondition belongs here.

**Where an unmeasurable site lands in the timeline:** a site that is not measurable now falls under the **22-working-day** clock, not the 12-working-day floor — see §6.

---

## 4. The vehicle, crane and lifting figures — AUTHORITATIVE HOME

✅ **OR-28 is CLOSED (3 September 2026). The `Lift Calculation & Crane Allocation SOP` DOES NOT EXIST.** `Technical Standards.md` §7 named it as the authoritative spec and `Installation Standards.md` cited it three times, but the document is not in the knowledge base and never was. The owner directed that the confirmed figures be **promoted to whichever source does exist — and that source is THIS DOCUMENT.**

⛔ **These figures now live here. This section is their authoritative home**: the **410 kg at 5.0 m radius** safe lift, the **7 m vertical reach**, and the **vehicle envelope**. Cite this section. ⛔ **The dangling citation to the missing SOP is REMOVED** — do not carry *"Authoritative spec: Lift Calculation & Crane Allocation SOP §4"* anywhere, and where `Installation Standards.md` still cites it, that citation points at nothing and must be repointed here.

Figures confirmed **22 Jul 2026** against the EMMATT purchase invoice #40020, the Isuzu spec sheet and the Cormach reach chart (as recorded in Technical Standards §7).

### Vehicle — Isuzu NNR 45-150 AMT MWB IFS Traypack (built Oct 2022)

| Attribute | Figure |
|---|---|
| Width | ~2.06 m |
| Cab height | ~2.24 m |
| Clear travel envelope, crane stowed | ≈ **2.5 m wide × ~3.0 m high** — **approximate, and it stays approximate** |
| GVM (max laden) | **4,500 kg** |
| Kerb weight (empty) | 2,285 kg |
| Surface-load check | Will the driveway / pavers bear a **fully-laden 4.5 t truck**? |

⚠ The ≈2.5 × ~3.0 m access minimum **retires the earlier ~3.5 × 4.0 m placeholder**, which was too generous.

✅ **OR-27 is CLOSED (3 September 2026), answered N/A.** The crane-stowed travel height is **not being measured**. The `~3.0 m` is derived rather than tape-measured and **remains an approximate working figure** — that is the settled position, not an outstanding action. **Drop the "TODO: tape-measure the built truck" wherever it still appears.** It stays approximate because the operative test is the *published clearance* at the site, checked against it with margin — and every clearance found so far (1.96–2.06 m in the Adelaide CBD) fails by a wide enough margin that a centimetre on the truck would not change the answer.

⚠ **Most CBD car parks are ~2.0 m and will not take the truck.** Verified in the precinct clearance range found at the Veriu lookup: 1.96–2.06 m.

### Crane — Cormach MICRO M20A, truck-mounted

| Attribute | Figure |
|---|---|
| Safe lift per piece | **410 kg at 5.0 m radius** — the conservative floor at full reach; capacity **rises at shorter radius** |
| Vertical reach to lift point | **7 m** = 5.0 m rated boom reach + ~2 m crane mount height above ground |
| Condition | Truck parked **directly below** the lift point |
| Beyond this | Any install needing vertical access beyond 7 m, or non-standard access, is discussed and quoted **at the sales stage** — never discovered on install day |
| Authority | **This section** `07` §4. There is no lifting SOP — see the note at the head of this section |

✅ **The 7 m figure is CONFIRMED.** MD confirmed it on **21 Jul 2026** against the Cormach MICRO M20A load chart, and Technical Standards v2.10 records the disambiguation (5 m rated boom / ~7 m effective from ground). The three **"⚠ MD confirm the 7 m figure"** flags still sitting in `Installation Standards.md` §2 are **stale and must not be carried**. Note also that 410 kg is the floor at full reach, not a flat per-piece limit — `Installation Standards.md` states it flat and is silent on the truck-directly-below condition.

⚠ **Both figures were confirmed against real sources — the invoice, the spec sheet and the load chart — and none of them was the missing SOP.** Nothing about them was ever in doubt; only their *filing* was, and that is what the promotion above fixes.

---

## 5. Occupancy `[R-OCCUPANCY v1]`

| Site condition | Screening outcome |
|---|---|
| **New build, builder-controlled** | 🟢 all clear |
| **Occupied dwelling** | 🔴 **BLOCKING → Needs Review — occupancy carve-out, NEVER an auto-decline** `[R-OCCUPANCY v1]` (carve-out ratified #61) |
| **Ongoing concern (cafe, bar, retail)** | 🔴 **BLOCKING → Needs Review — occupancy carve-out, never an auto-decline** `[R-OCCUPANCY v1]` (#61) |
| **CBD construction site, stripped out** | 🟡 assess — parking, loading dock, site hours |

✅ **OR-11 is CLOSED (3 September 2026) and the condition is now REGISTERED as `[R-OCCUPANCY v1]`** — a layer-1 blocking condition on `[R-BLOCK v3]`'s closed list. It had been applied as blocking since screening began with no rule behind it.

- 🔴 here means a **blocking risk flag routing to Needs Review** — a 🔴 RISK, a human call — not a ⛔ capability stop and not a decline `[R-ANDON v2]`.
- ⛔ **THE DECLINE LETTER MAY ONLY BE SENT AFTER A HUMAN REVIEW.** `T-DECLINE-05` is what a person sends **once they have decided to decline**. It is **never a triage output**, and no screen may emit it on occupancy evidence alone.
- ⛔ **Occupancy is ESTABLISHED BY THE ADDRESS LOOKUP, NEVER ASSUMED** `[R-SITE v1]` `[R-OCCUPANCY v1]`. A trading tenancy at street level makes it an occupied commercial building — a fact at screening, not something to confirm later. **A keyword in an email is not occupancy evidence.**
- **"New build" means new-cabinetry work, not new construction** (#59 ↔ #61, 21 Jul 2026). An occupied-dwelling renovation receiving a new kitchen through a confirmed strong cabinetmaker **can pass**; otherwise it declines on the retail gate, not on occupancy.
- Occupancy is a **single fact scored in two lanes** — C7 (client/operating environment) and Me1 (can we get in to measure) — on the **same citation**. Establish it from the address lookup, never assume it `[R-SITE v1]`.
- Measuring in an occupied or trading site is 🔴; CBD site-hours or parking constraints on the measure visit alone are 🟡.
- ⛔ **`SteedForm Identity.md`'s "Tenanted occupied residential building → DECLINE" is RETIRED**, as is "Occupied building with active tenants → DECLINE" `[R-OCCUPANCY v1]`. Both are superseded by the carve-out, and the reason is worth stating: **a machine may not turn away an occupied job on keyword evidence.** A stripped site in a CBD building scores 🟡, and everything above the 🟡 goes to a person.

---

## 6. Timeline — the two-factor rule

**Flag timeline pressure when the requested install date is earlier than:**

> (measure booking notice **~2 weeks**) + (**12 working days** measure-to-install) ≈ **22 working days from enquiry**

**If the site is measurable NOW, the floor is 12 working days from measure.**

| Property | Value |
|---|---|
| Verdict class | **Non-blocking** — the lead may stay Qualified; the flag travels to the deal `[R-BLOCK v3]` |
| Colour | 🟡 (Lead Risk, C6) |
| Input | ⛔ **PROSE ONLY.** The requested date as stated in the enquiry. **The Client Required-By column is RETIRED and must not be read** — see the note below `[R-BLOCK v3]` |
| What the flag must say | ⛔ **The flag DOES THE MATHS** — state the **earliest realistic install date**, never just "tight" |
| Follow-up | Confirm feasibility against slot capacity **before** quoting a date |
| Supersedes | The earlier flat 15-working-day proposal (Q7, decided 20 Jul 2026) |

⛔ **The two-factor rule now reads PROSE ONLY (RULED 3 September 2026, OR-24).** The **Client Required-By column is being RETIRED**: neither `date_mm64jz0c` nor `date_mm5ck0y1` is to be relied on, and both identifiers move to the retired table in `08-board-and-column-registry.md`. Take the requested date from the enquiry text. **Do not reinstate either column, and do not treat a blank column as "no date requested"** — that was always the silent-failure mode, and removing the column removes it.

**Supporting service timelines** (Technical Standards §7, from the SteedForm SLA guidelines — these are the SLA targets the two-factor rule is built on, not separate screening tests):

| Stage | Target | KPI |
|---|---|---|
| Quote response | 48 hours maximum | >95% on time |
| Job creation | Same day as written approval | — |
| Site measure proposal | Within 7 days of all details received | — |
| Site measure confirmation | Within 7 days (cabinetry must be "Ready to Measure") | >90% ascertain all info without a return visit |
| Production schedule | 10 days from customer sign-off to install (material must be in stock) | >95% meet a 12-day timeframe |
| Invoicing | Within 3 business days | >95% on time |
| Install completion | Within agreed timeframe | >90% |

⚠ The two 7-day measure stages are what the "~2 weeks measure booking notice" reflects. The production figures (10 days / 12-day KPI) are **calendar-framed and anchored on sign-off**, while the two-factor rule's 12 is **working days anchored on measure**.

### Production lead time — what was ruled, and what is still open (OR-20)

**Ruled on 3 September 2026:**

| | Figure |
|---|---|
| **The SLA** | **10–12 days** |
| **The current ACTUAL** | **14–16 days** |
| **The owner's intent** | bring the **actual back to the SLA** — the gap is a performance problem to close, not a target to restate |

**RULED 3 September 2026** `[R-LEADTIME v2]`. **Lead time is tier-dependent** — the two figures were never a conflict.

| Account | Measure-to-install | Two-factor threshold from enquiry |
|---|---|---|
| **A-tier** | **10–12 days** — scheduled to meet the SLA | ≈ **22 days** |
| **Everyone else** | **14–16 days** — the current actual | ≈ **24–26 days** |

⛔ **An UNTIERED account takes the non-A figure** `[R-ENTITY v1]`. Never quote the A-tier date to an account that has not been confirmed as A-tier — fail toward the longer date.

⚠ **That is 128 of 188 accounts — and a blank tier means UNVERIFIED, not "forgotten"** (owner, 3 Sep 2026). Customer Tier is **68% blank** (`08` §7.2), so most accounts take the 14–16 day figure. ⛔ **That is the right answer, not a backlog.** An account nobody has tiered is an account nobody has vouched for, and the SLA figure is what SteedForm schedules **for A-tier customers it has committed to** — everyone else gets the actual. **The blank is doing real work: it is the difference between a commitment and an estimate.**

**So the residual risk is narrow, and it is the only part worth chasing:** a genuine A-tier customer sitting untagged, quoted a date six days longer than the one SteedForm would actually hit for them. That is a **spot-check of the known A-tier relationships against the board**, not a project to tier 128 accounts. ⚠ **Do not "fix" the 128 by bulk-assigning a tier** — a tier assigned to clear a blank is worse than the blank, because it converts an honest *unverified* into a false *verified* and the fail-closed behaviour disappears with it.

⚠ **Using the A-tier threshold on a non-A job under-fires the flag by about a working week**, on exactly the accounts least able to absorb a slipped date. Resolve the tier before computing.

⚠ **Unit not stated.** Recorded as **working days**, consistent with the two-factor rule these feed. The source SLA table is calendar-framed and anchored on sign-off, and the two have never been reconciled — **confirm before the app quotes a date to a customer.**


⛔ **This matters because the screening flag states an EARLIEST REALISTIC INSTALL DATE, not a vague "tight".** **Quoting the 10–12 day SLA while production actually runs 14–16 days would UNDERSTATE that date** by up to six days, on a flag whose entire purpose is to be realistic. Until OR-20 is answered, **do not present an SLA-derived date to a customer as if it were the realistic one**: state the date, say which figure it was built from, and flag the gap for the reviewer.

**Site measurability feeds the maths.** Where cabinetry is not installed, the dwelling is staged, a "site ready by" date is given, or more than one visit is implied, that is 🟡 (price the visits) **and** it means the site is **not measurable now** — so the 22-working-day clock applies rather than the 12-working-day floor (Lead Risk, Me2 → C6).

---

## 7. Interstate material

**RULED 3 September 2026** `[R-INTERSTATE v1]`. Interstate-sourced material is a **customer-class gate**, and it is owned by the **CLIENT** dimension — not a Material amber, and not a decline trigger in its own right.

**The gate:** interstate scope is considered **only for an A-customer OR a commercial project** — either qualifies on its own. **A non-A residential job requiring interstate material is DECLINED on supply risk.**

⚠ **Why the dimension matters.** The old M3 rung scored interstate as a priced 🟡 under Material, which is where supply exposure lives. But the test is *who the customer is*, not what the material is. A decline outcome sitting in a 🟡 Material rung was **unhomed** under the closed six-heading taxonomy — M3 cannot emit a decline. It now homes under Client.

**`T-DECLINE-05` keeps its interstate trigger line.** Interstate-only material on a small scope with no existing supplier relationship remains a valid ground for that letter — sent, like every occupancy-class decline, only after a human review `[R-OCCUPANCY v1]`.

| Case | Outcome |
|---|---|
| **A-customer**, any scope, interstate material | Gate passed — proceed, priced |
| **Commercial project**, interstate material | Gate passed — proceed, priced |
| Non-A **residential** job requiring interstate material | **Declined on supply risk** `[R-INTERSTATE v1]` |
| Brand not local, or brand unknown | Supplier-proximity flag — M3 🟡. A note about supply, not the gate |

**Why it does not self-resolve.** `Lead Risk Assessment Standard.md`'s **v2.1 header ratifies the #93 delta** (*"interstate = A-customer OR commercial #93"*) while **its own body never implements it** — M3 still reads a flat 🟡. One document therefore carries both the gate and the amber, and neither `03-risk-scoring.md` (which carries M3) nor this section may be read as having decided against the other. The corpus declares no precedence, so the conflict stands.


⚠ **The one thing that is not in dispute:** `SteedForm Identity.md`'s older **job-value** decision tree (*"source interstate if it is the difference between winning and losing the job"*, with the small/residential branch declining) **is superseded and must not be carried**. None of the three live positions is a job-value test. Note that Identity's *"Interstate supplier, specified material → RED FLAG"* framing is the same superseded passage.

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed most of what this document used to carry — **OR-06** and **OR-29** (out-of-area is a registered layer-1 blocking condition, and the install-range frame has two ruled levels, §1), **OR-11** (occupancy is blocking → Needs Review, never an auto-decline, §5), **OR-15** (sea crossings, §2), **OR-24** (the Client Required-By column is retired; the timeline rule reads prose only, §6), **OR-27** (the crane travel height is N/A and stays approximate, §4) and **OR-28** (the lifting SOP does not exist; the figures now live in §4) are **ruled**, and their positions are stated plainly above.

**Two items remain:**

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-26** | The CRM boards could not be reached on 3 September 2026, so **no board or column identifier has been verified against a live board** — including Serviceable Areas `5029634649` and Deals `Job Type` `color_mm64htd3`, both of which this document instructs a screen to read. ⚠ **The 3 September board exports do NOT close this** — they confirm what the board holds, not what it is called | §1 (the zone read) and §6 (the Supply Only conversion). **A tag check is not an identifier check**: see the warning at the head of `08-board-and-column-registry.md` |
| **OR-39** *(new, 3 Sep 2026)* | The Serviceable Areas board carries a **third zone value, `Boundary — verify`**, and **no registered rule handles it.** One row today. The zone table in §1 routes it to Needs Review; nothing in `01-rule-register.md` says so | §1. **Interim only:** treat as Supply Only pending confirmation and flag — never Full Service |

**Also unresolved and scoped elsewhere:** **OR-38** — whether the Screening Philosophy / distance-from-optimum lens is retired and all stone moves to one ladder, **held for scoping**. It does not touch service area or site, and nothing in it may be applied as a rule.
