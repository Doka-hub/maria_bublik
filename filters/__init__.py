from aiogram import Dispatcher

from .is_admin import AdminFilter
from .whitelist import WhiteListFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(WhiteListFilter)
