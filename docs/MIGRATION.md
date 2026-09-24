# Migrating to SCRYMR

The distribution, import package, and console command are now `scrymr`.
Reinstall from this checkout in a fresh virtual environment with `pip install -e ".[dev]"`.
Update service commands to `python -m scrymr` (or `scrymr`) and update integrations to import `scrymr`.

Rename configuration keys:

| Previous key | Current key |
| --- | --- |
| `SCREAMRRRR_LOG_LEVEL` | `SCRYMR_LOG_LEVEL` |
| `SCREAMRRRR_POLICY_PATH` | `SCRYMR_POLICY_PATH` |
| `SCREAMRRRR_DRY_RUN` | `SCRYMR_DRY_RUN` |

Old environment keys remain a deprecated fallback so existing policy paths and dry-run settings are not silently lost. Current keys take precedence, including explicit false values. `DISCORD_TOKEN` is unchanged. Module imports and service commands must be migrated before restarting.

---

<p align="center"><sub>Built with code, coffee, and a healthy dislike of repetitive work.</sub></p>
