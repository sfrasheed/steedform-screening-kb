# 02 — Verdicts and Precedence

**Status:** Active. Subordinate to `01-rule-register.md`: where this document and the Rule Register disagree, the Register is correct and this file is stale.
**Owner:** MD
**Last updated:** 3 September 2026 — rulings of 3 September 2026 propagated
**Scope:**
- **Owns:** the verdict vocabulary; the order in which rules are applied to reach a verdict; the blocking / non-blocking test and the closed blocking list; the separation of capability from risk at verdict level; when a screened item must be screened again; the output contract for a screening brief.
- **Does not own:** the canonical statement of any rule (`01`); how each dimension is scored (`03`); what evidence is required to judge at all (`06`); the message sent once a verdict is reached (`09`).

---

## What this document decides

Four verdicts, one order of application. The order matters more than any single rule: client fit is settled before drawings are even looked at, a blocking flag routes to a human rather than to a decline, and missing paperwork only decides the outcome when nothing decisive is already known. Three conditions can never be auto-declined by a machine no matter how confident the evidence looks. When in doubt the answer is Needs Review, never a guess.

---

## 1. The verdict vocabulary

There are exactly four board verdicts. They are not interchangeable and they go to different people.

| Verdict | Meaning | Who acts next |
|---|---|---|
| **Qualified** | Clean, or carrying non-blocking flags only. The flags travel with it to the deal. | Estimating — proceed to quote |
| **Needs Info** | Something the **client** must supply is missing, and nothing decisive is known without it. | The client, via an information request `09` |
| **Needs Review** | A **human at SteedForm** must make a call before this goes further. | A named person — MD, GM or estimator |
| **Unqualified** | A confirmed decline rule applies, or client fit is unresolved or declined. | Decline communication `09` |

⚠ **Needs Info and Needs Review are not variants of each other.** `[R-DRAWINGS v1]` routes missing drawings to **Needs Info** — the client must supply something. `[R-BLOCK v3]` routes a blocking flag to **Needs Review** — a human decides. Collapsing the two sends the wrong request to the wrong party.

### The PDF brief vocabulary

A written Estimator Screening Brief uses **PROCEED / ASSESS / DECLINE**. The mapping is: PROCEED → Qualified · ASSESS → Needs Review · DECLINE → Unqualified. The mapping is always subject to the precedence ladder below — in particular the three carve-outs at step 1 are never auto-Unqualified in either vocabulary.

⚠ There is a known defect here: the renderer that produces the PDF accepts only the four board verdicts and rejects PROCEED / ASSESS / DECLINE outright, so the documented PDF vocabulary cannot currently be rendered. Recorded as **DEF-02**; the owner left it unprioritised on 3 September 2026, so the board vocabulary is the one in use.

---

## 2. Verdict precedence — apply in this order, stop at the first that resolves

| Step | Test | Verdict |
|---|---|---|
| **0** | `[R-CLIENTFIT v1]` — no safely linked Account and `Client Fit` is not `Approved New`; or `Client Fit = Declined` | **Unqualified.** Stop. |
| **1** | A confirmed auto-decline rule applies `[R-BLOCK v3]` — **except the three carve-outs below** | **Unqualified** |
| **2** | Any blocking flag `[R-BLOCK v3]` | **Needs Review** |
| **3** | Missing or unreadable documents **and nothing decisive is known** `[R-DRAWINGS v1]` | **Needs Info** |
| **4** | Clean, or non-blocking flags only | **Qualified** |

**When uncertain, Needs Review — never guess.**

### Step 0 is genuinely first

`[R-CLIENTFIT v1]` runs after junk triage and safe account matching, but **before drawings and before every technical and commercial disposition rule**. It therefore outranks Needs Info for missing drawings *and* Qualified for clean drawings. Drawing presence, readability, job size, material and technical merit **may never upgrade an unresolved client-fit outcome**. Preserve and file the supplied evidence; do not let a drawing rescan promote the lead.

### The three carve-outs at step 1 — never auto-declined

A machine may never turn these away on its own. Each forces **Needs Review** so a named human confirms first.

