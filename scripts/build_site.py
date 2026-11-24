"""Prerender the project cards and JSON-LD into index.html so crawlers see them without JavaScript.

Run after editing projects.json or stats.json:  python3 scripts/build_site.py
The page's JavaScript re-renders the same markup for filtering and sorting.
"""
import html
import json
import pathlib
import re

SITE = "https://oliverweissl.github.io/agents-science/"
root = pathlib.Path(__file__).resolve().parent.parent
projects = json.loads((root / "projects.json").read_text())
stats_file = root / "stats.json"
stats = json.loads(stats_file.read_text()) if stats_file.exists() else {}

RES = {"agent-tokens": "Agent tokens", "cpu": "CPU", "gpu": "GPU"}
FIELD = {"math": "Math", "biomedical": "Biomedical", "ml": "ML", "general": "General science"}
OP = {"community": "Community", "company": "Company", "academic": "Academic"}
ORDER = ["active", "early", "dormant", "finished"]
e = html.escape


def card(p):
    inactive = " inactive" if p["status"] in ("dormant", "finished") else ""
    s = stats.get(p["url"])
    star = f'<span class="stat">★ {s["stars"]}</span>' if s else ""
    tags = "".join(f'<span class="tag res">{RES[r]}</span>' for r in p["resources"])
    tags += f'<span class="tag">{FIELD[p["field"]]}</span><span class="tag">{OP[p["operator"]]}</span>'
    if p["status"] != "active":
        tags += f'<span class="tag{"" if p["status"] == "early" else " state"}">{p["status"]}</span>'
    return (
        f'<a class="card{inactive}" href="{e(p["join"])}" target="_blank" rel="noopener">'
        f'<div class="card-head"><h2>{e(p["name"])}</h2><div class="meta">{star}<span class="go">join →</span></div></div>'
        f'<p>{e(p["problem"])}</p><div class="tags">{tags}</div>'
        f'<p class="how">verified by: {e(p["verification"])}</p></a>'
    )


ordered = sorted(projects, key=lambda p: ORDER.index(p["status"]))
cards = "\n".join(card(p) for p in ordered)

ld = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "name": "Agents for Science", "url": SITE,
         "description": "Open research projects you can contribute AI agents and compute to."},
        {"@type": "ItemList", "name": "Open science projects that accept contributions from AI agents",
         "numberOfItems": len(projects),
         "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": p["name"], "url": p["join"], "description": p["problem"]}
             for i, p in enumerate(ordered)]},
    ],
}
ld_tag = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def swap(text, name, body):
    pat = re.compile(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"marker {name} missing in index.html")
    return pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), text)


idx = root / "index.html"
t = idx.read_text()
t = swap(t, "cards", cards)
t = swap(t, "ld", ld_tag)
t = re.sub(r'(<p id="count">)[^<]*(</p>)', rf"\g<1>{len(projects)} of {len(projects)} projects\g<2>", t)
idx.write_text(t)

(root / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{SITE}</loc></url>\n</urlset>\n"
)
(root / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
print(f"{len(projects)} cards prerendered")
