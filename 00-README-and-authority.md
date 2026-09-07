# 00 — How to Use This Knowledge Base

**Status:** Active.
**Owner:** MD
**Last updated:** 3 September 2026
**Scope:**
- **Owns:** what this set is, which file wins when two disagree, how to read a rule ID, and how to change something.
- **Does not own:** any rule. Nothing in this file is operational.

---

## What this is

Eleven documents that carry everything needed to screen a SteedForm quote or job, and nothing else. It replaces a twenty-document knowledge base in which the same rule appeared in up to seventeen files, restated eighty-nine times, drifting a little each time.

It is built on one principle, which the previous knowledge base arrived at the hard way:

> **A fact lives in exactly one place. Everywhere else cites it.**

---

## The documents

| # | Document | What it carries |
|---|---|---|
| **00** | How to Use This Knowledge Base | This file |
| **01** | **Rule Register** | **The canonical statement of every operational rule. The only file in which a rule is authored.** |
| **02** | Verdicts and Precedence | The four verdicts, the order rules are applied in, the blocking list |
| **03** | Risk Scoring | The six-dimension strip and every ladder that scores it |
| **04** | Customer and Account | Tier, rating, account matching, client fit, minimum job |
| **05** | Material and Capability | What we can and cannot make |
| **06** | Evidence Requirements | What must be known before a verdict is possible |
| **07** | Service Area and Site | Geography, access, logistics, timeline |
| **08** | Board and Column Registry | Every monday identifier, and the read/write traps |
| **09** | Response Templates | What we say once a verdict is reached |
| **10** | **Open Rulings** | **Questions that are NOT settled. Nothing here may be applied as a rule.** |

---

## Authority — which file wins

**1. `01-rule-register.md` wins over everything.** Where the Register and any other file disagree — this knowledge base, the Deep Screen app, a monday column description, a memory file, or anything else — **the Register is correct and the other file is stale.**

**2. Documents `02`–`09` explain and expand. They never author.** Each may carry reference data, tables and procedure that the Register deliberately excludes. Where they touch a rule they must cite its ID and may never contradict its canonical statement.

**3. `10-open-rulings.md` is quarantine.** It records what is *not* settled, so the screen never treats an undecided question as decided. **Nothing in it may be applied as a rule.**

**4. Live board data outranks any document** `[R-REF v2]`. Material class, print construction, appliance QC status, customer tier and service-area zone are all read from the board on every screen — never from memory, an earlier pass, a historical note, a pasted snapshot, or a value copied onto the lead. **A document tells you which field to read; the board tells you what it says.**

⛔ **"From the board" means the RECORD, not a column list.** A rule naming columns states the minimum, never the maximum. **If a field on the record would change a human's decision and no rule names it, that is a gap in the rule, not permission to ignore the field.**

---

## Reading a rule

Rules look like this: `R-D5 · v6 · LAW`.

- **`R-D5`** — the permanent ID. IDs are never reused and never renumbered. A superseded rule keeps its ID and points at what replaced it.
- **`v8`** — the version. Any document or executable restating the rule must carry the tag inline as `[R-D5 v9]`. That is how drift is caught: a carrier holding `v6` when the Register says `v8` is stale by definition.
- **`LAW`** — the class.

Each rule also carries a **`Why`** — the incident that produced it. Those are not decoration. Nearly every rule in the Register exists because something specific went wrong, and the Why is what stops a future reader "simplifying" a rule back into the defect it was written to prevent.

⚠ **A tag check is not an identifier check.** On 24 August 2026 a perfectly tagged, perfectly versioned rule addressed a monday column that did not exist, a drift check reported it clean, and an account-matching tier was silently dead for thirteen days. Board and column identifiers must be verified separately, against `08`.

---

## Two things that are easy to get wrong

**Needs Info and Needs Review are not variants of each other.** Missing drawings route to **Needs Info** — the client must supply something. A blocking flag routes to **Needs Review** — a human at SteedForm must decide. They go to different people. Collapsing them sends the wrong request to the wrong party.

**Capability is not risk** `[R-ANDON v2]`. **⛔ capability** means *we cannot make this* — a hard stop no human call can authorise. **🔴 risk** means *this is far from our optimum* — a human call, where taking the job at the right price and declining it are both valid answers. Blend them and either someone promises a job that physically cannot be made, or screening starts declining work SteedForm actively sells.

---

## The failure mode

**If the Rule Register cannot be read: KEEP CAPTURING, REFUSE TO JUDGE.**

Continue intake so no enquiry is lost. Do not issue verdicts, do not write risk strips, and say so plainly. **Never fall back to an inline copy of a rule** — "probably right" is exactly what produced the 25 July 2026 faceting mis-sell.

The same discipline applies whenever evidence is thin: **when the data is missing, fail toward the flag, never toward the promise.**

---

## Changing something

1. **Write it in `01-rule-register.md` first** — a new rule with a new ID, or a version bump on an existing one, with a dated `History` line and who decided it.
2. **Then propagate** to every document named in that rule's `Carried by` line.
3. **Then re-screen** any open lead the change affects `[R-RESCREEN v1]`. A rule can be corrected everywhere and still leave every previously screened lead carrying the old verdict — on 25 July 2026 a threshold changed and 84 strips were stale, found only because a person went looking.

**A rule written anywhere else first is an orphan.** That is not a style preference: the Register was created on 27 July 2026 after an audit found that every serious defect of the preceding week shared one cause — a rule decided in one place that never reached the file which executes it.

---

## What is deliberately not here

This knowledge base carries screening data only. The following were archived alongside it rather than carried into it, because a screen does not read them: install execution and rigging procedure, site-measure procedure, takeoff and nesting rules, pricing mechanics and rate cards, CRM pipeline operations, email intake, the automation inventory, brand and positioning material, the bulk of the supplier-manual reference in Technical Standards, and the historical decision log. Where one of those documents held something a screen *does* need, that content was migrated first — the five-item customer information requirements out of `Sales Qualification.md` into `06`, the vehicle and crane envelope out of `Technical Standards.md` into `07`, the markup tiers out of `Pricing Rules.md` into `04`.

`CHANGES.md`, beside this folder, lists every document archived and why, and every conflict that was resolved and on what evidence.

**Thirty-six of the thirty-seven open questions were ruled on 3 September 2026** — nine new rules and eleven version bumps, recorded in `RULINGS-2026-09-03.md`. Five of the new rules register conditions the screen had been applying for months with nothing written down behind them. ⚠ **Every open lead screened before that date is stale by definition** `[R-RESCREEN v1]`.

**Board exports supplied the same afternoon raised three more** — OR-39, OR-40 and OR-41 in `10-open-rulings.md`. They are a different kind of question from the rest: not *what is the rule*, but *is there data behind the rule*. **Two of them stop a correct rule from working.** The coverage record is `08-board-and-column-registry.md` §7, and the working is `DATA-VERIFICATION-2026-09-03.md`.

Fourteen registered rules also sit outside screening scope — email intake, CRM pipeline operations and build governance. They are real and live, and they are listed by ID in `01` §7 so their IDs can never be reissued. Their full text is in the archived original Rule Register.

---

*Start with `01-rule-register.md`. Everything else cites it.*
