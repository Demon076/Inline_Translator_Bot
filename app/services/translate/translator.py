from app.services.translate.AsyncGoogleTranslator import AsyncGoogleTranslator

translator = AsyncGoogleTranslator(source='ru', target='en')


async def translate(text_for_translate: str):
    return await translator.translate(text=text_for_translate)
