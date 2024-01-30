import arrow
import redis
import redis.asyncio
from disnake.ext import commands
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from counting import constants


__all__ = ("Kazoeru",)


class Kazoeru(commands.AutoShardedInteractionBot):
    """
    Base Bot instance.
    """

    name = constants.Client.name

    def __init__(self, redis_session: redis.asyncio.Redis, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.redis_session = redis_session

        self.db_engine = engine = create_async_engine(constants.Database.postgres_bind)
        self.db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

        self.start_time: arrow.Arrow

    @property
    def db(self) -> async_sessionmaker[AsyncSession]:
        """Alias for `db_session`."""
        return self.db_session

    @property
    def redis(self) -> redis.asyncio.Redis:
        """Alias for `redis_session`."""
        return self.redis_session

    @property
    def uptime(self) -> str:
        """Get the bot's uptime."""
        return self.start_time.humanize(only_distance=True)

    async def login(self, token: str) -> None:
        """Login to Discord and set the bot's start time."""
        self.start_time = arrow.utcnow()
        return await super().login(token)

    async def close(self) -> None:
        """Close the bot and close the database connection pool."""
        await super().close()

        if self.db_engine:
            await self.db_engine.dispose()

        if self.redis_session:
            await self.redis_session.close(close_connection_pool=True)
