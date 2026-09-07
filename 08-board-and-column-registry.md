# 08 — Board and Column Registry, and Board Mechanics

> # ⚠⚠ WARNING — NO IDENTIFIER IN THIS DOCUMENT HAS BEEN VERIFIED AGAINST A LIVE BOARD
>
> **As at 3 September 2026, not one board or column identifier in this document could be verified against a live monday board. This is UNRESOLVED.**
>
> **What was established.** An attempt was made to verify these identifiers against the live monday account reached by the connector. Authenticated **as the account owner**, **six board IDs named in this document were queried directly with `state: all`** — the parameter that returns archived and deleted boards as well as active ones. **Every one of them returned an empty array.** Separately, **there is no workspace named "SteedForm CRM" in that account.**
>
> **What was NOT established.** ⛔ **This does NOT establish that the identifiers in this document are wrong.** Two explanations fit the evidence equally well and nothing available distinguishes between them:
>
> 1. **The CRM boards live in a DIFFERENT monday account** from the one the connector reaches — in which case every identifier here may be perfectly correct, and the verification simply looked in the wrong place; or
> 2. **The IDs are dead** — the boards no longer exist under these identifiers.
>
> **Neither has been ruled out. Do not report the identifiers as wrong, and do not report them as right.**
>
> **What this means for a screen.** Continue to use these identifiers — they remain the best record the knowledge base holds, and there is no better one. But **a read that returns nothing is not proof the fact is absent** `[R-READ v1]`: it may be an identifier fault. **Treat an empty or not-found result on any board named here as a FINDING to be escalated, never as a clean result.** Where a rule depends on a read that came back empty, say so rather than reporting the rule as satisfied.
>
> **Why this warning sits at the top of this file.** ⛔ **A rule-version check will not catch an identifier fault.** On 24 August 2026 a perfectly tagged, perfectly versioned LAW addressed a column that did not exist, the drift checker reported it clean, and an account-matching tier was dead for thirteen days. **A tag check is not an identifier check** — that is precisely the defect class this document exists to catch, and today it cannot do its job. Tracked as `10-open-rulings.md` **OR-26**.
>
> **What the 3 September exports DID establish.** Board exports of Materials Library, Accounts and Serviceable Areas were supplied by the owner the same day and are recorded in §7. They confirm **column names and how populated each column is**. ⛔ **They do not confirm a single identifier** — an export carries no column IDs — so this warning stands in full.
>
> **This warning is removed only when a live board read succeeds and the identifiers are checked against it — not before.**

---

**Status:** Active, **with the identifier warning above outstanding**. Subordinate to `01-rule-register.md`: where this document and the Rule Register disagree, the Register is correct and this file is stale.
**Owner:** MD
**Last updated:** 3 September 2026 — the rulings of 3 September 2026 propagated from `01-rule-register.md`
**Scope:**
- **Owns:** every monday board and column identifier a screen reads or writes, in one place; which identifiers are retired; the read and write traps that make monday return a plausible-but-wrong answer; the long_text budget.
- **Does not own:** what any field *means* for a verdict (`03`–`07`); the canonical statement of any rule (`01`).

---

## What this document decides

Where every fact physically lives, and how to get it out or in without losing it. This document exists because identifiers are the one class of fact that a rule-version check cannot catch: on 24 August 2026 a perfectly tagged, perfectly versioned LAW addressed a column that did not exist, the drift checker reported it clean, and a matching tier was dead for thirteen days. **Every other document in this set should cite a field by name and point here for its identifier**, so that the next migration is one edit rather than twenty.

⚠ **The 11 August 2026 CRM migration re-issued every board and column identifier.** Anything written before that date may name a dead identifier. Retired identifiers are listed in §5 so they can be recognised and never written to.

⚠⚠ **AND SEE THE WARNING AT THE HEAD OF THIS FILE.** As at 3 September 2026 none of what follows has been verified against a live board — six board IDs queried with `state: all` all returned empty, and there is no "SteedForm CRM" workspace in the account the connector reaches. **That does not make the identifiers below wrong; it means they are unverified, and the reason is not yet known.** `10-open-rulings.md` **OR-26**.

---

## 1. Boards

| Board | Current ID | Retired ID | Notes |
|---|---|---|---|
| **Leads** | `5029570131` | `5029570430` | Any Message-ID column on the retired board is historical and must never be written `[R-INTAKE-ID v3]` |
| **Deals** | `5029570133` | `5029570431` | |
| **Deals — subitems** | `5029570139` | `5029641469` | |
| **Accounts** | `5029570132` | — | Reached from a Lead via `board_relation_mm64fq68` |
| **Contacts** | `5029570130` | `5029570422` · `5029570423` | The retired boards sat in the *monday CRM - Test Environment* workspace. Legacy contact IDs belong to `5029570423` |
| **Materials Library** | `5029570546` | — | Unchanged by the migration |
| **Appliance Library** | `5029694677` | — | ⛔ **Returned no readable board, 5 September 2026** — §2.5 |
| **SteedForm — Sink Library** | `5030603238` | — | Exists and reads. **Not the board §2.5 describes** — §2.5 |
| **Serviceable Areas** | `5029634649` | — | Authoritative for service-area zone `07` §1 |

