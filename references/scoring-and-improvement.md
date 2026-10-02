# Scoring and improvement strategy

## Build the rubric matrix

Use one row per official criterion or hard gate:

`item_id | official wording | weight/gate | judge question | intended claim | evidence_id | artifact location | status | gap | owner`

Quote only the minimum exact wording needed to preserve meaning. If weights are absent, do not invent them; use `unweighted` and label prioritization as analytical.

## Assess coverage

Use evidence-aware states instead of a cosmetic numeric score:

- **Demonstrated:** direct, current, scoped evidence supports the claim.
- **Partially demonstrated:** evidence exists but is indirect, stale, narrow, or incomplete.
- **Asserted:** the team states the claim but inspectable proof is absent.
- **Planned:** future work or forecast, clearly labeled.
- **Not addressed:** no meaningful claim or evidence.
- **Not applicable:** justified against the official rule.

An internal score may help prioritize work, but it must be labeled unofficial and must not be converted into a winning probability.

## Prioritize improvements

Order work by:

1. eligibility and rejection risk;
2. high-weight criteria with weak evidence;
3. contradictions across artifacts;
4. judge-visible feasibility and differentiation gaps;
5. presentation and polish.

For each improvement record `expected rubric impact`, `evidence needed`, `effort`, `owner`, `deadline`, and `dependency`. Prefer a small number of defensible improvements over adding unsupported features or claims.

## Positioning test

A defensible positioning statement should answer:

- Who has the problem, and how is it currently measured?
- What is materially different about the solution?
- What has actually been built or validated?
- Why is the team credible to execute the next milestone?
- Which limitation remains, and how will it be tested?

If any answer relies on future work, label it as such and move it to the proof plan rather than describing it as a current advantage.
