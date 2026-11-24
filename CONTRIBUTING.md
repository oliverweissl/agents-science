# Suggest or add a project

Two ways to add a project. Both are welcome.

## 1. Suggest it (no code)

Open an issue with the **Suggest a project** template. Fill in the form; a maintainer adds it.

## 2. Add it yourself (pull request)

1. Fork this repository.
2. Add one entry to `projects.json`, copying the template below.
3. Run `python3 scripts/build_readme.py` to refresh the README table.
4. Open a pull request and complete the checklist in the PR template.

### Entry template

```json
{
  "name": "Project name",
  "problem": "One line: what research problem it works on",
  "operator": "community",
  "resources": ["agent-tokens"],
  "verification": "How results are checked (Lean kernel, CI, verifier, peer review)",
  "url": "https://github.com/org/repo",
  "join": "https://link-to-the-join-or-start-instructions",
  "status": "active"
}
```

### Field values

| Field | Allowed values |
|---|---|
| `operator` | `community`, `company`, `academic` |
| `resources` | `agent-tokens`, `cpu`, `gpu` (list every kind the project needs) |
| `status` | `active`, `early` (small or young project) |

### Inclusion rules

- The project must accept contributions from outside agents, with public instructions.
- `join` must point to instructions an agent or its owner can follow today.
- `verification` must say how results are checked. "None" is acceptable, but state it.
- Do not claim a result is correct. This list does not validate scientific claims.
- One project per pull request, no promotional wording.
- Projects you could not inspect yourself do not belong here. Say so in the PR instead.
