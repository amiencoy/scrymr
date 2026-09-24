from unittest.mock import patch

import pytest

from scrymr.config import Settings


def test_new_environment_keys_override_legacy_values(monkeypatch):
    monkeypatch.setenv("DISCORD_TOKEN", "test-token")
    monkeypatch.setenv("SCREAMRRRR_DRY_RUN", "true")
    monkeypatch.setenv("SCRYMR_DRY_RUN", "false")
    monkeypatch.setenv("SCRYMR_POLICY_PATH", "policies/custom.yaml")
    with patch("scrymr.config.load_dotenv"):
        settings = Settings.from_env()
    assert settings.dry_run is False
    assert str(settings.policy_path) == "policies/custom.yaml"


def test_legacy_policy_configuration_is_not_silently_lost(monkeypatch):
    monkeypatch.setenv("DISCORD_TOKEN", "test-token")
    monkeypatch.delenv("SCRYMR_POLICY_PATH", raising=False)
    monkeypatch.delenv("SCRYMR_DRY_RUN", raising=False)
    monkeypatch.setenv("SCREAMRRRR_POLICY_PATH", "policies/existing.yaml")
    monkeypatch.setenv("SCREAMRRRR_DRY_RUN", "false")
    with patch("scrymr.config.load_dotenv"), pytest.warns(FutureWarning):
        settings = Settings.from_env()
    assert str(settings.policy_path) == "policies/existing.yaml"
    assert settings.dry_run is False