---

## 2. Columns by board

### 2.1 Accounts `5029570132`

| Field | Column ID | Screening role |
|---|---|---|
| Customer Tier | `color_mm64t0aj` | Commercial disposition — the only disposition **label** `[R-C1 v4]`. ⚠ **60 of 188 populated (68% blank)** — and under `[R-LEADTIME v2]` a blank tier now sets the quoted date, not just the waiver |
| Client Rating A/B/C | `color_mm64jqn0` | Behaviour. ⛔ **0 of 188 populated** |
| Rating — Payment | `color_mm64kd3q` | Sub-rating. **109 of 188 populated** — the only rating field carrying data |
| Rating — Measure-ready | `color_mm64je94` | Sub-rating. ⛔ **0 of 188 populated** — and OR-14's site-readiness ruling scores on it |
| Rating — Install-ready | `color_mm647dxb` | Sub-rating. ⛔ **0 of 188 populated** — same |
| **Notes / Flags** | `long_text_mm64njy4` | **MANDATORY evidence** `[R-ACCT v3]`. Carries `DUMP STOP` / `DUMP LOCKED` markers, ten-year revenue and win rate |
| Main POC email | `email_mm64cpfk` | Account-match ladder tier 2 `[R-ACCTMATCH v5]`. Full-string, case-insensitive. ⚠ **42 accounts have this field BLANK** (measured 10 Aug 2026), so tier 2 cannot fire for them — never a reason to fall through to an automatic name match |
| Markup | `numeric_mm64mvp3` | A per-account number. Its permitted values are undefined — see `10-open-rulings.md` |
| Account Status | `color_mm64cbq0` | ⛔ **Stale lifecycle data. Must never block, qualify, score or describe a Lead** `[R-C1 v4]`. May be displayed as context only |

⚠ **There is no `Account Value` column.** The migration did not carry it across. Ten-year revenue and win rate now exist **only** in Notes/Flags `[R-ACCTVALUE v1 SUPERSEDED]`.
⚠ **There is no `email` column** on the live Accounts board. The POC email is `email_mm64cpfk`. A query against `email` returns `ResourceNotFoundException: Column not found`.

✅ **OR-25 is CLOSED (3 September 2026). The generic-domain closed list is ELEVEN** `[R-ACCTMATCH v5]` — a domain-matching fact, recorded here because it governs which values in `email_mm64cpfk` may be matched on at all:

> gmail · hotmail · outlook · bigpond · internode · optusnet · yahoo · live · icloud · **people.net.au** · **adam.com.au**

⛔ **On a generic domain, ladder tiers 2 and 3 do not apply** — the enquiry drops to tier 4, **candidate only**, human confirmation required. The list was nine; `people.net.au` and `adam.com.au` are now ruled generic, taking it to **eleven**. The screening skill had been carrying both while simultaneously listing `adam.com.au` as a *non-generic collision* — it was on both sides of its own rule — and was short four of the original nine. ⚠ **A tag-based drift check cannot catch a short list**; count the entries.

#### 2.1.1 Nine Accounts columns this registry did not carry

Found in the 3 September 2026 export. **Column IDs are not known for any of them** — an export does not carry IDs — so they are listed by name until a live read supplies the identifier.

| Field | Populated | Why it matters to screening |
|---|---|---|
| **Segment** | 141 / 188 | ⚠ **The closest thing on the board to the trade-account test.** Cabinetmaker 50 · Builder 44 · Other 43 · Commercial 4. `[R-RETAIL v1]` turns on trade vs retail, and `[R-INTERSTATE v1]`'s gate turns on commercial. **Neither rule currently names a field** — this is the candidate, and it must be ruled before it is read |
| **Markup (SP)** | 130 / 188 | A **second** markup field, distinct from `numeric_mm64mvp3`. Values run −25 to −60, dominated by **−35 (71)** and **−40 (47)**. OR-30 records the markup-category list as "still to be set"; the board is already carrying a de facto one |
| Domain | — | Derived from the POC email. Does not replace the `[R-ACCTMATCH v5]` ladder |
| Rating updated | — | Date stamp on the rating fields |
| StonePro Customer # | — | Cross-system key. Not a screening input |
| Salesperson | — | Not a screening input |
| Legal Name | — | Not a screening input; **do not use for account matching** `[R-ACCTMATCH v5]` |
| ABN | — | Not a screening input |
| Industry | — | Overlaps Segment. Prefer Segment |

⛔ **None of these may be read by a rule until a rule names it.** They are recorded so the next person does not rediscover them, and so `Segment` in particular is not quietly wired into the retail gate without a ruling. `00` states the principle: **if a field on the record would change a human's decision and no rule names it, that is a gap in the rule** — Segment is that gap, written down.

⚠ **Do-Not-Quote appears in two fields and they disagree** — Customer Tier holds **13**, the stale Account Status holds **11**. `[R-C1 v4]` already rules the tier authoritative and the status excluded. This is that hazard, live, in the data.

### 2.2 Leads `5029570131`

