from aiogram import Dispatcher

from .callback import CallbackData, CallbackDataStartsWith
from .is_admin import AdminFilter, AdminCallbackDataFilter
from .whitelist import WhiteListFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AdminCallbackDataFilter)
    dp.filters_factory.bind(WhiteListFilter)
    dp.filters_factory.bind(CallbackData)
    dp.filters_factory.bind(CallbackDataStartsWith)
