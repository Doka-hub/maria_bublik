from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .start import bot_start
from .language import choose_language, change_language


def setup(dp: Dispatcher):
    # Старт
    dp.register_message_handler(bot_start, CommandStart())

    # Язык
    dp.register_callback_query_handler(choose_language, lambda callback: callback.data.startswith('choose_language '))
    dp.register_callback_query_handler(change_language, lambda callback: callback.data == 'change_language')