| Carve-out | Why it is a carve-out |
|---|---|
| **Live Customer Tier = `Do-Not-Quote`** `[R-C1 v4]` | Commercial disposition is a relationship decision. Cite the Account item ID and route to a person. |
| **The Dekton materiality exception** | The four-condition test is a judgement, not a keyword match. See `05-material-and-capability.md` §8. |
| **Building occupancy** `[R-OCCUPANCY v1]` | An occupied dwelling or trading ongoing concern is a carve-out, never an auto-decline. The decline letter may only be sent after a human review. |

The stated reason is the same in all three cases: **keyword evidence is too weak to auto-decline on.**

---

## 3. Blocking versus non-blocking

**The test:** *does resolving this change whether we WANT the job, or only what we charge or confirm?*

- Changes whether we want it → **blocking** → Needs Review.
- Changes only price or confirmation → **non-blocking** → the lead may stay Qualified and the flag travels to the deal.

### 3.1 The blocking list — TWO layers, both closed `[R-BLOCK v3]`

**LAYER 1 — the base list.** Applied since screening began; **registered 3 September 2026**, having had no rule behind it until then.

| Condition | Rule |
|---|---|
| Occupancy — occupied dwelling or trading ongoing concern | `[R-OCCUPANCY v1]` |
| Live Customer Tier `Do-Not-Quote`, or an unresolved account match | `[R-C1 v4]` `[R-ACCTMATCH v5]` |
| Out of area, while the Supply Only conversion is undecided | `[R-AREA v1]` |
| Spec conflicts | `[R-30MM v1]` `[R-PROFILE v5]` `[R-ALFRESCO v1]` |
| Below the one-slab minimum, non-A-tier | `[R-C3 v1]` |
| The natural-stone rule set | `[R-NATURAL v1]` |
| Unknown entity — "who is asking" | `[R-ENTITY v1]` |
| Interstate material on a non-A residential job | `[R-INTERSTATE v1]` |

**LAYER 2 — the 20 July 2026 addition set. SIX rules, not seven.**

| # | Blocking rule | Dimension | Rule |
|---|---|---|---|
| 1 | Clad fireplace with no published brand rule (a brand-ruled fireplace is non-blocking 🟡) | Detail, echoes to Install | |
| 2 | Trench or rebate to receive joinery | Detail | |
| 3 | First-of-kind fabrication with no fabrication rule | Manufacture | |
| 4 | Appliance QC Status = `Rejected — Do Not Use` | Manufacture | `[R-MA5 v3]` |
| 5 | Vein-match Level-3, or match-to-existing installed stone | Material | `[R-MA2 v1]` |
| 6 | Client-supplied stone — hard stop, **except on an A-tier account**, where it is 🔴 Needs Review | Material | `[R-SCOPE v2]` |

⚠ **"Seven" is stale wherever it appears.** The count has been found and fixed four separate times, and each time it silently revived the struck curves rule.

⛔ **"Curves >40mm" was STRUCK from layer 2 on 23 July 2026** and must never be re-added. Above a material's polish limit the curve becomes a faceted mitre — 🟡 plus a mandatory documented client sign-off, not a decline `[R-D5 v9]`.

⚠ **Ropox Flexi Electric is APPROVED and is NOT first-of-kind** `[R-BLOCK v3]`.

**Amendment authority:** both layers are amended only by an **MD or GM** decision, recorded in the Register with a version bump.

### 3.2 What the layers changed

Nothing the screen *does* changed on 3 September 2026. What changed is the authority behind it: seven conditions the screen had applied every day were registered for the first time, so a reader can now find the rule behind each one instead of finding only the behaviour.

### 3.3 Non-blocking flags

The lead may stay Qualified; the flags travel to the deal. Dimension gaps · colour TBC · access notes · expectation resets · part-slab waste pricing · first-natural-job confirms · timeline-pressure maths · vein-continuity geometry flags below Level 3 `[R-MA2 v1]` · masons-mitre substitute notes · overhang-limit flag-upfronts.

**Volume and room count are RETIRED as a verdict test.** Slab count appears only as a pricing note in flags. Complexity flags — curves, mitres, vein matching — still apply on top.

---

## 4. Capability is not risk `[R-ANDON v2]`

**⛔ CAPABILITY and 🔴 RISK are two different verdicts and must never blend.** This is an MD ruling of 23 July 2026, and it sits at verdict level, not just in the score strip.