| Field | Column ID | Screening role |
|---|---|---|
| Account relation | `board_relation_mm64fq68` | Follow this to Accounts. Reading it as ordinary text returns null `[R-READ v1]` |
| Client Fit | `color_mm69h52c` | `Recognised` · `Approved New` · `Review Required` · `Declined` `[R-CLIENTFIT v1]` |
| Screening Flags / Decline Reason | `long_text_mm64zg50` | ⛔ **Never prepend** `[R-LONGTEXT v2]` |
| Internet Message-ID | `text_mm64cjv2` | Stored **bare**, angle brackets stripped `[R-INTAKE-ID v3]` |
| Files | `file_mm64vge9` | Drawings and attachments |
| ⚠ Risk Profile | `long_text_mm64e8bs` | ✅ **CONFIRMED — the column of record** (OR-23, ruled 3 Sep 2026). Written as a **whole-column REPLACE** on every screen and re-screen `[R-LONGTEXT v2]`. The competing `long_text_mm5ddgqa` sits on the **retired** Leads board `5029570430` and is now in §5 |
| ~~Client Required-By~~ | ⛔ **RETIRED — do not read** | ⛔ **THE COLUMN IS BEING RETIRED** (OR-24, ruled 3 Sep 2026). **Neither `date_mm64jz0c` nor `date_mm5ck0y1` is to be relied on.** Both are in §5. The two-factor timeline rule reads **prose only** from now on — `07-service-area-and-site.md` §6 |

✅ **OR-23 is CLOSED.** The `⚠ Risk Profile` column is **`long_text_mm64e8bs`**, and the "disputed" marking is removed. The `mm64*` prefix matches every other current-board column, and `long_text_mm5ddgqa` belongs to the retired board. ⚠ **This is a documentary ruling, not a live-board verification** — it settles which identifier this knowledge base carries, and the warning at the head of this file still applies to it as to every other id here.

⛔ **OR-24 is CLOSED by RETIREMENT, not by choosing a winner.** The question was *"which of the two Client Required-By identifiers is live?"* The answer is **neither** — **the column is being retired**, both identifiers move to §5, and the two-factor timeline rule now reads the requested date from **prose only**. **Do not reinstate either id**, and do not treat a blank date column as evidence that no date was requested: that silent-failure mode is what the retirement removes.

### 2.3 Deals `5029570133`

| Field | Column ID |
|---|---|
| Quote Sent | `date_mm64e491` |
| Quote # | `text_mm643406` |
| Quote Revision | `text_mm64jj0j` |
| Job Type | `color_mm64htd3` |
| Suburb | `text_mm649q9d` |
| Quote Notes from Drawing | `long_text_mm6465nw` |
| Quote Summary | `long_text_mm64a7d` |
| CounterGo Quote PDF | `file_mm64df53` |
| Superseded quote | `file_mm64rcaj` |
| Client Drawings | `file_mm643zyy` |
| Drawing | `file_mm64g3zr` |
| Originating Lead | `board_relation_mm64xgbc` |
| Source Lead ID | `text_mm656wzh` |
| Confirm Order button | `button_mm653bn9` |
| Lock group | `group_mm64cyzj` |

**Deals subitems `5029570139`:** Material/Colour `text_mm658tz0` · Thickness `text_mm65wgm9` · Edge `text_mm65dakh` · Cut Out 1 `color_mm65kbrk` · Cut Out 2 `color_mm65pzp3` · Cutout notes `text_mm657f15` · Price `numeric_mm65bp9c` · Material linked `board_relation_mm655691` · Line Type `color_mm6525jy`.

### 2.4 Materials Library `5029570546`

| Field | Column ID | Screening role |
|---|---|---|
| Material Type | `color_mm4qt817` | Class, read **live**, never inferred from a brand name `[R-M1 v2]`. Class scoring: engineered 🟢 · porcelain + sintered 🟡 · natural 🔴. **Ceramic scores as porcelain / sintered — 🟡.** ✅ **392 / 392 populated, three values only** — Engineered Stone 171 · Porcelain 168 · Natural Stone 53. Maps cleanly onto the three rungs. ⚠ **OUTSTANDING DATA ACTION — see below** |
| **Brand / Range** | `dropdown_mm4p7eja` | **Which manufacturer's table applies.** `[D11]`'s overhang limits are per brand and differ by a factor of two between brands stocked side by side, so this column decides which row of `05` §6.1b is read. ⚠ **Brands live HERE, not in the item name** — item names are colours (*Absolute Black*, *Landr*). Verified 7 Sep 2026: Zenith Surfaces 57 · Dekton 50 · Caesarstone ICON 45 · Lavistone Gen Surface 41 · Sensa 35 · Vasari Porcelain 32 · Neolith 31 · Silestone QXERON 25 · Caesarstone Porcelain 24 · Smartstone Sintered 24 · Scalea 18 · Eclos 7 · Kaya Surfaces 3 |
| Stone Sub-Type | `dropdown_mm4rq7jd` | **Granite · Marble · Quartzite · Travertine · Limestone** — every branch `[R-D5 v8]` needs, corrected 7 Sep 2026 from an earlier note calling it granite vs non-granite. ✅ **Verified 3 Sep 2026: 3 of 392, all `Marble`** — Scalea Arabescato Corchia, Sensa Arabescato Corchia, Sensa Nero Portoro. Exactly what `[R-SUBTYPE v2]` records. The library holds **53 natural stones**, so `[R-D5 v8]`'s conservative fallback fires on **50 of 53** — a blank takes the conservative branch plus a visible flag `[R-SUBTYPE v2]` |
| **Print Construction** | `color_mm6hz0dd` | `Face-printed` · `Full body` · blank. **Blank FAILS CLOSED to review — never read blank as "not printed"** `[R-PROFILE v5]`. ⛔ **99% BLANK — see §7.1. The rule is correct and the column is not being maintained the way it assumes** |
| Bookmatch Available | `boolean_mm4r4qcp` | Vein-match feasibility `[R-MA2 v1]` |
| Discontinued | `boolean_mm4r934z` | A discontinued colour scores 🟡 |
| Alias Names | `long_text_mm4ps74s` | Alternate names for the same material. Matching remains exact and unique — no fuzzy or closest-result matching `[R-MATERIAL-TERMS v1]`. ⛔ **100% BLANK.** There are no aliases, so every alternative name a customer writes fails to match — silently, because exact matching has no fallback to report |
| **Outdoor Suitability** | *(ID unknown)* | ⚠ **Not previously in this registry.** 41 / 392, **all Lavistone**, all `Prohibited`. **Supplementary only — it may tighten `[R-ALFRESCO v1]`, never relax it.** See `05` §1.1.1 |
| **UV Resistance** | *(ID unknown)* | Same 41 rows, all `No`. No rule reads it |
| **Technical Reviewed** | *(ID unknown)* | Same 41 rows, all 18 Aug 2026. **This is the field that says how far the outdoor review actually got** — one brand |

