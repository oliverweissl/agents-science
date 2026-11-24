"""Fetch stars and creation date for every GitHub project in projects.json into stats.json."""
import json
import os
import pathlib
import re
import urllib.request

root = pathlib.Path(__file__).resolve().parent.parent
projects = json.loads((root / "projects.json").read_text())
out_path = root / "stats.json"
old = json.loads(out_path.read_text()) if out_path.exists() else {}

headers = {"Accept": "application/vnd.github+json", "User-Agent": "agents-science-stats"}
if os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]

stats = {}
for p in projects:
    m = re.match(r"https://github\.com/([^/]+/[^/#?]+)/?$", p["url"])
    if not m:
        continue
    repo = m.group(1)
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers)
        d = json.load(urllib.request.urlopen(req, timeout=20))
        stats[p["url"]] = {"stars": d["stargazers_count"], "created": d["created_at"][:10]}
    except Exception as e:  # keep the previous value so one failed call does not wipe data
        print(f"WARN {repo}: {e}")
        if p["url"] in old:
            stats[p["url"]] = old[p["url"]]

out_path.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n")
print(f"{len(stats)} repos")
