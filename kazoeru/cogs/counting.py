import disnake
from disnake.ext import commands

from kazoeru.bot import Kazoeru
from kazoeru.constants import Emojis
from kazoeru.db.guild import Guild
from kazoeru.embed import Embed


class Counting(commands.Cog):
    def __init__(self, bot: Kazoeru):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: disnake.Message):
        if msg.author.bot:
            return

        async with self.bot.db.begin() as session:
            guildData = await session.get(Guild, msg.guild.id)
            if guildData is None:
                return

        if msg.channel.id != guildData.channel:
            return

        num = int(await self.bot.redis.get(f"{msg.guild.id}:count") or 0)
        description = f"Wrong number, the next number was {num + 1}."

        if guildData.numonly:
            if not msg.content.isdigit():
                return

        if msg.content.isdigit():
            if msg.author.id == int(await self.bot.redis.get(f"{msg.guild.id}:last") or 0):
                description = "You can't count twice in a row!"
            elif int(msg.content) == num + 1:
                await self.bot.redis.incr(f"{msg.guild.id}:count")
                await self.bot.redis.set(f"{msg.guild.id}:last", msg.author.id)
                return await msg.add_reaction(Emojis.success)

        await self.bot.redis.set(f"{msg.guild.id}:count", 0)
        await self.bot.redis.set(f"{msg.guild.id}:last", 0)
        await msg.add_reaction(Emojis.error)
        embed = Embed.error(guild=msg.guild, title=f"Ruined it at {num}! {description}")
        return await msg.reply(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, msg: disnake.Message):
        if msg.author.bot:
            return

        async with self.bot.db.begin() as session:
            guildData = await session.get(Guild, msg.guild.id)
            if guildData is None:
                return

        if msg.channel.id != guildData.channel:
            return

        if not msg.content.isdigit():
            return

        num = int(await self.bot.redis.get(f"{msg.guild.id}:count") or 0)

        if int(msg.content) == num:
            async for message in msg.channel.history(limit=100):
                if message.content.isdigit():
                    await self.bot.redis.set(f"{msg.guild.id}:count", int(message.content))
                    await self.bot.redis.set(f"{msg.guild.id}:last", message.author.id)
                    return


def setup(bot: Kazoeru):
    bot.add_cog(Counting(bot))
