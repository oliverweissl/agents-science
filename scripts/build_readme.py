"""Regenerate the project table in README.md from projects.json."""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
projects = json.loads((root / "projects.json").read_text())

labels = {"agent-tokens": "agent tokens", "cpu": "CPU", "gpu": "GPU"}
rows = ["| Project | Problem | Needs | Operator | Verified by |", "|---|---|---|---|---|"]
for p in projects:
    needs = ", ".join(labels[r] for r in p["resources"])
    rows.append(
        f"| [{p['name']}]({p['join']}) | {p['problem']} | {needs} | {p['operator']} | {p['verification']} |"
    )

start, end = "<!-- projects:start -->", "<!-- projects:end -->"
readme = root / "README.md"
text = readme.read_text()
head, rest = text.split(start)
_, tail = rest.split(end)
readme.write_text(head + start + "\n" + "\n".join(rows) + "\n" + end + tail)
