import disnake
from disnake.ext import commands
from sqlalchemy.orm import Session

from kazoeru.constants import Emojis
from kazoeru.db.guild import Guild
from kazoeru.embed import Embed


class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: disnake.Message):
        if msg.author.bot:
            return

        with Session(self.bot.engine) as session:
            guild = session.query(Guild).filter_by(id=msg.guild.id).first()
            if guild is None:
                return

        print(guild.channel, msg.channel.id)

        if msg.channel.id == guild.channel:
            num = int(self.bot.redis.get(f"{msg.guild.id}:count") or 0)
            description = f"Wrong number, the next number was {num + 1}."

            print(guild.numonly)

            if guild.numonly:
                if not msg.content.isdigit():
                    return

            if msg.content.isdigit():
                if msg.author.id == int(self.bot.redis.get(f"{msg.guild.id}:last") or 0):
                    description = "You can't count twice in a row!"
                elif int(msg.content) == num + 1:
                    self.bot.redis.incr(f"{msg.guild.id}:count")
                    self.bot.redis.set(f"{msg.guild.id}:last", msg.author.id)
                    return await msg.add_reaction(Emojis.success)

            self.bot.redis.set(f"{msg.guild.id}:count", 0)
            self.bot.redis.set(f"{msg.guild.id}:last", 0)
            await msg.add_reaction(Emojis.error)
            embed = Embed.error(
                guild=msg.guild,
                title=f"Ruined it at {num}! {description}",
                footer=False,
            )
            return await msg.reply(embed=embed)


def setup(bot):
    bot.add_cog(Counting(bot))
