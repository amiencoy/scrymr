# Architecture

SCRYMR is designed as a Discord-native, event-driven sentinel. The Discord client is an adapter rather than the application core.

## Processing path

1. The Discord adapter receives an event.
2. The normalizer converts it into a platform-neutral domain event.
3. Rules, heuristics, and later ML detectors emit explainable findings.
4. A risk layer combines findings and proposes a response.
5. The policy engine allows, denies, or requires approval for the proposal.
6. The executor performs only policy-approved actions.
7. The audit layer records the event, finding, decision, and result.

## Boundaries

| Component | Owns | Must not own |
| --- | --- | --- |
| Discord adapter | Discord events and API objects | Detection or authorization policy |
| Detector | Evidence and explainable findings | Direct moderator actions |
| Risk layer | Scoring and response proposals | Discord API calls |
| Policy engine | Authorization and approval gates | Threat detection |
| Executor | Approved side effects | Deciding its own permissions |
| Audit layer | Decision records | Moderation decisions |

## MVP milestones

1. Read-only message signals and structured audit logs.
2. Moderator alerts and approval workflow.
3. Rate-aware spam, raid, and suspicious-link detectors.
4. Permission and webhook change monitoring.
5. Incident cases, evidence retention controls, and moderator dashboard.
6. Optional privacy-aware cross-server intelligence.

## Non-goals for the first release

- Autonomous mass moderation
- Unreviewed cross-server bans
- Permanent storage of raw message content
- A general-purpose conversational assistant
- Replacing Discord's permission model

## Future storage

The starter has no database. When persistence is introduced, separate operational state from privacy-sensitive evidence, define retention per tier, and avoid storing raw message content unless a server explicitly opts in.

---

<p align="center"><sub>Built with code, coffee, and a healthy dislike of repetitive work.</sub></p>
