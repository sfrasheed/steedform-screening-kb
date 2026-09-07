# 09 — Response Templates

⛔ **A DRAFT REPLY ASKS ONLY FOR WHAT IS NEEDED TO QUOTE** `[R-ASK v1]`. Dimensioned
drawings, the stone **range**, the scope, and the site address. **Never** a colour, an
edge profile, an appliance or sink model, a spec sheet, photos of installed cabinetry,
or a site contact — those are order facts, they stay on the job, and they are raised
when the job converts.

**Arris is assumed where no edge profile is noted**, per the Terms & Conditions. An
unstated profile is not a gap and must not be written into a reply as one.

⚠ This governs what a customer is **asked for**. It removes nothing from the risk
strip, the findings or the order-gate conditions — the screen still finds all of it.


**Status:** Active. Extracted from `Communications.md` v1.6 (27 August 2026). Subordinate to `01-rule-register.md`: where this document and the Rule Register disagree, the Register is correct and this file is stale. Template wording is carried **verbatim** — do not paraphrase, modernise or "tidy" a template before sending. Unresolved questions are quarantined in `10-open-rulings.md` and must not be acted on.
**Owner:** Matthew Rasheed (MD) — template wording and voice. Rule authorship stays with `01-rule-register.md`.
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns:** the trigger → template index; the decline, information-request and technical template texts; the agent instructions attached to each; the voice rules, audience-tier register and sign-off pattern; the standing Legacy Granite & Marble referral and its exceptions.
- **Does not own:** any operational rule. Rules are authored only in `01-rule-register.md` and are cited here as `[R-xxx vN]`. This document does not own screening criteria, scoring, verdicts, pricing, or technical reference data (substrate thicknesses, ventilation gaps, overhang limits) — it only carries the sentences SteedForm says once a verdict exists.

---

## What this document decides

Which message goes out once a screening verdict is reached, and exactly what it says. It maps every screening outcome to one template, gives the template's text as it is actually sent, states which are permanent declines and which leave the door open, and fixes the house voice a generated message must obey. Where a template's trigger is a Rule Register rule, the rule is cited by ID, never restated. **As at 3 September 2026 every decline ground in this document that has an authority has a REGISTERED one** — `[R-RETAIL v1]` grounds T-DECLINE-08 and `[R-DEKTON v1]` grounds T-DECLINE-06, both ratified that day. The templates that carry no rule (T-DECLINE-01, T-DECLINE-04, T-QUALIFY-01, T-FOLLOWUP-01) carry none because they are judgement or capacity calls, not because a ratification is outstanding.

---

## 1. Trigger → template index

Verdict vocabulary is the screening skill's board mode: **Qualified · Needs Info · Needs Review · Unqualified** (brief mode: PROCEED / ASSESS / DECLINE).

| Screening outcome / trigger | Verdict | Template | Variants | Rule authority | Redirect offered | Door open? |
|---|---|---|---|---|---|---|
| No readable drawings / insufficient documentation | Needs Info | **T-INFO-01** | Trade · Homeowner | `[R-DRAWINGS v1]` | Send the requirements PDF; quote in 2 business days once complete | Yes — the enquiry stays live |
| Trade / commercial enquiry SteedForm intends to quote but must scope first | Qualified → Info Gathering | **T-QUALIFY-01** | Single version (Trade / Commercial only) | — (not a decline) | Qualifying questions, then pricing | Yes |
| No response to T-INFO-01 | Needs Info (chase) | **T-FOLLOWUP-01** | All tiers | — | Restate the missing items | Yes |
| **No approved trade account behind the job** (retail / direct; DIY, kit and IKEA cabinetry) | Unqualified | **T-DECLINE-08** | Homeowner / Direct · Trade / Designer | **`[R-RETAIL v1]`** — the test is the trade account behind the job, never who sent the email (IKEA ground also: `[R-SCOPE v2]`) | **Primary: the trade route** (their cabinetmaker/builder contacts us, or a trade-account conversation). Legacy second | **No — permanent.** No "try us later" |
| Scope outside capability (non-stone, ultra-complex bespoke, outside geographic range) | Unqualified | **T-DECLINE-01** | Trade · Homeowner | None stated in source | Optional alternative supplier suggestion | Trade version invites the next fitting job |
| Client-supplied material / install-only / fab-and-install-only | **Unqualified** — except on an A-tier account, where it is **Needs Review** first | **T-DECLINE-07** | Trade / Cabinetmaker · Homeowner / Standard | `[R-SCOPE v2]` — client-supplied slabs are a hard stop for every account **except an A-tier account, the one carve-out in the table**, where they become a 🔴 RISK routed to Needs Review `[R-BLOCK v3]` for a named human to accept or decline | **SteedForm-supplied material — quote the full scope.** ⚠ **No Legacy referral** | Only by converting to a SteedForm-supplied job |
| Existing / DIY / re-used / relocated cabinetry | Unqualified | **T-DECLINE-03** | Trade · Homeowner | `[R-SCOPE v2]` — replacement or remedial work on someone else's stone, and IKEA kitchens, are **DECLINE or refer** items | Re-quote once new cabinetry is built by a qualified joiner and drawings exist | Conditional — on new cabinetry |
| At capacity / timeline conflict | Unqualified (timing, not policy) | **T-DECLINE-04** | Trade / Commercial · Homeowner | None — a capacity call, not a rule | Legacy, plus optional scope education for next time | **Yes — explicitly.** This is the only "try us later" decline |
| Operating environment — occupied building, ongoing concern, interstate-only supply on small scope | Needs Review first → then Unqualified if the human declines | **T-DECLINE-05** | Trade / Commercial · Homeowner | `[R-OCCUPANCY v1]` — occupancy is blocking → Needs Review `[R-BLOCK v3]`, **never an auto-decline. ⛔ This letter may only be sent AFTER a human review — never at triage.** Interstate is a **Client-dimension customer-class gate** `[R-AREA v1]` | Legacy, plus an explicit statement of what *does* fit | Yes — via "what does fit" |
| Dekton specified | **Needs Review** (decline-as-spec'd + substitution steer) | **T-DECLINE-06** | Trade / Commercial · Homeowner | **`[R-DEKTON v1]`.** The four-condition materiality exception is available to **A-TIER ACCOUNTS ONLY** — B-tier and below get no exception: decline and substitute | Substitute material (quote it); Legacy **only** if the spec is locked and the client won't substitute | Yes — substitution converts the enquiry |
| Flush-mount sink or cooktop specified | Condition on the job (🔴), not a whole-job decline | **T-TECHNICAL-01** | One version, all tiers | `[R-FLUSH v1]`; `[R-SCOPE v2]` makes flush mounting a **RESET**, not a decline | Over-mount or undermount detail | Yes — the job proceeds on a supported mount |
| Outdoor / alfresco porcelain or sintered benchtop | Info Gathering → Quoting | **T-TECHNICAL-02** | Builder / Cabinetmaker | **`[R-ALFRESCO v1]`** — the controlled standard `STD-0017` Rev 1 owns every alfresco figure and supersedes each earlier one; see the ⚠ on that template | Build-to spec so the job can proceed | Yes |
| Clean — no blocking flags | Qualified | No template (internal routing) | — | — | Proceeds to quoting (T-QUOTE-01) | — |

### Precedence when more than one decline fires

**Send the MORE SPECIFIC template.** If the enquiry also fails on scope (IKEA, client-supplied stone, existing cabinetry), use `T-DECLINE-03`, `T-DECLINE-07`, or the `[R-SCOPE v2]` ground that fits — because those name the *particular* thing that is wrong, and a specific reason is what the four-step pattern (§5) requires.

⚠ **The original reason for this ordering is spent.** The source rule read *"…because those carry Rule Register authority and this one does not yet."* **T-DECLINE-08 now carries `[R-RETAIL v1]`**, ratified 3 September 2026, so the authority asymmetry is gone. **The precedence itself still stands**, on specificity alone.

The common real case — a homeowner, with existing cabinetry, and no trade account — fires T-DECLINE-08, T-DECLINE-03 and a `[R-SCOPE v2]` ground at once. Send the **more specific** one.

### Retired

**T-DECLINE-02 is RETIRED. It is not live and must not be sent or reinstated.** Its content lives in T-DECLINE-07. The source's tombstone, carried verbatim:

**Merged into `T-DECLINE-07` (Client-Supplied Material / Install-Only).** T-DECLINE-07 has the
broader trigger — it also covers install-only and fab-and-install-only requests, which this
template did not — and it cites the locking authority (SteedForm Identity, Services, May 2026).
This template's fabrication reasoning (slab inspection, bookmatching, vein continuity, material
replacement) has been carried across as T-DECLINE-07's **trade/cabinetmaker version**.

