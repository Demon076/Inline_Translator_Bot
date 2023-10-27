from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from app.filters.role_filters import AdminFilter
from app.services.translate.translator import translate

router = Router()


@router.inline_query()
async def show_user_translate(inline_query: InlineQuery):
    if inline_query.query != "":
        trans = await translate(inline_query.query)
        results = [InlineQueryResultArticle(
            id="1",
            title="Перевод",
            description=trans,
            input_message_content=InputTextMessageContent(
                message_text=trans
            )
        )]
    else:
        results = [InlineQueryResultArticle(
            id="1",
            title="Перевод",
            description="Введите что-то для перевода!",
            input_message_content=InputTextMessageContent(
                message_text="Enter something to translate!!!"
            )
        )]
    await inline_query.answer(results, is_personal=True)