⛔ **OUTSTANDING DATA ACTION on `color_mm4qt817` — Vasari** `[R-M1 v2]`. **OR-19 is ruled: Vasari's class of record is CERAMIC**, and ceramic scores on the porcelain / sintered rung (🟡). **The Materials Library value for the Vasari items is TO BE SET to match.** Until it is set, the board and the ruling disagree, and the board is what a screen reads.

| | |
|---|---|
| **Column** | `color_mm4qt817` Material Type, Materials Library `5029570546` |
| **Items** | the Vasari items |
| **Action** | set Material Type to **ceramic** |
| **Status** | **NOT DONE.** This is a data action, not an open question — the class is ruled |
| **Interim** | score Vasari **🟡**, on the porcelain / sintered rung, per `[R-M1 v2]`. ⛔ **Do not infer the class from the brand name** in either direction, and do not read a stale board value as overriding the ruling — flag the mismatch |

⚠ **This is exactly the failure shape this document exists to catch:** a rule that is correct, tagged and current, pointing at a board value that has not yet been changed to match it. **The rule is not wrong and the column is not wrong — they simply do not yet agree.**

### 2.4b Contacts `5029570130` — how an emailed enquiry finds its account

**Verified live 7 September 2026.** 538 items. This section exists because
`[R-ACCTMATCH v5]`'s tiers 2 and 3 match on an EMAIL ADDRESS, and until today nothing
could query a column value — so those rungs never ran and every emailed enquiry from a
known customer stopped at "the link was never proved".

| Field | Column ID | Screening role |
|---|---|---|
| **Email** | `contact_email` | **The tier-2 rung.** Match the sender's address here *exactly* |
| **Accounts** | `contact_account` | **The way across.** A relation — read `linked_item_ids`, then fetch those records. This is what turns a matched contact into an account |
| Phone | `contact_phone` | Not a matching key |
| *Company | `text_mm64h04v` | Free text on the contact. **Not** the account name — the relation is the account |

**The ladder, as it actually runs:**

1. **Tier 2 — exact address.** Match the sender on `contact_email`. One hit gives you a
   contact; follow `contact_account` to the account and read the whole record.
2. **Tier 3 — domain.** Match the domain fragment on `contact_email`. ⛔ **A domain is
   only a match if EVERY hit points at the SAME account.** Two accounts on one domain is
   an ambiguous match, which is `Needs Review`, not a pick.
3. Accounts also carries `email_mm64cpfk` *Main POC email address* — one address per
   account, so it answers only when the sender happens to be that person. **Contacts is
   the broader index and should be tried first.**

⚠ **Worked example, 7 Sep 2026.** `adele@classiquerobes.com.au` matches contact *Adele
Steventon* exactly, whose `contact_account` is `2827398298`. A domain search returns ten
contacts, **all pointing at that same account** — an unambiguous tier-3 match. The answer
was one query away; the screen lacked the tool, and reported a missing capability as an
unconfirmed customer.

---

### 2.5 Appliance Library `5029694677`

⛔ **`5029694677` RETURNED NO READABLE BOARD ON 5 SEPTEMBER 2026.** Authorised by
Matthew Rasheed, recorded by Stella Rasheed. A direct read of that id through the app's own token came back with no board — the
same answer a board gives when it does not exist and when it has not been shared, and the two
cannot be told apart from a read. **Every column ID in the table below is therefore unverified
against anything live**, which is what `06-evidence-requirements.md` OR-26 already warned.

