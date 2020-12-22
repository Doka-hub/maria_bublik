from aiogram import types

from utils.db_api.user.user import get_or_create_user
from utils.misc.set_commands import set_commands

from loader import _


@set_commands
async def bot_start(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    username = message.from_user.username or None
    await get_or_create_user(user_id, username)

    await message.answer(_('Меню'))
