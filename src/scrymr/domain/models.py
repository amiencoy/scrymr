from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any


class Action(StrEnum):
    OBSERVE = "observe"
    ALERT = "alert"
    DELETE_MESSAGE = "delete_message"
    TIMEOUT_MEMBER = "timeout_member"
    KICK_MEMBER = "kick_member"
    BAN_MEMBER = "ban_member"


@dataclass(frozen=True, slots=True)
class NormalizedEvent:
    event_id: str
    event_type: str
    guild_id: int
    actor_id: int
    channel_id: int | None = None
    content: str = ""
    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class Finding:
    detector: str
    rule_id: str
    score: int
    reason: str
    proposed_action: Action = Action.ALERT


@dataclass(frozen=True, slots=True)
class PolicyDecision:
    allowed: bool
    requires_approval: bool
    reason: str
