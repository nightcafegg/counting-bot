from typing import Optional

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
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed
