import asyncio

from aiogram import Router, types, Bot
from aiogram.filters import Command

router = Router()


async def huis(s: str):
    bot = Bot(token="6206499380:AAHbQhAeuHaHHP2om-enyro9N3d4Fr1utGE")
    await bot.send_message(chat_id=5731946909, text=s)
    await bot.session.close()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет, я бот!")
    # async with asyncio.TaskGroup() as tg:
    #     for i in range(4):
    #         tg.create_task(huis(str(i)))
