import disnake

from counting import constants


class Embed:
    @staticmethod
    def success(guild: disnake.Guild, title: str, description: str = None) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.success,
        )
        embed.set_author(name=title, icon_url=constants.Icons.success)
        return embed

    @staticmethod
    def error(guild: disnake.Guild, title: str, description: str = None) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.error,
        )
        embed.set_author(name=title, icon_url=constants.Icons.error)
        return embed

    @staticmethod
    def info(guild: disnake.Guild, title: str, description: str = None) -> disnake.Embed:
        embed = disnake.Embed(
            description=f"> {description}" if description else None,
            color=constants.Colors.info,
        )
        embed.set_author(name=title, icon_url=constants.Icons.info)
        return embed
