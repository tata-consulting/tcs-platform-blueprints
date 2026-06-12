# Initial considerations for coding agents

This document captures initial guardrails for using coding agents in this repository, including GitHub Copilot and Gemini.

## 1. Scope and usage model

- Define where agents are allowed to assist (documentation only, scaffolding, or production code changes).
- Require a human reviewer for all agent-authored pull requests.
- Keep accountability clear: the code owner remains responsible for final outcomes.

## 2. Security and data handling

- Do not paste secrets, customer data, or internal credentials into prompts.
- Prefer least-privilege access for repository and CI tokens used by agent workflows.
- Run secret scanning and security checks on all agent-generated changes before merge.

## 3. Quality and validation

- Require the same test, lint, and build gates for agent-authored changes as for human-authored changes.
- Ask agents for small, focused changes to simplify review and rollback.
- Track recurring failure patterns and update prompts/checklists accordingly.

## 4. Copilot-specific considerations

- Standardize repository instructions so Copilot follows project conventions consistently.
- Use Copilot for implementation acceleration, but keep architectural decisions with maintainers.
- Validate generated dependency updates and API usage before accepting suggestions.

## 5. Gemini-specific considerations

- Use Gemini primarily for design exploration, trade-off analysis, and drafting implementation options.
- Verify generated code and commands against repository standards before committing.
- Keep prompts explicit about constraints (security, compatibility, and non-functional requirements).

## 6. Governance and continuous improvement

- Define measurable outcomes (lead time, review effort, defect rates) for agent adoption.
- Introduce an escalation path for unsafe or low-confidence outputs.
- Revisit these considerations regularly as policies, models, and tooling evolve.
