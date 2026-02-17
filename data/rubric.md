# Support Triage Rubric v1.0

## 🔴 Priority 0 (Critical) - Label: `P0`
- **Definition:** Total system outage, data loss, or major security vulnerability.
- **Criteria:** The core application is unusable for all users.
- **Action:** Add `P0` label + Comment: "🚨 Critical issue detected. Internal alert triggered."

## 🟡 Priority 1 (High) - Label: `P1`
- **Definition:** Major feature is broken with no easy workaround.
- **Criteria:** Significant impact on a specific subset of users (e.g., "Login failing on Safari").
- **Action:** Add `P1` label.

## 🔵 Priority 2 (Medium) - Label: `P2`
- **Definition:** Minor bug or UI inconsistency with a clear workaround.
- **Criteria:** Doesn't block core workflows (e.g., "Typo in footer" or "Button color is wrong").
- **Action:** Add `P2` label.

## 🟢 Task / Feature - Label: `enhancement`
- **Definition:** Request for new functionality or non-bug improvements.
- **Action:** Add `enhancement` label.

## 🛠️ Universal Rule: Missing Info
- If an issue is a **Bug** but has no "Steps to Reproduce," do NOT assign a priority.
- **Action:** Add `needs-info` label + Comment: "Thanks for the report! Could you please provide steps to reproduce this?"