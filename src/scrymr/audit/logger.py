from __future__ import annotations

import json
import logging
from dataclasses import asdict

from scrymr.actions.executor import ExecutionResult
from scrymr.domain.models import Finding, NormalizedEvent, PolicyDecision


def log_decision(
    logger: logging.Logger,
    event: NormalizedEvent,
    finding: Finding,
    decision: PolicyDecision,
    result: ExecutionResult,
) -> None:
    record = {
        "event": asdict(event),
        "finding": asdict(finding),
        "policy_decision": asdict(decision),
        "execution": asdict(result),
    }
    logger.info("sentinel_decision %s", json.dumps(record, default=str, sort_keys=True))