**The rules that read this board are unchanged and remain in force.** `[R-MA5 v3]`, its
`Rejected — Do Not Use` hard block and the `[R-EVIDENCE-BAR v2]` ORDER rows all stand. A rule
pointed at data that is not there is still a rule; deleting it would remove the gate as well as
the gap, and a rejected cutout would then screen clean with nothing to say why. The behaviour
below — **unverified by default, and a blank read is never a pass** — is what a screen does, and
it is the same whether the board is missing or merely unreachable.

⚠ **The Sink Library is NOT this board renumbered.** `5030603238 · SteedForm — Sink Library`
exists, reads, and holds 863 items — and it is a supplier-data reconciliation board, not a
verification library. None of the identifiers below appear on it. Its columns are
`color_mm667vav` Asset Status, `color_mm66evww` Audit Status, `text_mm662pp3` SF Cutout
Dimensions, `text_mm66fzfn` Supplier Cutout Dimensions, `dropdown_mm6664tg` Supplier
Installation Methods, and a family of `* Match` status columns comparing SteedForm's record
against the supplier's.

⛔ **`Audit Status` IS NOT `QC Status`.** One says whether SteedForm's copy of a supplier's data
agrees with the supplier's. The other says whether a physical unit has been measured, programmed,
cut and dry-fitted. **Reading one as the other would let a data-audit tick pass as a release
verdict.** Whether any part of the Sink Library may satisfy any part of the QC gate is an open
question for the owner of `[R-MA5 v3]` — it is carried in `10-open-rulings.md` and has not been
ruled. Until it is, nothing on `5030603238` closes an appliance gate.

| Field | Column ID | Screening role |
|---|---|---|
| **QC Status** | `color_mm4zzgaq` | **The release verdict — the operative column.** Labels: `Verified — Released` · `In Verification` · `Requested` · `Legacy — Needs Review` · `Rejected — Do Not Use` |
| Verification Stage | `color_mm4zvvhg` | The 9-stage workflow. **Not the QC verdict.** `Failed — Rework` is a value of *this* column and must never be cited as the QC block |
| Mount Type | `color_mm4zdfnd` | The mounting method. Required at the ORDER bar `[R-EVIDENCE-BAR v2]`; flush mount is not offered `[R-FLUSH v1]` |
| Cutout Spec | `long_text_mm4zayzp` | Dimensions and offsets taken from the dry fit. The source of the corner-radius conflict check |
| Received Date | `date_mm4zpzp0` | When the unit was receipted |

⚠ **`Released — Verified` is a GROUP TITLE, not a status label.** Matching on it silently fails. The label is `Verified — Released` `[R-MA5 v3]`.

⛔ **THE APPLIANCE LIBRARY IS A SINKS LIBRARY.** Confirmed by the owner, 3 September 2026: *"I only have sinks library, not appliance."* Everything in this section is real and applies **to sinks**. It follows that `[R-MA5 v3]`'s QC Status gate has **no data behind it for cooktops, ovens, rangehoods or barbecues** — a QC lookup on one of those returns nothing, and **nothing is not a pass** `[R-READ v1]`.

**What a screen must do until an appliance library exists:** treat a **non-sink** appliance as **unverified by default** and route it the way `[R-MA5 v3]` routes an unverified unit — the physical unit at SteedForm before measure, supplier CAD interim only. **Do not report the QC gate as satisfied because the lookup came back empty**, and do not let a blank read pass a cooktop cutout through as verified. ⚠ This is the same shape as the Print Construction finding: a rule that is correct, pointed at data that is not there.

---

## 3. Board mechanics — reads

### 3.1 Reference data comes from the board, every screen `[R-REF v2]`

Never from memory, an earlier pass, a historical note, a pasted snapshot, or a value copied onto the lead. **Cite the board item ID** so the read is auditable.

⛔ **"From the board" means the RECORD, not a column list.** A rule naming columns states the minimum, never the maximum. If a field on the record would change a human's decision and no rule names it, **that is a gap in the rule, not permission to ignore the field.**

⚠ **Mirror columns are API-blind.** Every `lookup_*` returns "Column value type is not supported". They are for human eyes only; follow the `board_relation` and read the linked item directly.

### 3.2 Three read traps `[R-READ v1]`

All three return a plausible-but-wrong answer, and **all three produce "nothing found" when something IS there.**

| Trap | What happens | What to do |
|---|---|---|
| **`board_relation` reads null** | Ordinary `text` and `value` reads return null even when correctly linked. Every linked account looks unlinked, silently disabling every account-keyed rule | Use a relation-aware read or a typed GraphQL fragment to get `linked_item_ids` |
| **Unpaginated scans** | The default page is 25 items. An unpaginated "scan the board" check inspects the first 25 and reports clean | **PAGINATE EVERY BOARD SCAN** |
| **Status-label filters** | Can return zero matches even when matching items exist | Prove the filter works on a known-positive before believing an empty result |

**Never treat an empty result as proof of absence until the read itself is proven.**

---

## 4. Board mechanics — writes

### 4.1 A success response does not mean the value persisted `[R-WRITE v2]`

**Verify by re-reading.** The shared shape: **monday fails LOUDLY on malformed structure and SILENTLY on content it dislikes.** A rejected mutation is the good case — you find out immediately.

