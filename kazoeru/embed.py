import disnake

from kazoeru import constants


class Embed:
    @staticmethod
    def success(guild: disnake.Guild, title: str, description: str = None, footer: bool = True) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.success,
        )
        embed.set_author(name=title, icon_url=constants.Icons.success)
        if footer:
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed

    @staticmethod
    def error(guild: disnake.Guild, title: str, description: str = None, footer: bool = True) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.error,
        )
        embed.set_author(name=title, icon_url=constants.Icons.error)
        if footer:
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed

    @staticmethod
    def info(guild: disnake.Guild, title: str, description: str = None, footer: bool = True) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.info,
        )
        embed.set_author(name=title, icon_url=constants.Icons.info)
        if footer:
            embed.set_footer(text=f"{guild.name} • {guild.id}")
        return embed
