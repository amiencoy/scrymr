from __future__ import annotations

import os
import warnings
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _setting(name: str, default: str) -> str:
    if name in os.environ:
        return os.environ[name]
    legacy = name.replace("SCRYMR_", "SCREAMRRRR_", 1)
    if legacy in os.environ:
        warnings.warn(f"{legacy} is deprecated; use {name}", FutureWarning, stacklevel=2)
        return os.environ[legacy]
    return default


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
            log_level=_setting("SCRYMR_LOG_LEVEL", "INFO").upper(),
            policy_path=Path(_setting("SCRYMR_POLICY_PATH", "policies/default.yaml")),
            dry_run=_as_bool(_setting("SCRYMR_DRY_RUN", "true")),
        )
