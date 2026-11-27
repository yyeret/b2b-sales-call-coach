---
name: sales-playbook-configurator
description: Configure, bootstrap, and recursively calibrate a B2B sales methodology and call-inspection scorecard (Sandler, Force Management, MEDDIC/MEDDPICC, Value-Based Selling, Challenger, Gap Selling, Science of Sales / Roberge, Blair Enns Four Conversations, Jonathan Stark Why Conversation). Use when choosing a sales methodology, extracting an initial ICP/playbook from early call recordings, generating a sales-playbook-config.yaml for sales-call-analyzer, or calibrating a playbook against call adherence and conversion outcomes.
metadata:
  origin: original
  brand: utility
  publish: shareable
  tags: outreach-sales, sales-enablement
  version: 1.1.0
---

# Sales Playbook Configurator

## Outcome

Build and continuously calibrate an opinionated, methodology-grounded `sales-playbook-config.yaml` so your sales force meets the right people, runs the right conversations, and moves as quickly as makes sense toward the right outcome (qualify out fast, advance, or close).

## Outcome Indicators

- Recommends **one** clear primary methodology (or a deliberate 2-part hybrid + Roberge coaching overlay) — never a vague "use everything" list.
- Outputs a complete, copy-pasteable `sales-playbook-config.yaml` with positioning adherence criteria, 5–7 weighted scoring criteria, explicit deal-quality signals, stage gates, and disqualifiers.
- Supports bootstrapping an ICP & discovery guide from raw early recordings, and recursively calibrating the playbook from Adherence × Outcome batches.

## Three Operating Modes

Choose the mode that matches what the user brings:

1. **Mode A — Interactive Configuration (Default):** User wants to choose a methodology and build a `sales-playbook-config.yaml` from scratch.
2. **Mode B — Bootstrap ICP & Playbook from Raw Transcripts:** User has 3–10 raw founder/early-rep discovery or "Mom Test" call transcripts (optionally with win/retention/bad-fit labels) and wants to extract their ICP, positioning criteria, and first playbook.
3. **Mode C — Recursive Playbook Calibration (Adherence × Outcome 2×2):** User has a batch of analyzed calls with **Positioning Adherence %** and **Actual Outcomes** (e.g., converted vs. stalled) and wants to improve the playbook, MQL/SQL definitions, or rep coaching focus.

---

## Mode A: Interactive Configuration

If not already provided, ask these 5 questions in one concise batch (if partial context is given, state assumptions and generate immediately):

1. **What do you sell, and what is your typical ACV / deal size?**
2. **Who is on the buying committee, and how long is the sales cycle?**
3. **What is the primary motion?** (Inbound, outbound, partner-led, founder-led, enterprise)
4. **What is your #1 sales bottleneck right now?** (e.g., pitching too early, happy ears / stalled Stage 1, losing to status quo, late-stage procurement surprises, inconsistent rep execution)
5. **What is your core positioning/story that every rep must land, and do you have any existing methodology or CRM stages?**

### Workflow
1. Read `references/methodologies-reference.md`.
2. Select 1 primary methodology (or a tight 2-part hybrid) + **Science of Sales (Roberge)** coaching overlay. Explain why it fits their bottleneck better than the alternatives.
3. Generate `sales-playbook-config.yaml` using the schema below.

---

## Mode B: Bootstrap ICP & Playbook from Raw Transcripts

Use when a team is early-stage or lacks a formal playbook:
1. Inspect the supplied transcripts (3–10 calls, ideally tagged `retained / won` vs. `churned / bad-fit / stalled`).
2. Extract **unstructured-data patterns**:
   - **Best-Fit ICP Signals:** Language, urgency triggers, buyer seniority, and problems that correlate with wins/retention.
   - **Bad-Fit / Disqualifier Signals:** Red flags that correlate with churn or endless stalls.
   - **Winning Discovery Questions & Positioning:** Moments where buyers leaned in or shared sensitive context.
3. Pair those findings with the best-fit methodology from `references/methodologies-reference.md` to output:
   - A concise **ICP & MQL/SQL Definition Draft**
   - A **First Discovery Guide** (5–7 high-leverage questions + Blair Enns conversation boundaries)
   - A ready-to-use **`sales-playbook-config.yaml`**

---

## Mode C: Recursive Playbook Calibration (Adherence × Outcome 2×2)

Use when inspecting multiple scored calls paired with conversion outcomes (e.g., Stage 1 → Stage 2, or Won vs. Stalled):

1. Bucket each call into the **Adherence × Outcome 2×2**:
   - **Low Adherence (<50%) + High Conversion:** *Field Breakthrough* — inspect what the rep said/did in the field that outperformed the official script.
   - **Low Adherence (<50%) + Stalled:** *Rep Coaching Gap* — rep skipped core discovery/positioning; prescribe specific coaching.
   - **High Adherence (≥70%) + Stalled:** *Playbook / ICP / Qualification Bug* — the rep followed the script and it still didn't convert; diagnose whether the messaging, MQL/SQL bar, or qualification gate is wrong.
   - **High Adherence (≥70%) + High Conversion:** *Gold Standard* — extract verbatim clips for rep onboarding/training.
