import asyncio
import logging
import os
import signal
import sys

import disnake
import redis
import redis.asyncio
from disnake.ext import commands

from counting import constants
from counting.bot import Kazoeru
from counting.db import Base


log = logging.getLogger(__name__)


def load_extensions(bot: commands.AutoShardedInteractionBot):
    for file in os.listdir("kazoeru/cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"kazoeru.cogs.{file[:-3]}")
            log.info(f"Loaded extension kazoeru.cogs.{file[:-3]}")


async def console_listener(loop: asyncio.AbstractEventLoop, future: asyncio.Future):
    while True:
        try:
            line = await loop.run_in_executor(None, sys.stdin.readline)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received")

        if line.strip() in ("quit", "exit", "stop", "shutdown", "q"):
            future.cancel()
            break


async def main():
    disnake.VoiceClient.warn_nacl = False

    if constants.Redis.use_fakeredis:
        try:
            import fakeredis
            import fakeredis.aioredis
        except ImportError as e:
            raise RuntimeError("You need to install fakeredis to use fakeredis") from e
        redis_session = fakeredis.aioredis.FakeRedis.from_url(constants.Redis.uri)
    else:
        pool = redis.asyncio.BlockingConnectionPool.from_url(constants.Redis.uri, max_connections=20, timeout=300)
        redis_session = redis.asyncio.Redis(connection_pool=pool)

    command_sync_flags = commands.CommandSyncFlags(
        allow_command_deletion=False,
        sync_guild_commands=True,
        sync_global_commands=True,
        sync_commands_debug=True,
        sync_on_cog_actions=True,
    )

    intents = disnake.Intents.default()
    intents.messages = True
    intents.message_content = True

    bot = Kazoeru(redis_session=redis_session, intents=intents, command_sync_flags=command_sync_flags)

    load_extensions(bot)

    async with bot.db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    loop = asyncio.get_running_loop()

    future: asyncio.Future = asyncio.ensure_future(bot.start(constants.Client.token or ""), loop=loop)
    listener_future: asyncio.Future = asyncio.ensure_future(console_listener(loop, future))

    if sys.platform != "win32":
        loop.add_signal_handler(signal.SIGINT, lambda: future.cancel())
        loop.add_signal_handler(signal.SIGTERM, lambda: future.cancel())

    try:
        await future
        if constants.Client.debug:
            await listener_future
    except asyncio.CancelledError:
        log.info("Received signal to terminate bot and event loop")
    finally:
        if not bot.is_closed():
            await bot.close()


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)
