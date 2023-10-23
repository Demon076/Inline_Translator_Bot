from aiogram import Dispatcher

from app.filters.role_filters import AdminFilter
from app.handlers import inline_query, admin
from app.handlers import base
from app.middlewares.log_middleware import LogMiddleware

dp = Dispatcher()


def registration_dispatcher(dispatcher: Dispatcher) -> None:
    dispatcher.update.middleware(LogMiddleware())
    dispatcher.include_routers(inline_query.router, base.router, admin.router())
