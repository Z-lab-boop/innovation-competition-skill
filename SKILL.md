---
name: innovation-competition
description: Prepare, revise, or audit evidence-grounded materials for Chinese university innovation and entrepreneurship competitions such as 大创, 挑战杯, 中国国际大学生创新大赛, and 创青春. Use for competition strategy, eligibility and rubric checks, business plans, pitch decks, financial forecasts, evidence packs, posters, roadshows, defense Q&A, or final submission review.
---

# Innovation and Entrepreneurship Competitions

## Core principle

Build every claim and deliverable from the same verified evidence base and the current official rules. A persuasive story may organize evidence; it must never replace it.

## Select an operating mode

Choose the smallest mode that satisfies the request. Combine modes only when the user asks for an end-to-end package.

| Mode | Use when | Primary outcome |
|---|---|---|
| Intake | Materials or competition context are incomplete | Context record, evidence inventory, blocker list |
| Audit | Existing plan, deck, spreadsheet, poster, or evidence needs review | Severity-ranked findings and correction plan |
| Strategy | Track selection, positioning, rubric coverage, or priority is unclear | Verified rubric map and improvement backlog |
| Build | The user wants one or more deliverables created or revised | Editable artifacts tied to the same brief and ledger |
| Defense | Roadshow, demo, script, or Q&A needs preparation | Timed narrative, red-team questions, answer evidence |
| Final QC | Submission is near | Gate report, rendered-file checks, frozen package |

Read [references/operating-modes.md](references/operating-modes.md) when choosing or combining modes.

## Required workflow

1. **Inspect before asking.** Review the provided files and existing project records first. Ask only for missing information that blocks the selected mode.
2. **Lock the competition context.** Record official name, year, organizer, track/category, stage, institution, deadline, eligibility, file limits, templates, rubric, and required deliverables.
3. **Verify current rules.** Prefer current official organizer sources. Record URL or file, title, issuer, publication date, access date, and the exact requirement supported. Read [references/competition-routing.md](references/competition-routing.md). If a rule cannot be verified, mark dependent guidance `provisional`; never import prior-year requirements as current facts.
4. **Inventory claims and evidence.** Classify each material claim as verified, user-asserted, planned/forecast, or missing. Record scope, date, permission, and where the claim is reused. Read [references/evidence-and-claims.md](references/evidence-and-claims.md).
5. **Maintain one competition brief.** Treat the brief, claim ledger, and rubric matrix as the shared source of truth for the plan, deck, finance model, poster, demo, and defense answers.
6. **Map the rubric.** Link every official scoring item or hard gate to a claim, evidence ID, deliverable location, owner, and gap. For strategy or audit work, read [references/scoring-and-improvement.md](references/scoring-and-improvement.md).
7. **Build or revise only requested artifacts.** Follow the official template first, then use [references/deliverables.md](references/deliverables.md) and the routing table below.
8. **Stress-test the defense.** When a roadshow, demo, or Q&A is in scope, read [references/defense-red-team.md](references/defense-red-team.md). Answers must point back to evidence or explicitly acknowledge uncertainty.
9. **Validate and freeze.** Run cross-file, render, permission, naming, and submission checks from [references/judging-and-qc.md](references/judging-and-qc.md). Freeze a submission candidate only after hard gates pass.

## Stage gates

Do not present downstream polish as proof that an upstream gate passed.

| Gate | Pass condition | If not passed |
|---|---|---|
| G0 Rules | Current eligibility, track, deadline, template, and limits verified | Stop finalization; mark provisional |
| G1 Evidence | Material claims have states, sources, dates, and permissions | Remove, qualify, or request proof |
| G2 Coherence | Brief, rubric map, narrative, finance, and milestones agree | Select authoritative values and propagate fixes |
| G3 Artifacts | Editable sources and exported files open and render correctly | Repair and re-render |
| G4 Defense | Timing, demo fallback, role split, and high-risk Q&A tested | Rehearse and close exposed gaps |
| G5 Submission | Naming, size, anonymity, signatures, permissions, and upload package pass | Report `Blocked`, not `Ready` |

## Optional project workspace

For a multi-deliverable project, initialize a traceable workspace instead of maintaining disconnected notes:

```bash
python3 scripts/init_competition_workspace.py <target-directory>
```

The script copies editable context, brief, claim-ledger, rubric, deliverable-register, defense, and submission-gate templates. It refuses to overwrite existing files. Read [references/workspace-and-versioning.md](references/workspace-and-versioning.md) when several artifacts or collaborators are involved.

## Deliverable routing

Use only skills available in the current runtime, and load one only when its deliverable is in scope.

| Need | Preferred skill |
|---|---|
| Editable PPTX | `presentations:Presentations` or `pptx` |
| Image-led slide deck | `baoyu-slide-deck` |
| Business plan or application DOCX | `documents:documents` |
| Financial model and charts | `spreadsheets:Spreadsheets` plus `startup-metrics-framework` |
| Market and competitor analysis | `competitive-landscape` plus `marketing-plan` |
| MVP and validation experiments | `lean-startup` |
| Poster, infographic, or architecture diagram | `canvas-design`, `baoyu-infographic`, or `baoyu-diagram` |
| Research evidence or prior art | `nature-academic-search` or `patent` |
| Academic or conference figure | `nature-figure`, `scientific-schematics`, or `scientific-visualization` |

## Output contract

Lead with the decision-relevant state, not generic praise:

1. **Submission status:** `Ready`, `Conditionally ready`, or `Blocked`, plus the verified competition context.
2. **Evidence status:** verified claims, attributed user claims, forecasts, missing proof, and permission risks.
3. **Rubric coverage:** strengths, high-weight gaps, hard gates, and the next best improvement per unit effort.
4. **Deliverables:** completed or proposed files, validation performed, and source-of-truth records used.
5. **Next actions:** action, owner, needed evidence, deadline, and consequence if unresolved.

For early-stage work, also deliver useful provisional output that is safe to produce; do not turn every missing field into a questionnaire.

## Non-negotiable boundaries

- Never fabricate or inflate patents, software copyrights, papers, awards, users, contracts, partners, orders, revenue, test results, market data, or team credentials.
- An application is not a grant; an intent letter is not a sale; a pilot is not scaled adoption; a prototype is not a validated product.
- Label forecasts and market estimates with assumptions, scenario, source, and date.
- Treat personal data, partner authorization, intellectual-property permissions, signatures, and organizer templates as hard gates.
- “冲刺”, “竞争力强”, or “容易获奖” are positioning judgments, never award guarantees.
- Never convert an internal score, AI review, or visual polish into an official result or predicted award.
- Preserve originals, editable sources, evidence IDs, and a frozen submission manifest so all deliverables remain auditable.
