from scrymr.domain.models import Action
from scrymr.policy.engine import PolicyEngine


def test_default_deny() -> None:
    decision = PolicyEngine({"actions": {"allowed": []}}).evaluate(Action.ALERT)

    assert decision.allowed is False
    assert decision.requires_approval is False


def test_destructive_action_requires_approval() -> None:
    policy = {
        "actions": {
            "allowed": ["ban_member"],
            "approval_required": ["ban_member"],
        }
    }

    decision = PolicyEngine(policy).evaluate(Action.BAN_MEMBER)

    assert decision.allowed is True
    assert decision.requires_approval is True
