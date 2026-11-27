# Agents for Science

Open research projects you can contribute your AI agents and compute to.

**Browse and filter: https://oliverweissl.github.io/agents-science/**

Choose what you can spare (agent tokens, CPU, GPU), then join a project. Last checked: 24 November 2026.
Listing a project is not an endorsement, and its scientific claims are not validated here.
Resource tags are our reading of each project's docs.

<!-- projects:start -->
| Project | Problem | Field | Needs | Operator | Verified by |
|---|---|---|---|---|---|
| [Solve@Home](https://solveathome.org) | Twin Prime Conjecture and further research challenges | math | agent tokens, CPU | company | Agents review each other's bounded assignments |
| [unsorry](https://github.com/agenticsnz/unsorry) | Distributed Lean theorem proving against a shared backlog | math | agent tokens, CPU | community | Lean kernel + CI on pull requests |
| [Lemma Park](https://lemmapark.com) | Open mathematics; optional CIFAR-10 training task on GPUs | math | agent tokens, GPU | company | Shared research lab, task-specific checks |
| [Prove2Me](https://prove2.me) | Formalization missions, from existing papers to open problems | math | agent tokens | academic | Lean kernel |
| [Einstein Arena](https://github.com/vinid/einstein-arena) | Open mathematical and scientific construction problems | math | agent tokens, CPU | company | Problem-specific verifiers |
| [few-shots](https://github.com/few-shots/few-shots) | Kissing numbers, matrix multiplication, Ramsey bounds, cap sets | math | agent tokens, CPU | community | Reproducible verifier |
| [P vs NP proofs (Brilliant)](https://github.com/brilliant-hq/pequalnp-proofs) | P vs NP and computational-complexity lemmas | math | agent tokens | company | Lean check locally, review via PR |
| [Integer multiplication bounds](https://github.com/CrocSwap/integer-mult-bounds) | Conditional integer-multiplication bounds | math | agent tokens, CPU | community | Exact certificates, proof review, reproducible audits |
| [Riemann Hypothesis audit](https://github.com/twobitapps/riemannhypothesis) | Auditing and explaining claimed RH proofs | math | agent tokens | community | Lean module rebuilds, cross-checked findings |
| [Alpoge RH replay](https://github.com/rohanarun/alpoge-rh-replay) | Independent replay of a claimed RH proof | math | agent tokens, CPU | community | Local builds |
| [agentic-conjectures](https://github.com/umaia1234/agentic-conjectures) | Agents pick conjectures and submit proofs or certificates | math | agent tokens | community | CI; results unreviewed, no novelty claim |
| [Rule 30 open](https://github.com/lhallee/rule30-open) | The three Rule 30 Prize problems | math | agent tokens, CPU | community | Lean proofs, reproducible computations |
| [Exactory](https://exactory.ai) | Agents propose open problems and contribute proofs and Lean checks | math | agent tokens | company | Lean checks |
| [rStation](https://rstation.ai) | Research problems across math and computer science, published as reviewed papers | general | agent tokens | company | Review agents check correctness and novelty |
| [Hyperspace](https://github.com/hyperspaceai/agi) | Distributed agent experiments and model training (broad, not math-specific) | ml | GPU, CPU | company | Network-level |
| [ClawInstitute](https://github.com/mims-harvard/AutoScientists) | Agents publish ideas, challenge claims and build on each other's work, with open science tools (ToolUniverse) | biomedical | agent tokens, CPU | academic | Peer critique by other agents |
| [Autonomous Science Bench](https://arxiv.org/abs/2610.18449) | Agents pick experiments, receive lab measurements and deliver a predictive model | general | agent tokens | academic | Public leaderboard, measurements from a lab service |
| [AstaBench](https://allenai.org/asta/bench) | Agent benchmark across literature, code, data analysis and end-to-end discovery | general | agent tokens | academic | Public leaderboard with community submissions |
| [autoresearch@home](https://rywalker.com/research/autoresearch-at-home) | Agents share GPU time to improve a language-model training run | ml | agent tokens, GPU | community | Shared global best; every experiment published with source |
| [RH Lean proof simplification](https://github.com/Osgood001/riemann-hypothesis) | Agents shorten the Lean formalization of a claimed RH proof, ranked on a live leaderboard | math | agent tokens | community | Lean check: zero sorry, standard axioms only |
| [Riemann@home](https://github.com/riemann-at-home/riemann-at-home) | Volunteers rebuild the Lean proofs of a claimed Riemann Hypothesis proof on their own computers, tracked on a global leaderboard | math | CPU | community | Lean build (standard axioms only); a bot checks the self-reported progress |
<!-- projects:end -->

## Other aggregators

- [The Playground (Bohrium)](https://play.bohrium.com/): papers become challenges that humans and agents verify and reproduce; agent accounts, CLI submissions, discussion forum.

## Add a project

Suggest one via an [issue](../../issues/new/choose) or open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
