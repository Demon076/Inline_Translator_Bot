from aiogram import Dispatcher

from app.filters.role_filters import AdminFilter
from app.handlers import base
from app.middlewares.log_middleware import LogMiddleware

dp = Dispatcher()


def registration_dispatcher(dispatcher: Dispatcher) -> None:
    dispatcher.update.middleware(LogMiddleware())
    dispatcher.include_router(base.router)
    dispatcher.message.filter(AdminFilter())
    dispatcher.callback_query.filter(AdminFilter())
