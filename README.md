# B2B Sales Call Coach & Inspection System

A portable, methodology-grounded pair of AI skills that turns raw sales/discovery transcripts into a **system of inspection** — not generic meeting summaries.

Designed for B2B sales leaders, RevOps, and sales reps who want their team to:
- **Meet the right people** (tighten MQL/SQL definitions from real call evidence)
- **Have the right conversations** (Peer/Advisor posture, no premature pitching, deep discovery)
- **Move quickly to the right outcome** (qualify out bad fits fast, advance real deals, or close)
- **Compound the revenue machine** after every meeting (pre-call context, prep, rep coaching, script/deck tweaks, and recursive playbook calibration)

---

## Install

### Claude Code / Cowork / Claude Desktop

```text
/plugin marketplace add yyeret/b2b-sales-call-coach
/plugin install b2b-sales-call-coach@yeret-sales-tools
```

Installed skills are available as `/b2b-sales-call-coach:sales-playbook-configurator` and `/b2b-sales-call-coach:sales-call-analyzer`.

### ChatGPT / Codex

From a local checkout, Codex picks up `.agents/plugins/marketplace.json` automatically (run `codex /plugins` to browse/enable), or copy `skills/*` into `$CODEX_HOME/skills` or `$HOME/.agents/skills`.

### ChatGPT Projects / Claude Projects (No CLI)

Create a Project and upload these three files as Project Knowledge:
- `skills/sales-playbook-configurator/SKILL.md`
- `skills/sales-playbook-configurator/references/methodologies-reference.md`
- `skills/sales-call-analyzer/SKILL.md`

### Plain Clone

```bash
git clone https://github.com/yyeret/b2b-sales-call-coach.git
```

---

## What's Inside

1. **[`sales-playbook-configurator`](skills/sales-playbook-configurator/SKILL.md)** — Choose, bootstrap, and calibrate your team's methodology:
   - **Mode A (Interactive Config):** Pick 1–2 vetted methodologies (**Sandler**, **Force Management**, **MEDDIC/MEDDPICC**, **Value-Based Selling**, **Challenger**, **Gap Selling**, **Blair Enns' Four Conversations**, **Jonathan Stark's Why Conversation**) + **Science of Sales (Mark Roberge)** coaching overlay → outputs a tailored `sales-playbook-config.yaml`.
   - **Mode B (Bootstrap from Raw Transcripts):** Feed 3–10 early discovery or customer-interview calls + win/retention outcomes to extract your ICP signals, first discovery guide, and `sales-playbook-config.yaml`.
   - **Mode C (Recursive Calibration — Adherence × Outcome 2×2):** Compare Positioning Adherence % against conversion outcomes to separate *rep coaching gaps* (low adherence + stalled) from *field breakthroughs* (low adherence + won → upgrade the playbook) and *broken scripts* (high adherence + stalled).

2. **[`sales-call-analyzer`](skills/sales-call-analyzer/SKILL.md)** — Inspect any call transcript against your playbook:
   - **How the Rep Showed Up:** Peer/Trusted Advisor vs. Vendor/Feature-Dumper, Blair Enns conversation discipline, Stark Why Conversation, talk/listen & question depth, buyer autonomy vs. pressure, friction/anti-patterns.
   - **Positioning Adherence (0–100%)** + **Methodology Scorecard (Evidence vs. Inference)** with verbatim quotes.
   - **Deal-Quality Signals Beyond CRM Stages:** Buyer seniority, multi-threading, sensitive info shared, champion tested, and stakeholder read (Champion / Hedger / Resister / Economic Buyer).
   - **Compounding the Revenue Machine:** Pre-call context, prep, #1 coaching habit + up to 3 transcript rewrites, script/deck tweaks, and MQL/SQL definition feedback.

3. **[`methodologies-reference.md`](skills/sales-playbook-configurator/references/methodologies-reference.md)** — Side-by-side comparison and scoring mechanics for all supported frameworks.

4. **[`examples/sample-playbook-config.yaml`](examples/sample-playbook-config.yaml)** — Ready-to-adapt mid-market B2B configuration.

---

## Quickstart (3 Steps)

1. **Configure your playbook:** Run `sales-playbook-configurator` (answer 5 short questions, or paste 3–10 raw transcripts to bootstrap from reality) and save `sales-playbook-config.yaml`.
2. **Analyze calls:** Run `sales-call-analyzer` with your `sales-playbook-config.yaml` + any call transcript (Zoom, Gong, Fathom, Granola, Teams).
3. **Calibrate recursively:** Periodically feed 5–10 scored calls with their actual outcomes back into `sales-playbook-configurator` (Mode C) to update your positioning, MQL/SQL gates, and coaching focus from what actually converts in the field.

---

## License & Trademark Attribution

- **License:** MIT — see [LICENSE](LICENSE). All skill instructions, rubrics, and configuration schemas in this repository are original works.
- **Trademarks:** Referenced commercial methodologies and trademarks (including Sandler®, Force Management® / Command of the Message®, MEDDIC / MEDDPICC, Challenger™, Gap Selling, and Win Without Pitching®) belong to their respective owners. This repository is an independent operational implementation and is not affiliated with, sponsored by, or endorsed by those organizations.
