from dataclasses import dataclass
from typing import Optional
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot=TgBot(env('BOT_TOKEN')))
