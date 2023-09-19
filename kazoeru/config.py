from dataclasses import dataclass

import yaml


@dataclass
class ColorConfig:
    error: hex
    success: hex
    info: hex


@dataclass
class ImageConfig:
    error: str
    success: str
    info: str


@dataclass
class EmoteConfig:
    error: str
    success: str
    info: str


with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

Color = ColorConfig(**config["color"])
Image = ImageConfig(**config["image"])
Emote = EmoteConfig(**config["emote"])
<<<<<<< HEAD
Image = ImageConfig(**config["image"])
Emote = EmoteConfig(**config["emote"])
=======
>>>>>>> 89950158ccee811ea71b643755e0e2ef417c5088