| Trap | Behaviour | Fix |
|---|---|---|
| **(a)** Text containing `<` | Sanitised to an **empty string**; write returns success | Strip angle brackets before writing, and before comparing on read |
| **(b)** `long_text` over ~2000 chars | Silently truncated, and the read-back shows the truncated value so it looks fine | Budget before writing — see §4.2 |
| **(c)** `board_relation` | Reads null for `text` and `value` even when correctly linked | Read `linked_item_ids` |
| **(d)** `email` and `phone` columns | **Reject** `change_simple_column_value` — it sends `text: null` and monday raises `ColumnValueException` | Use `change_multiple_column_values` with **both** fields: `{"email":{"email":"x@y.com","text":"x@y.com"}}` |
| **(e)** `status` labels | Cannot be created by `change_column_metadata` | Use `create_labels_if_missing: true` on a value write. Labels can be **created** this way but never deleted or renamed by API |

**(a), (b) and (c) all report success.** Those are the dangerous ones.

### 4.2 The long_text budget `[R-LONGTEXT v2]`

**A long_text column holds CURRENT STATE, never an unbounded log.**

1. **Budget before you write.** If the composed value would exceed **1,800 characters**, write a trimmed version ending `… full detail in updates` and post the remainder as an **item update** — updates have no cap.
2. **Compact, don't drop.** Keep every active flag and the verdict reasoning; move superseded entries to an item update, leaving a one-line pointer.
3. ⛔ **Never prepend to Leads `Screening Flags / Decline Reason` `long_text_mm64zg50`.** Append; and if you must cut, trim from the **middle** with an explicit `[…earlier detail in updates]` marker — never silently off either end.
4. **Verify by re-reading and comparing `len()` against the cap.** Checking only the final line is not a truncation check: a truncated append loses the END, a truncated prepend loses the BEGINNING. **Length is the only test that catches both.**

**A value of exactly 2000 characters is a truncation signature, not a coincidence.** Treat it as data loss.

**Which end you lose depends on how you write, and both ends matter.** A prepend drops the TAIL — which is where the original blocking flags and the decline reasoning live. The newest note survives and *why the lead was blocked* is what gets cut. That is exactly backwards.

**Watch bands, on all three long_text columns:**

| Band | Length | Action |
|---|---|---|
| **AT CAP** | = 2000 | Content already lost. Digest it |
| **CRITICAL** | ≥ 1900 | Compact in that run: snapshot the full text to an item update, then rewrite the column as active flags + verdict reasoning with a pointer |
| **WATCH** | ≥ 1750 | Monitor |

⚠ **Strips grow every run, so this worsens with time, not improves.**

---

## 5. Retired identifiers — recognise, never write

⚠ **Two kinds of entry live in this table.** Most are **superseded** — a live replacement exists and is named. **A retired COLUMN has no replacement**: the field itself is gone, and the rule that used to read it now works another way. Those rows say so explicitly.

| Retired | Replaced by | Board |
|---|---|---|
| `date_mm64jz0c` | ⛔ **NOTHING — the Client Required-By COLUMN IS RETIRED** (OR-24, 3 Sep 2026). The two-factor timeline rule reads **prose only**; see `07` §6 | Leads |
| `date_mm5ck0y1` | ⛔ **NOTHING — same retirement.** This identifier came from `Lead Risk Assessment Standard.md` C6; neither it nor `date_mm64jz0c` is to be relied on | Leads |
| `long_text_mm5ddgqa` | `long_text_mm64e8bs` — the `⚠ Risk Profile` column of record (OR-23, 3 Sep 2026). This id sits on the **retired** Leads board and must **never be written** | Leads (retired board `5029570430`) |
| `5029570430` | `5029570131` | Leads |
| `5029570431` | `5029570133` | Deals |
| `5029641469` | `5029570139` | Deals subitems |
| `5029570422` | `5029570130` | Contacts |
| `5029570423` | `5029570130` | Contacts (legacy IDs) |
| `email` (Accounts) | `email_mm64cpfk` | Accounts |
| `button_mm4x94bj` | `button_mm653bn9` | Deals |
| `group_mm4wdxht` | `group_mm64cyzj` | Deals |
| `text_mm4w4hxh` | `text_mm643406` | Deals — Quote # |
| `text_mm4wcmwt` | `text_mm64jj0j` | Deals — Revision |
| `color_mm4w2fb` | `color_mm64htd3` | Deals — Job Type |
| `text_mm4w6xr2` | `text_mm649q9d` | Deals — Suburb |
| `long_text_mm4wqyw0` | `long_text_mm6465nw` | Deals — Quote Notes |
| `long_text_mm4y7nhj` | `long_text_mm64a7d` | Deals — Quote Summary |
| `file_mm4wgbm1` | `file_mm64df53` | Deals — Quote PDF |
| `file_mm4zyrgx` | `file_mm64rcaj` | Deals — Superseded |
| `file_mm4zng0h` | `file_mm643zyy` | Deals — Client Drawings |
| `file_mm4yrww4` | `file_mm64g3zr` | Deals — Drawing |
| `text_mm4wtycc` | `text_mm658tz0` | Subitems — Material/Colour |
| `text_mm4wm1bg` | `text_mm65wgm9` | Subitems — Thickness |
| `text_mm4wvj1p` | `text_mm65dakh` | Subitems — Edge |
| `color_mm4wwb4f` | `color_mm65kbrk` | Subitems — Cut Out 1 |
| `color_mm4w53sx` | `color_mm65pzp3` | Subitems — Cut Out 2 |
| `text_mm4wv6qp` | `text_mm657f15` | Subitems — Cutout notes |
| `numeric_mm4wp1x` | `numeric_mm65bp9c` | Subitems — Price |
| `board_relation_mm4w7xr` | `board_relation_mm655691` | Subitems — Material linked |
| `status` | `color_mm6525jy` | Subitems — Line Type |

