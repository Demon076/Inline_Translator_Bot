from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from app.bot.settings import bot_settings


class AdminFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(self, update: Message | CallbackQuery | InlineQuery) -> bool:
        return update.from_user.id == bot_settings.ADMIN