| | Meaning | What follows |
|---|---|---|
| **⛔ CAPABILITY / NOT-OFFERED** | *"We cannot make this."* | A **hard stop**. No human call can authorise it — the tooling, the material physics or the ruled scope is not there. The spec is **reset**, not priced. |
| **🔴 RISK** | *"This is far from our optimum."* | A **human call**. Take it and price it properly, or decline it as not for us. **Both answers are valid.** |

**Say which one it is, every time.** Blend them and one of two failures follows:

- Treat a capability gap as risk → someone eventually **human-calls their way into promising a job that physically cannot be made**.
- Treat risk as capability → screening starts **declining work SteedForm actively sells**. A boxed island is 🔴 on geometry but is standard, all-material, charged work.

⚠ **Known live defect:** both currently render as one undifferentiated 🔴, in the risk strip and in the PDF alike. `[R-ANDON v2]` names this as the bug it was written to fix, and it is still unfixed. Recorded as **DEF-02**; the owner left it unprioritised on 3 September 2026, so the board vocabulary is the one in use.

**What action a ⛔ NOT-OFFERED item takes is now RULED, and it differs per item** `[R-SCOPE v2]`. `[R-ANDON v2]` classifies; `[R-SCOPE v2]` disposes.

| Action | Items |
|---|---|
| **DECLINE or refer** | Flooring · stone shower bases and fall drainers · drainer grooves · bathroom hobs · machined recesses, chutes, glazing · remedial work on someone else's stone · client-supplied slabs · IKEA kitchens |
| **RESET the spec** | Flush mounting → a supported mount `[R-FLUSH v1]` · masons mitre → the standard mitred build · ogee → a **lamb's tongue** (Provincial) |

⛔ **A DECLINE item is not a specification to be corrected.** ⛔ **A RESET item is not a decline** — the enquiry continues on a supported specification and the client is told before the quote goes out.

**Client-supplied slabs carry the only carve-out:** a hard stop for every account **except A-tier**, where it becomes 🔴 Needs Review for a named human. **The CNC masons-mitre exception is production's discretion and the screen must never promise it.**

---

## 5. Re-screening `[R-RESCREEN v1]`

Every risk strip records the rules version it was scored under. A verdict is only as current as the rules that produced it.

| Trigger | Status |
|---|---|
| **Account changed → re-screen.** A tier, status or rating change re-screens that account's open leads. | Live |
| **Rules changed → re-screen.** When a Register rule bumps its version, every open lead whose strip was stamped under the older version is **stale by definition**. | **Not built** |

**Why it matters:** on 25 July 2026 the faceting threshold changed and **84 strips were stale**. They were found only because a person went looking. A rule can be corrected everywhere and still leave every previously screened lead carrying the old verdict.

**Standing rule — new documents.** New or changed documents arriving on an already-screened lead force a re-screen; a human resets the Claude Scan status to `Requested`.

⚠ A brief that carries no rules-version stamp cannot be found by trigger 1 at all. The stamp should be treated as required, not optional.

---

## 6. The screening brief — output contract

A screen produces one of two outputs. **Board mode** writes the takeoff and verdict to the lead and produces no PDF. **Brief mode** produces an Estimator Screening Brief for an ad-hoc screening request.

### 6.1 What a brief must contain

| # | Section | Contents |
|---|---|---|
| 1 | **Header** | Project address, project name, builder, designer, owner, date |
| 2 | **Verdict box** | The verdict with a one-line summary |
| 3 | **Screening scorecard** | The six-dimension risk strip `03` |
| 4 | **Stone scope table** | Every stone item per residence or apartment: area, item type, edge treatment, level, notes |
| 5 | **Summary box** | Total item count, **plus what is NOT stone** — so the estimator knows the boundaries |
| 6 | **Conditions before quoting** | Numbered action items with owner assignments |
| 7 | **Why this job fits** (or does not) | The commercial reasoning |
| 8 | **Footer** | Source documents, screening framework version, job count |

⚠ Item 3 was originally specified as a **four-axis** scorecard (Material & Complexity, Supplier Proximity, Building Occupancy, Site Access). **Six is canonical.** The four-axis model survives only as an explanatory lens and must never act as a second operative scorer — see `03-risk-scoring.md` §4.

### 6.2 Conditions — owner and severity

Every condition gets a number, a bold title, detail text, and an **owner**.

