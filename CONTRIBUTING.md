# Contributing

SCREAMRRRR is in pre-alpha. Small, reviewable changes with tests are preferred.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest
```

## Pull requests

- Open an issue before large architectural changes.
- Keep Discord-specific objects at the adapter boundary.
- Do not bypass the policy engine for moderator actions.
- Add tests for detection and policy behavior.
- Never commit tokens, member data, or real incident evidence.
- Document new data collection and retention behavior.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
