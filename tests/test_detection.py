from scrymr.detection.rules import inspect_message
from scrymr.domain.models import NormalizedEvent


def test_suspicious_link_lure_is_flagged() -> None:
    event = NormalizedEvent(
        event_id="1",
        event_type="message_create",
        guild_id=1,
        actor_id=2,
        content="Claim reward now at https://example.invalid",
    )

    findings = inspect_message(event)

    assert [finding.rule_id for finding in findings] == ["suspicious-link-lure"]


def test_non_message_event_is_ignored() -> None:
    event = NormalizedEvent(event_id="1", event_type="member_join", guild_id=1, actor_id=2)

    assert inspect_message(event) == []
