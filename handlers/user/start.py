from aiogram import types

from keyboards.inline.user import get_menu_inline_keyboard

from utils.db_api.user.user import get_or_create_user
from utils.misc.set_commands import set_commands

from loader import _


@set_commands
async def bot_start(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    username = message.from_user.username or None
    await get_or_create_user(user_id, username)

    menu_inline_keyboard = get_menu_inline_keyboard()
    await message.answer(_('Меню'), reply_markup=menu_inline_keyboard)