---

## 6. Maintaining this registry

**Cite fields by name elsewhere, and identifiers only here.** Every document in this set that needs an identifier should point at this table rather than pinning the string in its own prose. The 11 August migration cost thirteen days of a dead matching tier precisely because identifiers were scattered through rule bodies.

**A rule-version check will not catch an identifier fault.** Verify identifiers against the live boards separately, on a stated cadence.

⛔ **That verification has NOT succeeded.** The attempt made on 3 September 2026 could not reach a single board this document names — see the warning at the head of this file and `10-open-rulings.md` **OR-26**. **Until it succeeds, this registry is the best record held and the only record held, and it is unverified.** Re-run the check the moment the correct monday account is identified, and record the date and the result here.

---

## 7. Data coverage — how full the columns actually are

**Source: board exports supplied by the owner, 3 September 2026** — Materials Library 392 rows, Accounts 188 rows, Serviceable Areas 608 rows. Full working in `DATA-VERIFICATION-2026-09-03.md`.

⚠ **Coverage is not identity.** These exports settle *how populated* a column is. They do **not** settle a single column ID, and they cannot: an export carries names, not identifiers. **OR-26 is untouched by this.**

**Why this section exists.** Several rules in this set **fail closed on blank data** — `[R-PROFILE v5]`, `[R-SUBTYPE v2]`, `[R-D5 v8]`, `[R-LEADTIME v2]`, `[R-MA5 v3]`. A fail-closed rule is only as good as the column behind it: **a rule that is perfectly correct against an empty column sends every job to review, and looks like a broken screen.** Coverage therefore belongs in the registry, beside the identifier, and should be re-measured whenever the boards are re-exported.

### 7.1 Print Construction — populated in full, 7 September 2026

| Value | Rows |
|---|---|
| `Face-printed` | **5** |
| **blank** | **387** |
| `Full body` | **0** |

✅ **FULLY POPULATED, 7 September 2026 — 392 of 392, no blanks.** 228 `Full body` · 164 `Face-printed`. Populated by Stella Rasheed. **This closes OR-40**, which turned on the column being kept as a positive marker while `[R-PROFILE v5]` read blank as unknown: with no blanks the two readings cannot disagree. The fail-closed branch is unchanged and now guards a new material added without being marked. The seven Cosentino **Eclos** rows that briefly read `Porcelain / Full body` were a type error and were corrected to `Engineered Stone` the same day; no porcelain now reads `Full body`.

⛔ **As it stands, 387 of 392 materials send every pencil-profile job to Needs Review**, and the reason would not be the rule — it would be an empty column.

| Option | Effect |
|---|---|
| **Populate `Full body` on the other 387** | Blank becomes meaningful again, the rule works as designed, and a genuinely unknown material still fails closed. **Recommended** — a bulk edit that preserves the safety property |
| Amend `[R-PROFILE v5]` so blank means full body | One line, no data work — but it removes the fail-closed guard, and a new face-printed range added without marking would then be priced with a pencil. **That is QU-58883** |

**Until one is chosen:** flag it, but say why. The flag reads *"print construction not recorded"* — **never** *"may be face-printed"*. ⚠ **Do not amend the rule on the quiet.** `[R-PROFILE v5]` is a LAW and this is a Register change, not a board change.

### 7.2 Coverage table

| Board · Field | Populated | Consequence |
|---|---|---|
| Materials · Material Type | **392 / 392** | ✅ Clean. Three values, mapping exactly onto `[R-M1 v2]` |
| Materials · Stone Sub-Type | 3 / 392 | Expected. `[R-D5 v8]` fallback fires on 50 of 53 naturals — **working as designed, and expensive.** No field is coming; the split is a per-job human call |
| Materials · Print Construction | **392 / 392** | ✅ Complete, 7 Sep 2026. 228 `Full body` · 164 `Face-printed`. OR-40 closed |
| Materials · Print Construction | 5 / 392 | ⛔ §7.1 |
| Materials · Alias Names | **0 / 392** | Every misnamed material fails to match, silently `[R-MATERIAL-TERMS v1]` |
| Materials · Outdoor Suitability | 41 / 392 (one brand) | Supplementary only — `05` §1.1.1 |
| Accounts · Customer Tier | 60 / 188 | 128 accounts now take the **14–16 day** quoted date `[R-LEADTIME v2]` as well as no waiver |
| Accounts · Client Rating A/B/C | **0 / 188** | The composite has no data |
| Accounts · Rating — Payment | 109 / 188 | A-VIP 15 · A 16 · B 53 · C 25. **The A/B/C rating is payment-only in practice** |
| Accounts · Rating — Measure-ready | **0 / 188** | ⛔ OR-14's site-readiness ruling scores on an empty column |
| Accounts · Rating — Install-ready | **0 / 188** | ⛔ Same |
| Accounts · Main POC email | 112 / 188 | Consistent with the 42-blank note in §2.1. **16 of the 112 sit on a generic domain** and drop to ladder tier 4 `[R-ACCTMATCH v5]` |
| Accounts · Notes / Flags | — | ✅ **14 DUMP markers — exactly what `[R-ACCT v3]` records** |
| Serviceable Areas · Zone | **608 / 608** | ✅ Comprehensive — `07` §1 |

