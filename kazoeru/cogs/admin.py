import logging

import disnake
from disnake.ext import commands
from sqlalchemy.orm import Session

from kazoeru.db.models import Guild
from kazoeru.embed import Embed


log = logging.getLogger(__name__)


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        Guild.__table__.create(self.bot.engine, checkfirst=True)

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error: Exception) -> None:
        if isinstance(error, commands.MissingPermissions):
            embed = Embed.error(
                inter.guild,
                "Missing Permissions!",
                "You don't have the required permissions to use this command.",
            )
            return await inter.response.send_message(embed=embed, ephemeral=True)

        embed = Embed.error(inter.guild, "Error!", "Something went wrong, please try again later.")

    @commands.slash_command(description="Configure the channel you would like to count in.")
    @commands.has_permissions(administrator=True, manage_guild=True)
    async def channel(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel) -> None:
        try:
            with Session(self.bot.engine) as session:
                guild = session.query(Guild).filter_by(id=inter.guild.id).first()
                if guild is None:
                    guild = Guild(id=inter.guild.id, channel=channel.id)
                    session.add(guild)
                else:
                    guild.channel = channel.id
                session.commit()
            embed = Embed.success(
                inter.guild,
                "Counting channel set!",
                f"{channel.mention} `{channel.id}`",
            )
            await inter.response.send_message(embed=embed)
        except Exception as e:
            log.error(e)
            embed = Embed.error(
                inter.guild,
                "Counting channel not set!",
                "Something went wrong, please try again later.",
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

    @commands.slash_command(
        description="Ruins the count if any message is sent if it is not either a valid number or bot command."
    )
    @commands.has_permissions(administrator=True, manage_guild=True)
    async def numbersonly(self, inter: disnake.ApplicationCommandInteraction, enabled: bool) -> None:
        try:
            with Session(self.bot.engine) as session:
                guild = session.query(Guild).filter_by(id=inter.guild.id).first()
                if guild is None:
                    guild = Guild(id=inter.guild.id, numonly=enabled)
                    session.add(guild)
                else:
                    guild.numonly = enabled
                session.commit()

            embed = Embed.success(inter.guild, f"Numbers only {'enabled' if enabled else 'disabled'}!")
            await inter.response.send_message(embed=embed)
        except Exception as e:
            log.error(e)
            embed = Embed.error(
                inter.guild,
                "Numbers only not set!",
                "Something went wrong, please try again later.",
            )
            await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Admin(bot))
