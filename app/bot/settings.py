from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    TOKEN: str
    ADMIN: list[int]


bot_settings = BotSettings()

