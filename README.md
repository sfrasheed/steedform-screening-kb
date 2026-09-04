# SteedForm screening criteria

The rules Deep Screen reads every job against. Eleven documents, and nothing
else.

**`01-rule-register.md` wins over everything.** Where it and any other file
disagree — including this repository, the app, a monday column description or
anyone's memory — the Register is correct and the other file is stale.

## Changing a rule

1. Write it in `01-rule-register.md` first: a new id, or a version bump on an
   existing one, with a dated `History` line and who decided it.
2. Propagate to every document named in that rule's `Carried by` line.
3. Commit, push, and load into the app.
4. **Re-screen any open job the change affects.** The app's Knowledge base page
   lists jobs screened against older rules — a rule can be corrected everywhere
   and still leave every previously screened job carrying the old answer.

A rule written anywhere else first is an orphan.

## Loading a change into the app

From the app's directory:

    npm run kb:load -- /Users/stellarasheed/steedform-screening-kb \
      --actor you@steedform.com \
      --base https://sfscreeningapp.srasheed.workers.dev

Replacing a file supersedes the old version rather than overwriting it, so a
screen that has already run still resolves to the exact words it read.

Or use **Choose files** on the app's Knowledge base page — same result.

## What does not belong here

Anything customer-specific that a rule needs at screening time: tier, client
fit, account match, rating, appliance QC, service-area zone. Those are read
from the monday board on every screen `[R-REF v2]`.

Where these documents name a real account, it is a worked example illustrating
a rule — frozen on the day it was written, and never the value for a live job.
