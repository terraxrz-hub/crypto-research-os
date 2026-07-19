# Security Policy

This repository contains no application code and has no runtime — the attack surface is limited to its GitHub Actions workflows and the secrets/tokens they use.

## Reporting a vulnerability or exposure

If you find:
- A leaked or overly-broad credential (e.g. `ADD_TO_PROJECT_PAT`, `ANTHROPIC_API_KEY`) referenced or exposed anywhere in this repository, its workflow logs, or its Issues,
- A workflow that could be manipulated by untrusted input (e.g. via a crafted issue body or PR title) into taking an unintended action, or
- Any other way the automation in `.github/workflows/` could be abused,

please **do not open a public Issue**. Instead, use GitHub's private vulnerability reporting: repository **Security** tab → **Report a vulnerability**. If that isn't available, contact the maintainer listed in `.github/CODEOWNERS` directly.

## Scope

In scope: this repository's workflows, Issue Forms, and repository configuration.

Out of scope: the third-party services referenced in the framework's evidence tables (Arkham, Glassnode, CertiK, etc.) — those are not part of this project and have their own security contacts.

## Response

This is a small, maintainer-operated repository without a formal SLA. Reports will be acknowledged as soon as reasonably possible and a fix or mitigation will be prioritized based on severity — a leaked write-scoped credential is treated as urgent; a hardening suggestion is not.
