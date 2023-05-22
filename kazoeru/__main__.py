import logging
import os

import disnake
import redis
import sqlalchemy
from disnake.ext import commands

from kazoeru import config

log = logging.getLogger(__name__)
_intents = disnake.Intents.default()
_intents.messages = True
_intents.message_content = True


def load_extensions(bot: commands.AutoShardedInteractionBot):
    for file in os.listdir("kazoeru/cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"kazoeru.cogs.{file[:-3]}")
            log.info(f"Loaded extension kazoeru.cogs.{file[:-3]}")


def main():
    disnake.VoiceClient.warn_nacl = False

    engine = sqlalchemy.create_engine(
        "sqlite:///kazoeru/data/kazoeru.sqlite",
    )

    r = redis.Redis(
        host=os.environ.get("REDIS_HOST"),
        port=os.environ.get("REDIS_PORT"),
        db=os.environ.get("REDIS_DB"),
    )

    command_sync_flags = commands.CommandSyncFlags(
        allow_command_deletion=False,
        sync_guild_commands=True,
        sync_global_commands=True,
        sync_commands_debug=True,
        sync_on_cog_actions=True,
    )

    bot = commands.AutoShardedInteractionBot(
        intents=_intents, command_sync_flags=command_sync_flags
    )

    bot.redis = r
    bot.engine = engine

    @bot.event
    async def on_ready():
        load_extensions(bot)
        log.info(f"Logged in as {bot.user} ({bot.user.id})")
        log.info(f"Connected to {len(bot.guilds)} guilds")

    @bot.event
    async def on_guild_join(guild: disnake.Guild):
        log.info(f"Joined guild {guild.name} [{guild.id}]")
        log.info(f"Connected to {len(bot.guilds)} guilds")

    bot.run(os.environ.get("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
