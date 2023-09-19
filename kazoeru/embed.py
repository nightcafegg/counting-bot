<<<<<<< HEAD
import disnake

from kazoeru import config
=======
from typing import Optional
>>>>>>> 89950158ccee811ea71b643755e0e2ef417c5088

import disnake

from kazoeru import config


class Embed:
    @staticmethod
    def success(
        guild: disnake.Guild, title: str, description: str = None, footer: bool = True
    ) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=config.Color.success,
        )
        embed.set_author(name=title, icon_url=config.Image.success)
        if footer:
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed

    @staticmethod
    def error(
        guild: disnake.Guild, title: str, description: str = None, footer: bool = True
    ) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=config.Color.error,
        )
        embed.set_author(name=title, icon_url=config.Image.error)
        if footer:
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed

    @staticmethod
    def info(
        guild: disnake.Guild, title: str, description: str = None, footer: bool = True
    ) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=config.Color.info,
        )
        embed.set_author(name=title, icon_url=config.Image.info)
        if footer:
<<<<<<< HEAD
            embed.set_footer(
                text=f"{guild.name} • {guild.id}"
            )
        return embed        return embed
=======
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed
>>>>>>> 89950158ccee811ea71b643755e0e2ef417c5088
