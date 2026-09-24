# SCRYMR

Formerly **SCREAMRRRR**.

SCRYMR is an open-source, Discord-native community security and incident-response sentinel.

It observes Discord events, normalizes them, evaluates rules and heuristics, assigns risk, proposes a response, checks that response against policy, and records the result. High-impact moderation actions require human approval by default.

> [!IMPORTANT]
> This repository is an early foundation. The default configuration runs in dry-run mode and does not automatically punish members.

## Initial scope

- Spam and flood detection
- Suspicious-link and phishing signals
- Raid and coordinated-abuse signals
- Toxicity and impersonation signals
- Permission and webhook abuse monitoring
- Consistent, auditable moderator response
- Cross-server threat intelligence as a later, privacy-aware capability

## Architecture

```text
Discord event -> Normalizer -> Detectors -> Risk score -> Proposed action
                                                       -> Policy engine
                                                       -> Approval or execution
                                                       -> Audit log
```

The Discord adapter stays thin. Detection, policy, action, and audit components are kept independent so they can be tested and evolved separately.

## Quick start

Requirements: Python 3.11+ and a Discord application with a bot token.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Set `DISCORD_TOKEN` in `.env`, enable the required intents in the Discord Developer Portal, then run:

```bash
python -m screamrrrr
```

The Python module remains `screamrrrr` for compatibility; the project and repository are now named SCRYMR.

Run checks:

```bash
ruff check .
pytest
```

## Safety defaults

- Dry-run is enabled.
- The bot ignores other bots.
- Destructive actions are denied unless explicitly declared in policy.
- Timeout, kick, and ban require moderator approval.
- Every proposal should produce an audit record.

See [Architecture](docs/architecture.md), [Contributing](CONTRIBUTING.md), and [Security Policy](SECURITY.md).

## Project status

SCRYMR is pre-alpha. Interfaces, policy schema, and detectors may change before the first tagged release.

## License

A project license has not been selected yet. Until a license is added, copyright law applies and no permission to copy, modify, or distribute the code is granted.
