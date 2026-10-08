"""Say which open jobs now carry an answer from older rules.

Reporting only. It is read by a person on the Actions summary and must never be
the reason a load looks failed — every path here exits 0.

⛔ Reads the response from a FILE. It must not be passed as an argument or an
environment variable: both go through execve, which caps a single string at
128 KB on Linux, and this response passed 143 KB in October 2026.
"""

import json
import pathlib

OUT = []


def say(line: str = "") -> None:
    OUT.append(line)


def main() -> int:
    say("## Criteria loaded\n")
    path = pathlib.Path("stale.json")
    if not path.exists() or path.stat().st_size == 0:
        say("_The rules loaded. The staleness check could not be reached — that is this step "
            "only, and says nothing about the load._")
        return 0

    raw = path.read_text(encoding="utf-8", errors="replace").strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        say("_The rules loaded. The staleness check did not return JSON — that is this step "
            "only. What came back starts:_\n")
        say("```")
        say(raw[:400])
        say("```")
        return 0

    rows = data.get("stale") or []
    say(f"Fingerprint `{str(data.get('fingerprint', ''))[:16]}…`\n")
    if not rows:
        say("Nothing open was screened against older rules.")
        return 0

    # A rule can be corrected everywhere and still leave every job already
    # screened carrying the old answer. [R-RESCREEN v1]
    say(f"**{len(rows)} open job(s) now screened against older rules — re-run them.**\n")
    for row in rows[:50]:
        say(f"- {row.get('client_name') or row.get('reference')}")
    if len(rows) > 50:
        say(f"- …and {len(rows) - 50} more")
    return 0


code = main()
print("\n".join(OUT))
raise SystemExit(code)
