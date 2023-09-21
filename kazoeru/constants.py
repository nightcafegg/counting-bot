from os import environ


__all__ = ("Client", "Colors", "Images", "Emojis")


class Client:
    token: str = environ.get("BOT_TOKEN")
    owner: int = 527147599942385674


class Colors:
    error: hex = 0xF08080
    success: hex = 0x7BF1A8
    info: hex = 0xFBF8CC


class Images:
    error: str = "https://imgur.com/jLmFNU8.png"
    success: str = "https://imgur.com/9sE0qDr.png"
    info: str = "https://imgur.com/dsCFSDu.png"


class Emojis:
    error: str = "<:error:1109467955437240371>"
    success: str = "<:success:1109467958054506536>"
    info: str = "<:info:1109467933270364241>"
