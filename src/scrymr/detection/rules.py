from __future__ import annotations

import re

from scrymr.domain.models import Action, Finding, NormalizedEvent

URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)
SUSPICIOUS_TERMS = ("free nitro", "steam gift", "claim reward", "verify wallet")


def inspect_message(event: NormalizedEvent) -> list[Finding]:
    """Return explainable starter findings for a normalized message event."""
    if event.event_type != "message_create":
        return []

    content = event.content.casefold()
    findings: list[Finding] = []

    if URL_PATTERN.search(content) and any(term in content for term in SUSPICIOUS_TERMS):
        findings.append(
            Finding(
                detector="message_rules",
                rule_id="suspicious-link-lure",
                score=70,
                reason="Message combines a link with a common social-engineering lure.",
                proposed_action=Action.ALERT,
            )
        )

    if len(content) >= 20 and len(set(content)) <= 3:
        findings.append(
            Finding(
                detector="message_rules",
                rule_id="repetitive-flood-content",
                score=35,
                reason="Message content is unusually repetitive.",
                proposed_action=Action.OBSERVE,
            )
        )

    return findings