Two templates for one situation guaranteed they would drift. Do not reinstate this one.

---

## 2. Decline templates

All decline templates carry the standing Legacy Granite & Marble referral (§6) **except T-DECLINE-07**, which forbids it, and **T-DECLINE-06**, where the referral is conditional. Every decline states a reason — an unexplained decline is a voice-rule breach (§5).

---

### T-DECLINE-01 — Scope Outside Capability

- **Trigger:** project involves scope SteedForm doesn't do (non-stone, ultra-complex bespoke, outside geographic range, etc.)
- **Stage / verdict:** Triage → Disqualified (Unqualified)
- **Rule authority:** none stated in the source. This is a capability/scope judgement, not a registered rule.
- **Variants:** Trade · Homeowner
- **Redirect:** an optional alternative-supplier suggestion in the trade version; the trade version closes by inviting the next job that fits.
- **Permanent?** Permanent for this project. Not a client-type decline.
- ⚠ **Do not conflate with T-DECLINE-08.** T-DECLINE-01 is about the *work*; T-DECLINE-08 is about *who is behind the job* `[R-RETAIL v1]`. A retail enquiry for work SteedForm does every day is a T-DECLINE-08, never a T-DECLINE-01.
- ⛔ **"Outside geographic range" is NOT a decline ground at screening** `[R-AREA v1]`. Out of area is **blocking → Needs Review** while the Supply Only conversion is undecided, and once `Job Type` is set to `Supply Only [− FREIGHT]` the job proceeds on that delivery model `[R-SUPPLYONLY v2]`. **Distance changes the delivery model, not whether SteedForm wants the work.** The template's optional service-area reason line may only be used once a human has decided to decline a job that could not be converted — never as a triage output, and never on a confirmed Supply Only zone.

**Trade version:**

> Hi {{recipient.first_name}},
>
> Thanks for thinking of us on this one. We've had a look and this project sits outside what we're set up to do well — [specific reason: e.g. "the curved laminated panels require tooling and materials we don't work with" / "the location is outside our standard service area for templating and installation"].
>
> Rather than take it on and deliver something we're not confident in, we'd prefer to be upfront about it.
>
> [If applicable: "You might want to try [alternative suggestion] — they're better set up for this kind of work."]
>
> Happy to help on the next one that fits.

**Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for considering SteedForm for your project.
>
> After reviewing the details, this particular project falls outside the scope of work we specialise in — [softer reason: e.g. "the materials involved aren't ones we fabricate" / "the level of custom detailing required goes beyond our standard offering"].
>
> We'd rather be honest about this upfront than take on something where we can't guarantee the quality we're known for.
>
> We wish you all the best with your project.

**Agent instruction:** Always populate the [specific reason] field. Pull the disqualification trigger from Sales Qualification and translate it to the appropriate audience register. Never send a decline without a reason.

---

### T-DECLINE-03 — DIY / Existing / Relocated Cabinetry

- **Trigger:** project involves existing, DIY, re-used, or relocated cabinetry
- **Stage / verdict:** Triage → Disqualified (Unqualified)
- **Rule authority:** `[R-SCOPE v2]` — replacement or remedial work on someone else's stone, and IKEA kitchens, are NOT-OFFERED items whose stated screening action is **DECLINE or refer**. ⛔ **They are not specifications to be corrected:** do not price them, do not substitute around them, do not render them 🟡.
- **Variants:** Trade · Homeowner
- **Redirect:** re-quote once the cabinetry is rebuilt or replaced by a qualified joiner/cabinetmaker and new dimensioned drawings exist.
- **Permanent?** Conditional — permanent for the cabinetry as it stands, reopens on new cabinetry.

**Trade version:**

> Hi {{recipient.first_name}},
>
> Thanks for sending this through. We can't take on projects where the cabinetry is existing, relocated, or DIY-built. The tolerances on these installations are too unpredictable for us to guarantee a quality outcome — stone fabrication requires precise, consistent cabinetry dimensions and level surfaces.
>
> If the cabinetry is being rebuilt or replaced by a qualified joiner, we'd be happy to quote once new dimensioned drawings are available.

**Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for your enquiry. After reviewing the details, we're not able to take on this project as it involves existing cabinetry.
>
> Stone benchtops require very precise cabinetry dimensions and level surfaces to ensure a proper fit and finish. Existing or relocated cabinets often have variations that make it difficult for us to guarantee the quality of the finished result.
>
> If the cabinetry is being rebuilt by a qualified cabinetmaker, we'd be happy to look at the project again once dimensioned drawings of the new cabinetry are available.

---

### T-DECLINE-04 — At Capacity / Timeline Conflict

- **Trigger:** SteedForm can do the work but cannot commit within the project's timeline due to capacity constraints
- **Stage / verdict:** Triage or Info Gathering → Disqualified
- **Rule authority:** none — a capacity call, not a policy or scope disqualification.
- **Variants:** Trade / Commercial · Homeowner
- **Redirect:** Legacy Granite & Marble (full details in both versions), plus an optional scope-education line for future enquiries.
- **Permanent?** **No — this is the one decline that explicitly keeps the door open.** It is the *only* correct home for "try us again later" language; never borrow that framing into T-DECLINE-08.

**Trade / Commercial version:**

> Hi {{recipient.first_name}},
>
> Thanks for the update.
>
> Unfortunately we are at capacity over the next few months and wouldn't be able to commit to this project within your proposed [timeframe] timeframe.
>
> Given the nature of this type of work, we'd rather be upfront than risk under-delivering on program or quality.
>
> [If applicable — scope education for future: "I also just wanted to note that for future opportunities, we typically require a bit more detail around scope and documentation to ensure we're pricing accurately and aligning expectations from the outset — particularly for [relevant item type]."]
>
> I appreciate you reaching out and thinking of us, and hopefully we can connect on a future project when timing aligns better.
>
> If you're still looking for someone, you could try:
> Legacy Granite & Marble
> 555 Churchill Road, Kilburn SA 5084
> 0480 282 715
> legacygraniteandmarble.com.au

**Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for considering SteedForm for your project.
>
> Unfortunately, we're at capacity over the coming months and wouldn't be able to take this on within your timeline. We'd rather be upfront about that than take on your project and not give it the attention it deserves.
>
> One option worth considering is Legacy Granite & Marble — they work directly with homeowners on projects like yours. You can reach them on 0480 282 715, and their website is legacygraniteandmarble.com.au.
>
> We wish you all the best with your project, and you're always welcome to reach out on future work.

**Agent instruction:** A capacity decline keeps the door open — always include a future-facing line ("hopefully we can connect on a future project"). If the enquiry also had scope or documentation issues, use this as an opportunity to educate for next time (see the optional scope education line). Never just decline on capacity — always provide the Legacy referral.

---

### T-DECLINE-05 — Project Screening Disqualification (Operating Environment)

- **Trigger:** the operating environment makes the job unviable — occupied commercial building requiring after-hours work; cafe/bar/retail that can't close for the measure-manufacture-install cycle; interstate-only material specification on a small scope with no existing supplier relationship. The stone work itself may be straightforward.
- **Stage / verdict:** occupancy is a **blocking** flag, so the screening verdict is **Needs Review** — a named human decides `[R-OCCUPANCY v1]` `[R-BLOCK v3]`. This template is the letter that goes out **after** that human has decided to decline.
- ⛔ **THIS TEMPLATE MAY ONLY BE SENT AFTER A HUMAN REVIEW. NEVER AT TRIAGE** (ruled 3 September 2026, OR-11). An occupied dwelling or a trading ongoing concern is **never an auto-decline** — the occupancy carve-out (#61) routes it to Needs Review, and a stripped site in a CBD building scores only 🟡. The Pipeline Communication Map's mapping of *"Disqualified — operating environment → T-DECLINE-05"* at **Triage** is stale and must not be followed.
- ⛔ **`SteedForm Identity`'s line — *"Tenanted occupied residential building → DECLINE"* — is RETIRED** `[R-OCCUPANCY v1]`. **A machine may not turn away an occupied job on keyword evidence.** ⚠ Identity has not yet been amended at source; the retirement is ruled regardless, and Identity is stale on this point.
- **Occupancy is established by the address lookup, never assumed** `[R-SITE v1]`. A trading tenancy at street level makes it an occupied commercial building — a fact at screening, not something to confirm later.
- **Rule authority:** `[R-OCCUPANCY v1]` for the occupancy ground; `[R-AREA v1]` for the interstate ground (below). The template itself authors nothing.
- ⚖ **The interstate trigger line is KEPT** (ruled 3 September 2026, OR-10). **Interstate is a CUSTOMER-CLASS GATE, and it is owned by the CLIENT dimension, not Material.** Interstate material is considered only for an **A-customer OR a commercial project** — either qualifies. **A non-A residential job is declined on supply risk.** The Material lane's 🟡 "brand not local / interstate / unknown" scoring is a supply-proximity note and does not own this decision.
- ⛔ **Interstate supplier policy is INTERNAL and never goes in the email** — see the agent instruction below. The gate decides the outcome; it is not a reason the client is given.
- **Variants:** Trade / Commercial · Homeowner
- **Redirect:** Legacy Granite & Marble, plus a mandatory closing statement of what *does* fit.
- **Permanent?** For this project; the "what does fit" close is a deliberate invitation to return with a better-fitting job.

**Trade / Commercial version:**

> Hi {{recipient.first_name}},
>
> Thanks for sending this through — we've had a good look.
>
> Unfortunately, we wouldn't be the right fit for this one. [Combine applicable reasons into one flowing sentence. Examples:]
>
> [Occupied building + ongoing concern:] The combination of an occupied building with after-hours access restrictions and an operating [cafe/bar/retail space] that can't close for our measure-manufacture-install cycle puts this outside how we operate best.
>
> [Occupied building only:] The building is occupied and operational, which means working around after-hours access restrictions and building management coordination — that puts this outside how we operate best.
>
> [Ongoing concern only:] The [cafe/bar/retail space] is an ongoing concern that can't close for our measure-manufacture-install cycle, and we need the space clear and accessible across all three stages.
>
> We'd rather be upfront about that than take it on and not deliver to our standard.
>
> If you're still looking for someone, you could try Legacy Granite & Marble — 555 Churchill Road, Kilburn SA 5084, 0480 282 715, legacygraniteandmarble.com.au.
>
> If you have any [describe what DOES fit — e.g. "new-build or renovation projects where we have clear site access during working hours"], that's where we do our best work — happy to help on the next one.

**Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for considering SteedForm for your project.
>
> After reviewing the details, this particular project isn't one we're able to take on. [Combine applicable external-facing reasons into one flowing sentence, softened. Example:]
>
> [Occupied building + ongoing concern:] The installation would need to work around an occupied building and an operating [cafe/space] that can't close during our process — and that combination puts this outside what we can reliably deliver well.
>
> We wish you all the best with the project.
>
> One option worth considering is Legacy Granite & Marble — they work directly with homeowners on projects like yours. You can reach them on 0480 282 715, and their website is legacygraniteandmarble.com.au.

**Agent instruction:** This template is modular — select the reason blocks that apply. Multiple reasons can be combined in a single flowing sentence rather than listed as separate issues. **Critical rule: only include external-facing reasons the client already knows about.** Occupied building and ongoing concern are visible operational realities — the client knows their building is occupied and their cafe is trading. Interstate supplier policy, internal margin thresholds, and screening framework logic are SteedForm's internal decisions — they do NOT go in the email. The client needs the minimum explanation to understand the decline, not a full audit of everything that failed screening. Keep it to one or two reasons maximum, flowing naturally. Always include the Legacy referral. **Always close by describing what DOES fit** — tell the builder what kind of project to bring next time. This educates them on SteedForm's sweet spot and gives them a reason to come back. The close should be the inverse of the decline reason (e.g. if declined for occupied building → "new-build or renovation projects where we have clear site access during working hours").

---

### T-DECLINE-06 — Dekton Specified (Material Phase-Out)

- **Trigger:** enquiry specifies Dekton as the material.
- **Stage / verdict:** **Needs Review — decline-as-spec'd plus a substitution steer, never an auto-Unqualify.** The source's Pipeline Communication Map maps this row to "Triage → Disqualified"; that is stale. `SKILL.md` Axis 1 and its verdict precedence make the Dekton materiality exception a carve-out that forces Needs Review, and the Lead Risk material dimension agrees (still 🔴, human call). Resolved against the map on that evidence.
- **Rule authority:** **`[R-DEKTON v1]`** — ratified 3 September 2026 (OR-09). Dekton is being phased out; specified anywhere → 🔴, decline as specified with a substitution steer. The flag string is fixed and is emitted **verbatim**: *"Dekton — phase-out in progress, do not quote"*.
- **The exception is the FOUR-CONDITION materiality test — explicitly NOT "if the client insists."** The source states it, and the ⛔ rule on what may be written to a customer, as follows (verbatim):

⛔ **THE EXCEPTION IS AVAILABLE TO A-TIER ACCOUNTS ONLY** `[R-DEKTON v1]`. **For a B-tier account or below there is no exception at all: decline and substitute.** Check the linked Account's live Customer Tier `color_mm64t0aj` **before** testing the four conditions — on a non-A account the test is never reached. An untiered or unconfirmed account is not A-tier `[R-ENTITY v1]`.

⚖ **On an A-tier account, the exception is a FOUR-CONDITION test — all four required — and it is explicitly NOT "if the client insists."** Dekton a minor component (≤ 1 room / 1–2 pieces) **AND** the bulk of the job in another material **AND** the job substantial (~$10k+) **AND** the customer won't substitute — then **Needs Review**, and a named human decides.

⛔ **The looser wording — *"do not quote on new Dekton work unless specifically requested by client"* — is RETIRED wherever it appears.**

⛔ **The exception converts the OUTCOME to a human call. It never lowers the colour** — the material line stays 🔴.

**Why the gate exists:** SteedForm would rather substitute in every case. The exception exists so a substantial A-tier job is not lost over one room — not so that any client who insists gets Dekton.

⛔ **Never put the commercial rationale in writing to a customer** (MD, 30 Jul 2026). The customer-facing line is the positive substitution framing below. Never disparage Dekton.

⚖ **Naming the substitute brands in this first email is RULED CORRECT — the template governs** (3 September 2026, OR-16). `T-DECLINE-06` **keeps naming Neolith, Caesarstone Porcelain and Smartstone Sintered** in the first email; that is the conversion path and the whole point of the template. **`SteedForm Identity`'s "never name substitute brands in a first-contact decline" is SUPERSEDED for this template.** ⚠ Identity has not been amended at source and is stale on this point; it needs amending there.


- **Variants:** Trade / Commercial · Homeowner
- **Redirect:** the substitute material — this is a conversion opportunity, not a lost enquiry. Legacy **only** if the spec is locked on Dekton and the client won't consider alternatives.
- **Permanent?** No — the enquiry converts the moment the client accepts a substitute.

**Trade / Commercial version:**

> Hi {{recipient.first_name}},
>
> Thanks for sending this through.
>
> We've reviewed the scope and the stone work itself is well within what we do. However, we've moved away from Dekton for new projects — we've found that alternative sintered products give our clients better overhang flexibility, simpler fabrication, and faster turnaround with no compromise on appearance or durability.
>
> For this application, we'd recommend [select based on application]:
> - **Neolith** — our preferred sintered product. Excellent outdoor rating, proven fabrication process, strong local supply.
> - **Caesarstone Porcelain** — strong indoor option with better overhang allowances than Dekton and standard adhesive systems.
> - **Smartstone Sintered** — versatile general-use sintered option.
>
> If the designer or client is open to one of these alternatives, we'd be happy to put pricing together. We can also provide technical comparison data if that helps the conversation with the specifier.
>
> If the spec is locked on Dekton specifically, you could try Legacy Granite & Marble — 555 Churchill Road, Kilburn SA 5084, 0480 282 715, legacygraniteandmarble.com.au.

**Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for considering SteedForm for your project.
>
> We've had a look at the scope, and the work itself is something we do well. However, we now recommend alternative products to Dekton — they offer the same look and durability with better flexibility for your benchtop design and a smoother process overall.
>
> We'd suggest [Neolith / Caesarstone Porcelain / Smartstone Sintered] as a great alternative for your project — happy to put pricing together if you'd like to explore that option.
>
> If you'd prefer to stay with Dekton, we'd recommend reaching out to Legacy Granite & Marble — they work directly with homeowners on projects like yours. You can reach them on 0480 282 715, and their website is legacygraniteandmarble.com.au.

**Agent instruction:** This template must always lead with the alternative, not the decline. The goal is to redirect the enquirer toward a better product, not to say no. If the client or specifier is open to substitution, SteedForm quotes the alternative — this is a conversion opportunity, not a lost enquiry. Only refer to Legacy if the spec is locked on Dekton and the client won't consider alternatives. Technical selling-against arguments (overhang restrictions, proprietary adhesive, blanket mitre reinforcement, complex radius rules) should be available for trade conversations if the builder or designer pushes back, but should NOT go in the initial email — use them in follow-up if needed. Never disparage Dekton directly — frame everything as "we've found alternatives that work better for our clients."

---

### T-DECLINE-07 — Client-Supplied Material / Install-Only

- **Trigger:** install-only, fab-and-install-only, or any arrangement where the customer supplies the slab — regardless of who the customer is or which supplier they source from, including SteedForm-relationship suppliers.
- **Stage / verdict:** Triage → Disqualified (Unqualified) on every account **except an A-tier one**. Client-supplied stone is also a layer-2 blocking rule `[R-BLOCK v3]`.
- **Rule authority:** `[R-SCOPE v2]` (client-supplied slabs — NOT OFFERED) **and** `[R-BLOCK v3]` (client-supplied stone). Policy locked in SteedForm Identity, Services section, May 2026.
- ⚖ **The two rules no longer disagree — ruled 3 September 2026 (OR-03).** `[R-SCOPE v2]` gives client-supplied slabs **the only carve-out in the NOT-OFFERED table**: a hard stop for every account, **except an A-tier account, where it becomes a 🔴 RISK routed to Needs Review** for a named human to accept or decline. **No other item in that table carries a carve-out.**
  - **Non-A account →** hard stop. This template is the decline, and there is no human call to wait for.
  - **A-tier account →** screen to **Needs Review** first; this template is the letter sent only if the named human decides to decline.
- **Variants:** **Trade / Cabinetmaker** (the full technical reason, carried over from the retired T-DECLINE-02) · **Homeowner / Standard**
- **Redirect: SteedForm-supplied material.** The closing offer to quote the full scope is the conversion path and must never be omitted.
- **Permanent?** Permanent as an install-only arrangement; converts if the customer lets SteedForm supply.
- ⚠ **This is the one decline with no Legacy referral** — see the source instruction below and §6.
- *Note:* the source's claim that this is "the only decline ground in this document that is carried by the Rule Register" is false and is not carried forward — `[R-SCOPE v2]` also grounds T-DECLINE-03 and the flush-mount case, `[R-FLUSH v1]` and `[R-DRAWINGS v1]` ground T-TECHNICAL-01 and T-INFO-01, and since 3 September 2026 `[R-RETAIL v1]` and `[R-DEKTON v1]` ground T-DECLINE-08 and T-DECLINE-06.

**Trade / Cabinetmaker version** (full technical reason — carried over from the retired T-DECLINE-02):

> Hi {{recipient.first_name}},
>
> Thanks for sending this through.
>
> We don't take on projects where the stone is supplied by the client. Managing the full supply and fabrication process — from slab selection through to installation — is how we control quality, handle any material variations, and stand behind our workmanship warranty.
>
> When we supply the material ourselves we can inspect slabs before cutting, manage bookmatching and vein continuity, and replace material if something unexpected turns up during fabrication. With client-supplied stone we lose that control and can't offer the same guarantees.
>
> If you'd like us to quote the project with material supply included, we'd be happy to do that.

**Homeowner / Standard version:**

> Hi {{recipient.first_name}},
>
> Thanks for reaching out.
>
> To ensure we deliver the level of quality, consistency, and warranty coverage we stand behind, we don't take on projects where the material is client-supplied. Managing the full supply and fabrication process allows us to carefully control slab selection, handle any variations or unforeseen issues, and provide our standard workmanship and product guarantees with confidence.
>
> We completely understand that material may sometimes be pre-purchased, and we hope you can appreciate that this approach helps us protect both your project and our standards.
>
> If you'd like SteedForm to handle the full scope including supply, we'd be happy to put a quote together — please let us know.

**Agent instruction:** This is a polite-but-firm categorical decline. The policy is locked — there is no negotiation path on install-only work. Do NOT propose to "do it this once" or invent exceptions. **The closing offer to handle the full scope is the conversion path and must never be omitted** — if the customer comes back willing to convert the slab purchase to a SteedForm-supplied job, that is a normal quote. Never disparage the customer's chosen supplier. If the customer is already locked in to a slab purchase they can't reverse, the decline stands.

⚠ **Do NOT refer these to Legacy Granite & Marble.** This is the one decline where the standing referral practice does not apply — the redirect is SteedForm supplying the material, and sending the enquirer to another fabricator throws away a live conversion.

**Why the policy exists (Technical Standards §9.3):** a client-supplied natural stone job produced **~$20k in remakes**. The client selected slabs at the supplier, SteedForm had no control over block matching or slab pairing, and SteedForm absorbed the full cost of the remake because the fabrication error was on our side. No material control, full liability. Use this if a trade contact pushes back — not in the initial email.

---

### T-DECLINE-08 — No Approved Trade Account (Retail / Direct)

**This is the highest-volume decline SteedForm sends** (4 in one month, August 2026). Added 27 August 2026 (v1.6); before that it had neither a rule nor a template.

- **Trigger:** no approved SteedForm trade customer is supplying and installing the cabinetry.
- ⚖ **The test is the trade account behind the job — NOT who sent the email** `[R-RETAIL v1]`. A homeowner whose kitchen is being built by an approved cabinetmaker is a normal trade job, routed through that cabinetmaker. A builder, designer or joiner with no SteedForm account is a decline, however they present. DIY, kit and IKEA cabinetry are always a decline (IKEA: `[R-SCOPE v2]`).
- **Stage / verdict:** Triage → Disqualified (Unqualified)
- **Rule authority:** **`[R-RETAIL v1]`** — ratified 3 September 2026 (OR-08), closing the position the MD recorded on 27 August 2026. **This template's ground carries full Register authority.** The precedence rule (§1) still sends an enquiry that also fails on scope to the more specific template, now on specificity rather than on any shortfall of authority.
- ⚖ **The Direct Homeowner x1.55+ markup tier SURVIVES** `[R-RETAIL v1]`. It continues to apply where a trade account **is** behind the job and the homeowner is driving it — the tier prices hand-holding. **It is not a route around this decline:** no trade account behind the job means a decline at any markup. See `04-customer-and-account.md` §7.1.
- ⛔ **The "qualified cabinetmaker" test is SUPERSEDED.** The screening skill's *"retail/homeowner-direct OK only for a new-build kitchen with a qualified cabinetmaker involved"* is retired. **The test is an approved SteedForm trade account**, not a qualified cabinetmaker — a competent, licensed cabinetmaker with no SteedForm account does not satisfy it.
- **Variants:** Homeowner / Direct · Trade / Designer, plus an optional supply-only block.
- **Redirect: the trade route is primary** — their cabinetmaker or builder gets in touch and the job proceeds through them, or (trade/designer version) a conversation about becoming an approved trade customer. The Legacy referral is **secondary** and sits below the trade line.
- **Permanent?** **Permanent. No "try us later" language** — capacity is `T-DECLINE-04`.
- **Key principle:** this is a **client-type** decline, not a capability one. Never imply SteedForm can't do the work.
- ⛔ **Never offer to find or introduce them to a cabinetmaker** — that is a third-party promise with no owner; invite *their* trade to contact us instead. ⚖ **This instruction stands UNQUALIFIED** (ruled 3 September 2026, OR-34): **retail enquiries are NOT referred to SteedForm's approved cabinetmakers.** The question of turning a lost retail enquiry into a lead for a trade customer was asked and answered **no**; it is not held open and needs no owner.
- ⚠ **Supply-only block guard:** the optional supply-only sentence must **not** be sent to an enquirer in a confirmed Supply Only zone — **Port Lincoln 5606 and Kingscote / Kangaroo Island 5223** — see `[R-SUPPLYONLY v2]`, which names those zones and makes supply-only **a different delivery model, never a decline ground**. Check the zone before including the block.

**Homeowner / Direct version:**

> Hi {{recipient.first_name}},
>
> Thank you for getting in touch[, and thanks to {{referrer}} for passing on our details].
>
> SteedForm is focused on trade and commercial projects — we supply and install benchtops onto new cabinetry manufactured and installed by an approved trade cabinetmaker, so we're not able to quote this one directly.
>
> If your cabinetmaker or builder would like to work with us, they're welcome to get in touch and we can look at the project through them.
>
> You may wish to contact Legacy Granite & Marble, who work directly with homeowners and may be able to assist:
>
> Legacy Granite & Marble
> 555 Churchill Road, Kilburn SA 5084
> 0480 282 715
> legacygraniteandmarble.com.au
>
> All the best with the project.

**Trade / Designer version** (builder, joiner or designer with no SteedForm account):

> Hi {{recipient.first_name}},
>
> Thanks for sending this through.
>
> We work through our approved trade accounts — measure, fabrication and installation onto cabinetry supplied and installed by an approved cabinetmaker. We don't have an account with you at this stage, so we're not in a position to price this one.
>
> If you'd like to talk about becoming an approved trade customer, I'm happy to have that conversation.
>
> If you need someone for this project now, you could try Legacy Granite & Marble — 555 Churchill Road, Kilburn SA 5084, 0480 282 715, legacygraniteandmarble.com.au.

**Optional block — supply only.** Include whenever the enquirer has asked for supply only,
"just a supply quote", or fabrication without installation:

> Supply only isn't something we offer on residential work — measure, fabrication and installation are one scope for us.

**Agent instruction:** The **primary redirect is the trade route**, not Legacy — a homeowner whose
cabinetmaker joins the conversation becomes a normal job, so that line goes above the Legacy block
and must never be omitted. Include Legacy per standing referral practice. ⛔ **Never offer to find
or introduce them to a cabinetmaker** — that is a third-party promise with no owner; invite *their*
trade to contact us instead. ⛔ **Never frame this as capability** ("we can't do that kind of work")
— we can, and saying otherwise is untrue and invites argument. ⛔ **No "try us again later"** — this
is permanent; capacity is `T-DECLINE-04`. If the enquiry ALSO fails on scope (IKEA, client-supplied
stone, existing cabinetry), use the more specific template — `T-DECLINE-03`, `07`, or a
`[R-SCOPE v2]` ground — because those name the particular thing that is wrong. **This template's own
ground is `[R-RETAIL v1]` and carries full Register authority**; the precedence is about specificity,
not authority.

---

## 3. Information-request templates

---

### T-INFO-01 — Information Required Before Quoting

- **Trigger:** enquiry received without sufficient documentation (drawings, specs, selections)
- **Stage / verdict:** Triage → Info Gathering. **Needs Info** `[R-DRAWINGS v1]`.
- **Rule authority:** `[R-DRAWINGS v1]`
- **Variants:** Trade / Builder / Cabinetmaker · Direct Homeowner
- **Attachment:** Customer Information Requirements PDF (Rev2, June 2024)
- **Turnaround promised:** a quote within two business days of the complete set arriving. Both versions state it — keep it.

**Trade / Builder / Cabinetmaker version:**

> Hi {{recipient.first_name}},
>
> Thanks for sending this through. To get a quote back to you, we need dimensioned cabinetry drawings, the stone range you're after, and which rooms are included.
>
> I've attached our information requirements document — it covers everything we need in one place. Once we have the complete set, we'll turn a quote around within two business days.
>
> Let me know if you have any questions.

**Direct Homeowner version:**

> Hi {{recipient.first_name}},
>
> Thank you for considering SteedForm for your project.
>
> Before we can prepare a quote, we need a few key pieces of information — most importantly, dimensioned drawings of your cabinetry from your builder or cabinetmaker, and the stone range you're considering.
>
> I've attached a document that explains everything we need. If you're unsure about any of the items, your cabinetmaker or builder should be able to help, or feel free to reply to this email and we'll guide you through it.
>
> Once we have everything, we'll review the details and have a quote back to you within two business days.

---

### T-QUALIFY-01 — Commercial / Trade Qualification Before Pricing

- **Trigger:** trade or commercial enquiry SteedForm is interested in but needs to qualify before pricing. More structured than T-INFO-01 — used when the enquiry is non-standard (custom items, commercial fit-outs, unfamiliar scope).
- **Stage / verdict:** Triage → Info Gathering. **Not a decline — a qualification gate.**
- **Rule authority:** none.
- **Variants:** one version. **Trade / Commercial only** — never send this to a direct homeowner.
- **Difference from T-INFO-01:** it proactively sets scope expectations, restates the client's brief back to them, and lists the assumptions pricing is based on.

> Hi {{recipient.first_name}},
>
> [Referral acknowledgment if applicable: "Good afternoon, and thanks for reaching out — I appreciate [referrer name] passing on our details."]
>
> This is definitely something we can assist with.
>
> Before we put pricing together, it would be great to confirm a few details to make sure we're aligning with your expectations and capturing the full scope correctly:
>
> [Bullet list of specific questions — always include: drawings, material/stone spec, structural details if relevant, timeline]
>
> From your note, we understand the scope is primarily [restate their brief], however we'll also review the plans and identify any additional stone elements if applicable. We'll clearly outline inclusions and exclusions in our pricing to avoid any ambiguity.
>
> As this would be a measure, manufacture and install scope, our pricing will be based on:
> - Site measure once joinery/substrates are installed and ready
> - Final approved shop drawings where required
> - Standard access and working conditions (we can adjust if there are any site-specific requirements such as after-hours work, restricted access, etc.)
>
> Once we have the drawings and the above details, we can turn around a price for you.

**Agent instruction:** This template is for serious commercial/trade enquiries where SteedForm intends to quote. It's not a decline — it's a qualification gate. Key differences from T-INFO-01: it proactively sets scope expectations ("we'll outline inclusions and exclusions"), restates the client's brief to confirm understanding, and lists what pricing assumptions are based on. The qualifying questions should always be specific to the project — never generic.

---

### T-FOLLOWUP-01 — Waiting on Information

- **Trigger:** information request sent (T-INFO-01), no response within [X] business days
- **Stage / verdict:** Info Gathering — the enquiry stays open.
- **Rule authority:** none.
- **Variants:** one version, all tiers.


> Hi {{recipient.first_name}},
>
> Just following up on the information we need to get your quote prepared. We're still waiting on [specific missing items: e.g. "dimensioned drawings and your edge profile selection"].
>
> Once we have the complete set, we'll have a quote back to you within two business days. If you're still waiting on drawings from your cabinetmaker, no rush — just let us know and we'll keep your enquiry open.

---

## 4. Technical templates

---

### T-TECHNICAL-01 — Technical Limitation: Flush Mount Sinks / Hotplates

- **Trigger:** client requests flush-mount sink or hotplate installation
- **Stage / verdict:** Info Gathering (or Triage if non-negotiable). This is a **condition on the job**, not a whole-job decline — the spec is reset to a supported mount and the job proceeds `[R-FLUSH v1]`.
- **Rule authority:** `[R-FLUSH v1]`; flush mounting is also on the `[R-SCOPE v2]` NOT-OFFERED list, where its stated action is **RESET** — the spec moves to a supported mount and the enquiry continues. ⛔ **A RESET item is not a decline**, and the client is told before the quote goes out.
- **Variants:** one version, all tiers — same depth for everyone. This is a technical education piece.
- **Redirect:** over-mount or undermount detail.
- **Timing:** the builder/client must be told **before the quote goes out** `[R-FLUSH v1]` — a flush-mount expectation discovered at install is a remake.
- *Provenance:* the source names this template as the one the entire SteedForm communication standard was derived from (§5, the four-step pattern).

> Hi {{recipient.first_name}},
>
> Thanks for the detail on the project. I wanted to specifically address the flush-mount sink/hotplate detail.
>
> Flush mounting requires a rebate machined into the stone surface using CNC tooling. Due to the nature of the tooling, it's not possible to achieve a perfectly sharp, clean internal edge. The process leaves fine chipping along the rebate edge — particularly in engineered stone, porcelain, and sintered surfaces.
>
> These chips may be small, but they're visible and become more noticeable over time and under certain lighting. In our experience, this finish is frequently deemed unacceptable by clients post-installation because it doesn't meet the expected visual standard of a clean, seamless detail.
>
> For that reason, we don't offer flush mounting. We'd be happy to suggest alternative installation methods — such as an over-mount or undermount detail — that achieve a clean, durable result while maintaining the design intent.
>
> Let me know how you'd like to proceed.

---

---

### T-TECHNICAL-02 — Alfresco / Outdoor Porcelain & Sintered Stone Requirements

- **Trigger:** project involves outdoor/alfresco benchtops in porcelain or sintered stone
- **Stage / verdict:** Info Gathering → Quoting. Not a decline.
- **Rule authority:** **`[R-ALFRESCO v1]`**, whose source is the controlled document **`STD-0017 Alfresco Standard`, Rev 1** (James Hill, 14 August 2026). **STD-0017 supersedes every earlier alfresco figure in this knowledge base.** The figures themselves are reference data owned by `05-material-and-capability.md`; never read one out of a template body.
- **Variants:** one version. Primarily Builder / Cabinetmaker — they build to this spec.
- **Attachment:** SteedForm Alfresco Standards document

⚠ **CORRECTED — and this note stays, because the figure it removed is still in circulation elsewhere.** The template body previously named a **12 mm fibre cement sheet**. That was a **conflation of two different components**, and `[R-ALFRESCO v1]` settles both:

- **12 mm is the SHADOWLINE** — a **12 mm thick × 50 mm wide** shadow line, installed **by the cabinetmaker**, which **must be in place before the site measure can be completed**. 12 mm compact, edged MDF or painted edge. Not required where the benchtop is thicker than 40 mm. Flag it at first builder contact — a measure that arrives to no shadowline is a wasted trip.
- **The FIBRE CEMENT is 6 mm or 9 mm**, selected by the **gap between stone and carcass** — not a fixed figure, and therefore not a number to state flatly in a template.
- ⛔ **A 12 mm fibre cement sheet is a RETIRED offering.** Wherever a document, template or skill says "12 mm fibre cement", it has made the same conflation and is wrong.

**The body below now names no substrate thickness, which is correct** — the figure depends on a gap the cabinetmaker measures, and the attached Alfresco Standards carry it. Do not reinstate a thickness here. *(The remaining "12mm" in the body is the **stone** thickness for the shadowline colour options, and is right as it stands.)*

> Hi {{recipient.first_name}},
>
> Attached are the SteedForm Alfresco Standards for porcelain and sintered stone benchtops.
>
> Outdoor environments require specific fabrication and installation methods to handle heat, moisture, and movement — and to maintain manufacturer warranties. Here's what the cabinetry design needs to accommodate:
>
> **Substrate:** Fully closed cabinet tops to support the fibre cement sheet (supplied and installed by SteedForm).
>
> **Ventilation gaps (manufacturer-required):**
> - Neolith (preferred sintered): +5mm
> - Caesarstone Porcelain & Vasari: +10mm
> - Dekton: +2mm *(note: Dekton is phasing out — for new work, recommend Neolith or CS Porcelain as alternatives)*
>
> **Appliance support:** Appliances cannot be clipped to the stone — they must be supported by a frame within the cabinetry.
>
> **Shadowline options (12mm stone):** Just White, Cement, Basalt Black, Pietra Di Luna, and Calacatta Roma.
>
> Please make sure the cabinetry design meets these standards before construction begins. If anything is unclear, let me know and I'll walk through it.

*The ventilation-gap figures above are quoted inside template prose. The full BBQ ventilation-gap brand table — Dekton 2mm · Vasari 10mm · Caesarstone Porcelain 10mm · Neolith 5mm · Smartstone 10mm — is being added to `05-material-and-capability.md`, which owns material reference data. Cite it from there; never read a gap figure out of a template body.*

---

## 5. Voice rules and sign-off patterns

These are the constraints any generated message must satisfy, whether it is a template send or an agent-drafted variation.

### The SteedForm Communication Standard — the four-step pattern

Every external communication follows one pattern, derived from SteedForm's best existing template (the flush-mount decline, T-TECHNICAL-01):

1. **Acknowledge what they asked for** — show you understood the request
2. **Give the real answer** — yes, no, or here's what we need. Be specific, not vague
3. **Explain why (if declining or constraining)** — use technical, honest, specific reasoning. Not corporate filler
4. **Redirect to what you can do** — always close with the next step or an alternative

The depth of explanation varies by audience tier; the structure does not.

### What SteedForm sounds like

- **Professional, not corporate.** No jargon, no buzzwords, no "please don't hesitate to reach out." Write like a competent tradesperson who respects the reader's time.
- **Direct, not blunt.** Say what you mean. Don't hide behind vague language. But frame things constructively — always end with a forward path.
- **Technically honest.** If there's a limitation, explain what it is and why. Don't pretend limitations don't exist. Clients trust honesty more than polish.
- **Warm where appropriate.** Homeowners get more explanation and a softer tone. Trade gets concise and factual. Both get respect.

### What SteedForm does NOT sound like

- No "please don't hesitate to contact us" — say "reply to this email" or "call us on [number]"
- No "unfortunately we are unable to assist you at this time" or similar corporate deadwood — the word "unfortunately" itself is fine when used naturally (e.g. "Unfortunately, we wouldn't be the right fit for this particular project" or "Unfortunately we are at capacity"). The ban is on the full formulaic phrase, not the word
- No "at this point in time" — say "now" or "currently"
- No unexplained declines — every no comes with a reason (specific for trade, softer for public)
- No false urgency or pressure selling — SteedForm doesn't chase. The work speaks for itself

### Additional constraints that bind a decline

- ⛔ **Never put a commercial rationale in writing to a customer** (MD, 30 Jul 2026) — applies to the Dekton phase-out and by extension to any decline whose real reason is commercial. Never disparage a product.
- ⚖ **Naming a substitute brand in a first-contact decline is PERMITTED IN `T-DECLINE-06`, and only there** (ruled 3 September 2026, OR-16). **The template governs:** T-DECLINE-06 keeps naming **Neolith · Caesarstone Porcelain · Smartstone Sintered** in the first email, because the named alternative *is* the conversion path. **`SteedForm Identity`'s "never name substitute brands in a first-contact decline" is SUPERSEDED for this template.** ⚠ **Identity needs amending at source** — it has not been, and is stale on this point. The discipline still binds every other template: nowhere else does a first-contact decline name a brand.
- **Only include external-facing reasons the client already knows about** (T-DECLINE-05 agent instruction). Occupied buildings and trading cafes are visible realities; internal margin thresholds, supplier policy and screening logic are not. One or two reasons maximum, flowing naturally — never a full audit of everything that failed screening.
- **Never disparage the customer's chosen supplier** (T-DECLINE-07).
- **Never frame a client-type decline as capability** (T-DECLINE-08).
- **Australian English throughout** — the source uses -ise spellings ("specialise", "revise", "compromise") and writes "program" (T-DECLINE-04, "under-delivering on program or quality"). Match the source's spelling exactly; never Americanise a template.

### Standard sign-off

All external emails use:

> Warm Regards,
> Matthew Rasheed

Not "Kind regards," not "Best," not "Cheers." "Warm Regards" is the SteedForm standard.

### Referral source acknowledgment

When a supplier or trade contact has referred the enquiry, acknowledge it in the opening line: "I appreciate Luke passing on our details" or "thanks for reaching out — [supplier] passed on your details." This strengthens the referral relationship and signals professionalism to the new contact.

T-DECLINE-08's homeowner version carries this as an inline optional clause: `[, and thanks to {{referrer}} for passing on our details]`.

### Merge field

**Front remains the inbox and the saved-reply store** (ruled 3 September 2026, OR-36). **The merge-field syntax stands**: all templates use the `{{recipient.first_name}}` merge field, and template IDs remain Front saved-reply names.

⚠ **This is not in tension with monday being the pipeline.** `[R-CRMSOT v2]` makes monday the single source of truth for **CRM-class items** — leads, deals, accounts, contacts, materials. Front is where the **email** lives and where the saved replies are stored. Two systems, two jobs; neither displaces the other.

### Audience tiers

Communications are adjusted by audience. **There are FIVE audiences, and Commercial is one of them** (ruled 3 September 2026, OR-35).

⛔ **The claim that "the four tiers match Sales Qualification and Pricing Rules exactly" is DROPPED.** It was never true: those documents carry **Commercial** as a tier and fold Cabinetmaker into Builder/Trade, and T-DECLINE-04, -05 and -06 all ship a "Trade / **Commercial** version" heading with no audience behind it. Commercial now has its own register below.

| Tier | Tone | Decline honesty | Example opener |
|---|---|---|---|
| **1. Builder / Trade** | Concise, factual, peer-to-peer. No hand-holding. Assume technical literacy. | Full technical reason. They can handle it and they'll respect you for it. | "Hi [Name]," — straight into content. |
| **2. Cabinetmaker** | Collaborative, technically specific. They're coordinating trades and need precise info to do their job. | Full technical reason, framed around how it affects their coordination role. | "Hi [Name]," — straight into content, but include context they can forward. |
| **3. Standard Residential** (referred through trade) | Professional, moderate explanation. They've been referred by a builder or cabinetmaker — they expect quality but aren't experts. | Real reason, but framed in outcome terms ("this approach leads to visible imperfections") not process terms ("our CNC tooling can't achieve the radius"). | "Hi [Name], thanks for getting in touch." |
| **4. Direct Homeowner** | Warm, patient, explanatory. They may not know what information is needed or how the process works. Guide them without condescending. | Softer framing. Focus on outcomes and quality protection rather than technical specifics. Never make them feel stupid for asking. | "Hi [Name], thank you for considering SteedForm for your project." |
| **5. Commercial** | Businesslike and programme-aware. The reader is coordinating a fit-out against a build programme and a budget, often on someone else's behalf. Lead with what it means for their schedule and scope, not with fabrication detail. | Full reason, stated in scope-and-programme terms. Give the constraint plainly and early — a commercial reader is deciding whether to keep you in the tender, and a soft decline wastes their time. | "Hi [Name]," — straight into content, and name the project. |

**Where the fifth audience is used.** T-DECLINE-04, T-DECLINE-05 and T-DECLINE-06 already carry a **"Trade / Commercial version"**; that heading is the Commercial audience in practice, and it is now a named audience rather than an orphan label. T-QUALIFY-01 is **Trade / Commercial only** and is the template a commercial enquiry most often receives.

---

## 6. The standing referral practice

When declining a project, refer the enquirer to:

> **Legacy Granite & Marble**
> 555 Churchill Road, Kilburn SA 5084
> 0480 282 715
> legacygraniteandmarble.com.au

**These are the corrected details.** There is **no email address** in this referral. An email address (`contact@stonesurfaces.page`) was carried in the homeowner-version declines (T-DECLINE-04/05/06) and in this referral block, and shipped to real customers, until v1.4 removed it: it matched neither the business named nor the website beside it. The trade versions were always correct. Never reintroduce an email address to this block, and never infer one.

This is SteedForm's standing referral for declined work — homeowner, trade, commercial. Include the full contact details in the decline. Frame it helpfully: "they work directly with homeowners on projects like yours" (for homeowners) or "you could try Legacy Granite & Marble" (for trade). Never leave someone with just a "no."

### Exceptions to "every decline"

The source's voice-rule wording is "when declining a project for **any reason** … include their full contact details in **every** decline." Two templates override it, and both are later and specific:

| Template | Referral treatment |
|---|---|
| **T-DECLINE-07** (client-supplied / install-only) | ⛔ **Never refer to Legacy.** The redirect is SteedForm supplying the material; a referral throws away a live conversion. |
| **T-DECLINE-06** (Dekton) | **Conditional.** Refer to Legacy *only* if the spec is locked on Dekton and the client won't consider alternatives. |
| **T-DECLINE-08** (no trade account) | Included, but **below** the trade-route redirect — never as the primary answer. |

---

## 7. Other templates in `Communications.md` (not screening-verdict responses)

Carried here as an index only; their text is not this document's to own. Full text remains in `Communications.md` v1.6.

| ID | Stage | Purpose | Note |
|---|---|---|---|
| T-QUOTE-01 | Quoting → Follow-Up | Quote delivery (Trade · Homeowner versions) | Attachment: CounterGo quote PDF |
| T-QUOTE-02 | Quoting | Quote revision after a scope change | — |
| T-FOLLOWUP-02 | Follow-Up | Quote follow-up, no response | — |
| T-FOLLOWUP-03 | Follow-Up → Close | Final follow-up / close-out | — |
| T-ORDER-01 | Order Confirmed | Order confirmation / next steps | ⚠ Declared a **placeholder structure** in the source — timelines to be populated from StonePro |

**Declared not yet written:** T-ORDER-02 (measure booking), T-ORDER-03 (install scheduling), T-STATUS-01 (production update), **T-VARIATION-01 (scope variation discovered at measure — the source's own highest-priority gap)**, T-WARRANTY-01, T-COMPLAINT-01. The Pipeline Communication Map lists T-ORDER-02, T-ORDER-03 and T-STATUS-01 as though they exist; they do not. Do not attempt to send them.

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed every item this document used to carry — **OR-03, OR-08, OR-09, OR-10, OR-11, OR-16, OR-18, OR-34, OR-35 and OR-36 are ruled**, and their positions are now stated plainly in the sections above. Four items remain open across the knowledge base; these are how they bear on this document.

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-20** | Whether the screen quotes the **10–12 day SLA** or the **14–16 day actual** to a customer. The internal two-factor math is unaffected — this is purely a question about what is said out loud | **The live risk in this document.** T-INFO-01 and T-FOLLOWUP-01 both promise *"a quote within two business days"* — that is quote turnaround and is **not** in dispute. What is unsettled is any **production or install lead time** a drafted message adds. **Until it is ruled, state no production lead time in an outgoing message**; give the quote-turnaround promise as written and leave the install date to the person sending |
| **OR-26** | **The CRM boards could not be reached, so no board identifier has been verified against the live board.** Corpus population counts are unreconciled on the same evidence | Light. This document cites one identifier — `color_mm64t0aj` Customer Tier, in T-DECLINE-06's A-tier gate — and it must be confirmed against `08-board-and-column-registry.md` before it is relied on. **A tag check is not an identifier check.** The counts quoted in template metadata (*"4 in one month, August 2026"*) are dated measurements, not live facts |
| **OR-38** | The wider implications of the OR-07 ruling, **held for scoping**: is the Screening Philosophy / distance-from-optimum lens retired, and does all stone move to one ladder? | Indirect — the lens belongs to `03` and `05`, and no template text turns on it. It is listed so a reader of this document alone does not have to guess whether the set of open items is complete. **Nothing in OR-38 may be applied as a rule** |
| **OR-30** | The markup-category list is still to be set — an **outstanding MD action** | Does not touch this document. Markup is a pricing lever and never appears in a template; it is owned by `04-customer-and-account.md` §1.4. Recorded here only so the four remaining items read as one set |

⚠ **Two things this document flags as needing amendment at their SOURCE — neither is an open question.** Both are ruled, and this document already states the ruled position: **`SteedForm Identity` still carries "never name substitute brands in a first-contact decline"** (superseded for T-DECLINE-06, §2 and §5) and **"Tenanted occupied residential building → DECLINE"** (retired, T-DECLINE-05). Identity is stale on both points until it is edited.
