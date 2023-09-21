import logging

import disnake
from disnake.ext import commands

from kazoeru import constants
from kazoeru.bot import Kazoeru
from kazoeru.embed import Embed


log = logging.getLogger(__name__)


class Default(commands.Cog):
    def __init__(self, bot: Kazoeru):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f"Logged in as {self.bot.user} [{self.bot.user.id}]")
        log.info(f"Connected to {len(self.bot.guilds)} guilds")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log.info(f"Joined guild {guild.name} [{guild.id}]")

        channel = self.bot.get_channel(constants.Channels.log)
        embed = Embed.info(
            guild,
            title="Joined Guild",
        )
        embed.add_field(name="Name", value=f"> `{guild.name}`", inline=False)
        embed.add_field(name="ID", value=f"> `{guild.id}`", inline=False)
        embed.add_field(name="Members", value=f"> `{guild.member_count}`", inline=False)

        await channel.send(embed=embed)

    @commands.slash_command(description="Information about the bot.")
    async def info(self, inter: disnake.ApplicationCommandInteraction) -> None:
        embed = Embed.info(
            inter.guild,
            title="Info | Kazoeru",
        )
        embed.add_field(name="Uptime", value=f"> {self.bot.uptime}", inline=False)
        embed.add_field(name="Guilds", value=f"> {len(self.bot.guilds)}", inline=False)

        await inter.response.send_message(embed=embed)


def setup(bot: Kazoeru):
    bot.add_cog(Default(bot))
