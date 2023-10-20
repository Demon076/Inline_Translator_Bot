from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from app.services.translate.translator import translate

router = Router()


@router.inline_query()
async def show_user_images(inline_query: InlineQuery):
    trans = await translate(inline_query.query)
    results = [InlineQueryResultArticle(
        id="1",  # ссылки у нас уникальные, потому проблем не будет
        title="Перевод",
        description=trans,
        input_message_content=InputTextMessageContent(
            message_text=trans
        )
    )]
    await inline_query.answer(results, is_personal=True)
