from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart

from states.user import TGUserState

from .start import bot_start
from .user import user_name__handler, user_material_format__handler


def setup(dp: Dispatcher):
    # Старт
    dp.register_message_handler(bot_start, CommandStart(), in_whitelist=True)

    # Пользователь
    dp.register_message_handler(user_name__handler, state=TGUserState.name)
    dp.register_callback_query_handler(user_material_format__handler,
                                       callback_data__startswith='material_format_choose ',
                                       state=TGUserState.material_format)