| Owner | Scope |
|---|---|
| **Builder** | Things the builder must do or supply |
| **SteedForm** | Internal actions — outdoor suitability check, BBQ cabinetry spec |
| **SteedForm + Client** | Joint decisions — stone colour selection, flush-mount alternative |
| **Programmer** | Technical prep — cutout specs, appliance library checks |

**Severity:** items that must be raised at first contact with the builder are marked **(FLAG UPFRONT)** in red. Hard technical constraints are red. Standard conditions take normal formatting.

Two conditions are always FLAG UPFRONT: **vertical access** where stone must reach an upper floor and the lift will not take it, and **flush mount** `[R-FLUSH v1]`. Both affect price, schedule and whether the job proceeds at all, and both are remakes if discovered at install.

### 6.3 Content rules

These exist because the opposite was tried and corrected.

1. **Only flag anomalies.** The estimator knows 20mm splashbacks are standard, that straight edges over 20mm are mitred, that undermount sinks need minimum edge distances. Do not explain standard rules — flag only what breaks them.
2. **Never propose substitution when the brand has a local supplier.** See the supplier list in `05-material-and-capability.md`.
3. **Do not explain edge-treatment rules in body text.** The scope table shows the edge for reference; the brief does not teach the estimator what mitred means.
4. **Summary box carries only what is NOT stone** — the item count and the non-stone items. No fabrication-method descriptions.
5. **Vertical access is an upfront flag, not a routine note.**
6. **Flush mount is NOT OFFERED and is flagged at screening** `[R-FLUSH v1]`, with the reason stated: chipping, silicone gap, brochure versus reality.
7. **An outdoor BBQ always raises a builder-communication condition.** The BBQ must fit *after* stone install, so the builder needs cabinetry dimensions, ventilation gaps, cutout specs and gas access **before** they build the cabinet.
8. **Brand caveats are relevant only when that brand is specified.** Caesarstone Porcelain restrictions on a job that uses another material are noise.

### 6.4 The renderer contract

The renderer is **data-only** — every value comes from the payload. Required: `job`, `client`, `address`, `verdict`, `risk` (all **six** dimensions), `summary`. Optional: `blocking`, `conditions`, `sources`, `screened_by`, `screened_on`, `rules_build`.

⚠ **`rules_build` should be treated as required, not optional.** A brief with no rules-version stamp cannot be found by the rules-changed re-screen trigger `[R-RESCREEN v1]`.

It refuses to render if archived-sample content appears in the payload, and raises if the risk strip is incomplete or the verdict is not one of the four board verdicts.

⛔ **The old `brief_template.py` was never a template.** It was a hard-coded script for one real job, carrying that customer's people, dates, verdict and conditions inline. Reusing it **leaked another client's facts into a new brief**. It was removed on 10 August 2026. Do not retrieve it from the archive to build a brief.

**Five defects in the current renderer are recorded in `10-open-rulings.md`** (DEF-01, DEF-02, DEF-04, DEF-05) — including that it rejects the PROCEED/ASSESS/DECLINE vocabulary specified above, that the andon symbols render as identical black squares, and that unescaped input silently drops content and crashes on the exact markup these rules ask an author to write.

---

## 7. What to do when the rules cannot be read

**KEEP CAPTURING, REFUSE TO JUDGE.** Continue intake so no enquiry is lost. Do not issue verdicts, do not write risk strips, and say so plainly. **Never fall back to an inline copy of a rule** — "probably right" is what produced the 25 July faceting mis-sell.

The same discipline applies at the ORDER gate: an ORDER screen without its accepted-quote baseline has not checked the thing it exists to check. Keep capturing, refuse to judge, and say so `[R-EVIDENCE-BAR v2]`.

---

---

## Open items

Recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.**

- **OR-20** — does the screen quote the 10–12 day SLA or the 14–16 day actual to a customer?
- **OR-26** — no board identifier could be verified against a live board on 3 September 2026
- **OR-38** — whether Screening Philosophy is retired and all stone moves to one ladder; held for scoping

⚠ **`[R-BLOCK v3]` restructures the blocking list, and the Register names an MD or GM as the amendment authority for that list.** The ruling is recorded as made; a countersign is outstanding.

---

*Related: `01-rule-register.md` (the rules themselves) · `03-risk-scoring.md` (how each dimension is scored) · `06-evidence-requirements.md` (what must be known before a verdict is possible) · `10-open-rulings.md` (what this document deliberately does not settle).*