✅ **`farquhar.co` is the only non-generic domain shared by two accounts.** The knowledge base names it as the known collision; the export confirms there are no others.

### 7.3 What a screen must not conclude from this

⛔ **A blank column is not permission to assume.** Every figure above describes data that is *missing*, and `00`'s failure mode governs all of it: **when the data is missing, fail toward the flag, never toward the promise.** The correct response to a 99%-blank Print Construction column is a clearer flag, not a relaxed rule — and the correct response to an empty Measure-ready rating is to drop site-readiness out of the composite openly, not to score it as good.

---

## Open items

Questions this document deliberately does not settle are recorded in `10-open-rulings.md`. **Nothing there may be applied as a rule.** The 3 September 2026 ruling round closed the identifier disputes this document used to carry — **OR-23** (the `⚠ Risk Profile` column is `long_text_mm64e8bs`, §2.2), **OR-24** (the Client Required-By column is retired and both identifiers move to §5) and **OR-25** (the generic-domain closed list is eleven, §2.1) are **ruled**.

**One item remains, and it is the largest thing in this document:**

| Item | What is open | Where it touches this document |
|---|---|---|
| **OR-26** | ⚠⚠ **NO IDENTIFIER IN THIS DOCUMENT HAS BEEN VERIFIED AGAINST A LIVE BOARD.** As at 3 September 2026, six board IDs queried with `state: all` while authenticated as the account owner **all returned an empty array**, and there is **no "SteedForm CRM" workspace** in the account the connector reaches. **Whether the CRM boards live in a different monday account, or the IDs are dead, is NOT established** — and neither is ruled out. ⛔ **This does not make the identifiers wrong. It makes them unverified** | **§1 and §2 in full** — every board and column id, including the three ruled above. Also §5: a retired id cannot be confirmed retired either. Until a live read succeeds, treat an empty result on any board named here as a **finding**, never a clean result `[R-READ v1]` |

**Also unresolved and scoped elsewhere:** **OR-38** — whether the Screening Philosophy / distance-from-optimum lens is retired and all stone moves to one ladder, **held for scoping**. It names no identifier and does not touch this registry; nothing in it may be applied as a rule.

**Outstanding DATA actions — not open questions.** Each is a board value that has to change, or a column that has to be filled, for a ruled rule to work:

| # | Action | Board | Why |
|---|---|---|---|
| 1 | ✅ **DONE 7 Sep 2026 — Print Construction populated, 392 of 392.** Pencil jobs are answered from the board instead of going to review | Materials | Was the biggest single unblock; §7.1 |
| 2 | **Spot-check the known A-tier relationships against Customer Tier** | Accounts | ⚠ **Not "tag the 128".** A blank tier means **unverified**, and 14–16 days is the correct answer for an unverified account `[R-LEADTIME v2]` (owner, 3 Sep 2026). The only real exposure is a genuine A-tier customer sitting untagged. ⛔ **Never bulk-assign a tier to clear blanks** — that turns an honest *unverified* into a false *verified* |
| 3 | **Populate Rating — Measure-ready and Install-ready, or rule site-readiness out of the composite** | Accounts | OR-14's ruling currently scores on two empty columns §7.2 |
| 4 | **Extend the outdoor technical review beyond Lavistone** | Materials | Then `Outdoor Suitability` can become the authority instead of a class rule plus a brand list `05` §1.1.1 |
| 5 | **Populate `Alias Names`, at least for the brands customers misname** | Materials | Exact matching with no aliases fails silently `[R-MATERIAL-TERMS v1]` |
| 6 | **Set Material Type for the Vasari items to ceramic** | Materials | The class is ruled `[R-M1 v2]`; only the board value is outstanding §2.4 |

⚠ **A new open question came out of the exports, and it is recorded in `10-open-rulings.md`, not here:** the Serviceable Areas board carries a third zone value, **`Boundary — verify`**, that no registered rule handles — `07` §1.

---

*Related: `01-rule-register.md` §5 (the canonical read/write rules) · `04-customer-and-account.md` (what the Accounts fields mean) · `05-material-and-capability.md` §1.1.1 (why `Outdoor Suitability` stays supplementary) · `07-service-area-and-site.md` §1 (the Serviceable Areas board as exported) and §6 (the timeline rule that no longer reads a date column) · `10-open-rulings.md` **OR-26** (the unverified identifiers) · `DATA-VERIFICATION-2026-09-03.md` (the export working behind §7).*
