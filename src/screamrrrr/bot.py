from __future__ import annotations

import logging

import discord

from screamrrrr.actions.executor import execute
from screamrrrr.audit.logger import log_decision
from screamrrrr.config import Settings
from screamrrrr.detection.rules import inspect_message
from screamrrrr.domain.models import NormalizedEvent
from screamrrrr.policy.engine import PolicyEngine

LOGGER = logging.getLogger("screamrrrr")


class SentinelClient(discord.Client):
    def __init__(self, *, settings: Settings) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.messages = True
        super().__init__(intents=intents)
        self.settings = settings
        self.policy = PolicyEngine.from_yaml(settings.policy_path)

    async def on_ready(self) -> None:
        LOGGER.info("SCREAMRRRR connected as %s", self.user)

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot or message.guild is None:
            return

        event = NormalizedEvent(
            event_id=str(message.id),
            event_type="message_create",
            guild_id=message.guild.id,
            actor_id=message.author.id,
            channel_id=message.channel.id,
            content=message.content,
        )
        for finding in inspect_message(event):
            decision = self.policy.evaluate(finding.proposed_action)
            result = execute(finding.proposed_action, decision, dry_run=self.settings.dry_run)
            log_decision(LOGGER, event, finding, decision, result)


def run() -> None:
    settings = Settings.from_env()
    logging.basicConfig(
        level=getattr(logging, settings.log_level, logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    SentinelClient(settings=settings).run(settings.discord_token, log_handler=None)
