from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True, slots=True)
class Settings:
    discord_token: str
    log_level: str = "INFO"
    policy_path: Path = Path("policies/default.yaml")
    dry_run: bool = True

    @classmethod
    def from_env(cls) -> Settings:
        load_dotenv()
        token = os.getenv("DISCORD_TOKEN", "").strip()
        if not token:
            raise RuntimeError("DISCORD_TOKEN is required")
        return cls(
            discord_token=token,
            log_level=os.getenv("SCREAMRRRR_LOG_LEVEL", "INFO").upper(),
            policy_path=Path(os.getenv("SCREAMRRRR_POLICY_PATH", "policies/default.yaml")),
            dry_run=_as_bool(os.getenv("SCREAMRRRR_DRY_RUN", "true")),
        )
