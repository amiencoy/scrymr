from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from screamrrrr.domain.models import Action, PolicyDecision


class PolicyEngine:
    def __init__(self, policy: dict[str, Any]) -> None:
        self._policy = policy

    @classmethod
    def from_yaml(cls, path: Path) -> PolicyEngine:
        with path.open(encoding="utf-8") as stream:
            policy = yaml.safe_load(stream) or {}
        return cls(policy)

    def evaluate(self, action: Action) -> PolicyDecision:
        actions = self._policy.get("actions", {})
        allowed = set(actions.get("allowed", []))
        forbidden = set(actions.get("forbidden", []))
        approval_required = set(actions.get("approval_required", []))

        if action.value in forbidden:
            return PolicyDecision(False, False, "Action is explicitly forbidden by policy.")
        if action.value not in allowed:
            return PolicyDecision(False, False, "Action is denied by default.")
        if action.value in approval_required:
            return PolicyDecision(True, True, "Moderator approval is required.")
        return PolicyDecision(True, False, "Action is allowed by policy.")
