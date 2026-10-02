# Workspace and versioning

## Source-of-truth records

Keep these records together for a multi-deliverable project:

- competition context and official source register;
- competition brief;
- claim-to-evidence ledger;
- rubric matrix;
- deliverable register;
- defense question bank;
- submission gate checklist.

Initialize them with `scripts/init_competition_workspace.py` when useful. Adapt fields to the verified organizer template; do not replace an official form with the local template.

## Deliverable register

For each artifact record:

`artifact_id | path | purpose | source records | owner | status | last updated | validation | stale dependencies`

If an authoritative number or claim changes, search every registered artifact using it and mark each dependent file stale until regenerated or checked.

## Candidate freeze

Before final QC:

1. copy or export the exact files intended for submission into a candidate directory;
2. add a manifest containing relative path, size, modification time, and SHA-256;
3. validate those exact files, not earlier working copies;
4. record rule sources and access dates;
5. do not silently edit the candidate after validation.

If any file changes, create a new candidate or update the manifest and rerun affected checks. Keep editable sources separate from the frozen upload package.