2. Output concrete **System Upgrades**:
   - Proposed patch to `sales-playbook-config.yaml` (positioning criteria, script/structure, or disqualifiers)
   - Updated **MQL / SQL** gate recommendations
   - Top 1–2 **team-wide training** priorities

---

## Output Schema: `sales-playbook-config.yaml`

```yaml
playbook_name: "<Team / Motion Name>"
version: "1.0"

deal_profile:
  acv_range: "<e.g. $25K-$75K>"
  sales_cycle: "<e.g. 45-90 days>"
  buying_committee: "<e.g. 2-4 stakeholders>"
  primary_motion: "<inbound | outbound | hybrid | enterprise>"

methodology:
  primary: "<Sandler | Force Management | MEDDPICC | Value-Based Selling | Challenger | Gap Selling | Blair Enns Four Conversations>"
  secondary_overlay: "<optional second lens, e.g. Stark Why Conversation>"
  coaching_framework: "Science of Sales (Roberge)"

positioning_criteria: # Scored 0-100% adherence separately from general discovery skill
  core_narrative: "<1-2 sentence positioning/value thesis the rep must land>"
  required_beats:
    - "<Beat 1: e.g. Name the expensive status-quo trap>"
    - "<Beat 2: e.g. Connect to measurable business outcome>"
    - "<Beat 3: e.g. Differentiate without feature-dumping>"

lead_definitions:
  mql_criteria: "<Who should be allowed to book / enter pipeline>"
  sql_criteria: "<What must be verified on Call 1 to count as a real qualified opportunity>"

call_stages:
  - name: "Probabilistic / Discovery"
    conversation_type: "Blair Enns: Probabilistic -> Qualifying"
    goal: "<What must be true to advance or disqualify fast>"
    target_talk_listen_ratio: "35-45% rep / 55-65% buyer"
  - name: "Value / Solution Alignment"
    conversation_type: "Blair Enns: Value Conversation"
    goal: "<Align on quantified value & options before any formal proposal>"
    target_talk_listen_ratio: "45-55% rep / 45-55% buyer"

deal_quality_signals: # Inspected from transcripts, independent of CRM stage
  - "Buyer seniority (director/VP/C-level vs. non-decider)"
  - "Multi-threading (2+ buyer roles engaged)"
  - "Sensitive info shared (budget, internal metrics, org politics, hard deadlines)"
  - "Champion tested (agreed to take an internal action)"

scoring_rubric: # 5-7 criteria, weights sum to 100
  - id: "posture_and_control"
    label: "Peer/Advisor Posture & Conversation Discipline"
    weight: 20
    what_good_looks_like: "<Equal stature, Up-Front Contract, no premature pitching>"
    anti_pattern: "<Vendor chasing, feature-dumping, or unpaid consulting>"
  - id: "pain_and_why"
    label: "Pain Funnel & Stark Why Conversation"
    weight: 25
    what_good_looks_like: "<Uncovers Why this, Why now, Why us, Why not do nothing>"
    anti_pattern: "<Accepting surface symptoms or polite interest>"
  - id: "qualification_and_deal_quality"
    label: "Qualification Rigor & Deal-Quality Signals"
    weight: 25
    what_good_looks_like: "<Verified authority, decision process, metrics, sensitive info>"
    anti_pattern: "<Assuming a friendly contact is a Champion or EB>"
  - id: "value_and_positioning"
    label: "Positioning & Co-Created Value"
    weight: 15
    what_good_looks_like: "<Lands core narrative tailored to buyer's KPIs>"
    anti_pattern: "<Generic pitch deck or early discounting>"
  - id: "next_step_or_disqualify"
    label: "Fast, Clean Outcome (Advance or Disqualify)"
    weight: 15
    what_good_looks_like: "<Booked next step with decision owner OR clean disqualification>"
    anti_pattern: "<'Send me info' or vague 'let's reconnect next month'>"

qualification_gates:
  advance_requires:
    - "<Verified pain + urgency (Why now)>"
    - "<Clear path to Economic Buyer / Decision Process>"
  disqualify_triggers:
    - "<No urgent project / pure curiosity with no timeline>"
    - "<Refusal to share impact or grant access to decision-making>"

coaching_cadence:
  focus_rule: "Pick 1 high-leverage behavior per rep per week (Roberge)."
  evidence_rule: "Separate verbatim buyer quotes from rep inference."
```

## Quality Gates

- Never recommend all methodologies at once — pick the tightest 1–2 + Roberge overlay.
- Weights in `scoring_rubric` MUST sum to 100.
- Every criterion MUST include concrete `what_good_looks_like` and `anti_pattern` behaviors.
- Keep 100% portable for any B2B sales team (no company-specific internal jargon).
