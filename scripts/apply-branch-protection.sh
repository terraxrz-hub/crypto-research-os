#!/usr/bin/env bash
# Applies the recommended branch protection for `main`, reproducibly.
# Requires: gh CLI (https://cli.github.com/), authenticated with repo admin
# access (`gh auth login` first).
#
# Usage: ./scripts/apply-branch-protection.sh [owner/repo]
# If no owner/repo is given, uses the current directory's git remote.

set -euo pipefail

REPO="${1:-$(gh repo view --json nameWithOwner -q .nameWithOwner)}"

echo "Applying branch protection to ${REPO}:main ..."

gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "repos/${REPO}/branches/main/protection" \
  -f "required_status_checks[strict]=true" \
  -f "required_status_checks[contexts][]=yaml-syntax" \
  -f "required_status_checks[contexts][]=doc-links" \
  -f "enforce_admins=true" \
  -f "required_pull_request_reviews[required_approving_review_count]=1" \
  -f "required_pull_request_reviews[dismiss_stale_reviews]=true" \
  -f "restrictions=null" \
  -f "required_conversation_resolution=true" \
  -f "allow_force_pushes=false" \
  -f "allow_deletions=false"

echo "Done. Direct pushes to main are now blocked; PRs require the Validate workflow to pass and one approval."
