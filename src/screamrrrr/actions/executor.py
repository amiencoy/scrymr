from __future__ import annotations

from dataclasses import dataclass

from screamrrrr.domain.models import Action, PolicyDecision


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    status: str
    detail: str


def execute(action: Action, decision: PolicyDecision, *, dry_run: bool) -> ExecutionResult:
    """Apply safety gates. Discord mutations will be added behind this boundary."""
    if not decision.allowed:
        return ExecutionResult("denied", decision.reason)
    if decision.requires_approval:
        return ExecutionResult("pending_approval", decision.reason)
    if dry_run:
        return ExecutionResult("dry_run", f"Would execute {action.value}.")
    if action in {Action.OBSERVE, Action.ALERT}:
        return ExecutionResult("executed", f"Executed {action.value}.")
    return ExecutionResult("not_implemented", "Discord mutation is not implemented yet.")
