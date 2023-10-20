from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    TOKEN: str
    ADMIN: int


bot_settings = BotSettings()

