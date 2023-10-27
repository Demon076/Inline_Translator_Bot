from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

router = Router()


@router.inline_query()
async def show_user_translate(inline_query: InlineQuery):
    results = [InlineQueryResultArticle(
        id="1",
        title="Если хотите попробовать перевод:",
        description='Напишите боту "Хочу попробовать перевод"',
        input_message_content=InputTextMessageContent(
            message_text="Если хотите попробовать перевод, напишите в бота "
                         "@inline_translator_bot \"Хочу попробовать перевод\"!!"
        )
    )]
    await inline_query.answer(results, is_personal=True)
