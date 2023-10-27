from aiogram import Router

from app.filters.role_filters import AdminFilter
from app.handlers.admin import inline_query


def router() -> Router:
    router = Router()
    router.message.filter(AdminFilter())
    router.callback_query.filter(AdminFilter())
    router.inline_query.filter(AdminFilter())
    router.include_router(inline_query.router)
    return router
